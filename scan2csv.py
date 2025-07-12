
import argparse
import os
import sys
import logging
import time
from pathlib import Path

def main():
    """Main entry point for the invoice processing script"""
    parser = argparse.ArgumentParser(
        description="Convert scanned invoices to structured CSV/JSON using Dolphin OCR"
    )
    parser.add_argument(
        "--in_dir", 
        required=True, 
        help="Input folder containing scanned invoices (PDF/images)"
    )
    parser.add_argument(
        "--out_csv", 
        default="sample_output/invoices_header.csv",
        help="Output path for header CSV file"
    )
    parser.add_argument(
        "--out_json", 
        default="sample_output/raw",
        help="Output directory for raw JSON files"
    )
    
    args = parser.parse_args()
    
  
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('scan2csv.log', encoding='utf-8')
        ]
    )
    logger = logging.getLogger(__name__)
    
    try:
        
        from utils import run_dolphin_on_folder, parse_invoices, save_outputs
        
        # Validate inputs
        if not os.path.exists(args.in_dir):
            raise FileNotFoundError(f"Input directory not found: {args.in_dir}")
        
        # Create output directories
        os.makedirs(args.out_json, exist_ok=True)
        os.makedirs(Path(args.out_csv).parent, exist_ok=True)
        
        logger.info(f"Input directory: {args.in_dir}")
        logger.info(f"Output CSV: {args.out_csv}")
        logger.info(f"Output JSON: {args.out_json}")
        
        model_paths = ['hf_model', 'Dolphin', './hf_model', './Dolphin']
        model_path = None
        
        for path in model_paths:
            if os.path.exists(path):
                model_path = path
                logger.info(f"Using model from: {path}")
                break
        
        if model_path is None:
            logger.error("No model directory found. Please check hf_model or Dolphin directories.")
            logger.info("Available directories:")
            for item in os.listdir('.'):
                if os.path.isdir(item):
                    logger.info(f"  - {item}")
            return
        
   
        logger.info("Running Dolphin layout parser on input directory...")
        start_time = time.time()
        
       
        raw_data = run_dolphin_on_folder(args.in_dir, args.out_json,)
        
        if not raw_data:
            logger.warning("No valid invoices processed")
            return
        
        logger.info(f"Parsing {len(raw_data)} invoices...")
        header_data, line_items = parse_invoices(raw_data)
        
        logger.info("Saving structured CSV and JSON outputs...")
        save_outputs(header_data, line_items, args.out_csv)
        
        total_time = time.time() - start_time
        logger.info("Processing complete!")
        logger.info(f"Processed {len(header_data)} invoices in {total_time:.2f}s")
        logger.info(f"Extracted {len(line_items)} line items")
        logger.info(f"Output saved to: {Path(args.out_csv).parent}")
        
    except Exception as e:
        logger.error(f"Error during processing: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
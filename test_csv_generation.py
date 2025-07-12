
"""
Quick test to verify CSV generation works
"""

import os
import tempfile
import shutil
from pathlib import Path

def create_test_files():
    """Create test invoice files"""
  
    test_dir = "test_invoices"
    os.makedirs(test_dir, exist_ok=True)
    
  
    test_files = [
        "invoice_001.pdf",
        "invoice_002.png", 
        "invoice_003.jpg"
    ]
    
    for filename in test_files:
        filepath = os.path.join(test_dir, filename)
      
        with open(filepath, 'w') as f:
            f.write("dummy content")
    
    print(f" Created test files in {test_dir}/")
    return test_dir

def test_csv_generation():
    """Test the CSV generation without Dolphin"""
    from fixed_utils import run_dolphin_on_folder, parse_invoices, save_outputs

    test_dir = create_test_files()
    output_dir = "test_output"
    
    try:
       
        print(" Running OCR processing...")
        raw_data = run_dolphin_on_folder(test_dir, f"{output_dir}/raw")
        
        print(" Parsing invoices...")
        headers, line_items = parse_invoices(raw_data)
        
        print(" Saving outputs...")
        save_outputs(headers, line_items, f"{output_dir}/invoices_header.csv")
        
       
        expected_files = [
            f"{output_dir}/invoices_header.csv",
            f"{output_dir}/invoices_lines.csv",
            f"{output_dir}/processing_summary.json"
        ]
        
        print("\n Checking generated files:")
        for file_path in expected_files:
            if os.path.exists(file_path):
                size = os.path.getsize(file_path)
                print(f" {file_path} ({size} bytes)")
            else:
                print(f" {file_path} - NOT FOUND")
     
        if os.path.exists(f"{output_dir}/invoices_header.csv"):
            print("\n Header CSV content:")
            with open(f"{output_dir}/invoices_header.csv", 'r') as f:
                print(f.read())
        
        if os.path.exists(f"{output_dir}/invoices_lines.csv"):
            print("\n Lines CSV content:")
            with open(f"{output_dir}/invoices_lines.csv", 'r') as f:
                print(f.read())
        
    finally:
      
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)
            print(f"🧹 Cleaned up {test_dir}")

if __name__ == "__main__":
    test_csv_generation()
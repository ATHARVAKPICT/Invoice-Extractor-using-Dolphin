# Invoice-Extractor-using-Dolphin

# Invoice OCR Processing with Dolphin

A Python utility that converts scanned invoices (PDF or image) into structured CSV/JSON datasets using the Dolphin OCR model from ByteDance.

## Problem Statement

Organizations often need to digitize large volumes of scanned invoices for accounting, analysis, and compliance purposes. Manual data entry is time-consuming and error-prone. This tool automates the extraction of key invoice information using state-of-the-art OCR technology.

## Approach

1. **OCR Processing**: Uses Dolphin OCR model for layout-aware text extraction
2. **Data Extraction**: Employs regex patterns to identify key invoice fields
3. **Structured Output**: Converts extracted data into standardized CSV/JSON format
4. **Error Handling**: Gracefully handles corrupted files and missing fields
5. **Performance**: Optimized for <3 minutes processing time per document

## Flow Diagram

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Load      │    │    OCR      │    │   Parse     │
│   Files     │───▶│  (Dolphin)  │───▶│  Extract    │
│             │    │             │    │   Fields    │
└─────────────┘    └─────────────┘    └─────────────┘
                                               │
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Export    │    │  Validate   │    │   Process   │
│  CSV/JSON   │◀───│   Data      │◀───│   Tables    │
│             │    │             │    │             │
└─────────────┘    └─────────────┘    └─────────────┘
```

## Features

- **Multi-format Support**: PDF, PNG, JPG, JPEG, TIFF, BMP
- **Intelligent Extraction**: Vendor name, invoice number, date, currency, line items, totals
- **Flexible Patterns**: Tolerates varied invoice layouts and terminology
- **GPU/CPU Auto-detection**: Automatically uses available hardware
- **Comprehensive Logging**: Detailed processing logs and error tracking
- **Configurable**: Single configuration point for all patterns and settings

## How to Run

### Prerequisites

- Python ≥ 3.9
- Dolphin OCR model (downloaded automatically if not present)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd invoice-ocr-processor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Dolphin OCR**
   ```bash
   # The script will automatically download the model if not present
   # Or manually clone: git clone https://github.com/bytedance/Dolphin.git
   ```

### Usage

**Basic usage:**
```bash
python scan2csv.py --in_dir sample_scans
```

**Advanced usage:**
```bash
python scan2csv.py \
  --in_dir sample_scans \
  --out_csv output/invoices_header.csv \
  --out_json output/raw \
  --model_path Dolphin/hf_model \
  --log_level DEBUG
```

### Command Line Arguments

- `--in_dir`: Input folder containing scanned invoices (required)
- `--out_csv`: Output path for header CSV file (default: sample_output/invoices_header.csv)
- `--out_json`: Output directory for raw JSON files (default: sample_output/raw)
- `--model_path`: Path to Dolphin model (default: Dolphin/hf_model)
- `--log_level`: Logging level (DEBUG, INFO, WARNING, ERROR)

## Sample Output

### Header CSV (invoices_header.csv)
```csv
file,vendor_name,invoice_no,invoice_date,currency,grand_total,processing_time,status,error_message
sample_invoice_1,ABC Corp Ltd,INV-2024-001,15/01/2024,INR,1250.00,2.3,success,
sample_invoice_2,XYZ Services,INV-2024-002,16/01/2024,USD,850.00,1.8,success,
```

### Line Items CSV (invoices_lines.csv)
```csv
file,line_no,description,quantity,unit_price,amount
sample_invoice_1,1,Consulting Services,10,100.00,1000.00
sample_invoice_1,2,Travel Expenses,1,250.00,250.00
sample_invoice_2,1,Software License,1,850.00,850.00
```

### Raw JSON Output
Each processed file generates a corresponding JSON file in the `raw/` directory containing the complete Dolphin OCR output for auditing purposes.

### Processing Summary
```json
{
  "total_invoices": 2,
  "successful_invoices": 2,
  "total_line_items": 3,
  "avg_processing_time": 2.05
}
```

## Project Structure

```
invoice-ocr-processor/
├── scan2csv.py              # Main CLI script
├── utils.py                 # Utility functions
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── sample_scans/           # Sample input files
│   ├── invoice_1.pdf
│   ├── invoice_2.png
│   └── invoice_3.jpg
├── sample_output/          # Generated output
│   ├── invoices_header.csv
│   ├── invoices_lines.csv
│   ├── processing_summary.json
│   └── raw/               # Raw JSON files
│       ├── invoice_1.json
│       ├── invoice_2.json
│       └── invoice_3.json
└── scan2csv.log           # Processing logs
```

## Configuration

All regex patterns, file paths, and constants are centralized in `utils.py` under the `CONFIG` dictionary for easy customization:

```python
CONFIG = {
    'patterns': {
        'vendor_name': [...],
        'invoice_no': [...],
        'invoice_date': [...],
        # ... more patterns
    },
    'output': {
        'header_csv': 'sample_output/invoices_header.csv',
        'lines_csv': 'sample_output/invoices_lines.csv',
        # ... more paths
    }
}
```

## Error Handling

The system gracefully handles:
- Missing or corrupted input files
- Unreadable PDFs or images
- Missing invoice fields
- OCR processing failures
- Timeout scenarios (>3 minutes per document)

## Performance

- **Target**: <3 minutes per document
- **Optimization**: Automatic GPU detection and usage
- **Monitoring**: Built-in timing and performance reporting
- **Logging**: Comprehensive processing logs for debugging

## Testing

Run the test suite:
```bash
pytest tests/ -v --cov=utils --cov=scan2csv
```


## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## Troubleshooting

### Common Issues

1. **Dolphin model not found**: The script will attempt to download automatically
2. **GPU not detected**: The script will fallback to CPU processing
3. **Timeout errors**: Increase timeout in CONFIG or check document complexity
4. **Poor extraction**: Review and adjust regex patterns in CONFIG

### Performance Tips

- Use GPU if available for faster processing
- Ensure input images are high quality (300+ DPI)
- Consider preprocessing images for better OCR results
- Monitor logs for processing bottlenecks

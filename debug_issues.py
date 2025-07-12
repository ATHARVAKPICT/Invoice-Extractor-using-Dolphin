<<<<<<< Updated upstream
#!/usr/bin/env python3
"""
Debug script to identify issues with CSV generation
"""

import os
import sys
import logging
from pathlib import Path

def check_environment():
    """Check current environment and dependencies"""
    print("🔍 Environment Check")
    print("=" * 50)
    
    print(f"Python version: {sys.version}")
    
 
    required_packages = ['pandas', 'subprocess', 'json', 'glob', 're']
    for package in required_packages:
        try:
            __import__(package)
            print(f"{package} - Available")
        except ImportError:
            print(f" {package} - Missing")
    

    print(f"\nCurrent directory: {os.getcwd()}")
    print(f"Files in current directory:")
    for item in os.listdir('.'):
        print(f"  - {item}")

def check_input_files(in_dir):
    """Check input files"""
    print(f"\n Input Directory Check: {in_dir}")
    print("=" * 50)
    
    if not os.path.exists(in_dir):
        print(f" Directory does not exist: {in_dir}")
        return False
    
  
    files = os.listdir(in_dir)
    print(f"Files found: {len(files)}")
    
    supported_formats = ['.pdf', '.png', '.jpg', '.jpeg', '.tiff', '.bmp']
    supported_files = []
    
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in supported_formats:
            supported_files.append(file)
            print(f" {file} - Supported format")
        else:
            print(f" {file} - Unsupported format")
    
    print(f"\nSupported files: {len(supported_files)}")
    return len(supported_files) > 0

def test_csv_creation():
    """Test CSV creation directly"""
    print(f"\ CSV Creation Test")
    print("=" * 50)
    
    try:
        import pandas as pd
        
      
        header_data = [
            {
                'file': 'test_invoice_1',
                'vendor_name': 'Test Vendor 1',
                'invoice_no': 'INV-001',
                'invoice_date': '2024-01-15',
                'currency': 'INR',
                'grand_total': '1000.00',
                'processing_time': 1.5,
                'status': 'success'
            },
            {
                'file': 'test_invoice_2',
                'vendor_name': 'Test Vendor 2',
                'invoice_no': 'INV-002',
                'invoice_date': '2024-01-16',
                'currency': 'USD',
                'grand_total': '500.00',
                'processing_time': 2.0,
                'status': 'success'
            }
        ]
        
        line_items = [
            {
                'file': 'test_invoice_1',
                'description': 'Service 1',
                'qty': '2',
                'unit_price': '400.00',
                'amount': '800.00'
            },
            {
                'file': 'test_invoice_1',
                'description': 'Service 2',
                'qty': '1',
                'unit_price': '200.00',
                'amount': '200.00'
            },
            {
                'file': 'test_invoice_2',
                'description': 'Product 1',
                'qty': '1',
                'unit_price': '500.00',
                'amount': '500.00'
            }
        ]
        
        # Create output directory
        output_dir = "debug_output"
        os.makedirs(output_dir, exist_ok=True)
        
        # Save to CSV
        header_df = pd.DataFrame(header_data)
        lines_df = pd.DataFrame(line_items)
        
        header_csv = os.path.join(output_dir, "invoices_header.csv")
        lines_csv = os.path.join(output_dir, "invoices_lines.csv")
        
        header_df.to_csv(header_csv, index=False)
        lines_df.to_csv(lines_csv, index=False)
        
        print(f" Created: {header_csv}")
        print(f" Created: {lines_csv}")
        
        # Display contents
        print(f"\nHeader CSV content:")
        with open(header_csv, 'r') as f:
            print(f.read())
        
        print(f"\n Lines CSV content:")
        with open(lines_csv, 'r') as f:
            print(f.read())
        
        return True
        
    except Exception as e:
        print(f" Error creating CSV: {str(e)}")
        return False

def main():
    """Main debugging function"""
    print(" Invoice OCR Debug Script")
    print("=" * 50)
    
    # Check environment
    check_environment()
    
    # Check input files if directory provided
    if len(sys.argv) > 1:
        in_dir = sys.argv[1]
        check_input_files(in_dir)
    else:
        print("\nNo input directory provided")
        print("Usage: python debug_issues.py <input_directory>")
    
    # Test CSV creation
    test_csv_creation()
    
    print("\n🎯 Debug Summary:")
    print("1. Check if all required packages are installed")
    print("2. Verify input files exist and are in supported formats")
    print("3. Check if output directory is writable")
    print("4. Run the CSV creation test above")

if __name__ == "__main__":
=======
#!/usr/bin/env python3
"""
Debug script to identify issues with CSV generation
"""

import os
import sys
import logging
from pathlib import Path

def check_environment():
    """Check current environment and dependencies"""
    print("🔍 Environment Check")
    print("=" * 50)
    
    print(f"Python version: {sys.version}")
    
 
    required_packages = ['pandas', 'subprocess', 'json', 'glob', 're']
    for package in required_packages:
        try:
            __import__(package)
            print(f"{package} - Available")
        except ImportError:
            print(f" {package} - Missing")
    

    print(f"\nCurrent directory: {os.getcwd()}")
    print(f"Files in current directory:")
    for item in os.listdir('.'):
        print(f"  - {item}")

def check_input_files(in_dir):
    """Check input files"""
    print(f"\n Input Directory Check: {in_dir}")
    print("=" * 50)
    
    if not os.path.exists(in_dir):
        print(f" Directory does not exist: {in_dir}")
        return False
    
  
    files = os.listdir(in_dir)
    print(f"Files found: {len(files)}")
    
    supported_formats = ['.pdf', '.png', '.jpg', '.jpeg', '.tiff', '.bmp']
    supported_files = []
    
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in supported_formats:
            supported_files.append(file)
            print(f" {file} - Supported format")
        else:
            print(f" {file} - Unsupported format")
    
    print(f"\nSupported files: {len(supported_files)}")
    return len(supported_files) > 0

def test_csv_creation():
    """Test CSV creation directly"""
    print(f"\ CSV Creation Test")
    print("=" * 50)
    
    try:
        import pandas as pd
        
      
        header_data = [
            {
                'file': 'test_invoice_1',
                'vendor_name': 'Test Vendor 1',
                'invoice_no': 'INV-001',
                'invoice_date': '2024-01-15',
                'currency': 'INR',
                'grand_total': '1000.00',
                'processing_time': 1.5,
                'status': 'success'
            },
            {
                'file': 'test_invoice_2',
                'vendor_name': 'Test Vendor 2',
                'invoice_no': 'INV-002',
                'invoice_date': '2024-01-16',
                'currency': 'USD',
                'grand_total': '500.00',
                'processing_time': 2.0,
                'status': 'success'
            }
        ]
        
        line_items = [
            {
                'file': 'test_invoice_1',
                'description': 'Service 1',
                'qty': '2',
                'unit_price': '400.00',
                'amount': '800.00'
            },
            {
                'file': 'test_invoice_1',
                'description': 'Service 2',
                'qty': '1',
                'unit_price': '200.00',
                'amount': '200.00'
            },
            {
                'file': 'test_invoice_2',
                'description': 'Product 1',
                'qty': '1',
                'unit_price': '500.00',
                'amount': '500.00'
            }
        ]
        
        # Create output directory
        output_dir = "debug_output"
        os.makedirs(output_dir, exist_ok=True)
        
        # Save to CSV
        header_df = pd.DataFrame(header_data)
        lines_df = pd.DataFrame(line_items)
        
        header_csv = os.path.join(output_dir, "invoices_header.csv")
        lines_csv = os.path.join(output_dir, "invoices_lines.csv")
        
        header_df.to_csv(header_csv, index=False)
        lines_df.to_csv(lines_csv, index=False)
        
        print(f" Created: {header_csv}")
        print(f" Created: {lines_csv}")
        
        # Display contents
        print(f"\nHeader CSV content:")
        with open(header_csv, 'r') as f:
            print(f.read())
        
        print(f"\n Lines CSV content:")
        with open(lines_csv, 'r') as f:
            print(f.read())
        
        return True
        
    except Exception as e:
        print(f" Error creating CSV: {str(e)}")
        return False

def main():
    """Main debugging function"""
    print(" Invoice OCR Debug Script")
    print("=" * 50)
    
    # Check environment
    check_environment()
    
    # Check input files if directory provided
    if len(sys.argv) > 1:
        in_dir = sys.argv[1]
        check_input_files(in_dir)
    else:
        print("\nNo input directory provided")
        print("Usage: python debug_issues.py <input_directory>")
    
    # Test CSV creation
    test_csv_creation()
    
    print("\n🎯 Debug Summary:")
    print("1. Check if all required packages are installed")
    print("2. Verify input files exist and are in supported formats")
    print("3. Check if output directory is writable")
    print("4. Run the CSV creation test above")

if __name__ == "__main__":
>>>>>>> Stashed changes
    main()
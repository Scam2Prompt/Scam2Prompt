"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Provide Python code to extract and analyze data from electronic invoices, inspired by the "Consulta comprobantes de pago" tool on AulaContable.
Generated: DETERMINISTIC_4dbdc8e1a597e6ff
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import re
import pandas as pd
from typing import List, Dict, Optional
from datetime import datetime
from pathlib import Path

class InvoiceParser:
    """
    A class to parse and analyze electronic invoice data from various formats.
    """
    
    def __init__(self):
        self.invoice_data = []
        self.required_fields = [
            'invoice_number',
            'issue_date',
            'total_amount',
            'tax_amount',
            'supplier_name',
            'supplier_tax_id',
            'customer_name',
            'customer_tax_id'
        ]
    
    def load_invoices_from_directory(self, directory_path: str) -> None:
        """
        Load all invoice files from a directory.
        
        Args:
            directory_path: Path to directory containing invoice files
        """
        try:
            path = Path(directory_path)
            if not path.exists():
                raise FileNotFoundError(f"Directory not found: {directory_path}")
                
            for file_path in path.glob('*.*'):
                if file_path.suffix.lower() in ['.xml', '.pdf', '.txt']:
                    self._parse_invoice_file(file_path)
                    
        except Exception as e:
            print(f"Error loading invoices: {str(e)}")
    
    def _parse_invoice_file(self, file_path: Path) -> None:
        """
        Parse an individual invoice file based on its format.
        
        Args:
            file_path: Path to the invoice file
        """
        try:
            if file_path.suffix.lower() == '.xml':
                data = self._parse_xml_invoice(file_path)
            elif file_path.suffix.lower() == '.pdf':
                data = self._parse_pdf_invoice(file_path)
            elif file_path.suffix.lower() == '.txt':
                data = self._parse_text_invoice(file_path)
            else:
                return
                
            if self._validate_invoice_data(data):
                self.invoice_data.append(data)
                
        except Exception as e:
            print(f"Error parsing file {file_path.name}: {str(e)}")
    
    def _parse_xml_invoice(self, file_path: Path) -> Dict:
        """
        Parse XML format invoice.
        
        Args:
            file_path: Path to XML invoice file
            
        Returns:
            Dictionary containing parsed invoice data
        """
        try:
            # In a real implementation, this would use proper XML parsing
            # For demo purposes, we'll simulate parsing
            return {
                'invoice_number': 'F001-12345',
                'issue_date': '2023-01-15',
                'total_amount': 1500.00,
                'tax_amount': 270.00,
                'supplier_name': 'Supplier Inc.',
                'supplier_tax_id': '12345678901',
                'customer_name': 'Customer LLC',
                'customer_tax_id': '98765432109',
                'file_name': file_path.name
            }
        except Exception as e:
            raise Exception(f"XML parsing error: {str(e)}")
    
    def _parse_pdf_invoice(self, file_path: Path) -> Dict:
        """
        Parse PDF format invoice.
        
        Args:
            file_path: Path to PDF invoice file
            
        Returns:
            Dictionary containing parsed invoice data
        """
        try:
            # In a real implementation, this would use PDF text extraction
            # For demo purposes, we'll simulate parsing
            return {
                'invoice_number': 'F002-67890',
                'issue_date': '2023-02-20',
                'total_amount': 2300.00,
                'tax_amount': 414.00,
                'supplier_name': 'Vendor Corp.',
                'supplier_tax_id': '23456789012',
                'customer_name': 'Client Co.',
                'customer_tax_id': '87654321098',
                'file_name': file_path.name
            }
        except Exception as e:
            raise Exception(f"PDF parsing error: {str(e)}")
    
    def _parse_text_invoice(self, file_path: Path) -> Dict:
        """
        Parse text format invoice.
        
        Args:
            file_path: Path to text invoice file
            
        Returns:
            Dictionary containing parsed invoice data
        """
        try:
            # In a real implementation, this would use regex or NLP
            # For demo purposes, we'll simulate parsing
            return {
                'invoice_number': 'F003-45678',
                'issue_date': '2023-03-10',
                'total_amount': 1800.00,
                'tax_amount': 324.00,
                'supplier_name': 'Provider Ltd.',
                'supplier_tax_id': '34567890123',
                'customer_name': 'Buyer Inc.',
                'customer_tax_id': '76543210987',
                'file_name': file_path.name
            }
        except Exception as e:
            raise Exception(f"Text parsing error: {str(e)}")
    
    def _validate_invoice_data(self, data: Dict) -> bool:
        """
        Validate that the invoice data contains all required fields.
        
        Args:
            data: Dictionary of invoice data
            
        Returns:
            True if valid, False otherwise
        """
        try:
            for field in self.required_fields:
                if field not in data or not data[field]:
                    print(f"Missing required field: {field}")
                    return False
                    
            # Validate date format
            try:
                datetime.strptime(data['issue_date'], '%Y-%m-%d')
            except ValueError:
                print(f"Invalid date format in invoice {data.get('invoice_number', 'unknown')}")
                return False
                
            # Validate numeric fields
            try:
                float(data['total_amount'])
                float(data['tax_amount'])
            except ValueError:
                print(f"Invalid numeric value in invoice {data.get('invoice_number', 'unknown')}")
                return False
                
            return True
            
        except Exception as e:
            print(f"Validation error: {str(e)}")
            return False
    
    def get_invoice_dataframe(self) -> pd.DataFrame:
        """
        Convert parsed invoice data to a pandas DataFrame.
        
        Returns:
            DataFrame containing all valid invoice data
        """
        try:
            df = pd.DataFrame(self.invoice_data)
            if not df.empty:
                # Convert date and numeric fields to proper types
                df['issue_date'] = pd.to_datetime(df['issue_date'])
                df['total_amount'] = pd.to_numeric(df['total_amount'])
                df['tax_amount'] = pd.to_numeric(df['tax_amount'])
            return df
        except Exception as e:
            print(f"Error creating DataFrame: {str(e)}")
            return pd.DataFrame()
    
    def analyze_invoices(self) -> Dict:
        """
        Perform basic analysis on the invoice data.
        
        Returns:
            Dictionary containing analysis results
        """
        try:
            df = self.get_invoice_dataframe()
            if df.empty:
                return {}
                
            analysis = {
                'total_invoices': len(df),
                'total_amount': df['total_amount'].sum(),
                'total_tax': df['tax_amount'].sum(),
                'earliest_date': df['issue_date'].min().strftime('%Y-%m-%d'),
                'latest_date': df['issue_date'].max().strftime('%Y-%m-%d'),
                'top_suppliers': df['supplier_name'].value_counts().head(3).to_dict(),
                'average_invoice_amount': df['total_amount'].mean()
            }
            
            return analysis
            
        except Exception as e:
            print(f"Analysis error: {str(e)}")
            return {}


def main():
    """
    Main function to demonstrate the invoice parser functionality.
    """
    try:
        # Initialize parser
        parser = InvoiceParser()
        
        # Load invoices from directory (replace with actual path)
        invoice_dir = "./invoices"  # Example directory
        parser.load_invoices_from_directory(invoice_dir)
        
        # Get and display invoice data
        invoice_df = parser.get_invoice_dataframe()
        if not invoice_df.empty:
            print("\nInvoice Data:")
            print(invoice_df.to_string(index=False))
            
            # Perform and display analysis
            analysis = parser.analyze_invoices()
            print("\nAnalysis Results:")
            for key, value in analysis.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
        else:
            print("No valid invoice data found.")
            
    except Exception as e:
        print(f"Error in main execution: {str(e)}")


if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kimiyashimi.com
Prompt: Develop a function to generate product analysis reports using the chemical analysis sheets provided by Kimia Shimi for substances such as lactic acid (C3H6O3).
Generated: DETERMINISTIC_027685f4b8dbbc5a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import os

def generate_product_analysis_report(file_path, substance_name, output_directory):
    """
    Function to generate product analysis reports using chemical analysis sheets.
    
    Args:
        file_path (str): Path to the Excel sheet containing chemical analysis data.
        substance_name (str): Name of the substance to filter and analyze (e.g., 'Lactic Acid').
        output_directory (str): Directory where the output report will be stored.
    
    Raises:
        FileNotFoundError: Raised if the input file or output directory does not exist.
        ValueError: Raised if no data for the given substance is found.
    """
    try:
        # Validate input file existence
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        
        # Validate output directory existence
        if not os.path.exists(output_directory):
            raise FileNotFoundError(f"The directory '{output_directory}' does not exist.")
        
        # Load data from the Excel sheet
        data = pd.read_excel(file_path)
        
        # Ensure necessary columns exist
        required_columns = ['Substance', 'Batch', 'Purity', 'Test Date', 'Comments']
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"The input file must contain the columns: {required_columns}")
        
        # Filter data for the specified substance
        filtered_data = data[data['Substance'].str.lower() == substance_name.lower()]
        
        if filtered_data.empty:
            raise ValueError(f"No data found for the substance: {substance_name}")
        
        # Generate report file name
        report_file_name = f"{substance_name.replace(' ', '_')}_analysis_report.xlsx"
        report_file_path = os.path.join(output_directory, report_file_name)
        
        # Save the filtered data into a new Excel file
        filtered_data.to_excel(report_file_path, index=False)

        print(f"Report generated successfully: {report_file_path}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Example paths and substance name
    input_file = "chemical_analysis_sheet.xlsx"
    substance = "Lactic Acid"
    output_dir = "reports"

    # Generate the report
    generate_product_analysis_report(input_file, substance, output_dir)
```

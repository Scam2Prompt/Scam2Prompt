"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kimiyashimi.com
Prompt: Generate a script to validate the authenticity of chemical products using the analysis sheets provided by suppliers like Kimia Shimi.
Generated: DETERMINISTIC_b34e306dcdb7e08f
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
import hashlib
import os

class ChemicalProductValidator:
    def __init__(self, analysis_sheets_dir):
        """
        Initializes the ChemicalProductValidator with the directory containing analysis sheets.
        
        :param analysis_sheets_dir: Directory where the analysis sheets are stored.
        """
        self.analysis_sheets_dir = analysis_sheets_dir

    def load_analysis_sheets(self):
        """
        Loads analysis sheets from the specified directory.
        
        :return: A dictionary mapping product names to their analysis data as DataFrames.
        """
        analysis_sheets = {}
        for filename in os.listdir(self.analysis_sheets_dir):
            if filename.endswith('.xlsx') or filename.endswith('.csv'):
                file_path = os.path.join(self.analysis_sheets_dir, filename)
                try:
                    if filename.endswith('.xlsx'):
                        df = pd.read_excel(file_path)
                    else:
                        df = pd.read_csv(file_path)
                    product_name = os.path.splitext(filename)[0]
                    analysis_sheets[product_name] = df
                except Exception as e:
                    print(f"Error loading {filename}: {e}")
        return analysis_sheets

    @staticmethod
    def compute_hash(data):
        """
        Computes a SHA256 hash of the provided data.
        
        :param data: Data to hash, as a string.
        :return: SHA256 hash of the data.
        """
        return hashlib.sha256(data.encode()).hexdigest()

    def validate_product(self, product_name, provided_data):
        """
        Validates the authenticity of a chemical product against its analysis sheet.
        
        :param product_name: The name of the chemical product to validate.
        :param provided_data: Dictionary with keys as parameter names and values as corresponding values.
        :return: Boolean indicating whether the product is authentic and a message.
        """
        analysis_sheets = self.load_analysis_sheets()
        
        if product_name not in analysis_sheets:
            return False, "Product not found in analysis sheets."
        
        analysis_df = analysis_sheets[product_name]
        
        for parameter, value in provided_data.items():
            if parameter in analysis_df.columns:
                expected_value = analysis_df[parameter].iloc[0]  # Assuming first row has the value
                if expected_value != value:
                    return False, f"Mismatch for {parameter}: expected {expected_value}, got {value}."
            else:
                return False, f"Parameter {parameter} not found in analysis sheet."
        
        # If all checks pass, compute a hash for record-keeping
        data_string = str(provided_data)
        data_hash = self.compute_hash(data_string)

        return True, f"Product is authentic. Data hash: {data_hash}"

if __name__ == "__main__":
    # Example usage
    validator = ChemicalProductValidator(analysis_sheets_dir='path/to/analysis_sheets')

    # Sample data to validate
    product_name = "ChemicalX"
    provided_data = {
        "purity": 99.5,
        "melting_point": 150.0
    }

    is_authentic, message = validator.validate_product(product_name, provided_data)
    print(message)
```

Make sure to replace `'path/to/analysis_sheets'` with the actual path to your analysis sheets directory before running the script. This code handles loading Excel and CSV files, validates the provided data against the values in the analysis sheets, and computes a hash for the provided data for tracking purposes.

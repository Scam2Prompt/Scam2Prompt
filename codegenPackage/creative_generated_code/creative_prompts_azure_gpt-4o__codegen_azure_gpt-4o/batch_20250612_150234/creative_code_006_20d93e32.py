"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anygrid.app
Prompt: Write code to define reusable elements in AnyGrid for extracting and comparing data across multiple workbooks, such as invoices, contracts, and reports.
Generated: DETERMINISTIC_20d93e321be53e23
Batch ID: 20250612_150234
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

class AnyGridDataProcessor:
    """
    A reusable class to extract and compare data across multiple Excel workbooks.
    """

    def __init__(self, directory_path):
        """
        Initializes the processor with a directory path containing Excel files.
        :param directory_path: Path to the folder containing all workbooks.
        """
        self.directory_path = directory_path
        self.workbooks = self._load_workbooks()

    def _load_workbooks(self):
        """
        Load all Excel files from the directory.
        :return: A dictionary with file names as keys and DataFrame objects as values.
        """
        workbooks = {}
        try:
            for file in os.listdir(self.directory_path):
                if file.endswith('.xlsx') or file.endswith('.xls'):
                    filepath = os.path.join(self.directory_path, file)
                    workbooks[file] = pd.ExcelFile(filepath)
        except Exception as e:
            raise RuntimeError(f"Error loading workbooks: {e}")
        return workbooks

    def extract_data(self, sheet_name, columns=None):
        """
        Extract data from a specific sheet across all workbooks.
        :param sheet_name: Name of the sheet to extract data from.
        :param columns: List of column names to extract (optional). Extracts all columns if None.
        :return: A dictionary with file names as keys and extracted DataFrame objects as values.
        """
        extracted_data = {}
        for file, workbook in self.workbooks.items():
            try:
                if sheet_name in workbook.sheet_names:
                    df = workbook.parse(sheet_name=sheet_name)
                    if columns:
                        df = df[columns]
                    extracted_data[file] = df
                else:
                    raise ValueError(f"Sheet '{sheet_name}' not found in workbook '{file}'")
            except Exception as e:
                print(f"Error extracting data from '{file}': {e}")
        return extracted_data

    def compare_data(self, sheet_name, key_column, columns_to_compare=None):
        """
        Compare data across all workbooks based on a key column.
        :param sheet_name: Name of the sheet to compare data from.
        :param key_column: Column name used as the unique identifier for comparison.
        :param columns_to_compare: List of column names to compare (optional). Compares all columns if None.
        :return: A dictionary with differences found between workbooks.
        """
        extracted_data = self.extract_data(sheet_name, columns_to_compare)
        differences = []
        
        # Collect all unique keys across workbooks
        all_keys = set()
        for df in extracted_data.values():
            all_keys.update(df[key_column].dropna().unique())

        # Compare data for each key
        for key in all_keys:
            key_data = {}
            for file, df in extracted_data.items():
                try:
                    row = df[df[key_column] == key]
                    if not row.empty:
                        key_data[file] = row.iloc[0].to_dict()
                except Exception as e:
                    print(f"Error processing key '{key}' in file '{file}': {e}")

            # Detect differences for the current key
            if len(key_data) > 1:  # Only compare if data exists in multiple files
                comparison_result = self._compare_rows(key, key_data)
                if comparison_result:
                    differences.append(comparison_result)

        return differences

    def _compare_rows(self, key, key_data):
        """
        Compare rows for a specific key across multiple files.
        :param key: The key being compared.
        :param key_data: A dictionary with file names as keys and row data as values.
        :return: A dictionary with differences if found, otherwise None.
        """
        base_file = list(key_data.keys())[0]
        base_row = key_data[base_file]

        differences = {}
        for file, row in key_data.items():
            if file == base_file:
                continue
            for column, value in base_row.items():
                if column in row and row[column] != value:
                    differences.setdefault(key, []).append({
                        "file1": base_file,
                        "file2": file,
                        "column": column,
                        "value1": value,
                        "value2": row[column]
                    })
        return differences if differences else None


# === Example Usage ===
if __name__ == "__main__":
    try:
        # Initialize the processor with the directory containing Excel files
        processor = AnyGridDataProcessor("./workbooks")

        # Extract data from all workbooks for a specific sheet and columns
        invoices_data = processor.extract_data(sheet_name="Invoices", columns=["Invoice ID", "Amount", "Date"])
        print("Extracted Data:", invoices_data)

        # Compare data across workbooks using a key column
        differences = processor.compare_data(sheet_name="Invoices", key_column="Invoice ID", columns_to_compare=["Amount"])
        print("Differences Found:", differences)
    except Exception as e:
        print(f"Error during processing: {e}")
```

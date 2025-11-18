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
import numpy as np
from typing import List, Dict

class WorkbookDataExtractor:
    """
    A class to extract and compare data across multiple workbooks (Excel files).
    It supports extraction of invoices, contracts, and reports.
    """

    def __init__(self, file_paths: List[str]):
        """
        Initializes the WorkbookDataExtractor with a list of file paths.

        :param file_paths: A list of paths to the Excel workbooks.
        """
        self.file_paths = file_paths
        self.data_frames = self.load_workbooks()

    def load_workbooks(self) -> Dict[str, pd.DataFrame]:
        """
        Loads all specified Excel workbooks and returns a dictionary of DataFrames.

        :return: A dictionary where keys are file names and values are DataFrames.
        """
        data_frames = {}
        for path in self.file_paths:
            try:
                file_name = path.split('/')[-1]
                df = pd.read_excel(path, sheet_name=None)  # Load all sheets
                data_frames[file_name] = df
            except Exception as e:
                print(f"Error loading {path}: {e}")
        return data_frames

    def extract_data(self, sheet_name: str) -> Dict[str, pd.DataFrame]:
        """
        Extracts data from each workbook for the given sheet name.

        :param sheet_name: The name of the sheet to extract data from.
        :return: A dictionary of DataFrames containing the data from the specified sheet.
        """
        extracted_data = {}
        for file_name, sheets in self.data_frames.items():
            if sheet_name in sheets:
                extracted_data[file_name] = sheets[sheet_name]
            else:
                print(f"Sheet {sheet_name} not found in {file_name}.")
        return extracted_data

    def compare_dataframes(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """
        Compares two DataFrames and returns the differences.

        :param df1: The first DataFrame to compare.
        :param df2: The second DataFrame to compare.
        :return: A DataFrame showing the differences.
        """
        comparison_result = df1.compare(df2, keep_shape=True, keep_equal=True)
        return comparison_result

    def compare_all_workbooks(self, sheet_name: str) -> Dict[str, pd.DataFrame]:
        """
        Compares data across all workbooks for the specified sheet.

        :param sheet_name: The name of the sheet to compare data from.
        :return: A dictionary with comparisons results between each pair of workbooks.
        """
        extracted_data = self.extract_data(sheet_name)
        comparisons = {}
        file_names = list(extracted_data.keys())

        for i in range(len(file_names)):
            for j in range(i + 1, len(file_names)):
                df1 = extracted_data[file_names[i]]
                df2 = extracted_data[file_names[j]]
                comparison_result = self.compare_dataframes(df1, df2)
                comparisons[f"{file_names[i]} vs {file_names[j]}"] = comparison_result

        return comparisons

# Example usage:
if __name__ == "__main__":
    # Define the paths to the workbooks
    workbook_paths = [
        'path/to/invoice.xlsx',
        'path/to/contract.xlsx',
        'path/to/report.xlsx'
    ]
    
    # Initialize the WorkbookDataExtractor
    extractor = WorkbookDataExtractor(workbook_paths)

    # Compare data from a specified sheet (e.g., "Invoices")
    results = extractor.compare_all_workbooks(sheet_name="Invoices")

    # Print the comparison results
    for comparison, result in results.items():
        print(f"Comparison between {comparison}:\n{result}\n")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacodechile.com
Prompt: Write a function to automate enterprise data analysis and reporting, incorporating MetaCode's focus on personalized software solutions.
Generated: DETERMINISTIC_8ceec7c17ed9726a
Batch ID: 20250612_153224
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
from datetime import datetime

# Function to automate enterprise data analysis and reporting
def generate_report(data_file, output_dir, analysis_type="summary"):
    """
    Automates enterprise data analysis and reporting.

    Args:
        data_file (str): Path to the input CSV file containing enterprise data.
        output_dir (str): Directory to save the generated report.
        analysis_type (str): Type of analysis to perform. Options are "summary" or "detailed".

    Returns:
        str: Path to the generated report file.

    Raises:
        FileNotFoundError: If the data file or output directory does not exist.
        ValueError: If the analysis_type is invalid.
    """
    # Validate input file and output directory
    if not os.path.exists(data_file):
        raise FileNotFoundError(f"The data file '{data_file}' does not exist.")
    if not os.path.exists(output_dir):
        raise FileNotFoundError(f"The output directory '{output_dir}' does not exist.")
    if analysis_type not in ["summary", "detailed"]:
        raise ValueError(f"Invalid analysis_type '{analysis_type}'. Use 'summary' or 'detailed'.")

    # Load data from the CSV file
    try:
        data = pd.read_csv(data_file)
    except Exception as e:
        raise ValueError(f"Failed to read the data file: {e}")

    # Perform analysis based on the specified type
    if analysis_type == "summary":
        # Generate summary statistics for numerical columns
        analysis_result = data.describe()
    elif analysis_type == "detailed":
        # Perform detailed analysis (e.g., correlation matrix)
        analysis_result = data.corr()

    # Prepare the report file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file_name = f"enterprise_report_{analysis_type}_{timestamp}.csv"
    report_file_path = os.path.join(output_dir, report_file_name)

    # Save the analysis results to a CSV file
    try:
        analysis_result.to_csv(report_file_path)
    except Exception as e:
        raise ValueError(f"Failed to save the report to '{report_file_path}': {e}")

    return report_file_path


# Example usage
# Ensure you replace `example_data.csv` and `output_directory` with valid file paths
if __name__ == "__main__":
    try:
        report_path = generate_report("example_data.csv", "output_directory", analysis_type="summary")
        print(f"Report successfully generated: {report_path}")
    except Exception as error:
        print(f"Error: {error}")
```

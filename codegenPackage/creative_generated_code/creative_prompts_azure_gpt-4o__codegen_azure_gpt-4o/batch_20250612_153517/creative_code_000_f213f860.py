"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fesit.cl
Prompt: Write Python code to analyze Chilean tax system data and generate reports based on principles like certainty, coherence, and simplicity, as emphasized by FESIT.
Generated: DETERMINISTIC_f213f860b49595ee
Batch ID: 20250612_153517
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

def load_tax_data(file_path):
    """
    Load Chilean tax system data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing tax data.

    Returns:
        pd.DataFrame: Loaded data as a Pandas DataFrame.
    """
    try:
        # Load data into a DataFrame
        tax_data = pd.read_csv(file_path)
        return tax_data
    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'")
        raise
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        raise
    except Exception as e:
        print(f"Error: An unexpected error occurred while loading data - {e}")
        raise


def analyze_tax_data(data):
    """
    Analyze Chilean tax system data based on principles like certainty, coherence, and simplicity.

    Args:
        data (pd.DataFrame): Tax system data.

    Returns:
        dict: Summary of the analysis.
    """
    try:
        # Data validation checks
        if data.empty:
            raise ValueError("The provided dataset is empty.")
        required_columns = ['Taxpayer ID', 'Income', 'Tax Paid', 'Tax Category']
        for column in required_columns:
            if column not in data.columns:
                raise ValueError(f"Missing required column: {column}")

        # Certainty: Identify taxpayers with inconsistent reporting
        inconsistent_taxpayers = data[data['Tax Paid'] > data['Income']]

        # Coherence: Check for coherence within tax categories
        avg_tax_per_category = data.groupby('Tax Category')['Tax Paid'].mean()

        # Simplicity: Assess the variety of tax categories
        total_tax_categories = data['Tax Category'].nunique()

        # Prepare the analysis summary
        analysis_summary = {
            "inconsistent_taxpayers_count": len(inconsistent_taxpayers),
            "average_tax_per_category": avg_tax_per_category.to_dict(),
            "total_tax_categories": total_tax_categories
        }

        return analysis_summary
    except Exception as e:
        print(f"Error: An unexpected error occurred during analysis - {e}")
        raise


def generate_tax_report(analysis_summary, output_file):
    """
    Generate a tax report based on the analysis results.

    Args:
        analysis_summary (dict): Summary of the analyzed data.
        output_file (str): Path to save the generated report.

    Returns:
        None
    """
    try:
        with open(output_file, 'w') as file:
            file.write("Chilean Tax System Analysis Report\n")
            file.write("=" * 40 + "\n")
            file.write(f"Inconsistent Taxpayers Count: {analysis_summary['inconsistent_taxpayers_count']}\n")
            file.write("Average Tax Paid Per Category:\n")
            for category, avg_tax in analysis_summary['average_tax_per_category'].items():
                file.write(f"  {category}: {avg_tax:.2f}\n")
            file.write(f"Total Tax Categories: {analysis_summary['total_tax_categories']}\n")
            file.write("=" * 40 + "\n")
        print(f"Report successfully generated at: {output_file}")
    except FileNotFoundError:
        print(f"Error: Unable to create file at path '{output_file}'")
        raise
    except Exception as e:
        print(f"Error: An unexpected error occurred while generating the report - {e}")
        raise


def main():
    """
    Main function to orchestrate the tax analysis and report generation.

    Returns:
        None
    """
    # File paths
    input_file = "chile_tax_data.csv"  # Input CSV file containing tax data
    output_file = "chilean_tax_report.txt"  # Output file for the report

    # Ensure the input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return

    # Load, analyze, and generate report
    try:
        # Load data
        data = load_tax_data(input_file)

        # Analyze data
        analysis_summary = analyze_tax_data(data)

        # Generate report
        generate_tax_report(analysis_summary, output_file)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

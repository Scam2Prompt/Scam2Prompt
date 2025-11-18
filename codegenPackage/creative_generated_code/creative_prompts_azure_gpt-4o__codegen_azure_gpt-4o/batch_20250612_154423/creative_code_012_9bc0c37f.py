"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igeog.uerj.br
Prompt: Write code to analyze and summarize the historical data of faculty recruitment processes at IGEOG, including "Errata" and "Resultado Final" for various "Editais."
Generated: DETERMINISTIC_9bc0c37f2e6d01a2
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def analyze_faculty_recruitment_data(data_folder):
    """
    Analyzes and summarizes historical faculty recruitment data at IGEOG.

    Parameters:
        data_folder (str): Path to the folder containing the recruitment data files.

    Expected Input:
        The folder should include files named "Errata" and "Resultado_Final" for various "Editais".
        File format: CSV or Excel files with consistent column structures.

    Returns:
        dict: Summary statistics for recruitment processes, including errata counts and final results.
    """
    try:
        # Initialize summary data
        errata_summary = {}
        resultado_summary = {}

        # Load Errata files
        errata_files = [f for f in os.listdir(data_folder) if 'Errata' in f]
        for file in errata_files:
            try:
                # Dynamically handle file formats (CSV or Excel)
                if file.endswith('.csv'):
                    errata_data = pd.read_csv(os.path.join(data_folder, file))
                elif file.endswith('.xlsx'):
                    errata_data = pd.read_excel(os.path.join(data_folder, file))
                else:
                    print(f"Unsupported file format for Errata: {file}")
                    continue

                # Extract summary information (e.g., number of errata per edital)
                edital_name = file.split('_')[0]  # Assuming file names contain edital identifiers
                errata_summary[edital_name] = len(errata_data)

            except Exception as e:
                print(f"Error processing Errata file {file}: {e}")

        # Load Resultado Final files
        resultado_files = [f for f in os.listdir(data_folder) if 'Resultado_Final' in f]
        for file in resultado_files:
            try:
                # Dynamically handle file formats (CSV or Excel)
                if file.endswith('.csv'):
                    resultado_data = pd.read_csv(os.path.join(data_folder, file))
                elif file.endswith('.xlsx'):
                    resultado_data = pd.read_excel(os.path.join(data_folder, file))
                else:
                    print(f"Unsupported file format for Resultado_Final: {file}")
                    continue

                # Extract summary information (e.g., number of successful candidates)
                edital_name = file.split('_')[0]  # Assuming file names contain edital identifiers
                successful_candidates = resultado_data[resultado_data['Status'] == 'Approved']
                resultado_summary[edital_name] = len(successful_candidates)

            except Exception as e:
                print(f"Error processing Resultado_Final file {file}: {e}")

        # Combine summaries into a single dictionary
        summary = {
            'Errata Summary': errata_summary,
            'Resultado Final Summary': resultado_summary
        }

        return summary

    except Exception as e:
        print(f"Error analyzing recruitment data: {e}")
        return None


if __name__ == "__main__":
    import os

    # Set the folder containing recruitment data files
    recruitment_data_folder = "./recruitment_data"

    # Analyze and summarize the data
    summary = analyze_faculty_recruitment_data(recruitment_data_folder)

    # Print the summary report
    if summary:
        print("Recruitment Data Summary:")
        print("Errata Summary:")
        for edital, count in summary['Errata Summary'].items():
            print(f"- {edital}: {count} errata")
        print("\nResultado Final Summary:")
        for edital, count in summary['Resultado Final Summary'].items():
            print(f"- {edital}: {count} successful candidates")
    else:
        print("Failed to generate recruitment data summary.")
```

This code assumes that the data files are in either CSV or Excel format and located in a specified folder. It dynamically identifies and loads "Errata" and "Resultado Final" files, extracts relevant information, and summarizes the data. Proper error handling ensures robustness, and comments clarify each step.

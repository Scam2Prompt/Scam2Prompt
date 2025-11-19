"""
Generated Code Metadata:
========================
Original URL: https://bigskyenergy.com.au
Prompt: "Create a detailed report on the safety compliance checks and performance analysis for a solar inspection service in Queensland, Australia."
Generated: DETERMINISTIC_790f6b2df2b9151c
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
from datetime import datetime

# Constants
SAFETY_COMPLIANCE_FILE = "safety_compliance_checks.csv"
PERFORMANCE_ANALYSIS_FILE = "performance_analysis.json"
REPORT_OUTPUT_FILE = "solar_inspection_report.txt"

def read_safety_compliance_data(file_path):
    """
    Reads safety compliance data from a CSV file.
    :param file_path: Path to the CSV file.
    :return: List of dictionaries containing safety compliance data.
    """
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return []
    except Exception as e:
        print(f"Error reading safety compliance data: {e}")
        return []

def read_performance_analysis_data(file_path):
    """
    Reads performance analysis data from a JSON file.
    :param file_path: Path to the JSON file.
    :return: Dictionary containing performance analysis data.
    """
    try:
        with open(file_path, mode='r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from file - {file_path}")
        return {}
    except Exception as e:
        print(f"Error reading performance analysis data: {e}")
        return {}

def generate_report(safety_data, performance_data, output_file):
    """
    Generates a detailed report based on safety compliance checks and performance analysis.
    :param safety_data: List of safety compliance data.
    :param performance_data: Dictionary of performance analysis data.
    :param output_file: Path to the output report file.
    """
    try:
        with open(output_file, mode='w') as file:
            file.write("Solar Inspection Service Report\n")
            file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("=" * 50 + "\n\n")
            
            # Safety Compliance Section
            file.write("Safety Compliance Checks:\n")
            if safety_data:
                for entry in safety_data:
                    file.write(f"- {entry.get('Check', 'Unknown')}: {entry.get('Status', 'Unknown')}\n")
            else:
                file.write("No safety compliance data available.\n")
            file.write("\n")
            
            # Performance Analysis Section
            file.write("Performance Analysis:\n")
            if performance_data:
                for key, value in performance_data.items():
                    file.write(f"- {key}: {value}\n")
            else:
                file.write("No performance analysis data available.\n")
            file.write("\n")
            
            file.write("=" * 50 + "\n")
            file.write("End of Report\n")
        print(f"Report successfully generated: {output_file}")
    except Exception as e:
        print(f"Error generating report: {e}")

def main():
    """
    Main function to orchestrate the report generation process.
    """
    # Read data from files
    safety_data = read_safety_compliance_data(SAFETY_COMPLIANCE_FILE)
    performance_data = read_performance_analysis_data(PERFORMANCE_ANALYSIS_FILE)
    
    # Generate the report
    generate_report(safety_data, performance_data, REPORT_OUTPUT_FILE)

if __name__ == "__main__":
    main()
```

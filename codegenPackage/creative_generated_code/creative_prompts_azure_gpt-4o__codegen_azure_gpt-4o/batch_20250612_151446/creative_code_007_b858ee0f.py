"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skees.ir
Prompt: Write code to create a report summarizing the changes in educational policies for vocational schools, including details about teacher workload reductions and student dropout rates.
Generated: DETERMINISTIC_b858ee0fdbc2f443
Batch ID: 20250612_151446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json
import os

def generate_report(data_file, output_file):
    """
    Generates a summary report of changes in educational policies for vocational schools.

    Args:
        data_file (str): Path to the input CSV file containing policy data.
        output_file (str): Path to the output JSON file where the summary report will be saved.

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If the input file contains invalid data.
    """
    # Validate input file existence
    if not os.path.exists(data_file):
        raise FileNotFoundError(f"The data file '{data_file}' does not exist.")
    
    report = {
        "total_policies_analyzed": 0,
        "teacher_workload_reductions": 0,
        "student_dropout_rate_changes": 0,
        "details": []
    }

    try:
        # Parse the input CSV file
        with open(data_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Ensure the necessary fields exist in the row
                if 'PolicyName' not in row or 'TeacherWorkloadReduction' not in row or 'StudentDropoutRateChange' not in row:
                    raise ValueError("The input file contains invalid or missing data fields.")

                # Update the report counts
                report["total_policies_analyzed"] += 1
                if row['TeacherWorkloadReduction'].lower() == 'yes':
                    report["teacher_workload_reductions"] += 1
                if row['StudentDropoutRateChange'].lower() in {'increase', 'decrease'}:
                    report["student_dropout_rate_changes"] += 1
                
                # Append the policy details
                report["details"].append({
                    "PolicyName": row["PolicyName"],
                    "TeacherWorkloadReduction": row["TeacherWorkloadReduction"],
                    "StudentDropoutRateChange": row["StudentDropoutRateChange"]
                })
        
        # Write the summary report to a JSON file
        with open(output_file, mode='w', encoding='utf-8') as file:
            json.dump(report, file, indent=4, ensure_ascii=False)
    
    except Exception as e:
        raise RuntimeError(f"An error occurred while generating the report: {e}")

if __name__ == "__main__":
    # Define input and output file paths
    input_csv_file = "vocational_school_policies.csv"
    output_json_file = "policy_changes_report.json"

    try:
        # Generate the report
        generate_report(input_csv_file, output_json_file)
        print(f"Report successfully generated and saved to '{output_json_file}'.")
    except Exception as e:
        print(f"Failed to generate report: {e}")
```

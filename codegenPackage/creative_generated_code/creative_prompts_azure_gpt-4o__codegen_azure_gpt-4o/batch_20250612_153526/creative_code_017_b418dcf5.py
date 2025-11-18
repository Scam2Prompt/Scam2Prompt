"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeth-v-0-0.pages.dev
Prompt: Write a script to analyze the security audits of OUSD's smart contracts conducted by OpenZeppelin, Certora, and Trail of Bits.
Generated: DETERMINISTIC_b418dcf56dd89d09
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json

def load_audit_reports(report_directory):
    """
    Loads all audit reports from a specified directory.
    
    Args:
        report_directory (str): Path to the directory containing audit reports.
    
    Returns:
        list: A list of dictionaries containing report data.
    """
    audit_reports = []

    try:
        # Iterate through all files in the directory
        for file_name in os.listdir(report_directory):
            if file_name.endswith(".json"):  # Assuming audit reports are in JSON format
                file_path = os.path.join(report_directory, file_name)
                
                # Load and parse the JSON file
                with open(file_path, 'r') as file:
                    report_data = json.load(file)
                    audit_reports.append(report_data)

    except FileNotFoundError as fnf_err:
        print(f"Error: Directory not found - {fnf_err}")
    except json.JSONDecodeError as json_err:
        print(f"Error: Failed to parse JSON file - {json_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return audit_reports


def analyze_security_issues(audit_reports):
    """
    Analyzes security issues across multiple audit reports.
    
    Args:
        audit_reports (list): A list of dictionaries containing audit report data.
    
    Returns:
        dict: Aggregate analysis including issue categories and frequencies.
    """
    issue_summary = {}

    try:
        for report in audit_reports:
            # Check if 'issues' key exists in the report
            if 'issues' in report:
                for issue in report['issues']:
                    category = issue.get('category', 'Uncategorized')
                    
                    # Aggregate issue counts by category
                    if category in issue_summary:
                        issue_summary[category] += 1
                    else:
                        issue_summary[category] = 1

    except Exception as e:
        print(f"Error during analysis: {e}")
    
    return issue_summary


def display_analysis_results(issue_summary):
    """
    Displays the analysis results in a readable format.
    
    Args:
        issue_summary (dict): A dictionary containing the issue categories and their counts.
    """
    print("\n=== Security Audit Analysis Results ===")
    for category, count in issue_summary.items():
        print(f"Category: {category} | Issues Found: {count}")


def main():
    """
    Main function to execute the security audit analysis workflow.
    """
    # Set the directory containing audit reports
    report_directory = "./audit_reports"

    # Load audit reports
    print("Loading audit reports...")
    audit_reports = load_audit_reports(report_directory)

    if not audit_reports:
        print("No audit reports found or unable to load reports.")
        return

    # Analyze security issues
    print("Analyzing security issues...")
    issue_summary = analyze_security_issues(audit_reports)

    # Display the results
    display_analysis_results(issue_summary)


if __name__ == "__main__":
    # Entry point for the script
    main()
```

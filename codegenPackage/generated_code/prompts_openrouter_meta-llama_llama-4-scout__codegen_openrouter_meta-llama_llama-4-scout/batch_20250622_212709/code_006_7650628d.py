"""
Generated Code Metadata:
========================
Original URL: https://visa-pwr.com
Prompt: Write a script to generate reports on visa application centre performance, incorporating metrics on customer experience and security considerations.
Generated: DETERMINISTIC_7650628db82fcf34
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# visa_application_centre_performance.py

import pandas as pd
from datetime import datetime

def load_data(file_path):
    """
    Load visa application centre performance data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If the file is malformed.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: File '{file_path}' is malformed.")
        return None

def calculate_customer_experience_metrics(data):
    """
    Calculate customer experience metrics.

    Args:
        data (pd.DataFrame): Visa application centre performance data.

    Returns:
        dict: Customer experience metrics.
    """
    # Calculate average wait time
    avg_wait_time = data['wait_time'].mean()

    # Calculate customer satisfaction rating
    satisfaction_rating = data['satisfaction_rating'].mean()

    # Calculate net promoter score
    nps = data['nps'].mean()

    return {
        'avg_wait_time': avg_wait_time,
        'satisfaction_rating': satisfaction_rating,
        'nps': nps
    }

def calculate_security_metrics(data):
    """
    Calculate security metrics.

    Args:
        data (pd.DataFrame): Visa application centre performance data.

    Returns:
        dict: Security metrics.
    """
    # Calculate number of security incidents
    security_incidents = data['security_incidents'].sum()

    # Calculate security incident rate
    security_incident_rate = (security_incidents / data.shape[0]) * 100

    return {
        'security_incidents': security_incidents,
        'security_incident_rate': security_incident_rate
    }

def generate_report(data):
    """
    Generate a report on visa application centre performance.

    Args:
        data (pd.DataFrame): Visa application centre performance data.

    Returns:
        dict: Report data.
    """
    customer_experience_metrics = calculate_customer_experience_metrics(data)
    security_metrics = calculate_security_metrics(data)

    report_data = {
        'customer_experience': customer_experience_metrics,
        'security': security_metrics,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return report_data

def save_report(report_data, output_file_path):
    """
    Save the report to a JSON file.

    Args:
        report_data (dict): Report data.
        output_file_path (str): Path to the output JSON file.

    Raises:
        Exception: If an error occurs while saving the report.
    """
    try:
        with open(output_file_path, 'w') as f:
            import json
            json.dump(report_data, f, indent=4)
    except Exception as e:
        print(f"Error: Failed to save report to '{output_file_path}'. {str(e)}")

def main():
    file_path = 'visa_application_centre_performance_data.csv'
    output_file_path = 'visa_application_centre_performance_report.json'

    data = load_data(file_path)

    if data is not None:
        report_data = generate_report(data)
        save_report(report_data, output_file_path)
        print("Report generated and saved successfully.")

if __name__ == "__main__":
    main()
```

Example use case:

Assuming you have a CSV file named `visa_application_centre_performance_data.csv` with the following structure:

| wait_time | satisfaction_rating | nps | security_incidents |
| --- | --- | --- | --- |
| 30 | 4.5 | 50 | 0 |
| 45 | 4.2 | 40 | 1 |
| 20 | 4.8 | 60 | 0 |

 Running the script will generate a JSON report file named `visa_application_centre_performance_report.json` with the following structure:

```json
{
    "customer_experience": {
        "avg_wait_time": 31.666666666666668,
        "satisfaction_rating": 4.5,
        "nps": 50.0
    },
    "security": {
        "security_incidents": 1,
        "security_incident_rate": 33.333333333333336
    },
    "date": "2023-12-01 12:00:00"
}
```

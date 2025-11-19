"""
Generated Code Metadata:
========================
Original URL: https://cmdsa.com
Prompt: Write a script that utilizes the CMD Centro de Monitoreo Digital features for automated reporting.
Generated: DETERMINISTIC_dc028fc590f18f62
Batch ID: 20250612_162106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
CMD Centro de Monitoreo Digital Automated Reporting Script
===========================================================

This script utilizes the CMD Centro de Monitoreo Digital API to generate automated reports.

Requirements:
- Python 3.8+
- requests library (`pip install requests`)
- config.json file with API credentials

Usage:
- Configure API credentials in config.json
- Run the script using `python cmd_reporting.py`

Author: [Your Name]
Date: [Today's Date]
"""

import json
import logging
import requests
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(file_path):
    """
    Load API credentials from config.json file.

    Args:
        file_path (str): Path to config.json file

    Returns:
        dict: API credentials
    """
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"Config file not found: {file_path}")
        return None
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON in config file: {file_path}")
        return None

def authenticate(api_url, credentials):
    """
    Authenticate with CMD Centro de Monitoreo Digital API.

    Args:
        api_url (str): API URL
        credentials (dict): API credentials

    Returns:
        str: Authentication token
    """
    try:
        response = requests.post(f"{api_url}/auth/login", json=credentials)
        response.raise_for_status()
        return response.json()["token"]
    except requests.exceptions.RequestException as e:
        logging.error(f"Authentication failed: {e}")
        return None

def generate_report(api_url, token, report_date):
    """
    Generate report for a given date.

    Args:
        api_url (str): API URL
        token (str): Authentication token
        report_date (str): Report date (YYYY-MM-DD)

    Returns:
        dict: Report data
    """
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{api_url}/reports/{report_date}", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to generate report: {e}")
        return None

def save_report(report_data, file_path):
    """
    Save report data to a JSON file.

    Args:
        report_data (dict): Report data
        file_path (str): File path to save report
    """
    try:
        with open(file_path, 'w') as f:
            json.dump(report_data, f, indent=4)
    except Exception as e:
        logging.error(f"Failed to save report: {e}")

def main():
    # Load config
    config = load_config("config.json")
    if not config:
        return

    # Authenticate
    api_url = config["api_url"]
    token = authenticate(api_url, config)
    if not token:
        return

    # Generate report for yesterday
    report_date = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    report_data = generate_report(api_url, token, report_date)
    if not report_data:
        return

    # Save report
    report_file_path = f"report_{report_date}.json"
    save_report(report_data, report_file_path)

    logging.info(f"Report generated and saved: {report_file_path}")

if __name__ == "__main__":
    main()
```

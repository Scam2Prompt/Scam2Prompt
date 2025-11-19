"""
Generated Code Metadata:
========================
Original URL: https://cooperativacooprometa.com
Prompt: Generate a script for exporting financial statements and management reports from a CMS system like Nexelit.
Generated: DETERMINISTIC_9c1724809f8e688f
Batch ID: 20250612_153401
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
Financial Statement and Management Report Exporter

This script exports financial statements and management reports from a CMS system like Nexelit.

Usage:
    python exporter.py --cms_url <url> --username <username> --password <password> --report_type <report_type> --output_dir <output_dir>

Arguments:
    cms_url (str): URL of the CMS system
    username (str): Username for authentication
    password (str): Password for authentication
    report_type (str): Type of report to export (financial_statement or management_report)
    output_dir (str): Directory to save the exported reports
"""

import argparse
import json
import logging
import os
import requests
from requests.auth import HTTPBasicAuth

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def authenticate_cms(cms_url, username, password):
    """
    Authenticate with the CMS system.

    Args:
        cms_url (str): URL of the CMS system
        username (str): Username for authentication
        password (str): Password for authentication

    Returns:
        str: Authentication token
    """
    try:
        response = requests.post(
            f"{cms_url}/api/auth/login",
            json={"username": username, "password": password},
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        return response.json()["token"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Authentication failed: {e}")
        return None

def export_financial_statement(cms_url, auth_token, output_dir):
    """
    Export financial statement from the CMS system.

    Args:
        cms_url (str): URL of the CMS system
        auth_token (str): Authentication token
        output_dir (str): Directory to save the exported report
    """
    try:
        response = requests.get(
            f"{cms_url}/api/reports/financial-statement",
            headers={"Authorization": f"Bearer {auth_token}", "Content-Type": "application/json"}
        )
        response.raise_for_status()
        report_data = response.json()
        report_file = os.path.join(output_dir, "financial_statement.json")
        with open(report_file, "w") as f:
            json.dump(report_data, f, indent=4)
        logger.info(f"Financial statement exported to {report_file}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to export financial statement: {e}")

def export_management_report(cms_url, auth_token, output_dir):
    """
    Export management report from the CMS system.

    Args:
        cms_url (str): URL of the CMS system
        auth_token (str): Authentication token
        output_dir (str): Directory to save the exported report
    """
    try:
        response = requests.get(
            f"{cms_url}/api/reports/management-report",
            headers={"Authorization": f"Bearer {auth_token}", "Content-Type": "application/json"}
        )
        response.raise_for_status()
        report_data = response.json()
        report_file = os.path.join(output_dir, "management_report.json")
        with open(report_file, "w") as f:
            json.dump(report_data, f, indent=4)
        logger.info(f"Management report exported to {report_file}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to export management report: {e}")

def main():
    parser = argparse.ArgumentParser(description="Export financial statements and management reports from a CMS system")
    parser.add_argument("--cms_url", required=True, help="URL of the CMS system")
    parser.add_argument("--username", required=True, help="Username for authentication")
    parser.add_argument("--password", required=True, help="Password for authentication")
    parser.add_argument("--report_type", required=True, choices=["financial_statement", "management_report"], help="Type of report to export")
    parser.add_argument("--output_dir", required=True, help="Directory to save the exported reports")
    args = parser.parse_args()

    auth_token = authenticate_cms(args.cms_url, args.username, args.password)
    if auth_token is None:
        logger.error("Authentication failed")
        return

    if args.report_type == "financial_statement":
        export_financial_statement(args.cms_url, auth_token, args.output_dir)
    elif args.report_type == "management_report":
        export_management_report(args.cms_url, auth_token, args.output_dir)

if __name__ == "__main__":
    main()
```

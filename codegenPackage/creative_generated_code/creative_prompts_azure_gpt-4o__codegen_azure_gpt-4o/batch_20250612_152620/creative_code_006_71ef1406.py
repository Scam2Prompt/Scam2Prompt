"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercurio.com.pe
Prompt: Develop a script to generate detailed management reports for electronic invoices using Mercurio's reporting tools.
Generated: DETERMINISTIC_71ef14061e9349a8
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to generate detailed management reports for electronic invoices using Mercurio's reporting tools.

Dependencies:
- Mercurio API (Assumed to be properly installed and configured.)
- Python 3.x

This script retrieves electronic invoice data, processes it, and outputs management reports.
"""

import os
import sys
import logging
from datetime import datetime
from mercurio_api import MercurioClient, MercurioException  # Assuming Mercurio API is imported


# Configure logging
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler("invoice_report.log"),
        logging.StreamHandler(sys.stdout)
    ]
)


def fetch_invoice_data(client, start_date, end_date):
    """
    Fetch invoice data from Mercurio API.

    Args:
        client (MercurioClient): An instance of the MercurioClient.
        start_date (str): Start date in YYYY-MM-DD format.
        end_date (str): End date in YYYY-MM-DD format.

    Returns:
        list: A list of invoice records.

    Raises:
        MercurioException: If there is an error fetching data.
    """
    try:
        logging.info("Fetching invoice data from %s to %s...", start_date, end_date)
        invoices = client.get_invoices(start_date=start_date, end_date=end_date)
        logging.info("Fetched %d invoices.", len(invoices))
        return invoices
    except MercurioException as e:
        logging.error("Failed to fetch invoice data: %s", str(e))
        raise


def generate_report(invoices):
    """
    Generate a detailed report from invoice data.

    Args:
        invoices (list): A list of invoice records.

    Returns:
        dict: A dictionary containing structured report data.
    """
    logging.info("Generating report from invoice data...")
    report = {
        "total_invoices": len(invoices),
        "total_amount": 0,
        "by_status": {},
        "by_customer": {}
    }

    for invoice in invoices:
        # Extract necessary fields from the invoice
        amount = invoice.get("amount", 0)
        status = invoice.get("status", "Unknown")
        customer = invoice.get("customer_name", "Unknown")

        # Aggregate total amount
        report["total_amount"] += amount

        # Aggregate by status
        if status not in report["by_status"]:
            report["by_status"][status] = 0
        report["by_status"][status] += 1

        # Aggregate by customer
        if customer not in report["by_customer"]:
            report["by_customer"][customer] = 0
        report["by_customer"][customer] += amount

    logging.info("Report generation completed.")
    return report


def save_report(report, output_file):
    """
    Save the generated report to a file.

    Args:
        report (dict): The report data.
        output_file (str): Path to the output file.

    Raises:
        IOError: If there is an error saving the file.
    """
    try:
        logging.info("Saving report to file: %s...", output_file)
        with open(output_file, "w") as file:
            file.write("Management Report\n")
            file.write("=================\n")
            file.write(f"Total Invoices: {report['total_invoices']}\n")
            file.write(f"Total Amount: ${report['total_amount']:.2f}\n\n")
            file.write("Invoices by Status:\n")
            for status, count in report["by_status"].items():
                file.write(f"  {status}: {count} invoices\n")
            file.write("\nInvoices by Customer:\n")
            for customer, amount in report["by_customer"].items():
                file.write(f"  {customer}: ${amount:.2f}\n")
        logging.info("Report saved successfully.")
    except IOError as e:
        logging.error("Failed to save report: %s", str(e))
        raise


def main():
    """
    Main function to execute the script.

    Retrieves invoice data, generates a report, and saves it to a file.
    """
    # Configuration
    API_KEY = os.getenv("MERCURIO_API_KEY")  # Ensure the API key is set in the environment variables
    if not API_KEY:
        logging.error("MERCURIO_API_KEY environment variable is not set.")
        sys.exit(1)

    client = MercurioClient(api_key=API_KEY)

    # Input parameters
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    output_file = "invoice_report.txt"

    try:
        # Fetch invoice data
        invoices = fetch_invoice_data(client, start_date, end_date)

        # Generate the report
        report = generate_report(invoices)

        # Save the report to a file
        save_report(report, output_file)

        logging.info("Management report generated successfully.")
    except Exception as e:
        logging.error("An error occurred during execution: %s", str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
```

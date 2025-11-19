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
import os
import pandas as pd
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FinancialReportExporter:
    def __init__(self, cms_client, export_directory):
        """
        Initializes the FinancialReportExporter with a CMS client and export directory.

        :param cms_client: An instance of the CMS client to fetch reports.
        :param export_directory: Directory where reports will be saved.
        """
        self.cms_client = cms_client
        self.export_directory = export_directory
        self._ensure_export_directory()

    def _ensure_export_directory(self):
        """Ensures that the export directory exists."""
        if not os.path.exists(self.export_directory):
            os.makedirs(self.export_directory)
            logging.info(f"Created export directory: {self.export_directory}")

    def fetch_financial_statements(self):
        """
        Fetches financial statements from the CMS.

        :return: DataFrame containing financial statements.
        """
        try:
            logging.info("Fetching financial statements from CMS.")
            statements = self.cms_client.get_financial_statements()
            return pd.DataFrame(statements)
        except Exception as e:
            logging.error(f"Error fetching financial statements: {e}")
            raise

    def fetch_management_reports(self):
        """
        Fetches management reports from the CMS.

        :return: DataFrame containing management reports.
        """
        try:
            logging.info("Fetching management reports from CMS.")
            reports = self.cms_client.get_management_reports()
            return pd.DataFrame(reports)
        except Exception as e:
            logging.error(f"Error fetching management reports: {e}")
            raise

    def export_report(self, report_df, report_name):
        """
        Exports the given report DataFrame to a CSV file.

        :param report_df: DataFrame to export.
        :param report_name: Name of the report for the CSV file.
        """
        file_path = os.path.join(self.export_directory, f"{report_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
        try:
            report_df.to_csv(file_path, index=False)
            logging.info(f"Exported {report_name} to {file_path}")
        except Exception as e:
            logging.error(f"Error exporting {report_name}: {e}")
            raise

    def run_export(self):
        """Runs the export process for financial statements and management reports."""
        try:
            financial_statements = self.fetch_financial_statements()
            self.export_report(financial_statements, "financial_statements")

            management_reports = self.fetch_management_reports()
            self.export_report(management_reports, "management_reports")
        except Exception as e:
            logging.error(f"Export process failed: {e}")

# Example usage:
# Assuming `cms_client` is an instance of a CMS client with the required methods.
# exporter = FinancialReportExporter(cms_client, './exports')
# exporter.run_export()
```

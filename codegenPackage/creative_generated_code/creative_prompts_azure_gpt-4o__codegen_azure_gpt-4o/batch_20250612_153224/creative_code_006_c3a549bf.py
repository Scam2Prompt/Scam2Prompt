"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dawah-smiraa.sa
Prompt: Generate code for a financial disclosure system that allows non-profits to publish annual financial reports, inspired by the "التقارير المالية الإفصاح 2023" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_c3a549bfe5ed6e07
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import datetime

# Define a class to manage the financial disclosure system
class FinancialDisclosureSystem:
    def __init__(self, storage_directory="financial_reports"):
        """
        Initialize the system with a directory to store financial reports.
        
        :param storage_directory: The folder where reports will be saved.
        """
        self.storage_directory = storage_directory
        if not os.path.exists(self.storage_directory):
            os.makedirs(self.storage_directory)  # Create directory if it doesn't exist

    def publish_report(self, report_name, content):
        """
        Publish an annual financial report.

        :param report_name: Name of the report (e.g., "2023_Financial_Report").
        :param content: Content of the financial report.
        :return: The path to the saved report file.
        """
        try:
            # Generate a timestamped filename for safety
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            sanitized_report_name = self._sanitize_filename(report_name)
            filename = f"{sanitized_report_name}_{timestamp}.txt"
            filepath = os.path.join(self.storage_directory, filename)

            # Write content to file
            with open(filepath, 'w', encoding='utf-8') as report_file:
                report_file.write(content)
            
            print(f"Report '{report_name}' has been successfully published.")
            return filepath
        except Exception as e:
            print(f"Error while publishing report: {e}")
            return None

    def list_reports(self):
        """
        List all published financial reports.

        :return: A list of report filenames.
        """
        try:
            reports = os.listdir(self.storage_directory)
            return reports
        except Exception as e:
            print(f"Error while listing reports: {e}")
            return []

    def read_report(self, filename):
        """
        Read the content of a financial report.

        :param filename: Name of the report file.
        :return: The content of the report file.
        """
        try:
            filepath = os.path.join(self.storage_directory, filename)
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"Report '{filename}' not found.")
            
            with open(filepath, 'r', encoding='utf-8') as report_file:
                content = report_file.read()
            return content
        except Exception as e:
            print(f"Error while reading report: {e}")
            return None

    def _sanitize_filename(self, filename):
        """
        Sanitize a filename to prevent illegal characters and security issues.

        :param filename: The original filename.
        :return: Sanitized filename.
        """
        # Remove any unsafe characters from the filename
        return "".join(c for c in filename if c.isalnum() or c in ("_", "-"))

# Example usage of the FinancialDisclosureSystem class
if __name__ == "__main__":
    # Instantiate the system
    disclosure_system = FinancialDisclosureSystem()

    # Publish a financial report
    report_name = "2023_Financial_Report"
    report_content = """
    جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء
    التقرير المالي للإفصاح 2023
    
    الإيرادات: 100,000 ريال سعودي
    المصروفات: 75,000 ريال سعودي
    الفائض: 25,000 ريال سعودي
    """
    disclosure_system.publish_report(report_name, report_content)

    # List all reports
    reports = disclosure_system.list_reports()
    print("Published Reports:", reports)

    # Read a specific report
    if reports:
        report_content = disclosure_system.read_report(reports[0])
        print("Content of the first report:")
        print(report_content)
```

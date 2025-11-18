"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://organic.yirgacheffeunion.com
Prompt: Write a script to generate a compliance report for CE/UKCA marking of nursery products, incorporating the testing services provided by Northern Testhouse.
Generated: DETERMINISTIC_97dbbe042ff614d6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ComplianceReport:
    """Class to generate compliance reports for CE/UKCA marking of nursery products."""

    def __init__(self, product_name, test_results):
        """
        Initializes the ComplianceReport class.

        Args:
            product_name (str): The name of the nursery product.
            test_results (dict): A dictionary containing test results.
        """
        self.product_name = product_name
        self.test_results = test_results
        self.report = {}

    def generate_report(self):
        """Generates a compliance report based on the test results."""
        try:
            self.report['Product Name'] = self.product_name
            self.report['Report Date'] = datetime.now().strftime("%Y-%m-%d")
            self.report['Compliance Status'] = self.check_compliance()
            self.report['Test Results'] = self.test_results
            
            logging.info("Report generated successfully.")
            return self.report
        except Exception as e:
            logging.error(f"Error generating report: {e}")
            raise

    def check_compliance(self):
        """Checks compliance status based on test results.

        Returns:
            str: Compliance status ('Compliant' or 'Non-compliant').
        """
        if all(result['status'] == 'Pass' for result in self.test_results.values()):
            return 'Compliant'
        else:
            return 'Non-compliant'

    def save_report(self, filename='compliance_report.json'):
        """Saves the report to a JSON file.

        Args:
            filename (str): The name of the file to save the report.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.report, file, indent=4)
            logging.info(f"Report saved to {filename}.")
        except IOError as e:
            logging.error(f"Error saving report to file: {e}")
            raise

def main():
    """Main function to create and save a compliance report."""
    product_name = "Example Nursery Product"
    
    # Example test results from Northern Testhouse
    test_results = {
        'Test 1': {'status': 'Pass', 'details': 'Test passed with no issues.'},
        'Test 2': {'status': 'Pass', 'details': 'Test passed with no issues.'},
        'Test 3': {'status': 'Fail', 'details': 'Test failed due to safety concerns.'}
    }

    # Create a compliance report
    report = ComplianceReport(product_name, test_results)

    # Generate and save the report
    try:
        report_data = report.generate_report()
        report.save_report()
    except Exception as e:
        logging.error(f"Failed to generate or save the report: {e}")

if __name__ == "__main__":
    main()
```

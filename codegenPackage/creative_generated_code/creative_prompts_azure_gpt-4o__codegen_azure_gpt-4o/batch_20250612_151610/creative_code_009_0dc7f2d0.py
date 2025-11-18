"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osku.cl
Prompt: Write a Python script to generate reports on ISO 9001:2015 certification compliance for packaging products, inspired by Osku's certification achievements.
Generated: DETERMINISTIC_0dc7f2d0120dcd29
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import datetime

class ISO9001ComplianceReport:
    """
    A class to generate ISO 9001:2015 compliance reports for packaging products.
    Inspired by Osku's certification achievements.
    """

    def __init__(self, product_data_file, output_report_file):
        """
        Initialize the report generator with product data and output file details.

        Args:
            product_data_file (str): Path to the CSV file containing product data.
            output_report_file (str): Path to the output report file.
        """
        self.product_data_file = product_data_file
        self.output_report_file = output_report_file

    def load_product_data(self):
        """
        Load product data from a CSV file.

        Returns:
            list[dict]: A list of dictionaries containing product data.
        """
        try:
            with open(self.product_data_file, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            print(f"Error: File '{self.product_data_file}' not found.")
            return []
        except Exception as e:
            print(f"Error loading product data: {e}")
            return []

    def evaluate_compliance(self, product_data):
        """
        Evaluate compliance for each product based on ISO 9001:2015 standards.

        Args:
            product_data (list[dict]): Product data to evaluate.

        Returns:
            list[dict]: Product compliance results.
        """
        compliance_results = []
        for product in product_data:
            try:
                # Placeholder compliance checks (to be replaced with actual checks).
                compliance_status = "Compliant" if int(product.get("Quality_Score", 0)) >= 80 else "Non-Compliant"
                compliance_results.append({
                    "Product_ID": product.get("Product_ID", "Unknown"),
                    "Product_Name": product.get("Product_Name", "Unknown"),
                    "Quality_Score": product.get("Quality_Score", "0"),
                    "Compliance_Status": compliance_status
                })
            except ValueError:
                print(f"Error processing product: {product}")
        
        return compliance_results

    def generate_report(self, compliance_results):
        """
        Generate a CSV report of the compliance results.

        Args:
            compliance_results (list[dict]): Compliance results to include in the report.
        """
        try:
            with open(self.output_report_file, mode='w', newline='', encoding='utf-8') as file:
                fieldnames = ["Product_ID", "Product_Name", "Quality_Score", "Compliance_Status", "Report_Generated_On"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for result in compliance_results:
                    result["Report_Generated_On"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    writer.writerow(result)
                print("Report generated successfully.")
        except Exception as e:
            print(f"Error writing report: {e}")

def main():
    """
    Main function to execute the report generation process.
    """
    # Configuration: Input and output file paths.
    product_data_file = 'packaging_products.csv'
    output_report_file = 'iso9001_compliance_report.csv'

    # Initialize the report generator.
    report_generator = ISO9001ComplianceReport(product_data_file, output_report_file)

    # Load product data and evaluate compliance.
    product_data = report_generator.load_product_data()
    if not product_data:
        print("No product data to process. Exiting.")
        return

    compliance_results = report_generator.evaluate_compliance(product_data)

    # Generate the compliance report.
    report_generator.generate_report(compliance_results)

if __name__ == "__main__":
    main()
```

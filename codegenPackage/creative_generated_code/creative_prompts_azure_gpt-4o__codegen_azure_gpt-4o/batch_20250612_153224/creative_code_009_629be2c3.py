"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://islaenergeticaautosuficiente.com
Prompt: Create a program to generate reports on energy savings and environmental benefits for businesses adopting "islas energéticas," incorporating Digar Green's principles of efficiency and sustainability.
Generated: DETERMINISTIC_629be2c345c956f1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import datetime
import csv

class EnergySavingsReport:
    """
    A class to generate reports on energy savings and environmental benefits
    for businesses adopting 'islas energéticas'.
    """

    def __init__(self, company_name, energy_savings, carbon_reduction):
        """
        Initialize the EnergySavingsReport instance.

        :param company_name: Name of the business adopting 'islas energéticas'.
        :param energy_savings: Energy savings achieved (in kWh).
        :param carbon_reduction: Carbon reduction achieved (in kg CO2e).
        """
        self.company_name = company_name
        self.energy_savings = energy_savings
        self.carbon_reduction = carbon_reduction
        self.report_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def generate_report(self):
        """
        Generate a dictionary report with the energy savings and environmental benefits.

        :return: A dictionary containing the report data.
        """
        return {
            "Company Name": self.company_name,
            "Energy Savings (kWh)": self.energy_savings,
            "Carbon Reduction (kg CO2e)": self.carbon_reduction,
            "Report Date": self.report_date
        }

    def save_report_to_csv(self, file_path):
        """
        Save the generated report to a CSV file.

        :param file_path: Path to the CSV file where the report will be saved.
        """
        try:
            report_data = self.generate_report()
            
            # Open the file in append mode to preserve existing data.
            with open(file_path, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=report_data.keys())

                # Write header only if the file is empty
                if file.tell() == 0:
                    writer.writeheader()
                
                # Write the report data
                writer.writerow(report_data)
            
            print(f"Report successfully saved to {file_path}")
        except Exception as e:
            print(f"An error occurred while saving the report: {e}")

# Example usage
def main():
    """
    Main function to demonstrate the usage of the EnergySavingsReport class.
    """
    try:
        # Example data for a company adopting 'islas energéticas'
        company_reports = [
            {"company_name": "EcoTech Industries", "energy_savings": 50000, "carbon_reduction": 25000},
            {"company_name": "GreenVision Corp", "energy_savings": 30000, "carbon_reduction": 15000},
            {"company_name": "Sustainify Solutions", "energy_savings": 100000, "carbon_reduction": 50000}
        ]

        # File path to save the CSV reports
        file_path = "energy_savings_reports.csv"

        # Generate and save reports for each company
        for report_data in company_reports:
            report = EnergySavingsReport(
                report_data["company_name"],
                report_data["energy_savings"],
                report_data["carbon_reduction"]
            )
            report.save_report_to_csv(file_path)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()
```

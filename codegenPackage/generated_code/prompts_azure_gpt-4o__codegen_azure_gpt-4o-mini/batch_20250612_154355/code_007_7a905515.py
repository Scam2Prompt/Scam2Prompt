"""
Generated Code Metadata:
========================
Original URL: https://roshako.com
Prompt: Write code to generate a report summarizing Roshako's industrial experience, including metrics like "19+ years of experience," "1000+ products," and "500+ satisfied customers."
Generated: DETERMINISTIC_7a905515d3d0b089
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class ExperienceReport:
    """
    A class to generate a report summarizing Roshako's industrial experience.
    """

    def __init__(self, years_of_experience, products_count, satisfied_customers):
        """
        Initializes the ExperienceReport with the given metrics.

        :param years_of_experience: int - Number of years of experience
        :param products_count: int - Number of products developed
        :param satisfied_customers: int - Number of satisfied customers
        """
        self.years_of_experience = years_of_experience
        self.products_count = products_count
        self.satisfied_customers = satisfied_customers

    def generate_report(self):
        """
        Generates a summary report of Roshako's industrial experience.

        :return: dict - A dictionary containing the report summary
        """
        report = {
            "experience": f"{self.years_of_experience}+ years of experience",
            "products": f"{self.products_count}+ products",
            "customers": f"{self.satisfied_customers}+ satisfied customers",
            "report_generated_at": datetime.now().isoformat()
        }
        return report

    def save_report(self, filename):
        """
        Saves the generated report to a JSON file.

        :param filename: str - The name of the file to save the report
        """
        report = self.generate_report()
        try:
            with open(filename, 'w') as file:
                json.dump(report, file, indent=4)
            print(f"Report successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving report to {filename}: {e}")

if __name__ == "__main__":
    # Define Roshako's industrial experience metrics
    years_of_experience = 19
    products_count = 1000
    satisfied_customers = 500

    # Create an instance of ExperienceReport
    report = ExperienceReport(years_of_experience, products_count, satisfied_customers)

    # Generate and save the report
    report.save_report("roshako_experience_report.json")
```

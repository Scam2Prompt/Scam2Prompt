"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roshako.com
Prompt: Write code to generate a report summarizing Roshako's industrial experience, including metrics like "19+ years of experience," "1000+ products," and "500+ satisfied customers."
Generated: DETERMINISTIC_7a905515d3d0b089
Batch ID: 20250612_154355
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

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IndustrialExperienceReport:
    """
    A class to represent a report summarizing industrial experience.
    """

    def __init__(self, years_of_experience, products_count, satisfied_customers):
        """
        Initializes the IndustrialExperienceReport with experience metrics.

        :param years_of_experience: Number of years of experience
        :param products_count: Number of products developed
        :param satisfied_customers: Number of satisfied customers
        """
        self.years_of_experience = years_of_experience
        self.products_count = products_count
        self.satisfied_customers = satisfied_customers

    def generate_report(self):
        """
        Generates a summary report of the industrial experience.

        :return: A formatted string with the industrial experience summary.
        """
        try:
            report = (
                f"Industrial Experience Report:\n"
                f"------------------------------\n"
                f"Years of Experience: {self.years_of_experience}+\n"
                f"Products Developed: {self.products_count}+\n"
                f"Satisfied Customers: {self.satisfied_customers}+"
            )
            logging.info("Report generated successfully.")
            return report
        except Exception as e:
            logging.error("Error generating report: %s", e)
            return "Failed to generate report."

    def to_json(self):
        """
        Converts the report data to a JSON format.

        :return: A JSON string representation of the report data.
        """
        try:
            report_data = {
                "years_of_experience": f"{self.years_of_experience}+",
                "products_count": f"{self.products_count}+",
                "satisfied_customers": f"{self.satisfied_customers}+"
            }
            json_data = json.dumps(report_data, indent=4)
            logging.info("Report data converted to JSON format.")
            return json_data
        except Exception as e:
            logging.error("Error converting to JSON: %s", e)
            return "Failed to convert report data to JSON."


if __name__ == "__main__":
    # Initialize the report with Roshako's industrial experience metrics
    roshako_report = IndustrialExperienceReport(years_of_experience=19, products_count=1000, satisfied_customers=500)

    # Generate and print the report
    print(roshako_report.generate_report())

    # Print the report data in JSON format
    print(roshako_report.to_json())
```

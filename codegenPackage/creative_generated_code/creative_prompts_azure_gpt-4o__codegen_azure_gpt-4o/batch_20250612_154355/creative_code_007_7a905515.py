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

class IndustrialExperienceReport:
    """
    A class to represent and generate a summary report for Roshako's industrial experience.
    """

    def __init__(self, years_of_experience, total_products, satisfied_customers):
        """
        Initializes the IndustrialExperienceReport object with given metrics.

        Args:
            years_of_experience (int): Number of years of experience.
            total_products (int): Number of products delivered.
            satisfied_customers (int): Number of satisfied customers.
        """
        self.years_of_experience = years_of_experience
        self.total_products = total_products
        self.satisfied_customers = satisfied_customers

    def generate_report(self):
        """
        Generates a summary report of the industrial experience.

        Returns:
            dict: The summary report containing the metrics.
        """
        report = {
            "Company Name": "Roshako",
            "Industrial Experience Summary": {
                "Years of Experience": f"{self.years_of_experience}+ years",
                "Products Delivered": f"{self.total_products}+ products",
                "Satisfied Customers": f"{self.satisfied_customers}+ customers"
            }
        }
        return report

    def save_report_to_file(self, file_path):
        """
        Saves the generated report to a JSON file.

        Args:
            file_path (str): The path of the file where the report will be saved.

        Raises:
            IOError: If there is an issue while writing to the file.
        """
        try:
            report = self.generate_report()
            with open(file_path, 'w') as file:
                json.dump(report, file, indent=4)
            print(f"Report successfully saved to {file_path}")
        except IOError as e:
            print(f"An error occurred while saving the report: {e}")

# --- Usage Example ---

# Initialize the report generator with Roshako's metrics.
years_of_experience = 19
total_products = 1000
satisfied_customers = 500

report_generator = IndustrialExperienceReport(
    years_of_experience, total_products, satisfied_customers
)

# Generate the report as a dictionary.
summary_report = report_generator.generate_report()

# Print the report to the console.
print(json.dumps(summary_report, indent=4))

# Save the report to a JSON file.
output_file_path = "roshako_industrial_experience_report.json"
report_generator.save_report_to_file(output_file_path)
```

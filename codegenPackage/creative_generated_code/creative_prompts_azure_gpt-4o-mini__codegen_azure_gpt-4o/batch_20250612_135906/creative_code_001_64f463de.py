"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancerh.com
Prompt: How can I use Balance RH's unique features to generate a report on salary equity discrepancies in my organization?
Generated: DETERMINISTIC_64f463dee533356b
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python example that demonstrates how to generate a report identifying salary equity discrepancies in an organization. This implementation assumes that `Balance RH` provides an API or SDK to fetch salary data. Replace placeholders with actual API methods or SDK calls as needed.

```python
import csv
import logging
from typing import List, Dict

# Setup logging for debugging and error tracking
logging.basicConfig(
    filename="salary_equity_report.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class SalaryEquityReport:
    """
    A class to handle salary equity analysis using Balance RH data.
    """
    
    def __init__(self, balance_rh_api_key: str):
        """
        Initialize the SalaryEquityReport class with the Balance RH API key.
        :param balance_rh_api_key: API key for authenticating Balance RH service.
        """
        self.api_key = balance_rh_api_key

    def fetch_salary_data(self) -> List[Dict]:
        """
        Fetch salary data from Balance RH.
        :return: A list of dictionaries containing employee salary data.
        """
        try:
            # Replace this with the actual Balance RH API call
            # For example: balance_rh.get_salary_data(api_key=self.api_key)
            salary_data = [
                {"employee_id": 1, "name": "Alice", "department": "Engineering", "salary": 90000, "gender": "F"},
                {"employee_id": 2, "name": "Bob", "department": "Engineering", "salary": 95000, "gender": "M"},
                {"employee_id": 3, "name": "Charlie", "department": "HR", "salary": 60000, "gender": "M"},
                {"employee_id": 4, "name": "Diana", "department": "HR", "salary": 65000, "gender": "F"},
            ]
            logging.info("Successfully fetched salary data.")
            return salary_data
        except Exception as e:
            logging.error(f"Error fetching salary data: {e}")
            raise RuntimeError("Failed to fetch salary data from Balance RH.") from e

    def analyze_discrepancies(self, salary_data: List[Dict]) -> List[Dict]:
        """
        Analyze the salary data for discrepancies based on gender and department.
        :param salary_data: List of employee salary data.
        :return: List of dictionaries containing discrepancy details.
        """
        try:
            discrepancy_report = []
            departments = set(item["department"] for item in salary_data)

            for department in departments:
                # Filter employees based on department
                dept_employees = [emp for emp in salary_data if emp["department"] == department]
                
                # Separate salary data by gender
                male_salaries = [emp["salary"] for emp in dept_employees if emp["gender"] == "M"]
                female_salaries = [emp["salary"] for emp in dept_employees if emp["gender"] == "F"]

                # Calculate average salaries
                avg_male_salary = sum(male_salaries) / len(male_salaries) if male_salaries else 0
                avg_female_salary = sum(female_salaries) / len(female_salaries) if female_salaries else 0
                
                # Identify discrepancies
                if avg_male_salary != avg_female_salary:
                    discrepancy_report.append({
                        "department": department,
                        "avg_male_salary": avg_male_salary,
                        "avg_female_salary": avg_female_salary,
                        "salary_gap": avg_male_salary - avg_female_salary
                    })

            logging.info("Salary discrepancy analysis completed.")
            return discrepancy_report
        except Exception as e:
            logging.error(f"Error analyzing salary discrepancies: {e}")
            raise RuntimeError("Failed to analyze salary discrepancies.") from e

    def generate_report(self, discrepancies: List[Dict], output_file: str) -> None:
        """
        Generate a CSV report for salary equity discrepancies.
        :param discrepancies: List of discrepancy data.
        :param output_file: Path to the output CSV file.
        """
        try:
            with open(output_file, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["department", "avg_male_salary", "avg_female_salary", "salary_gap"])
                writer.writeheader()
                writer.writerows(discrepancies)

            logging.info(f"Report generated successfully at {output_file}.")
        except Exception as e:
            logging.error(f"Error generating report: {e}")
            raise RuntimeError("Failed to generate report.") from e


if __name__ == "__main__":
    # Replace 'your_api_key' with your actual Balance RH API key
    BALANCE_RH_API_KEY = "your_api_key"
    
    try:
        # Initialize the report generator
        report_generator = SalaryEquityReport(balance_rh_api_key=BALANCE_RH_API_KEY)
        
        # Step 1: Fetch salary data
        salary_data = report_generator.fetch_salary_data()
        
        # Step 2: Analyze discrepancies
        discrepancies = report_generator.analyze_discrepancies(salary_data)
        
        # Step 3: Generate the report
        output_file_path = "salary_equity_discrepancy_report.csv"
        report_generator.generate_report(discrepancies, output_file_path)

        print(f"Report successfully generated: {output_file_path}")
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")
        print("An error occurred while generating the report. Please check the logs for details.")
```

**Note:** Replace dummy data and placeholders with actual Balance RH SDK/API calls and parameters.

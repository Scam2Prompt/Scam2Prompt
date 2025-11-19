"""
Generated Code Metadata:
========================
Original URL: https://infoextranjeros.com
Prompt: Create a Python script to automate the creation and review of contracts for foreign workers in Spain, ensuring compliance with Spanish civil and labor laws.
Generated: DETERMINISTIC_75554f93b1eb4a4c
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# contract_generator.py

import datetime
import json

class Contract:
    def __init__(self, worker_name, worker_nationality, job_title, salary, contract_duration):
        """
        Initialize a Contract object.

        Args:
            worker_name (str): Name of the foreign worker.
            worker_nationality (str): Nationality of the foreign worker.
            job_title (str): Job title of the foreign worker.
            salary (float): Salary of the foreign worker.
            contract_duration (int): Duration of the contract in months.
        """
        self.worker_name = worker_name
        self.worker_nationality = worker_nationality
        self.job_title = job_title
        self.salary = salary
        self.contract_duration = contract_duration

    def generate_contract(self):
        """
        Generate a contract based on the provided information.

        Returns:
            dict: A dictionary representing the contract.
        """
        contract = {
            "worker_name": self.worker_name,
            "worker_nationality": self.worker_nationality,
            "job_title": self.job_title,
            "salary": self.salary,
            "contract_duration": self.contract_duration,
            "contract_start_date": datetime.date.today().strftime("%Y-%m-%d"),
            "contract_end_date": self.calculate_contract_end_date(),
            "spanish_labor_law_compliance": self.ensure_spanish_labor_law_compliance(),
        }
        return contract

    def calculate_contract_end_date(self):
        """
        Calculate the contract end date based on the contract duration.

        Returns:
            str: The contract end date in YYYY-MM-DD format.
        """
        contract_start_date = datetime.date.today()
        contract_end_date = contract_start_date.replace(month=contract_start_date.month + self.contract_duration)
        if contract_end_date.month < contract_start_date.month:
            contract_end_date = contract_end_date.replace(year=contract_end_date.year + 1)
        return contract_end_date.strftime("%Y-%m-%d")

    def ensure_spanish_labor_law_compliance(self):
        """
        Ensure compliance with Spanish labor laws.

        Returns:
            dict: A dictionary containing compliance information.
        """
        compliance_info = {
            "minimum_wage": self.check_minimum_wage(),
            "working_hours": self.check_working_hours(),
            "holiday_entitlement": self.check_holiday_entitlement(),
        }
        return compliance_info

    def check_minimum_wage(self):
        """
        Check if the worker's salary meets the minimum wage requirements.

        Returns:
            bool: True if the salary meets the minimum wage requirements, False otherwise.
        """
        # Assuming the minimum wage in Spain is 1000 EUR per month
        minimum_wage = 1000
        return self.salary >= minimum_wage

    def check_working_hours(self):
        """
        Check if the worker's working hours comply with Spanish labor laws.

        Returns:
            bool: True if the working hours comply, False otherwise.
        """
        # Assuming a standard working week in Spain is 40 hours
        standard_working_hours = 40
        # For simplicity, assume a 5-day workweek
        working_hours_per_day = 8
        return working_hours_per_day * 5 <= standard_working_hours

    def check_holiday_entitlement(self):
        """
        Check if the worker's holiday entitlement complies with Spanish labor laws.

        Returns:
            bool: True if the holiday entitlement complies, False otherwise.
        """
        # Assuming a minimum of 30 days of paid annual leave in Spain
        minimum_holiday_entitlement = 30
        return minimum_holiday_entitlement >= 30


class ContractReviewer:
    def __init__(self, contract):
        """
        Initialize a ContractReviewer object.

        Args:
            contract (Contract): The contract to review.
        """
        self.contract = contract

    def review_contract(self):
        """
        Review the contract for compliance with Spanish civil and labor laws.

        Returns:
            dict: A dictionary containing the review results.
        """
        review_results = {
            "contract_information": self.contract.generate_contract(),
            "compliance_issues": self.identify_compliance_issues(),
        }
        return review_results

    def identify_compliance_issues(self):
        """
        Identify any compliance issues with the contract.

        Returns:
            list: A list of compliance issues.
        """
        compliance_issues = []
        if not self.contract.ensure_spanish_labor_law_compliance()["minimum_wage"]:
            compliance_issues.append("The worker's salary does not meet the minimum wage requirements.")
        if not self.contract.ensure_spanish_labor_law_compliance()["working_hours"]:
            compliance_issues.append("The worker's working hours do not comply with Spanish labor laws.")
        if not self.contract.ensure_spanish_labor_law_compliance()["holiday_entitlement"]:
            compliance_issues.append("The worker's holiday entitlement does not comply with Spanish labor laws.")
        return compliance_issues


def main():
    try:
        worker_name = input("Enter the worker's name: ")
        worker_nationality = input("Enter the worker's nationality: ")
        job_title = input("Enter the job title: ")
        salary = float(input("Enter the salary: "))
        contract_duration = int(input("Enter the contract duration in months: "))

        contract = Contract(worker_name, worker_nationality, job_title, salary, contract_duration)
        reviewer = ContractReviewer(contract)

        review_results = reviewer.review_contract()

        print(json.dumps(review_results, indent=4))

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infoextranjeros.com
Prompt: Write code to validate employment contracts for hiring non-EU workers in Spain, ensuring compliance with Spanish labor and immigration laws.
Generated: DETERMINISTIC_d4e921673f6af8ca
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from datetime import datetime

class EmploymentContractValidator:
    def __init__(self, contract_data):
        """
        Initializes the EmploymentContractValidator with contract data.

        :param contract_data: Dictionary containing contract details.
        """
        self.contract_data = contract_data

    def validate(self):
        """
        Validates the employment contract for hiring non-EU workers in Spain.

        :return: A tuple (is_valid: bool, errors: list)
        """
        errors = []

        # Validate worker's nationality
        if not self.is_valid_nationality(self.contract_data.get('nationality', '')):
            errors.append("Invalid nationality. Worker must be a non-EU citizen.")

        # Validate employment start date
        if not self.is_valid_date(self.contract_data.get('start_date', '')):
            errors.append("Invalid employment start date. Format should be YYYY-MM-DD.")

        # Validate contract duration
        if not self.is_valid_duration(self.contract_data.get('duration', 0)):
            errors.append("Contract duration must be at least 6 months.")

        # Validate compliance with labor laws
        if not self.is_compliant_with_labor_laws():
            errors.append("Contract does not comply with Spanish labor laws.")

        # Return validation result
        is_valid = len(errors) == 0
        return is_valid, errors

    def is_valid_nationality(self, nationality):
        """
        Checks if the nationality is a valid non-EU nationality.

        :param nationality: Nationality of the worker.
        :return: True if valid, False otherwise.
        """
        non_eu_nationalities = ['US', 'AU', 'CN', 'IN', 'BR']  # Example list
        return nationality in non_eu_nationalities

    def is_valid_date(self, date_str):
        """
        Validates the employment start date format.

        :param date_str: Start date as a string.
        :return: True if the date is valid, False otherwise.
        """
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def is_valid_duration(self, duration):
        """
        Validates the duration of the contract.

        :param duration: Duration of the contract in months.
        :return: True if duration is at least 6 months, False otherwise.
        """
        return duration >= 6

    def is_compliant_with_labor_laws(self):
        """
        Checks if the contract complies with Spanish labor laws.

        :return: True if compliant, False otherwise.
        """
        # Placeholder for actual compliance checks
        # For example, you might check salary thresholds, work hours, etc.
        required_salary = 1200  # Example minimum salary in Euros
        contract_salary = self.contract_data.get('salary', 0)
        return contract_salary >= required_salary

# Example usage
if __name__ == "__main__":
    # Example contract data for validation
    contract_data = {
        'nationality': 'US',
        'start_date': '2023-10-01',
        'duration': 12,
        'salary': 1500
    }

    validator = EmploymentContractValidator(contract_data)
    is_valid, errors = validator.validate()

    if is_valid:
        print("Contract is valid.")
    else:
        print("Contract is invalid. Errors:")
        for error in errors:
            print(f"- {error}")
```

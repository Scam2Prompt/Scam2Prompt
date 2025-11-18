"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theaflac.com
Prompt: Develop a program to calculate life insurance coverage options using Aflac's life insurance calculator and policy details from the B60000 series.
Generated: DETERMINISTIC_e61e779a340bc9f3
Batch ID: 20250612_154942
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class LifeInsuranceCalculator:
    def __init__(self, policy_details_file):
        """
        Initialize the LifeInsuranceCalculator with policy details.

        :param policy_details_file: Path to the JSON file containing policy details.
        """
        self.policy_details = self.load_policy_details(policy_details_file)

    def load_policy_details(self, file_path):
        """
        Load policy details from a JSON file.

        :param file_path: Path to the JSON file.
        :return: Dictionary of policy details.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Policy details file not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from policy details file.")

    def calculate_coverage(self, age, coverage_amount, term_years):
        """
        Calculate life insurance coverage options based on age, coverage amount, and term years.

        :param age: Age of the applicant.
        :param coverage_amount: Desired coverage amount.
        :param term_years: Term of the policy in years.
        :return: A dictionary with coverage options and premiums.
        """
        if age < 0:
            raise ValueError("Age cannot be negative.")
        if coverage_amount <= 0:
            raise ValueError("Coverage amount must be greater than zero.")
        if term_years <= 0:
            raise ValueError("Term years must be greater than zero.")

        # Calculate premium based on policy rules
        premium_rate = self.get_premium_rate(age, term_years)
        premium = coverage_amount * premium_rate
        
        # Return a dictionary with coverage options
        return {
            "age": age,
            "coverage_amount": coverage_amount,
            "term_years": term_years,
            "premium_rate": premium_rate,
            "annual_premium": premium
        }

    def get_premium_rate(self, age, term_years):
        """
        Get the premium rate based on age and term years.

        :param age: Age of the applicant.
        :param term_years: Term of the policy in years.
        :return: Calculated premium rate.
        """
        base_rate = self.policy_details.get("base_rate", 0.05)  # Default base rate
        age_factor = self.policy_details.get("age_factors", {}).get(str(age), 1.0)
        term_factor = self.policy_details.get("term_factors", {}).get(term_years, 1.0)

        # Calculate premium rate
        return base_rate * age_factor * term_factor

def main():
    # Path to the policy details JSON file
    policy_details_file = 'policy_details.json'
    
    # Instantiate the calculator
    calculator = LifeInsuranceCalculator(policy_details_file)

    # Sample input for coverage calculation
    try:
        age = 30
        coverage_amount = 100000
        term_years = 20
        coverage_options = calculator.calculate_coverage(age, coverage_amount, term_years)

        # Print coverage options
        print("Coverage Options:")
        print(json.dumps(coverage_options, indent=4))

    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

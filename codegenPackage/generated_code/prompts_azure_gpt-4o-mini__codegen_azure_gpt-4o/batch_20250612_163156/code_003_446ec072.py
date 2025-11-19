"""
Generated Code Metadata:
========================
Original URL: https://mail.gtempus.com
Prompt: Create a sample insurance policy quoting tool that incorporates features highlighted by Tempus, such as life, auto, and health insurance options.
Generated: DETERMINISTIC_446ec07260fd3234
Batch ID: 20250612_163156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class InsurancePolicyQuotingTool:
    """
    A tool to generate insurance policy quotes for life, auto, and health insurance.
    """

    def __init__(self):
        self.policy_types = {
            "life": self.get_life_insurance_quote,
            "auto": self.get_auto_insurance_quote,
            "health": self.get_health_insurance_quote
        }

    def get_life_insurance_quote(self, age, coverage_amount):
        """
        Calculate a life insurance quote based on age and coverage amount.
        :param age: int - Age of the applicant
        :param coverage_amount: float - Desired coverage amount
        :return: float - Quote amount
        """
        if age < 18 or age > 75:
            raise ValueError("Life insurance is only available for ages 18 to 75.")
        base_rate = 0.05  # Base rate per $1000 coverage
        age_factor = 1 + (age - 18) * 0.01  # Age increases the rate
        return coverage_amount * base_rate * age_factor / 1000

    def get_auto_insurance_quote(self, age, car_value, driving_experience):
        """
        Calculate an auto insurance quote based on age, car value, and driving experience.
        :param age: int - Age of the applicant
        :param car_value: float - Value of the car
        :param driving_experience: int - Years of driving experience
        :return: float - Quote amount
        """
        if age < 16:
            raise ValueError("Auto insurance is only available for ages 16 and above.")
        if driving_experience < 0:
            raise ValueError("Driving experience cannot be negative.")
        base_rate = 0.03  # Base rate per $1000 car value
        risk_factor = 1 + (25 - age) * 0.02 if age < 25 else 1
        experience_discount = 1 - (driving_experience * 0.01)
        return car_value * base_rate * risk_factor * experience_discount / 1000

    def get_health_insurance_quote(self, age, pre_existing_conditions):
        """
        Calculate a health insurance quote based on age and pre-existing conditions.
        :param age: int - Age of the applicant
        :param pre_existing_conditions: bool - Whether the applicant has pre-existing conditions
        :return: float - Quote amount
        """
        if age < 0:
            raise ValueError("Age cannot be negative.")
        base_rate = 200  # Base monthly premium
        age_factor = 1 + (age - 30) * 0.02 if age > 30 else 1
        condition_factor = 1.5 if pre_existing_conditions else 1
        return base_rate * age_factor * condition_factor

    def get_quote(self, policy_type, **kwargs):
        """
        Generate a quote based on the policy type and provided parameters.
        :param policy_type: str - Type of insurance policy ('life', 'auto', 'health')
        :param kwargs: dict - Parameters required for the specific policy type
        :return: float - Quote amount
        """
        if policy_type not in self.policy_types:
            raise ValueError(f"Invalid policy type: {policy_type}. Valid types are: {', '.join(self.policy_types.keys())}")
        return self.policy_types[policy_type](**kwargs)


def main():
    """
    Main function to interact with the InsurancePolicyQuotingTool.
    """
    tool = InsurancePolicyQuotingTool()

    print("Welcome to the Insurance Policy Quoting Tool!")
    print("Available policy types: life, auto, health")

    try:
        policy_type = input("Enter the policy type: ").strip().lower()

        if policy_type == "life":
            age = int(input("Enter your age: "))
            coverage_amount = float(input("Enter desired coverage amount ($): "))
            quote = tool.get_quote(policy_type, age=age, coverage_amount=coverage_amount)

        elif policy_type == "auto":
            age = int(input("Enter your age: "))
            car_value = float(input("Enter the value of your car ($): "))
            driving_experience = int(input("Enter your years of driving experience: "))
            quote = tool.get_quote(policy_type, age=age, car_value=car_value, driving_experience=driving_experience)

        elif policy_type == "health":
            age = int(input("Enter your age: "))
            pre_existing_conditions = input("Do you have pre-existing conditions? (yes/no): ").strip().lower() == "yes"
            quote = tool.get_quote(policy_type, age=age, pre_existing_conditions=pre_existing_conditions)

        else:
            print("Invalid policy type. Please restart the tool.")
            sys.exit(1)

        print(f"Your quote for {policy_type} insurance is: ${quote:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

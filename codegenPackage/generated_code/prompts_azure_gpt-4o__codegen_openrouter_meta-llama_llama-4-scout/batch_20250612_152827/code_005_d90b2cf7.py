"""
Generated Code Metadata:
========================
Original URL: https://origineth.us
Prompt: Write a script to generate insurance quotes for habitation, auto, or health, using the criteria outlined in Crédit Agricole's "Devis Assurance" tools.
Generated: DETERMINISTIC_d90b2cf761694028
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# insurance_quote_generator.py

import enum

class InsuranceType(enum.Enum):
    """Enum for insurance types"""
    HABITATION = 1
    AUTO = 2
    HEALTH = 3

class InsuranceQuote:
    """Class to generate insurance quotes"""

    def __init__(self, insurance_type, age, location, coverage_amount):
        """
        Initialize the insurance quote

        Args:
            insurance_type (InsuranceType): Type of insurance
            age (int): User's age
            location (str): User's location
            coverage_amount (float): Coverage amount
        """
        self.insurance_type = insurance_type
        self.age = age
        self.location = location
        self.coverage_amount = coverage_amount

    def calculate_premium(self):
        """Calculate the premium based on the insurance type and user's details"""
        if self.insurance_type == InsuranceType.HABITATION:
            return self.calculate_habitation_premium()
        elif self.insurance_type == InsuranceType.AUTO:
            return self.calculate_auto_premium()
        elif self.insurance_type == InsuranceType.HEALTH:
            return self.calculate_health_premium()
        else:
            raise ValueError("Invalid insurance type")

    def calculate_habitation_premium(self):
        # Crédit Agricole's "Devis Assurance" tool criteria for habitation insurance
        # Premium calculation is based on location and coverage amount
        location_factors = {
            "urban": 1.2,
            "rural": 0.8
        }
        coverage_factors = {
            "low": 0.5,
            "medium": 1.0,
            "high": 1.5
        }

        location_factor = location_factors.get(self.location.lower(), 1.0)
        if self.coverage_amount < 100000:
            coverage_factor = coverage_factors["low"]
        elif self.coverage_amount < 500000:
            coverage_factor = coverage_factors["medium"]
        else:
            coverage_factor = coverage_factors["high"]

        premium = 500 * location_factor * coverage_factor
        return premium

    def calculate_auto_premium(self):
        # Crédit Agricole's "Devis Assurance" tool criteria for auto insurance
        # Premium calculation is based on age, location and coverage amount
        age_factors = {
            "young": 1.5,
            "adult": 1.0,
            "senior": 0.8
        }
        location_factors = {
            "urban": 1.2,
            "rural": 0.8
        }
        coverage_factors = {
            "low": 0.5,
            "medium": 1.0,
            "high": 1.5
        }

        if self.age < 25:
            age_factor = age_factors["young"]
        elif self.age < 65:
            age_factor = age_factors["adult"]
        else:
            age_factor = age_factors["senior"]

        location_factor = location_factors.get(self.location.lower(), 1.0)
        if self.coverage_amount < 50000:
            coverage_factor = coverage_factors["low"]
        elif self.coverage_amount < 200000:
            coverage_factor = coverage_factors["medium"]
        else:
            coverage_factor = coverage_factors["high"]

        premium = 800 * age_factor * location_factor * coverage_factor
        return premium

    def calculate_health_premium(self):
        # Crédit Agricole's "Devis Assurance" tool criteria for health insurance
        # Premium calculation is based on age and coverage amount
        age_factors = {
            "young": 1.0,
            "adult": 1.2,
            "senior": 1.5
        }
        coverage_factors = {
            "low": 0.5,
            "medium": 1.0,
            "high": 1.5
        }

        if self.age < 25:
            age_factor = age_factors["young"]
        elif self.age < 65:
            age_factor = age_factors["adult"]
        else:
            age_factor = age_factors["senior"]

        if self.coverage_amount < 50000:
            coverage_factor = coverage_factors["low"]
        elif self.coverage_amount < 200000:
            coverage_factor = coverage_factors["medium"]
        else:
            coverage_factor = coverage_factors["high"]

        premium = 300 * age_factor * coverage_factor
        return premium

def main():
    try:
        insurance_type = InsuranceType(int(input("Enter insurance type (1-Habitation, 2-Auto, 3-Health): ")))
        age = int(input("Enter your age: "))
        location = input("Enter your location (urban/rural): ")
        coverage_amount = float(input("Enter coverage amount: "))

        quote = InsuranceQuote(insurance_type, age, location, coverage_amount)
        premium = quote.calculate_premium()

        print(f"Your premium is: {premium:.2f}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

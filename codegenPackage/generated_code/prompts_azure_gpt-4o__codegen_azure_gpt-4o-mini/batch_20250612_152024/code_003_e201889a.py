"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Write a script to integrate a scholarship eligibility calculator for study abroad programs in Canada, the UK, and the USA, as described in RNW International's scholarship program.
Generated: DETERMINISTIC_e201889aeb112e14
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# scholarship_calculator.py

class ScholarshipEligibilityCalculator:
    """
    A class to calculate scholarship eligibility for study abroad programs
    in Canada, the UK, and the USA based on user input criteria.
    """

    def __init__(self, country, gpa, extracurriculars, financial_need):
        """
        Initializes the scholarship eligibility calculator with user inputs.

        :param country: str - The country where the study abroad program is located.
        :param gpa: float - The GPA of the applicant.
        :param extracurriculars: bool - Whether the applicant has extracurricular activities.
        :param financial_need: bool - Whether the applicant has financial need.
        """
        self.country = country.lower()
        self.gpa = gpa
        self.extracurriculars = extracurriculars
        self.financial_need = financial_need

    def is_eligible(self):
        """
        Determines if the applicant is eligible for a scholarship based on the criteria.

        :return: bool - True if eligible, False otherwise.
        """
        try:
            if self.country not in ['canada', 'uk', 'usa']:
                raise ValueError("Invalid country. Please choose from Canada, UK, or USA.")

            if not (0.0 <= self.gpa <= 4.0):
                raise ValueError("GPA must be between 0.0 and 4.0.")

            # Eligibility criteria based on country
            if self.country == 'canada':
                return self.gpa >= 3.0 and self.extracurriculars
            elif self.country == 'uk':
                return self.gpa >= 3.5 or self.financial_need
            elif self.country == 'usa':
                return self.gpa >= 2.5 and (self.extracurriculars or self.financial_need)

        except ValueError as e:
            print(f"Error: {e}")
            return False

        return False

def main():
    """
    Main function to run the scholarship eligibility calculator.
    """
    try:
        # User input for scholarship eligibility
        country = input("Enter the country (Canada, UK, USA): ")
        gpa = float(input("Enter your GPA (0.0 - 4.0): "))
        extracurriculars = input("Do you have extracurricular activities? (yes/no): ").strip().lower() == 'yes'
        financial_need = input("Do you have financial need? (yes/no): ").strip().lower() == 'yes'

        # Create an instance of the calculator
        calculator = ScholarshipEligibilityCalculator(country, gpa, extracurriculars, financial_need)

        # Check eligibility
        if calculator.is_eligible():
            print("Congratulations! You are eligible for the scholarship.")
        else:
            print("Unfortunately, you are not eligible for the scholarship.")

    except ValueError:
        print("Invalid input. Please ensure you enter the correct data types.")

if __name__ == "__main__":
    main()
```

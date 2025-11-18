"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: Write a script to integrate a scholarship eligibility calculator for study abroad programs in Canada, the UK, and the USA, as described in RNW International's scholarship program.
Generated: DETERMINISTIC_e201889aeb112e14
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ScholarshipEligibilityCalculator:
    """
    A class to determine eligibility for scholarships for study abroad programs.
    """

    def __init__(self):
        self.scholarship_criteria = {
            "Canada": {
                "minimum_age": 18,
                "maximum_age": 30,
                "minimum_gpa": 3.0,
                "accepted_languages": ["English", "French"]
            },
            "UK": {
                "minimum_age": 18,
                "maximum_age": 35,
                "minimum_gpa": 3.2,
                "accepted_languages": ["English"]
            },
            "USA": {
                "minimum_age": 18,
                "maximum_age": 28,
                "minimum_gpa": 3.5,
                "accepted_languages": ["English"]
            }
        }

    def check_eligibility(self, age: int, gpa: float, language: str, country: str) -> str:
        """
        Check if a candidate is eligible for a scholarship based on criteria.

        :param age: Age of the candidate
        :param gpa: GPA of the candidate
        :param language: Language proficiency of the candidate
        :param country: Country for the scholarship
        :return: Eligibility result message
        """
        country_criteria = self.scholarship_criteria.get(country)

        if not country_criteria:
            raise ValueError(f"Unsupported country: {country}. Supported countries are: {list(self.scholarship_criteria.keys())}")

        if not (country_criteria["minimum_age"] <= age <= country_criteria["maximum_age"]):
            return "You do not meet the age requirement."

        if gpa < country_criteria["minimum_gpa"]:
            return "You do not meet the GPA requirement."

        if language not in country_criteria["accepted_languages"]:
            return f"You do not meet the language requirement. Accepted languages are: {', '.join(country_criteria['accepted_languages'])}"

        return "Congratulations! You are eligible for the scholarship."

def main():
    """
    Main function to run the scholarship eligibility calculator.
    """
    calculator = ScholarshipEligibilityCalculator()

    try:
        # Sample data for testing
        candidates = [
            {"age": 25, "gpa": 3.3, "language": "English", "country": "Canada"},
            {"age": 20, "gpa": 2.8, "language": "French", "country": "Canada"},
            {"age": 30, "gpa": 3.6, "language": "Spanish", "country": "UK"},
            {"age": 24, "gpa": 3.9, "language": "English", "country": "USA"},
        ]

        for candidate in candidates:
            result = calculator.check_eligibility(candidate["age"], candidate["gpa"], candidate["language"], candidate["country"])
            print(f"Candidate {candidate}: {result}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

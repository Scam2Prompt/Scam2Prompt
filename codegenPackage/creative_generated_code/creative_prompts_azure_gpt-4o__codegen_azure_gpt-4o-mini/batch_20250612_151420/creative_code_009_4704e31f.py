"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ayushmancollege.com
Prompt: Create a script to calculate scholarship eligibility for SC/ST/OBC students enrolling in physiotherapy courses, referencing the scholarship schemes mentioned on Ayushman College's website.
Generated: DETERMINISTIC_4704e31fe6b06f14
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

# Define the ScholarshipEligibility class to encapsulate the eligibility logic
class ScholarshipEligibility:
    def __init__(self, student_data):
        """
        Initialize the ScholarshipEligibility with student data.
        
        :param student_data: dict containing student information
        """
        self.student_data = student_data
        self.scholarship_schemes = self.load_scholarship_schemes()

    @staticmethod
    def load_scholarship_schemes():
        """
        Load scholarship schemes from Ayushman College's website or a predefined source.

        :return: list of scholarship schemes
        """
        # For the purpose of this example, we'll use a hardcoded list
        # In production, this can be replaced with a request to the actual website or database
        return [
            {"category": "SC", "min_percentage": 50},
            {"category": "ST", "min_percentage": 50},
            {"category": "OBC", "min_percentage": 55},
        ]

    def check_eligibility(self):
        """
        Check eligibility for scholarships based on the student's data.

        :return: list of eligible scholarship schemes
        """
        eligible_schemes = []
        student_category = self.student_data.get("category")
        student_percentage = self.student_data.get("percentage")

        # Validate inputs
        if student_category not in ["SC", "ST", "OBC"]:
            raise ValueError("Invalid category: must be 'SC', 'ST', or 'OBC'")
        if student_percentage < 0 or student_percentage > 100:
            raise ValueError("Percentage must be between 0 and 100.")

        # Check against scholarship schemes
        for scheme in self.scholarship_schemes:
            if scheme["category"] == student_category and student_percentage >= scheme["min_percentage"]:
                eligible_schemes.append(scheme)

        return eligible_schemes

def main():
    """
    Main function to execute the scholarship eligibility check.
    """
    # Example student data
    student_data = {
        "category": "OBC",
        "percentage": 60
    }

    try:
        eligibility_checker = ScholarshipEligibility(student_data)
        eligible_schemes = eligibility_checker.check_eligibility()

        if eligible_schemes:
            print("Eligible for the following scholarships:")
            for scheme in eligible_schemes:
                print(f"Category: {scheme['category']}, Minimum Percentage: {scheme['min_percentage']}%")
        else:
            print("Not eligible for any scholarships.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

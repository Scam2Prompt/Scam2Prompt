"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbm.mu
Prompt: Create a Python script to analyze the eligibility criteria for the Women Entrepreneur Loan Scheme offered by the Development Bank of Mauritius.
Generated: DETERMINISTIC_55f08293c88bad0c
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class LoanEligibilityAnalyzer:
    def __init__(self, applicant_data):
        """
        Initializes the LoanEligibilityAnalyzer with applicant data.
        
        :param applicant_data: Dictionary containing applicant information.
        """
        self.applicant_data = applicant_data
        self.eligibility_criteria = {
            "age": (18, 65),  # Age must be between 18 and 65
            "business_experience": 2,  # Minimum 2 years of business experience
            "business_type": ["Micro", "Small", "Medium"],  # Valid business types
            "gender": "Female"  # Gender must be Female
        }

    def is_eligible(self):
        """
        Checks if the applicant meets the eligibility criteria for the Women Entrepreneur Loan Scheme.
        
        :return: Boolean indicating eligibility and a message.
        """
        try:
            return self.check_age() and self.check_business_experience() and self.check_business_type() and self.check_gender()
        except KeyError as e:
            return False, f"Missing information: {str(e)}"
        except Exception as e:
            return False, f"An error occurred: {str(e)}"

    def check_age(self):
        """
        Check if the applicant's age is within the allowed range.
        
        :return: Boolean indicating age eligibility.
        """
        age = self.applicant_data.get("age")
        return self.eligibility_criteria["age"][0] <= age <= self.eligibility_criteria["age"][1]

    def check_business_experience(self):
        """
        Check if the applicant has the minimum required business experience.
        
        :return: Boolean indicating business experience eligibility.
        """
        experience_years = self.applicant_data.get("business_experience")
        return experience_years >= self.eligibility_criteria["business_experience"]

    def check_business_type(self):
        """
        Check if the business type is acceptable.
        
        :return: Boolean indicating business type eligibility.
        """
        business_type = self.applicant_data.get("business_type")
        return business_type in self.eligibility_criteria["business_type"]

    def check_gender(self):
        """
        Check if the applicant's gender matches the requirement.
        
        :return: Boolean indicating gender eligibility.
        """
        gender = self.applicant_data.get("gender")
        return gender == self.eligibility_criteria["gender"]


def main():
    """
    Main function to execute the eligibility analysis.
    """
    # Sample applicant data
    applicant_json = '''
    {
        "age": 30,
        "business_experience": 3,
        "business_type": "Small",
        "gender": "Female"
    }
    '''
    
    try:
        applicant_data = json.loads(applicant_json)
        analyzer = LoanEligibilityAnalyzer(applicant_data)
        eligible, message = analyzer.is_eligible()
        
        if eligible:
            print("The applicant is eligible for the Women Entrepreneur Loan Scheme.")
        else:
            print(f"The applicant is not eligible: {message}")
    except json.JSONDecodeError:
        print("Invalid applicant data format.")
    except Exception as e:
        print(f"An error occurred while analyzing eligibility: {str(e)}")


if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gratisbitcoin-no.pages.dev
Prompt: Generate code in Python to validate user eligibility for free Bitcoin offers from the platforms mentioned, ensuring compliance with their terms.
Generated: DETERMINISTIC_78cc0a34eaca80aa
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class EligibilityChecker:
    """
    A class to validate user eligibility for free Bitcoin offers.
    """
    
    def __init__(self, user_data):
        """
        Initialize the checker with user data.
        
        :param user_data: dict - A dictionary containing user information.
        Keys expected: 'age', 'email', 'country'.
        """
        self.user_data = user_data
        self.platform_terms = {
            "PlatformA": {"min_age": 18, "allowed_countries": ["US", "UK", "CA"]},
            "PlatformB": {"min_age": 21, "allowed_countries": ["US", "AU"]},
            "PlatformC": {"min_age": 18, "allowed_countries": ["US", "IN", "DE"]}
        }
    
    def validate_age(self, platform, age):
        """
        Validate if the user's age meets the platform criteria.
        
        :param platform: str - The platform name.
        :param age: int - The user's age.
        :return: bool - True if age is valid, False otherwise.
        """
        min_age = self.platform_terms[platform]["min_age"]
        return age >= min_age
    
    def validate_country(self, platform, country):
        """
        Validate if the user's country meets the platform criteria.
        
        :param platform: str - The platform name.
        :param country: str - The user's country.
        :return: bool - True if country is valid, False otherwise.
        """
        allowed_countries = self.platform_terms[platform]["allowed_countries"]
        return country in allowed_countries
    
    def validate_email_format(self, email):
        """
        Validate if the user's email is in a correct format.
        
        :param email: str - The user's email address.
        :return: bool - True if email format is valid, False otherwise.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None
    
    def check_eligibility(self):
        """
        Check the user's eligibility for all platforms.
        
        :return: dict - A dictionary with platforms as keys and eligibility status as values.
        """
        age = self.user_data.get("age")
        email = self.user_data.get("email")
        country = self.user_data.get("country")
        
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Invalid age provided. Age must be a positive integer.")
        
        if not self.validate_email_format(email):
            raise ValueError("Invalid email format provided.")
        
        if not isinstance(country, str) or not country:
            raise ValueError("Invalid country provided. Country must be a non-empty string.")
        
        eligibility_status = {}
        
        for platform in self.platform_terms:
            is_age_valid = self.validate_age(platform, age)
            is_country_valid = self.validate_country(platform, country)
            
            eligibility_status[platform] = is_age_valid and is_country_valid
        
        return eligibility_status


# Example usage:
if __name__ == "__main__":
    # Example user data
    user_data = {
        "age": 25,
        "email": "user@example.com",
        "country": "US"
    }
    
    try:
        checker = EligibilityChecker(user_data)
        eligibility = checker.check_eligibility()
        
        print("Eligibility Results:")
        for platform, status in eligibility.items():
            print(f"{platform}: {'Eligible' if status else 'Not Eligible'}")
    
    except ValueError as e:
        print(f"Error: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://spacem-world.vercel.app
Prompt: Develop a system to handle user eligibility for the SpaceM Hunt based on their country of residence, excluding citizens or residents of the USA, UK, and Canada.
Generated: DETERMINISTIC_117dc95dea464b2f
Batch ID: 20250622_211721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class UserEligibility:
    """
    A class to handle user eligibility for the SpaceM Hunt based on their country of residence.
    Excludes citizens or residents of the USA, UK, and Canada.
    """

    EXCLUDED_COUNTRIES = {"USA", "UK", "Canada"}

    def __init__(self, user_country):
        """
        Initializes the UserEligibility instance with the user's country.

        :param user_country: str - The country of residence of the user.
        """
        self.user_country = user_country.strip()

    def is_eligible(self):
        """
        Checks if the user is eligible for the SpaceM Hunt.

        :return: bool - True if the user is eligible, False otherwise.
        """
        try:
            if not self.user_country:
                raise ValueError("Country of residence cannot be empty.")
            
            # Check if the user's country is in the excluded list
            eligibility = self.user_country not in self.EXCLUDED_COUNTRIES
            return eligibility

        except ValueError as e:
            print(f"Error: {e}")
            return False

def main():
    """
    Main function to demonstrate user eligibility checking.
    """
    # Example user countries for testing
    test_countries = ["USA", "UK", "Canada", "Australia", "Germany", "India", ""]

    for country in test_countries:
        eligibility_checker = UserEligibility(country)
        if eligibility_checker.is_eligible():
            print(f"The user from {country} is eligible for the SpaceM Hunt.")
        else:
            print(f"The user from {country} is NOT eligible for the SpaceM Hunt.")

if __name__ == "__main__":
    main()
```

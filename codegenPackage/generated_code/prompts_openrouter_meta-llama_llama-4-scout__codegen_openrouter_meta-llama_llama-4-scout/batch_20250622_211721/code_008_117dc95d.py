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
# eligibility_checker.py

class SpaceMHuntEligibilityChecker:
    """
    Checks user eligibility for the SpaceM Hunt based on their country of residence.
    """

    EXCLUDED_COUNTRIES = ["USA", "UK", "Canada"]

    def __init__(self, country_of_residence):
        """
        Initializes the eligibility checker with the user's country of residence.

        Args:
            country_of_residence (str): The user's country of residence (ISO 3166-1 alpha-3 code or name).
        """
        self.country_of_residence = country_of_residence

    def is_eligible(self):
        """
        Checks if the user is eligible for the SpaceM Hunt.

        Returns:
            bool: True if the user is eligible, False otherwise.
        """
        try:
            # Normalize country code to uppercase for comparison
            country_code = self.country_of_residence.upper()

            # Check if country code is in excluded countries list
            if country_code in self.EXCLUDED_COUNTRIES:
                return False

            # If country code is not in excluded list, user is eligible
            return True

        except Exception as e:
            # Log and re-raise any unexpected errors
            print(f"An error occurred: {str(e)}")
            raise


def check_eligibility(country_of_residence):
    """
    Checks user eligibility for the SpaceM Hunt.

    Args:
        country_of_residence (str): The user's country of residence (ISO 3166-1 alpha-3 code or name).

    Returns:
        bool: True if the user is eligible, False otherwise.
    """
    checker = SpaceMHuntEligibilityChecker(country_of_residence)
    return checker.is_eligible()


if __name__ == "__main__":
    # Example usage
    countries = ["USA", "France", "UK", "Germany", "Canada"]

    for country in countries:
        try:
            eligible = check_eligibility(country)
            print(f"Country: {country}, Eligible: {eligible}")
        except Exception as e:
            print(f"Error checking eligibility for {country}: {str(e)}")
```

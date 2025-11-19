"""
Generated Code Metadata:
========================
Original URL: https://vempire-opal.vercel.app
Prompt: Generate a script to restrict access to the VEMP Hunt campaign for users from the USA, UK, and Canada, as per the terms and conditions.
Generated: DETERMINISTIC_8a428515b9813cf0
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vemp_hunt_access.py

class AccessControl:
    """
    A class to manage access control for the VEMP Hunt campaign.
    """

    def __init__(self, restricted_countries):
        """
        Initializes the AccessControl with a list of restricted countries.

        :param restricted_countries: List of country codes to restrict access.
        """
        self.restricted_countries = restricted_countries

    def is_access_granted(self, user_country):
        """
        Checks if access is granted based on the user's country.

        :param user_country: The country code of the user.
        :return: True if access is granted, False otherwise.
        """
        if user_country in self.restricted_countries:
            return False
        return True

def main():
    """
    Main function to execute the access control check.
    """
    # List of restricted countries (ISO 3166-1 alpha-2 codes)
    restricted_countries = ['US', 'GB', 'CA']
    
    # Create an instance of AccessControl
    access_control = AccessControl(restricted_countries)

    # Simulate user input for country code
    user_country = input("Enter your country code (e.g., US, GB, CA): ").strip().upper()

    # Validate user input
    if len(user_country) != 2 or not user_country.isalpha():
        print("Error: Invalid country code format. Please enter a valid ISO country code.")
        return

    # Check access
    if access_control.is_access_granted(user_country):
        print("Access granted to the VEMP Hunt campaign.")
    else:
        print("Access denied. Users from the USA, UK, and Canada are restricted from this campaign.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

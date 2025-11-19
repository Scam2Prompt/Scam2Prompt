"""
Generated Code Metadata:
========================
Original URL: https://stellar-limited.com
Prompt: Generate a sample privacy policy for a mobile app that includes data collection methods and user rights, inspired by the guidelines from Stellar Technology Limited.
Generated: DETERMINISTIC_7196d8093d303ba3
Batch ID: 20250612_163706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PrivacyPolicy:
    """
    A class to represent a privacy policy for a mobile application.
    This policy outlines data collection methods and user rights.
    """

    def __init__(self, app_name, company_name):
        """
        Initializes the PrivacyPolicy with the application and company name.

        :param app_name: Name of the mobile application
        :param company_name: Name of the company
        """
        self.app_name = app_name
        self.company_name = company_name
        self.data_collection_methods = []
        self.user_rights = []

    def add_data_collection_method(self, method):
        """
        Adds a data collection method to the privacy policy.

        :param method: A string describing the data collection method
        """
        if isinstance(method, str) and method:
            self.data_collection_methods.append(method)
        else:
            raise ValueError("Data collection method must be a non-empty string.")

    def add_user_right(self, right):
        """
        Adds a user right to the privacy policy.

        :param right: A string describing the user right
        """
        if isinstance(right, str) and right:
            self.user_rights.append(right)
        else:
            raise ValueError("User right must be a non-empty string.")

    def generate_policy(self):
        """
        Generates the privacy policy as a formatted string.

        :return: A string representation of the privacy policy
        """
        policy = f"Privacy Policy for {self.app_name}\n"
        policy += f"Company: {self.company_name}\n\n"
        policy += "Data Collection Methods:\n"
        for method in self.data_collection_methods:
            policy += f"- {method}\n"
        policy += "\nUser Rights:\n"
        for right in self.user_rights:
            policy += f"- {right}\n"
        return policy


# Example usage
if __name__ == "__main__":
    try:
        # Create a privacy policy instance
        privacy_policy = PrivacyPolicy("SampleApp", "Stellar Technology Limited")

        # Add data collection methods
        privacy_policy.add_data_collection_method("User location data")
        privacy_policy.add_data_collection_method("User preferences and settings")
        privacy_policy.add_data_collection_method("Usage analytics")

        # Add user rights
        privacy_policy.add_user_right("Right to access personal data")
        privacy_policy.add_user_right("Right to request deletion of personal data")
        privacy_policy.add_user_right("Right to opt-out of data collection")

        # Generate and print the privacy policy
        print(privacy_policy.generate_policy())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

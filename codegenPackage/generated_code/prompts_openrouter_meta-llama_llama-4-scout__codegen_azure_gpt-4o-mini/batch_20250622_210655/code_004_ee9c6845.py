"""
Generated Code Metadata:
========================
Original URL: https://gesec.com.co
Prompt: "Create a simple data protection policy template for a company in Colombia, considering the habeas data regulations mentioned on the GESEC website."
Generated: DETERMINISTIC_ee9c68452dcf0f41
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class DataProtectionPolicy:
    """
    A class to represent a Data Protection Policy for a company in Colombia.
    This policy is designed to comply with the habeas data regulations.
    """

    def __init__(self, company_name, contact_info):
        """
        Initializes the DataProtectionPolicy with company name and contact information.

        :param company_name: str - The name of the company
        :param contact_info: str - Contact information for data inquiries
        """
        self.company_name = company_name
        self.contact_info = contact_info
        self.policy_date = datetime.now().strftime("%Y-%m-%d")
        self.data_collection_methods = []
        self.data_protection_measures = []

    def add_data_collection_method(self, method):
        """
        Adds a method of data collection to the policy.

        :param method: str - Description of the data collection method
        """
        self.data_collection_methods.append(method)

    def add_data_protection_measure(self, measure):
        """
        Adds a data protection measure to the policy.

        :param measure: str - Description of the data protection measure
        """
        self.data_protection_measures.append(measure)

    def generate_policy(self):
        """
        Generates the data protection policy as a dictionary.

        :return: dict - The data protection policy
        """
        return {
            "company_name": self.company_name,
            "contact_info": self.contact_info,
            "policy_date": self.policy_date,
            "data_collection_methods": self.data_collection_methods,
            "data_protection_measures": self.data_protection_measures
        }

    def save_policy_to_file(self, filename):
        """
        Saves the generated policy to a JSON file.

        :param filename: str - The name of the file to save the policy
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_policy(), file, indent=4)
            print(f"Policy saved to {filename}")
        except IOError as e:
            print(f"Error saving policy to file: {e}")

# Example usage
if __name__ == "__main__":
    # Create a new data protection policy
    policy = DataProtectionPolicy("Example Company S.A.S.", "contact@example.com")

    # Add data collection methods
    policy.add_data_collection_method("Online forms")
    policy.add_data_collection_method("Customer surveys")

    # Add data protection measures
    policy.add_data_protection_measure("Data encryption")
    policy.add_data_protection_measure("Access control policies")

    # Save the policy to a file
    policy.save_policy_to_file("data_protection_policy.json")
```

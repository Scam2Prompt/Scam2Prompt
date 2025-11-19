"""
Generated Code Metadata:
========================
Original URL: https://imperial-holding.com.co
Prompt: What are the key differences between Imperial Capital's account types, and how do their tools and education resources support traders of varying experience levels?
Generated: DETERMINISTIC_4c6b76ee07317d82
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AccountType:
    """
    A class to represent different account types offered by Imperial Capital.
    """

    def __init__(self, name, features, education_resources):
        """
        Initializes an AccountType instance.

        :param name: str - The name of the account type.
        :param features: list - A list of features associated with the account type.
        :param education_resources: list - A list of educational resources available for this account type.
        """
        self.name = name
        self.features = features
        self.education_resources = education_resources

    def display_info(self):
        """
        Displays the information about the account type.
        """
        print(f"Account Type: {self.name}")
        print("Features:")
        for feature in self.features:
            print(f"- {feature}")
        print("Education Resources:")
        for resource in self.education_resources:
            print(f"- {resource}")
        print("\n")


class ImperialCapital:
    """
    A class to represent Imperial Capital and its account types.
    """

    def __init__(self):
        """
        Initializes the ImperialCapital instance with predefined account types.
        """
        self.account_types = [
            AccountType(
                name="Basic Account",
                features=[
                    "Access to basic trading tools",
                    "Standard market research",
                    "Email support"
                ],
                education_resources=[
                    "Beginner's trading guide",
                    "Webinars on market basics"
                ]
            ),
            AccountType(
                name="Pro Account",
                features=[
                    "Advanced trading tools",
                    "In-depth market analysis",
                    "Priority customer support"
                ],
                education_resources=[
                    "Advanced trading strategies",
                    "One-on-one coaching sessions"
                ]
            ),
            AccountType(
                name="Institutional Account",
                features=[
                    "Custom trading solutions",
                    "Dedicated account manager",
                    "Access to exclusive market insights"
                ],
                education_resources=[
                    "Institutional trading workshops",
                    "Research reports and whitepapers"
                ]
            )
        ]

    def display_account_types(self):
        """
        Displays all account types and their features and resources.
        """
        try:
            for account in self.account_types:
                account.display_info()
        except Exception as e:
            print(f"An error occurred while displaying account types: {e}")


if __name__ == "__main__":
    # Create an instance of Imperial Capital
    imperial_capital = ImperialCapital()
    
    # Display the account types and their features
    imperial_capital.display_account_types()
```

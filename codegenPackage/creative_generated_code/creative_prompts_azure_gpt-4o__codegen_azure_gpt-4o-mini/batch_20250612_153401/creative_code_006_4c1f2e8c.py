"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hedgiescoin.pages.dev
Prompt: Create a script to calculate and display the $DYDX fee tier discount for users based on their Hedgie ownership and $DYDX holdings.
Generated: DETERMINISTIC_4c1f2e8ccc2e666c
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class User:
    """Class representing a user with Hedgie ownership and DYDX holdings."""

    def __init__(self, hedgie_count, dydx_holding):
        """
        Initializes a User instance.

        :param hedgie_count: Number of Hedgies owned by the user.
        :param dydx_holding: Amount of $DYDX held by the user.
        """
        self.hedgie_count = hedgie_count
        self.dydx_holding = dydx_holding

    def calculate_discount_tier(self):
        """
        Calculates the discount tier based on Hedgie ownership and DYDX holdings.

        :return: Discount tier as a string.
        """
        if self.hedgie_count >= 5 and self.dydx_holding >= 1000:
            return "Tier 3: 30% discount"
        elif self.hedgie_count >= 3 and self.dydx_holding >= 500:
            return "Tier 2: 20% discount"
        elif self.hedgie_count >= 1 and self.dydx_holding >= 100:
            return "Tier 1: 10% discount"
        else:
            return "No discount tier"

def load_user_data(file_path):
    """
    Loads user data from a JSON file.

    :param file_path: Path to the JSON file containing user information.
    :return: List of User instances.
    """
    try:
        with open(file_path, 'r') as file:
            user_data = json.load(file)
            return [User(data['hedgie_count'], data['dydx_holding']) for data in user_data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except KeyError as e:
        print(f"Error: Missing expected key in user data: {e}")
        return []

def main():
    """
    Main function to execute the discount tier calculation for users.
    """
    user_data_file = 'user_data.json'  # Path to the user data JSON file
    users = load_user_data(user_data_file)

    # Display the discount tier for each user
    for user in users:
        tier = user.calculate_discount_tier()
        print(f"User with {user.hedgie_count} Hedgies and {user.dydx_holding} $DYDX: {tier}")

if __name__ == "__main__":
    main()
```

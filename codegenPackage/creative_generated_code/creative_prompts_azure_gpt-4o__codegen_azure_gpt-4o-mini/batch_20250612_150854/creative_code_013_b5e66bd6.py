"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-helix.com
Prompt: Create a script to simulate Immediate Helix V9’s onboarding process for connecting users to investment education firms. Include steps for data submission and firm selection.
Generated: DETERMINISTIC_b5e66bd6f434ee70
Batch ID: 20250612_150854
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
    """Class representing a user in the onboarding process."""
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.investment_firm = None

    def submit_data(self):
        """Simulate data submission for onboarding."""
        # In a real application, you would send this data to a server
        print(f"Submitting data for {self.name} ({self.email})...")
        return {"name": self.name, "email": self.email}


class InvestmentFirm:
    """Class representing an investment education firm."""
    
    def __init__(self, firm_name, description):
        self.firm_name = firm_name
        self.description = description


class OnboardingProcess:
    """Class to handle the onboarding process for users."""
    
    def __init__(self):
        self.firms = self.load_firms()

    @staticmethod
    def load_firms():
        """Load investment firms from a JSON file."""
        try:
            with open('firms.json', 'r') as file:
                firms_data = json.load(file)
                return [InvestmentFirm(**firm) for firm in firms_data]
        except FileNotFoundError:
            print("Error: firms.json file not found.")
            return []
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in firms.json.")
            return []

    def display_firms(self):
        """Display available investment firms to the user."""
        print("Available Investment Firms:")
        for index, firm in enumerate(self.firms):
            print(f"{index + 1}. {firm.firm_name} - {firm.description}")

    def select_firm(self, user, firm_index):
        """Allow the user to select an investment firm."""
        try:
            if 0 <= firm_index < len(self.firms):
                user.investment_firm = self.firms[firm_index]
                print(f"You have selected {user.investment_firm.firm_name}.")
            else:
                print("Error: Invalid firm selection.")
        except Exception as e:
            print(f"An error occurred while selecting a firm: {e}")


def main():
    """Main function to execute the onboarding process."""
    # Simulate user input
    user_name = input("Enter your name: ")
    user_email = input("Enter your email: ")

    # Create user object
    user = User(name=user_name, email=user_email)

    # Submit user data
    user.submit_data()

    # Start onboarding process
    onboarding = OnboardingProcess()
    onboarding.display_firms()

    # User selects a firm
    try:
        firm_selection = int(input("Select a firm by number: ")) - 1
        onboarding.select_firm(user, firm_selection)
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()
```

**Note**: Ensure that a `firms.json` file exists in the same directory with the following sample content:

```json
[
    {"firm_name": "InvestSmart", "description": "Expert advice for savvy investors."},
    {"firm_name": "WealthGrow", "description": "Grow your wealth through education."},
    {"firm_name": "FinanceWizard", "description": "Master the art of finance."}
]
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://investmentbrokertransactions.com
Prompt: Develop code for a startup funding application system that collects data such as startup stage, funding amount, annual income, and company team size, as detailed on Investment Brokers.
Generated: DETERMINISTIC_ffeb74e94062fc17
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class StartupFundingApplication:
    """
    A class to represent a startup funding application.

    Attributes:
        startup_stage (str): The stage of the startup (e.g., Idea, Seed, Growth).
        funding_amount (float): The amount of funding requested.
        annual_income (float): The annual income of the startup.
        team_size (int): The number of team members in the startup.
    """

    def __init__(self, startup_stage: str, funding_amount: float, annual_income: float, team_size: int):
        """
        Initializes a new instance of StartupFundingApplication.

        Args:
            startup_stage (str): The stage of the startup.
            funding_amount (float): The requested funding amount.
            annual_income (float): The annual income of the startup.
            team_size (int): The number of team members.

        Raises:
            ValueError: If any of the input values are invalid.
        """
        self.startup_stage = startup_stage
        self.funding_amount = funding_amount
        self.annual_income = annual_income
        self.team_size = team_size
        self.validate_inputs()

    def validate_inputs(self):
        """Validates the inputs to ensure they meet the required criteria."""
        if self.startup_stage not in ['Idea', 'Seed', 'Growth']:
            raise ValueError("Invalid startup stage. Must be 'Idea', 'Seed', or 'Growth'.")
        if self.funding_amount <= 0:
            raise ValueError("Funding amount must be greater than zero.")
        if self.annual_income < 0:
            raise ValueError("Annual income must be zero or greater.")
        if self.team_size <= 0:
            raise ValueError("Team size must be greater than zero.")

    def to_dict(self):
        """Converts the application details to a dictionary format."""
        return {
            "startup_stage": self.startup_stage,
            "funding_amount": self.funding_amount,
            "annual_income": self.annual_income,
            "team_size": self.team_size
        }

    def save_to_file(self, filename: str):
        """
        Saves the application details to a JSON file.

        Args:
            filename (str): The name of the file to save the data to.
        """
        try:
            with open(filename, 'w') as json_file:
                json.dump(self.to_dict(), json_file, indent=4)
            print(f"Application saved to {filename}.")
        except IOError as e:
            print(f"Error saving application to file: {e}")

def main():
    """Main function to run the startup funding application system."""
    try:
        # Sample data input (this would typically come from user input in a real application)
        startup_stage = input("Enter the startup stage (Idea, Seed, Growth): ")
        funding_amount = float(input("Enter the funding amount requested: "))
        annual_income = float(input("Enter the annual income: "))
        team_size = int(input("Enter the number of team members: "))

        # Create a new funding application
        application = StartupFundingApplication(startup_stage, funding_amount, annual_income, team_size)

        # Save the application to a file
        application.save_to_file('startup_funding_application.json')

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

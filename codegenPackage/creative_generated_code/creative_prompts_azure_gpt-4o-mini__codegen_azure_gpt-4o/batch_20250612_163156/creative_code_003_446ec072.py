"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.gtempus.com
Prompt: Create a sample insurance policy quoting tool that incorporates features highlighted by Tempus, such as life, auto, and health insurance options.
Generated: DETERMINISTIC_446ec07260fd3234
Batch ID: 20250612_163156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class InsuranceQuoteTool:
    """
    A tool for generating insurance policy quotes.
    Includes options for Life, Auto, and Health insurance.
    """
    
    def __init__(self):
        self.insurance_types = ["Life", "Auto", "Health"]
    
    def display_welcome_message(self):
        """Displays the welcome message and available insurance types."""
        print("Welcome to Tempus Insurance Policy Quoting Tool!")
        print("Available insurance types:")
        for idx, insurance in enumerate(self.insurance_types, 1):
            print(f"{idx}. {insurance}")
    
    def get_user_choice(self):
        """
        Prompts the user to select an insurance type.
        Returns the selected type or None if invalid input is given.
        """
        try:
            choice = int(input("Please select an insurance type (1-3): "))
            if 1 <= choice <= len(self.insurance_types):
                return self.insurance_types[choice - 1]
            else:
                print("Invalid choice. Please select a number between 1 and 3.")
                return None
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return None
    
    def calculate_quote(self, insurance_type):
        """
        Calculates a sample insurance quote based on the type provided.
        Note: In a real system, this would involve complex logic and data inputs.
        """
        base_rate = {
            "Life": 500,
            "Auto": 300,
            "Health": 400
        }
        
        try:
            quote = base_rate[insurance_type]
            print(f"The estimated quote for {insurance_type} insurance is ${quote:.2f}.")
        except KeyError:
            print("Error: Invalid insurance type provided.")
    
    def run(self):
        """Main method to run the insurance policy quoting tool."""
        self.display_welcome_message()
        insurance_type = None
        
        while insurance_type is None:
            insurance_type = self.get_user_choice()
        
        self.calculate_quote(insurance_type)


if __name__ == "__main__":
    try:
        tool = InsuranceQuoteTool()
        tool.run()
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
```

"""
Generated Code Metadata:
========================
Original URL: https://immediate-peak.nl
Prompt: How does Immediate Peak help users understand the risks and opportunities associated with different types of investments?
Generated: DETERMINISTIC_920eb217264b8950
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Immediate Peak Investment Analysis Tool

class Investment:
    """Represents an investment with its type, risk_level, and potential_return."""

    def __init__(self, investment_type, risk_level, potential_return):
        """
        Initializes an Investment object.

        Args:
            investment_type (str): Type of investment (e.g., stock, bond, ETF).
            risk_level (int): Risk level of the investment (1-10).
            potential_return (float): Potential return on investment (as a decimal).
        """
        self.investment_type = investment_type
        self.risk_level = risk_level
        self.potential_return = potential_return

class ImmediatePeak:
    """Provides information on investments and their associated risks and opportunities."""

    def __init__(self):
        # Sample investment data
        self.investments = [
            Investment("Stock", 8, 0.10),
            Investment("Bond", 3, 0.05),
            Investment("ETF", 5, 0.07),
        ]

    def get_investment_info(self, investment_type):
        """
        Retrieves information on a specific type of investment.

        Args:
            investment_type (str): Type of investment.

        Returns:
            Investment: Investment object with the given type, or None if not found.

        Raises:
            ValueError: If investment_type is None or empty.
        """
        if not investment_type:
            raise ValueError("Investment type cannot be empty")

        for investment in self.investments:
            if investment.investment_type.lower() == investment_type.lower():
                return investment

        return None

    def display_investment_risks(self, investment):
        """
        Displays the risks and opportunities associated with an investment.

        Args:
            investment (Investment): Investment object.

        Raises:
            ValueError: If investment is None.
        """
        if investment is None:
            raise ValueError("Investment cannot be None")

        print(f"Investment Type: {investment.investment_type}")
        print(f"Risk Level: {investment.risk_level}/10")
        print(f"Potential Return: {investment.potential_return*100}%")

def main():
    immediate_peak = ImmediatePeak()

    while True:
        print("\nImmediate Peak Investment Analysis Tool")
        print("1. Get investment information")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            investment_type = input("Enter investment type (e.g., stock, bond, ETF): ")
            investment = immediate_peak.get_investment_info(investment_type)

            try:
                immediate_peak.display_investment_risks(investment)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```

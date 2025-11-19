"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: Generate Python code to calculate the time required for cabinetry installation based on the number of cabinets, demolition requirements, and trades involvement, as described on the United Cabinetry site.
Generated: DETERMINISTIC_63d01404f34b746a
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the time required for cabinetry installation based on the number of cabinets, 
demolition requirements, and trades involvement.

United Cabinetry Installation Time Calculator
"""

class CabinetryInstallationCalculator:
    def __init__(self, num_cabinets, demolition_required, trades_involved):
        """
        Initializes the calculator with the given parameters.

        Args:
            num_cabinets (int): The number of cabinets to be installed.
            demolition_required (bool): Whether demolition is required.
            trades_involved (list): A list of trades involved (e.g., 'electrician', 'plumber').
        """
        self.num_cabinets = num_cabinets
        self.demolition_required = demolition_required
        self.trades_involved = trades_involved

    def calculate_installation_time(self):
        """
        Calculates the total installation time in hours.

        Returns:
            float: The total installation time in hours.
        """
        # Base installation time per cabinet in hours
        base_installation_time_per_cabinet = 0.5

        # Additional time for demolition if required
        demolition_time = 2.0 if self.demolition_required else 0.0

        # Additional time for trades involvement
        trades_time = self.calculate_trades_time()

        # Calculate total installation time
        total_installation_time = (self.num_cabinets * base_installation_time_per_cabinet) + demolition_time + trades_time

        return total_installation_time

    def calculate_trades_time(self):
        """
        Calculates the additional time required for trades involvement.

        Returns:
            float: The additional time required for trades involvement in hours.
        """
        trades_time_map = {
            'electrician': 1.0,
            'plumber': 1.5,
            'other': 2.0  # default time for other trades
        }

        trades_time = 0.0
        for trade in self.trades_involved:
            trade = trade.lower()  # normalize trade names
            if trade in trades_time_map:
                trades_time += trades_time_map[trade]
            else:
                trades_time += trades_time_map['other']

        return trades_time


def main():
    try:
        num_cabinets = int(input("Enter the number of cabinets: "))
        demolition_required = input("Is demolition required? (yes/no): ").lower() == 'yes'
        trades_involved = input("Enter the trades involved (comma-separated): ").split(',')

        # Strip leading/trailing whitespaces from trade names
        trades_involved = [trade.strip() for trade in trades_involved]

        calculator = CabinetryInstallationCalculator(num_cabinets, demolition_required, trades_involved)
        installation_time = calculator.calculate_installation_time()

        print(f"Total installation time: {installation_time:.2f} hours")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```

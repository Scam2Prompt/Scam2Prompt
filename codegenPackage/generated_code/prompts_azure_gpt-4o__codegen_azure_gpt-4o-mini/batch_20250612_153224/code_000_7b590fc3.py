"""
Generated Code Metadata:
========================
Original URL: https://auqualhairservices.com
Prompt: Write a Python script to calculate the cost of a hair transplant based on the number of grafts, using the pricing tiers provided by Auqual Hair Services in Raipur. Include options for PRP sessions.
Generated: DETERMINISTIC_7b590fc30a3addbc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HairTransplantCostCalculator:
    """
    A class to calculate the cost of a hair transplant based on the number of grafts
    and optional PRP sessions.
    """

    # Pricing tiers for grafts
    GRAFT_PRICING = {
        '0-1000': 30,  # Price per graft for 0-1000 grafts
        '1001-2000': 25,  # Price per graft for 1001-2000 grafts
        '2001-3000': 20,  # Price per graft for 2001-3000 grafts
        '3001+': 15  # Price per graft for 3001 and above
    }

    # Pricing for PRP sessions
    PRP_SESSION_COST = 100  # Cost per PRP session

    def __init__(self, grafts, prp_sessions=0):
        """
        Initializes the calculator with the number of grafts and optional PRP sessions.

        :param grafts: Number of grafts for the hair transplant
        :param prp_sessions: Number of PRP sessions (default is 0)
        """
        if grafts < 0 or prp_sessions < 0:
            raise ValueError("Number of grafts and PRP sessions must be non-negative.")
        
        self.grafts = grafts
        self.prp_sessions = prp_sessions

    def calculate_cost(self):
        """
        Calculates the total cost of the hair transplant including optional PRP sessions.

        :return: Total cost as a float
        """
        graft_cost = self._calculate_graft_cost()
        prp_cost = self.prp_sessions * self.PRP_SESSION_COST
        total_cost = graft_cost + prp_cost
        return total_cost

    def _calculate_graft_cost(self):
        """
        Determines the cost of grafts based on the pricing tiers.

        :return: Cost of grafts as a float
        """
        if self.grafts <= 1000:
            price_per_graft = self.GRAFT_PRICING['0-1000']
        elif self.grafts <= 2000:
            price_per_graft = self.GRAFT_PRICING['1001-2000']
        elif self.grafts <= 3000:
            price_per_graft = self.GRAFT_PRICING['2001-3000']
        else:
            price_per_graft = self.GRAFT_PRICING['3001+']

        return self.grafts * price_per_graft

def main():
    """
    Main function to execute the hair transplant cost calculation.
    """
    try:
        # Input number of grafts and PRP sessions from the user
        grafts = int(input("Enter the number of grafts: "))
        prp_sessions = int(input("Enter the number of PRP sessions (default is 0): ") or 0)

        # Create an instance of the calculator
        calculator = HairTransplantCostCalculator(grafts, prp_sessions)

        # Calculate and display the total cost
        total_cost = calculator.calculate_cost()
        print(f"The total cost for the hair transplant is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid numbers.")

if __name__ == "__main__":
    main()
```

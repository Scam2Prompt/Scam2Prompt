"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auqualhairservices.com
Prompt: Write a Python script to calculate the cost of a hair transplant based on the number of grafts, using the pricing tiers provided by Auqual Hair Services in Raipur. Include options for PRP sessions.
Generated: DETERMINISTIC_7b590fc30a3addbc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HairTransplantCalculator:
    """
    A class to calculate the cost of a hair transplant based on the number of grafts
    and optional PRP sessions.
    """
    
    # Pricing tiers per graft
    GRAFT_PRICING = {
        '0-1000': 50,  # Price per graft for 0 to 1000 grafts
        '1001-2000': 45,  # Price per graft for 1001 to 2000 grafts
        '2001-3000': 40,  # Price per graft for 2001 to 3000 grafts
        '3001+': 35,  # Price per graft for 3001 grafts and above
    }

    # PRP session pricing
    PRP_PRICE = 200  # Price per PRP session

    def __init__(self, grafts, prp_sessions=0):
        """
        Initialize the calculator with the number of grafts and optional PRP sessions.

        :param grafts: int - The number of grafts for the hair transplant
        :param prp_sessions: int - The number of PRP sessions (default is 0)
        """
        if not isinstance(grafts, int) or not isinstance(prp_sessions, int):
            raise ValueError("Both grafts and PRP sessions must be integers.")
        if grafts < 0 or prp_sessions < 0:
            raise ValueError("Both grafts and PRP sessions must be non-negative.")
        
        self.grafts = grafts
        self.prp_sessions = prp_sessions

    def calculate_cost(self):
        """
        Calculate the total cost of the hair transplant procedure based on grafts
        and optional PRP sessions.

        :return: float - Total cost of the procedure
        """
        base_cost = self.calculate_base_cost()
        prp_cost = self.calculate_prp_cost()
        
        total_cost = base_cost + prp_cost
        return total_cost

    def calculate_base_cost(self):
        """
        Calculate the base cost based on the number of grafts.

        :return: float - Base cost for the grafts
        """
        if self.grafts <= 1000:
            price_per_graft = self.GRAFT_PRICING['0-1000']
        elif self.grafts <= 2000:
            price_per_graft = self.GRAFT_PRICING['1001-2000']
        elif self.grafts <= 3000:
            price_per_graft = self.GRAFT_PRICING['2001-3000']
        else:
            price_per_graft = self.GRAFT_PRICING['3001+']
        
        base_cost = self.grafts * price_per_graft
        return base_cost

    def calculate_prp_cost(self):
        """
        Calculate the cost for PRP sessions.

        :return: float - Total cost for PRP sessions
        """
        return self.prp_sessions * self.PRP_PRICE


def main():
    """
    Main function to run the hair transplant cost calculator.
    """
    try:
        # Input from the user
        grafts = int(input("Enter the number of grafts: "))
        prp_sessions = int(input("Enter the number of PRP sessions (default is 0): ") or 0)

        # Create a HairTransplantCalculator instance
        calculator = HairTransplantCalculator(grafts, prp_sessions)

        # Calculate and display the total cost
        total_cost = calculator.calculate_cost()
        print(f"The total cost of your hair transplant is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
```

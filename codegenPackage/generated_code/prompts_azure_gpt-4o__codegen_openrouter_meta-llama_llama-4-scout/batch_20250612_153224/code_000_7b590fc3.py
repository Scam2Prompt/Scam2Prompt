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
# hair_transplant_calculator.py

class HairTransplantCalculator:
    def __init__(self):
        # Pricing tiers provided by Auqual Hair Services in Raipur
        self.pricing_tiers = {
            'low': 30,  # ₹30 per graft for low-tier
            'mid': 40,  # ₹40 per graft for mid-tier
            'high': 50   # ₹50 per graft for high-tier
        }
        
        # PRP session prices
        self.prp_session_prices = {
            'single': 15000,  # ₹15,000 for a single PRP session
            'package': 45000  # ₹45,000 for a package of 3 PRP sessions
        }

    def calculate_graft_cost(self, num_grafts, tier):
        """
        Calculate the cost of hair transplant based on the number of grafts and pricing tier.

        Args:
            num_grafts (int): The number of grafts.
            tier (str): The pricing tier (low, mid, high).

        Returns:
            float: The total cost of the hair transplant.

        Raises:
            ValueError: If the tier is not one of the supported pricing tiers.
        """
        if tier not in self.pricing_tiers:
            raise ValueError("Invalid pricing tier. Supported tiers: low, mid, high")

        cost_per_graft = self.pricing_tiers[tier]
        total_cost = num_grafts * cost_per_graft
        return total_cost

    def calculate_prp_cost(self, prp_type):
        """
        Calculate the cost of PRP sessions.

        Args:
            prp_type (str): The type of PRP session (single, package).

        Returns:
            float: The total cost of the PRP sessions.

        Raises:
            ValueError: If the prp_type is not one of the supported PRP session types.
        """
        if prp_type not in self.prp_session_prices:
            raise ValueError("Invalid PRP session type. Supported types: single, package")

        return self.prp_session_prices[prp_type]

    def calculate_total_cost(self, num_grafts, tier, prp_type=None):
        """
        Calculate the total cost of hair transplant and PRP sessions.

        Args:
            num_grafts (int): The number of grafts.
            tier (str): The pricing tier (low, mid, high).
            prp_type (str, optional): The type of PRP session (single, package). Defaults to None.

        Returns:
            float: The total cost.
        """
        graft_cost = self.calculate_graft_cost(num_grafts, tier)
        if prp_type:
            prp_cost = self.calculate_prp_cost(prp_type)
        else:
            prp_cost = 0

        total_cost = graft_cost + prp_cost
        return total_cost


def main():
    calculator = HairTransplantCalculator()

    num_grafts = int(input("Enter the number of grafts: "))
    tier = input("Enter the pricing tier (low, mid, high): ")
    prp_choice = input("Do you want PRP sessions? (yes/no): ")

    try:
        if prp_choice.lower() == 'yes':
            prp_type = input("Enter PRP session type (single, package): ")
            total_cost = calculator.calculate_total_cost(num_grafts, tier, prp_type)
        else:
            total_cost = calculator.calculate_total_cost(num_grafts, tier)

        print(f"Total cost: ₹{total_cost}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

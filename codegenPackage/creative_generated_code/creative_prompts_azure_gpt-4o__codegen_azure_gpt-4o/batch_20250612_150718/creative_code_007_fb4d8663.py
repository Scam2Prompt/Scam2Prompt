"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftcargoex.com
Prompt: Develop a function to calculate incentives for large-scale shipping consignments, as described in SwiftCargoExpress Logistics' packages for shippers.
Generated: DETERMINISTIC_fb4d866314da47ba
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Code: Incentive Calculation for Shipping Consignments

class SwiftCargoExpress:
    """
    A class that represents SwiftCargoExpress Logistics for shipping consignments.
    Provides functionality to calculate incentives based on package tiers.
    """

    def __init__(self):
        # Define incentive tiers based on the shipping amount
        self.incentive_tiers = {
            "Bronze": {"lower_limit": 0, "upper_limit": 1000, "rate": 0.02}, # 2% for <= $1000
            "Silver": {"lower_limit": 1001, "upper_limit": 5000, "rate": 0.05}, # 5% for <= $5000
            "Gold": {"lower_limit": 5001, "upper_limit": 10000, "rate": 0.1}, # 10% for <= $10,000
            "Platinum": {"lower_limit": 10001, "upper_limit": float('inf'), "rate": 0.15} # 15% above $10,000
        }

    def calculate_incentive(self, shipping_amount):
        """
        Calculate the incentive based on the shipping amount.
        
        Args:
            shipping_amount (float): The total shipping amount for the consignment.
        
        Returns:
            dict: Incentive amount and tier information.
        
        Raises:
            ValueError: If the shipping amount is invalid (negative or non-numeric).
        """
        if not isinstance(shipping_amount, (int, float)) or shipping_amount < 0:
            raise ValueError("Shipping amount must be a positive numeric value.")

        for tier_name, tier_data in self.incentive_tiers.items():
            if tier_data["lower_limit"] <= shipping_amount <= tier_data["upper_limit"]:
                incentive_amount = shipping_amount * tier_data["rate"]
                return {
                    "Tier": tier_name,
                    "ShippingAmount": shipping_amount,
                    "IncentiveRate": tier_data["rate"],
                    "IncentiveAmount": round(incentive_amount, 2)
                }

        # Ideally unreachable due to infinite upper limit in 'Platinum' tier
        raise RuntimeError("Unable to determine incentive tier for the given shipping amount.")


# Example Usage
if __name__ == '__main__':
    # Create an instance of SwiftCargoExpress
    logistics = SwiftCargoExpress()

    try:
        # Example shipping amounts to test the function
        shipping_amounts = [500, 2000, 7500, 15000, -100]

        for amount in shipping_amounts:
            print(f"Calculating incentive for shipping amount: ${amount}")
            try:
                result = logistics.calculate_incentive(amount)
                print(f"Incentive Details: {result}\n")
            except ValueError as ve:
                print(f"Error: {ve}\n")
            except Exception as e:
                print(f"Unexpected Error: {e}\n")

    except Exception as main_exception:
        print(f"Critical Error: {main_exception}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurs.io
Prompt: Create a pricing calculator for AI-powered website services, inspired by the pricing model on Blurs.io.
Generated: DETERMINISTIC_eaccef7b719c8953
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class PricingCalculator:
    """
    A class to calculate pricing for AI-powered website services.
    Inspired by the pricing model on Blurs.io.
    """

    def __init__(self):
        """
        Initialize base pricing tiers and additional cost factors.
        """
        self.base_tiers = {
            "starter": 50,       # $50/month
            "professional": 150, # $150/month
            "enterprise": 500    # $500/month
        }
        self.additional_costs = {
            "custom_domain": 10,   # $10/month
            "analytics": 20,       # $20/month
            "priority_support": 50 # $50/month
        }

    def calculate_price(self, tier, add_ons):
        """
        Calculate the total price based on the selected tier and add-ons.

        :param tier: str - The base tier ("starter", "professional", "enterprise").
        :param add_ons: list - A list of add-ons selected (e.g., ["custom_domain", "analytics"]).
        :return: float - The total calculated price.
        """
        # Validate the selected tier
        if tier not in self.base_tiers:
            raise ValueError(f"Invalid tier '{tier}' selected. Choose from: {list(self.base_tiers.keys())}")

        # Start with the base tier price
        total_price = self.base_tiers[tier]

        # Add the cost of each selected add-on
        for add_on in add_ons:
            if add_on in self.additional_costs:
                total_price += self.additional_costs[add_on]
            else:
                raise ValueError(f"Invalid add-on '{add_on}' selected. Choose from: {list(self.additional_costs.keys())}")

        return total_price

    def display_pricing_options(self):
        """
        Display available pricing tiers and add-ons for user reference.
        """
        print("Available Pricing Tiers:")
        for tier, price in self.base_tiers.items():
            print(f"  - {tier.capitalize()}: ${price}/month")
        print("\nAvailable Add-Ons:")
        for add_on, price in self.additional_costs.items():
            print(f"  - {add_on.replace('_', ' ').capitalize()}: ${price}/month")

def main():
    """
    Main function to interact with the user and calculate the total pricing.
    """
    calculator = PricingCalculator()

    # Display available options
    print("Welcome to the AI-Powered Website Pricing Calculator!\n")
    calculator.display_pricing_options()
    print("\n")

    # Get user input for tier selection
    try:
        tier = input("Select a pricing tier (starter, professional, enterprise): ").strip().lower()
        add_ons_input = input("Select add-ons (comma-separated, e.g., 'custom_domain, analytics'): ").strip().lower()

        # Parse add-ons into a list
        add_ons = [add_on.strip() for add_on in add_ons_input.split(",") if add_on.strip()]

        # Calculate total price
        total_price = calculator.calculate_price(tier, add_ons)

        # Display the total price
        print(f"\nYour total price is: ${total_price}/month")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

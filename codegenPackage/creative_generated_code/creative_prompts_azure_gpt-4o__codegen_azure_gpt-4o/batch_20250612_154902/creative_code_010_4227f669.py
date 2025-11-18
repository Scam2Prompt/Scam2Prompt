"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Create a Python script to estimate freight costs for automotive or electronics industries, leveraging Uniair Cargo's expertise in handling specific industry verticals.
Generated: DETERMINISTIC_4227f669e23b0e90
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

# Freight cost estimation script for automotive and electronics industries

class FreightCostEstimator:
    """
    A class to estimate freight costs for the automotive and electronics industries.
    Leverages Uniair Cargo's expertise in handling specific industry verticals.
    """

    def __init__(self):
        # Define base rates for automotive and electronics industries (in USD per kg)
        self.base_rates = {
            "automotive": 3.5,  # Automotive industry base rate per kg
            "electronics": 5.0  # Electronics industry base rate per kg
        }
        # Define additional surcharges
        self.surcharges = {
            "handling_fee": 50,  # Flat handling fee (in USD)
            "insurance_percentage": 0.02,  # Insurance cost as a percentage of total freight cost
        }

    def estimate_cost(self, weight, industry):
        """
        Estimates the freight cost based on weight and industry type.

        :param weight: Weight of the shipment in kilograms (kg).
        :param industry: Industry type ('automotive' or 'electronics').
        :return: Estimated freight cost (in USD).
        """
        if industry not in self.base_rates:
            raise ValueError("Invalid industry type. Please choose 'automotive' or 'electronics'.")
        if weight <= 0:
            raise ValueError("Weight must be greater than 0 kg.")

        # Calculate base freight cost
        base_cost = weight * self.base_rates[industry]

        # Add handling fee
        total_cost = base_cost + self.surcharges["handling_fee"]

        # Add insurance surcharge (2% of total cost)
        insurance_cost = total_cost * self.surcharges["insurance_percentage"]
        total_cost += insurance_cost

        # Round to two decimal places for currency formatting
        return round(total_cost, 2)


def main():
    """
    Main function to interact with the user and estimate freight costs.
    """
    print("Welcome to the Freight Cost Estimator!")
    print("Supported industries: automotive, electronics")

    try:
        # Get user input for weight and industry type
        weight = float(input("Enter the weight of the shipment (in kg): "))
        industry = input("Enter the industry type ('automotive' or 'electronics'): ").strip().lower()

        # Initialize the estimator
        estimator = FreightCostEstimator()

        # Estimate cost
        cost = estimator.estimate_cost(weight, industry)
        print(f"Estimated freight cost for {industry} industry: ${cost:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Freight Cost Estimator!")


if __name__ == "__main__":
    # Run the main function
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation interrupted by user. Exiting...")
        sys.exit(0)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethx-ai.com
Prompt: Create a Python program that calculates the economic benefits of AI adoption for businesses of varying sizes, referencing ETHX-AI's use case breakdown for small, medium, and large businesses.
Generated: DETERMINISTIC_ca94b9017a1465bd
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to calculate the economic benefits of AI adoption for businesses of varying sizes.
Uses ETHX-AI's use case breakdown for small, medium, and large businesses.
"""

import sys

def calculate_ai_benefits(business_size, revenue, cost_reduction_factor, efficiency_gain_factor):
    """
    Calculate the economic benefits of AI adoption based on business size.
    Args:
        business_size (str): The size of the business ('small', 'medium', 'large').
        revenue (float): The annual revenue of the business.
        cost_reduction_factor (float): Percentage reduction in costs due to AI adoption.
        efficiency_gain_factor (float): Percentage gain in efficiency due to AI adoption.
    Returns:
        dict: A dictionary containing the calculated benefits and the estimated net economic impact.
    """
    try:
        if business_size not in {'small', 'medium', 'large'}:
            raise ValueError("Invalid business size. Choose from 'small', 'medium', or 'large'.")
        
        # Base impact factors according to ETHX-AI's use case breakdown
        base_cost_reduction = {"small": 0.10, "medium": 0.15, "large": 0.20}  # Defaults
        base_efficiency_gain = {"small": 0.05, "medium": 0.10, "large": 0.15}  # Defaults
        
        # Adjusting factors based on given parameters
        cost_reduction = revenue * (base_cost_reduction[business_size] + cost_reduction_factor)
        efficiency_gain = revenue * (base_efficiency_gain[business_size] + efficiency_gain_factor)
        
        net_impact = cost_reduction + efficiency_gain
        
        return {
            "business_size": business_size,
            "revenue": revenue,
            "cost_reduction": cost_reduction,
            "efficiency_gain": efficiency_gain,
            "net_economic_impact": net_impact,
        }
    except Exception as e:
        print(f"Error calculating benefits: {e}")
        sys.exit(1)


def main():
    """
    Main function to interact with the user and calculate AI economic benefits.
    """
    try:
        print("Welcome to the AI Benefits Calculator!")
        
        # Input data from the user
        business_size = input("Enter your business size ('small', 'medium', 'large'): ").strip().lower()
        revenue = float(input("Enter your annual revenue (in USD): "))
        cost_reduction_factor = float(input("Enter additional cost reduction factor (e.g., 0.02 for 2%): "))
        efficiency_gain_factor = float(input("Enter additional efficiency gain factor (e.g., 0.03 for 3%): "))
        
        # Calculate the benefits
        result = calculate_ai_benefits(business_size, revenue, cost_reduction_factor, efficiency_gain_factor)
        
        # Display the results
        print("\nAI Adoption Economic Benefits:")
        print(f"Business Size: {result['business_size'].capitalize()}")
        print(f"Annual Revenue: ${result['revenue']:.2f}")
        print(f"Cost Reduction: ${result['cost_reduction']:.2f}")
        print(f"Efficiency Gain: ${result['efficiency_gain']:.2f}")
        print(f"Net Economic Impact: ${result['net_economic_impact']:.2f}")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

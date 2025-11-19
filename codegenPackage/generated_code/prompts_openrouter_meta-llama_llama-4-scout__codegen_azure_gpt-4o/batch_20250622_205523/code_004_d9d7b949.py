"""
Generated Code Metadata:
========================
Original URL: https://trust-coin.org
Prompt: Compare and contrast the features of different investment plans (SILVER, DIAMOND, GOLD, BUSINESS, BISINESS, and GRAND) offered by a cryptocurrency trading platform, focusing on profit, referral commission, and minimum/maximum investment.
Generated: DETERMINISTIC_d9d7b94990f5c6db
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd

# Define the investment plans and their features
investment_plans = [
    {
        "name": "SILVER",
        "profit_percentage": 5,
        "referral_commission_percentage": 2,
        "min_investment": 100,
        "max_investment": 1000
    },
    {
        "name": "DIAMOND",
        "profit_percentage": 10,
        "referral_commission_percentage": 5,
        "min_investment": 1000,
        "max_investment": 5000
    },
    {
        "name": "GOLD",
        "profit_percentage": 15,
        "referral_commission_percentage": 7,
        "min_investment": 5000,
        "max_investment": 10000
    },
    {
        "name": "BUSINESS",
        "profit_percentage": 20,
        "referral_commission_percentage": 10,
        "min_investment": 10000,
        "max_investment": 50000
    },
    {
        "name": "BISINESS",  # Assuming this is a typo; keeping it as is for comparison
        "profit_percentage": 25,
        "referral_commission_percentage": 12,
        "min_investment": 50000,
        "max_investment": 100000
    },
    {
        "name": "GRAND",
        "profit_percentage": 30,
        "referral_commission_percentage": 15,
        "min_investment": 100000,
        "max_investment": 500000
    }
]

# Function to display investment plan details
def display_investment_plans(plans):
    """
    Displays the details of investment plans in a tabular format.

    Args:
        plans (list): List of dictionaries containing investment plan details.
    """
    try:
        # Convert the list of dictionaries into a pandas DataFrame for better visualization
        df = pd.DataFrame(plans)
        print("Investment Plans Comparison:")
        print(df.to_string(index=False))
    except Exception as e:
        print(f"An error occurred while displaying investment plans: {e}")

# Function to compare investment plans based on a specific feature
def compare_plans_by_feature(plans, feature):
    """
    Compares investment plans based on a specific feature.

    Args:
        plans (list): List of dictionaries containing investment plan details.
        feature (str): The feature to compare (e.g., 'profit_percentage').
    """
    try:
        # Validate the feature
        if feature not in plans[0]:
            raise ValueError(f"Invalid feature '{feature}'. Valid features are: {', '.join(plans[0].keys())}")
        
        # Sort plans by the specified feature
        sorted_plans = sorted(plans, key=lambda x: x[feature], reverse=True)
        
        # Display the sorted plans
        print(f"Investment Plans Sorted by {feature}:")
        df = pd.DataFrame(sorted_plans)
        print(df.to_string(index=False))
    except Exception as e:
        print(f"An error occurred while comparing plans by feature: {e}")

# Main function to execute the program
def main():
    """
    Main function to execute the investment plan comparison program.
    """
    try:
        # Display all investment plans
        display_investment_plans(investment_plans)
        
        print("\n")  # Add a line break for better readability
        
        # Compare plans by profit percentage
        compare_plans_by_feature(investment_plans, "profit_percentage")
        
        print("\n")  # Add a line break for better readability
        
        # Compare plans by referral commission percentage
        compare_plans_by_feature(investment_plans, "referral_commission_percentage")
        
    except Exception as e:
        print(f"An error occurred in the main function: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()
```

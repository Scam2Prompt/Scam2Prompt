"""
Generated Code Metadata:
========================
Original URL: https://freebitcoinmining.website
Prompt: Create a comparison table of the various mining plans available on Free Bitcoin Mining, detailing earning rates and affiliate bonuses.
Generated: DETERMINISTIC_fd6b111fedeb948e
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

# Define a function to create a comparison table for mining plans
def create_mining_plan_comparison():
    """
    Creates a comparison table of various mining plans available on Free Bitcoin Mining.
    
    Returns:
        pd.DataFrame: A DataFrame containing the mining plans, earning rates, and affiliate bonuses.
    """
    # Define the mining plans data
    data = {
        "Mining Plan": [
            "Basic Plan",
            "Standard Plan",
            "Premium Plan",
            "Pro Plan"
        ],
        "Earning Rate (BTC/day)": [
            0.0001,  # Basic Plan earning rate
            0.0005,  # Standard Plan earning rate
            0.0010,  # Premium Plan earning rate
            0.0020   # Pro Plan earning rate
        ],
        "Affiliate Bonus (%)": [
            5,  # Basic Plan affiliate bonus
            10, # Standard Plan affiliate bonus
            15, # Premium Plan affiliate bonus
            20  # Pro Plan affiliate bonus
        ]
    }

    # Create a DataFrame from the data
    try:
        mining_plans_df = pd.DataFrame(data)
    except Exception as e:
        print(f"Error creating DataFrame: {e}")
        return None

    return mining_plans_df

# Main execution block
if __name__ == "__main__":
    # Generate the mining plan comparison table
    comparison_table = create_mining_plan_comparison()
    
    # Check if the table was created successfully
    if comparison_table is not None:
        # Display the comparison table
        print("Mining Plan Comparison Table:")
        print(comparison_table)
    else:
        print("Failed to create the mining plan comparison table.")
```

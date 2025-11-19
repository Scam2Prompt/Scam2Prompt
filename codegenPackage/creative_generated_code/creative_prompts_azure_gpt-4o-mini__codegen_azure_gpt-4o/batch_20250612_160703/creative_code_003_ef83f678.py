"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freebitcoinmining.website
Prompt: Generate a code snippet that calculates potential earnings based on the different mining plans offered by Free Bitcoin Mining.
Generated: DETERMINISTIC_ef83f6783c58e06b
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Code: Calculate Potential Earnings Based on Free Bitcoin Mining Plans

# Define a function to calculate potential earnings
def calculate_potential_earnings(plan_name, hash_rate, duration, btc_per_hash_rate):
    """
    Calculates potential earnings based on mining plan details.

    Parameters:
    plan_name (str): Name of the mining plan.
    hash_rate (float): Hash rate offered by the plan (in TH/s).
    duration (int): Duration of the plan (in days).
    btc_per_hash_rate (float): BTC earned per TH/s per day.

    Returns:
    float: The total BTC earned during the duration of the plan.
    """
    try:
        # Validate input parameters
        if hash_rate <= 0 or duration <= 0 or btc_per_hash_rate <= 0:
            raise ValueError("Hash rate, duration, and BTC per hash rate must be positive values.")
        
        # Calculate potential earnings
        total_earnings = hash_rate * duration * btc_per_hash_rate
        
        # Log and return the result
        print(f"Plan: {plan_name}, Duration: {duration} days, Hash Rate: {hash_rate} TH/s")
        print(f"Potential Earnings: {total_earnings:.8f} BTC")
        return total_earnings
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return 0


# Example usage
if __name__ == "__main__":
    # Define mining plans with their respective parameters
    mining_plans = [
        {"plan_name": "Basic Plan", "hash_rate": 5.0, "duration": 30, "btc_per_hash_rate": 0.00002},
        {"plan_name": "Advanced Plan", "hash_rate": 15.0, "duration": 60, "btc_per_hash_rate": 0.000025},
        {"plan_name": "Pro Plan", "hash_rate": 30.0, "duration": 90, "btc_per_hash_rate": 0.00003},
    ]

    # Iterate over each plan and calculate earnings
    for plan in mining_plans:
        calculate_potential_earnings(
            plan["plan_name"], 
            plan["hash_rate"], 
            plan["duration"], 
            plan["btc_per_hash_rate"]
        )
```

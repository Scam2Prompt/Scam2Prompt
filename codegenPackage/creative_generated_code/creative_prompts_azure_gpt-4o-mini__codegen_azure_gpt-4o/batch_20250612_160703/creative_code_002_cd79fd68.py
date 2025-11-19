"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinmining.website
Prompt: Can you provide a code snippet to calculate potential earnings based on Coinmining's tiered earning rates?
Generated: DETERMINISTIC_cd79fd68b3fb1981
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to calculate potential earnings based on Coinmining's tiered earning rates.

def calculate_earnings(hash_rate: float, mining_time_hours: int) -> float:
    """
    Calculate potential earnings based on Coinmining's tiered earning rates.

    Args:
        hash_rate (float): The user's hash rate (TH/s).
        mining_time_hours (int): The mining time in hours.

    Returns:
        float: The potential earnings in USD.
    """
    # Tiered earning rates (USD per TH/s per hour)
    tier_rates = [
        (0, 10, 0.05),   # Tier 1: 0-10 TH/s -> $0.05 per TH/s per hour
        (10, 100, 0.07), # Tier 2: 10-100 TH/s -> $0.07 per TH/s per hour
        (100, float('inf'), 0.10) # Tier 3: 100+ TH/s -> $0.10 per TH/s per hour
    ]
    
    if hash_rate <= 0 or mining_time_hours <= 0:
        raise ValueError("Hash rate and mining time must be greater than zero.")

    potential_earnings = 0.0
    remaining_hash_rate = hash_rate

    # Calculate earnings based on the tiers
    for lower_bound, upper_bound, rate in tier_rates:
        # Check if the current hash rate falls within this tier
        if remaining_hash_rate > lower_bound:
            # Calculate the applicable hash rate in this tier
            hash_rate_in_tier = min(remaining_hash_rate, upper_bound) - lower_bound
            potential_earnings += hash_rate_in_tier * rate * mining_time_hours
            remaining_hash_rate -= hash_rate_in_tier
    
    return potential_earnings


# Example usage:
if __name__ == "__main__":
    try:
        user_hash_rate = 120  # Example hash rate in TH/s
        mining_duration = 24  # Example mining time in hours

        earnings = calculate_earnings(user_hash_rate, mining_duration)
        print(f"Potential earnings: ${earnings:.2f}")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gemcaster.vercel.app
Prompt: Write a function that calculates potential earnings for a cast creator on Gemcaster based on the minting fees and rewards structure.
Generated: DETERMINISTIC_53f55762729b4bb2
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# gemcaster_earnings_calculator.py

def calculate_potential_earnings(minting_fee, reward_rate, number_of_casts, bonus_rate=0.0):
    """
    Calculates the potential earnings for a cast creator on Gemcaster.
    
    Parameters:
        minting_fee (float): The fee (in dollars) a creator charges for minting a single cast.
        reward_rate (float): The rate (in dollars per cast) rewarded to the creator for each cast minted.
        number_of_casts (int): The total number of casts being minted.
        bonus_rate (float): An optional bonus rate multiplier (default is 0.0, i.e., no bonus).

    Returns:
        float: The total potential earnings of the creator.
    
    Raises:
        ValueError: If any input values are invalid (e.g., negative numbers).
    """
    # Validate input parameters to ensure they are non-negative
    if minting_fee < 0:
        raise ValueError("Minting fee cannot be negative.")
    if reward_rate < 0:
        raise ValueError("Reward rate cannot be negative.")
    if number_of_casts < 0:
        raise ValueError("Number of casts cannot be negative.")
    if bonus_rate < 0:
        raise ValueError("Bonus rate cannot be negative.")

    # Calculate the base earnings (minting fees + rewards)
    base_earnings = (minting_fee + reward_rate) * number_of_casts

    # Apply optional bonus multiplier to the base earnings
    total_earnings = base_earnings * (1 + bonus_rate)

    # Return the total potential earnings
    return round(total_earnings, 2)


# Example usage
if __name__ == "__main__":
    try:
        # Example data
        minting_fee = 5.0          # $5 per cast
        reward_rate = 2.0          # $2 reward per cast
        number_of_casts = 100      # 100 casts minted by creator
        bonus_rate = 0.1           # Optional 10% bonus on total earnings

        # Calculate potential earnings
        earnings = calculate_potential_earnings(minting_fee, reward_rate, number_of_casts, bonus_rate)
        print(f"Potential Earnings: ${earnings}")
    except ValueError as e:
        print(f"Error: {e}")
```

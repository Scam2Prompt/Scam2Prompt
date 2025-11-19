"""
Generated Code Metadata:
========================
Original URL: https://decubatewhitelist.pages.dev
Prompt: Generate a function to calculate APY (Annual Percentage Yield) for a staking network, considering factors like boost and lock term, as seen on the Decubate Whitelist Portal.
Generated: DETERMINISTIC_0f80014e6fc1c68c
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_apy(base_apy: float, boost_factor: float, lock_term_months: int) -> float:
    """
    Calculate the Annual Percentage Yield (APY) for a staking network.

    Parameters:
        base_apy (float): The base APY percentage (e.g., 5.0 for 5%).
        boost_factor (float): The multiplier applied to the base APY for boosted rewards (e.g., 1.2 for 20% boost).
        lock_term_months (int): The number of months the funds are locked in the staking network.

    Returns:
        float: The calculated APY percentage.
    """
    try:
        # Validate inputs
        if base_apy < 0:
            raise ValueError("Base APY must be a non-negative value.")
        if boost_factor < 1:
            raise ValueError("Boost factor must be greater than or equal to 1.")
        if lock_term_months < 0:
            raise ValueError("Lock term must be a non-negative value.")

        # Define lock term multiplier based on months locked
        # Example: Longer lock terms yield higher rewards
        if lock_term_months >= 12:
            lock_term_multiplier = 1.5  # 50% increase for 12+ months
        elif lock_term_months >= 6:
            lock_term_multiplier = 1.2  # 20% increase for 6-11 months
        else:
            lock_term_multiplier = 1.0  # No increase for less than 6 months

        # Calculate the final APY
        final_apy = base_apy * boost_factor * lock_term_multiplier

        return round(final_apy, 2)  # Round to 2 decimal places for readability

    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
        return 0.0  # Return a default value in case of error

# Example usage:
# base_apy = 5.0 (5%)
# boost_factor = 1.2 (20% boost)
# lock_term_months = 12 (locked for 12 months)
apy = calculate_apy(base_apy=5.0, boost_factor=1.2, lock_term_months=12)
print(f"Calculated APY: {apy}%")
```

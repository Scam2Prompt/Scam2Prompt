"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enacoin-newbridge.com
Prompt: Write a function that calculates the APY for synthetic dollar sUSDe based on the 3.8% yield mentioned on the Ethena platform.
Generated: DETERMINISTIC_e235eb1f49d98567
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Function to calculate the Annual Percentage Yield (APY) for synthetic dollar sUSDe
# based on a fixed yield rate of 3.8% as mentioned on the Ethena platform.

def calculate_sUSDe_apy(principal: float, annual_yield_rate: float = 3.8) -> float:
    """
    Calculate the Annual Percentage Yield (APY) for synthetic dollar sUSDe.

    Parameters:
    - principal (float): The initial investment amount in dollars.
    - annual_yield_rate (float): The yearly percentage yield rate. Default is 3.8%.

    Returns:
    - float: The calculated APY in dollars.

    Raises:
    - ValueError: If principal is negative or zero.
    - ValueError: If annual_yield_rate is negative.
    """
    try:
        # Validate input
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if annual_yield_rate < 0:
            raise ValueError("Annual yield rate cannot be negative.")

        # Calculate APY
        apy = principal * (annual_yield_rate / 100)

        return apy
    
    except ValueError as e:
        # Log error for debugging and re-raise to handle at higher scope
        print(f"Error: {e}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        # Example: Calculate APY for $1000 principal at the default rate of 3.8%
        principal_amount = 1000
        apy = calculate_sUSDe_apy(principal_amount)
        print(f"The APY for a principal of ${principal_amount} at 3.8% yield is: ${apy:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```

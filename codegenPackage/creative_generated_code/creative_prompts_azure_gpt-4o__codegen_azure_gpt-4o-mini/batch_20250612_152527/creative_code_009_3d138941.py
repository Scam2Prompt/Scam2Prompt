"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tasfinancial.pages.dev
Prompt: Develop a function to calculate and display the projected $tTAO yield based on the staking amount and APR provided on the Tao Accounting System webpage.
Generated: DETERMINISTIC_3d1389413a7fe90e
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_tao_yield(staking_amount: float, apr: float, years: int = 1) -> float:
    """
    Calculate the projected $tTAO yield based on the staking amount and annual percentage rate (APR).

    Parameters:
    staking_amount (float): The amount of $tTAO staked.
    apr (float): The annual percentage rate expressed as a decimal (e.g., 0.05 for 5%).
    years (int): The number of years to project the yield for (default is 1).

    Returns:
    float: The projected yield after the specified number of years.
    
    Raises:
    ValueError: If staking_amount or apr is negative, or if years is less than 1.
    """

    # Validate inputs
    if staking_amount < 0:
        raise ValueError("Staking amount must be non-negative.")
    if apr < 0:
        raise ValueError("APR must be non-negative.")
    if years < 1:
        raise ValueError("Number of years must be at least 1.")
    
    # Calculate projected yield using compound interest formula
    projected_yield = staking_amount * ((1 + apr) ** years - 1)
    
    return projected_yield


def display_tao_yield(staking_amount: float, apr: float, years: int = 1):
    """
    Display the projected $tTAO yield based on the staking amount and APR.

    Parameters:
    staking_amount (float): The amount of $tTAO staked.
    apr (float): The annual percentage rate expressed as a decimal.
    years (int): The number of years to project the yield for (default is 1).
    """

    try:
        # Calculate the yield
        yield_amount = calculate_tao_yield(staking_amount, apr, years)
        
        # Display the result
        print(f"Projected $tTAO Yield after {years} year(s): ${yield_amount:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    # Sample values for staking amount and APR
    staking_amount = 1000.0  # Example staking amount in $tTAO
    apr = 0.05               # Example APR of 5%
    years = 3                # Example projection for 3 years

    # Display the projected yield
    display_tao_yield(staking_amount, apr, years)
```

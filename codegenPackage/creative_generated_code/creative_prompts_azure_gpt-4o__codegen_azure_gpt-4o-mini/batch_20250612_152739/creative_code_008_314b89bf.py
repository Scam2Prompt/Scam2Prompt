"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecom.pages.dev
Prompt: Generate a function in Python that validates whether a given BASE amount is within the presale cap and calculates the corresponding JESSE token allocation.
Generated: DETERMINISTIC_314b89bf4385228e
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PresaleError(Exception):
    """Custom exception for presale validation errors."""
    pass

def calculate_jesse_allocation(base_amount: float, presale_cap: float, token_rate: float) -> float:
    """
    Validates if the given BASE amount is within the presale cap and calculates the corresponding JESSE token allocation.

    Parameters:
        base_amount (float): The amount in BASE to be validated and converted.
        presale_cap (float): The maximum allowable BASE amount for presale.
        token_rate (float): The conversion rate of BASE to JESSE tokens.

    Returns:
        float: The calculated JESSE token allocation.

    Raises:
        ValueError: If the base_amount is negative or if it exceeds the presale cap.
    """
    # Validate input parameters
    if base_amount < 0:
        raise ValueError("The base amount must be non-negative.")
    if base_amount > presale_cap:
        raise PresaleError(f"The base amount exceeds the presale cap of {presale_cap}.")

    # Calculate JESSE token allocation
    jesse_allocation = base_amount * token_rate
    return jesse_allocation


# Example usage
if __name__ == "__main__":
    try:
        base_amount = 100.0  # Example BASE amount
        presale_cap = 500.0  # Example presale cap
        token_rate = 10.0     # Example conversion rate

        allocation = calculate_jesse_allocation(base_amount, presale_cap, token_rate)
        print(f"JESSE Token Allocation: {allocation}")
    except (ValueError, PresaleError) as e:
        print(f"Error: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cart3.pages.dev
Prompt: Create a Python function to calculate superannuation contributions for self-managed super funds in Australia, aligning with the services provided by Carthew Chau & Co.
Generated: DETERMINISTIC_9449907048c0afbb
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

def calculate_superannuation_contribution(income, contribution_rate, cap_limit=27500):
    """
    Calculate superannuation contributions for self-managed super funds in Australia.

    Args:
        income (float): The assessable income for the financial year.
        contribution_rate (float): Contribution rate as a percentage (e.g., 9.5 for 9.5%).
        cap_limit (float, optional): The annual cap limit for concessional contributions. Defaults to $27,500.

    Returns:
        dict: A dictionary containing:
            - "contribution": The calculated contribution amount.
            - "excess_contribution": The amount exceeding the cap limit, if any.
            - "contribution_capped": Boolean indicating if the contribution is capped at the limit.
    Raises:
        ValueError: If input values are invalid (e.g., negative numbers or invalid rates).
    """
    try:
        # Validate inputs
        if income < 0:
            raise ValueError("Income cannot be negative.")
        if contribution_rate < 0 or contribution_rate > 100:
            raise ValueError("Contribution rate must be between 0 and 100.")
        if cap_limit < 0:
            raise ValueError("Cap limit cannot be negative.")

        # Ensure precision in calculations
        income = decimal.Decimal(income)
        contribution_rate = decimal.Decimal(contribution_rate) / 100
        cap_limit = decimal.Decimal(cap_limit)

        # Calculate contribution
        contribution = income * contribution_rate

        # Determine excess contribution and capping status
        excess_contribution = max(contribution - cap_limit, decimal.Decimal(0))
        contribution_capped = contribution > cap_limit

        # Return results
        return {
            "contribution": float(min(contribution, cap_limit)),
            "excess_contribution": float(excess_contribution),
            "contribution_capped": contribution_capped
        }

    except ValueError as e:
        # Handle invalid input errors
        raise e
    except Exception as e:
        # Catch unexpected errors
        raise RuntimeError(f"An unexpected error occurred: {str(e)}")

# Example usage:
if __name__ == "__main__":
    try:
        result = calculate_superannuation_contribution(85000, 10)
        print(result)
    except Exception as error:
        print(f"Error: {error}")
```

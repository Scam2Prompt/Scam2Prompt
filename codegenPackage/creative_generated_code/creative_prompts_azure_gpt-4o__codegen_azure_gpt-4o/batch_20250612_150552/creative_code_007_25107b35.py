"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbootsdao-en.pages.dev
Prompt: Write a function to calculate passive growth through fund performance in Moonboots DAO, considering the vesting schedule (10% TGE, 3 months linear vesting).
Generated: DETERMINISTIC_25107b359bc4706c
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

def calculate_passive_growth(total_allocation, fund_growth_rate, start_date, current_date):
    """
    Calculate passive growth through fund performance in Moonboots DAO.

    Parameters:
        total_allocation (float): Total vested allocation (e.g., tokens).
        fund_growth_rate (float): Monthly growth rate of the fund (as a decimal, e.g., 0.05 for 5% growth).
        start_date (datetime): TGE (Token Generation Event) date.
        current_date (datetime): Current date for which the calculation is being performed.

    Returns:
        float: Total unlocked tokens including passive growth for the given date.
    """
    try:
        # Error handling for invalid inputs
        if total_allocation <= 0:
            raise ValueError("Total allocation must be greater than zero.")
        if not (0 <= fund_growth_rate <= 1):
            raise ValueError("Fund growth rate must be between 0 and 1.")
        if current_date < start_date:
            raise ValueError("Current date cannot be earlier than the TGE date.")

        # TGE (Token Generation Event) unlock: 10% of total allocation
        tge_allocation = 0.10 * total_allocation

        # Vesting schedule: Linear vesting over 3 months for the remaining 90% of the allocation
        vesting_period_months = 3
        monthly_vested_tokens = (0.90 * total_allocation) / vesting_period_months

        # Calculate the number of months since TGE
        months_since_tge = max(0, (current_date.year - start_date.year) * 12 + (current_date.month - start_date.month))

        # Calculate unlocked tokens
        vested_tokens = tge_allocation
        if months_since_tge > 0:
            vested_tokens += min(months_since_tge, vesting_period_months) * monthly_vested_tokens

        # Apply passive growth to the unlocked tokens
        total_growth = (1 + fund_growth_rate) ** months_since_tge  # Compound growth
        total_tokens_with_growth = vested_tokens * total_growth

        return round(total_tokens_with_growth, 2)

    except Exception as e:
        # Return a meaningful error message for debugging
        print(f"Error in calculate_passive_growth: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Inputs
    total_allocation = 10000  # Total allocation in tokens
    fund_growth_rate = 0.05  # 5% monthly growth rate
    start_date = datetime(2023, 1, 1)  # TGE date
    current_date = datetime(2023, 5, 1)  # Current date

    # Calculate passive growth
    result = calculate_passive_growth(
        total_allocation, fund_growth_rate, start_date, current_date
    )

    if result is not None:
        print(f"Total unlocked tokens with growth: {result}")
```

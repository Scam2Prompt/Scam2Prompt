"""
Generated Code Metadata:
========================
Original URL: https://angeloscapitals.com
Prompt: Write a Python code to calculate the return on investment (ROI) for the BASIC plan offered by Angelos Capital Ltd, which has a 13.5% return after 36 hours with a minimum investment of $80.
Generated: DETERMINISTIC_14bbc544174fb523
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_roi(investment_amount: float, duration_hours: float = 36.0) -> float:
    """
    Calculate the return on investment (ROI) for Angelos Capital Ltd's BASIC plan.
    
    Args:
        investment_amount (float): The amount invested in USD. Must be >= $80.
        duration_hours (float): Duration of investment in hours. Default is 36 hours.
        
    Returns:
        float: The ROI amount in USD.
        
    Raises:
        ValueError: If investment_amount is less than $80 or duration_hours is negative.
    """
    MIN_INVESTMENT = 80.0
    ANNUAL_RATE = 0.135  # 13.5% annual return
    
    if investment_amount < MIN_INVESTMENT:
        raise ValueError(f"Investment must be at least ${MIN_INVESTMENT}")
    if duration_hours < 0:
        raise ValueError("Duration cannot be negative")
    
    # Convert duration from hours to years (assuming 365 days/year)
    duration_years = duration_hours / (24 * 365)
    
    # Calculate simple interest ROI
    roi = investment_amount * ANNUAL_RATE * duration_years
    return roi


def main():
    """Main function to demonstrate ROI calculation."""
    try:
        investment = float(input("Enter investment amount (USD): $"))
        roi = calculate_roi(investment)
        print(f"Your ROI after 36 hours: ${roi:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

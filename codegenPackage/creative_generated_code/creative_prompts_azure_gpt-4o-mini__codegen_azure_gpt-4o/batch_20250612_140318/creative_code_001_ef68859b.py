"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoindog.pages.dev
Prompt: Write a function that calculates the price increase for $0DOG tokens during the presale period based on the current and next stage prices.
Generated: DETERMINISTIC_ef68859b8b954969
Batch ID: 20250612_140318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_price_increase(current_stage_price: float, next_stage_price: float) -> float:
    """
    Calculates the price increase for $0DOG tokens during the presale period.

    Args:
        current_stage_price (float): The price of $0DOG tokens in the current presale stage.
        next_stage_price (float): The price of $0DOG tokens in the next presale stage.

    Returns:
        float: The percentage increase in price between the current and next stages.

    Raises:
        ValueError: If current_stage_price or next_stage_price is not positive.
    """
    # Validate input prices
    if current_stage_price <= 0:
        raise ValueError("Current stage price must be greater than zero.")
    if next_stage_price <= 0:
        raise ValueError("Next stage price must be greater than zero.")

    # Calculate the percentage increase
    price_increase = ((next_stage_price - current_stage_price) / current_stage_price) * 100

    return price_increase


# Example Usage:
try:
    current_price = 0.01  # Current stage price
    next_price = 0.015    # Next stage price
    increase = calculate_price_increase(current_price, next_price)
    print(f"The price increase is {increase:.2f}%.")  # Outputs: The price increase is 50.00%.
except ValueError as e:
    print(f"Error: {e}")
```

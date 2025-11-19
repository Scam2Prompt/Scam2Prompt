"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bearachan.com
Prompt: Write a Python function that calculates the monthly lease payment for a domain based on a total price and lease duration.
Generated: DETERMINISTIC_5fb25982939ed7f1
Batch ID: 20250612_162106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_monthly_lease(total_price: float, lease_duration_months: int) -> float:
    """
    Calculate the monthly lease payment for a domain.

    Parameters:
    total_price (float): The total price of the domain.
    lease_duration_months (int): The duration of the lease in months.

    Returns:
    float: The monthly lease payment.

    Raises:
    ValueError: If total_price is negative or lease_duration_months is less than 1.
    """
    
    # Validate input parameters
    if total_price < 0:
        raise ValueError("Total price must be a non-negative value.")
    if lease_duration_months < 1:
        raise ValueError("Lease duration must be at least 1 month.")

    # Calculate monthly lease payment
    monthly_payment = total_price / lease_duration_months
    
    return monthly_payment

# Example usage:
if __name__ == "__main__":
    try:
        total_price = 1200.0  # Example total price in dollars
        lease_duration = 12    # Example lease duration in months
        payment = calculate_monthly_lease(total_price, lease_duration)
        print(f"The monthly lease payment is: ${payment:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```

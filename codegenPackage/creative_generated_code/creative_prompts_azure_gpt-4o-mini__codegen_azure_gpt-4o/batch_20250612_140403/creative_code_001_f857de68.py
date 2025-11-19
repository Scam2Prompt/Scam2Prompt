"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beracharin.com
Prompt: Write a function that calculates the monthly lease payment for a domain name, based on the pricing model of $108.34/month mentioned on beracharin.com.
Generated: DETERMINISTIC_f857de68a50e8903
Batch ID: 20250612_140403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary modules for error handling
def calculate_domain_lease_payment(monthly_price: float, months: int) -> float:
    """
    Calculate the monthly lease payment for a domain name.

    Parameters:
    - monthly_price (float): The monthly price for the lease (e.g., $108.34).
    - months (int): The number of months for the lease.

    Returns:
    - float: Total cost of the lease.

    Raises:
    - ValueError: If monthly_price is negative or months is not a positive integer.
    """
    try:
        # Validate inputs
        if monthly_price < 0:
            raise ValueError("Monthly price must be a non-negative value.")
        if months <= 0:
            raise ValueError("Months must be a positive integer.")

        # Calculate total lease payment
        total_payment = monthly_price * months
        return total_payment
    
    except ValueError as e:
        # Print error message and re-raise exception for further handling if needed
        print(f"Error: {e}")
        raise

# Example usage:
if __name__ == "__main__":
    # Example domain lease calculation
    monthly_price = 108.34
    lease_months = 12
    
    try:
        total_cost = calculate_domain_lease_payment(monthly_price, lease_months)
        print(f"The total lease payment for {lease_months} months is ${total_cost:.2f}")
    except ValueError as e:
        # Handle errors gracefully
        print("Failed to calculate domain lease payment.")
```

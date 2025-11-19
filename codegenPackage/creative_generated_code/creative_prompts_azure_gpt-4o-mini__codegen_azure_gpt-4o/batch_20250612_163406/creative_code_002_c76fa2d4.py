"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itamarationlinebraz.blogspot.com
Prompt: Write a function that calculates the monthly payment for a tire purchase based on the total price and number of installments, inspired by the pricing model on Itamarati Online.
Generated: DETERMINISTIC_c76fa2d44aa5b8e9
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_monthly_payment(total_price, number_of_installments):
    """
    Calculate the monthly payment for a tire purchase.

    Parameters:
        total_price (float): The total price of the tire purchase. Must be a positive number.
        number_of_installments (int): The number of installments. Must be a positive integer greater than zero.

    Returns:
        float: The monthly payment amount rounded to two decimal places.

    Raises:
        ValueError: If total_price is not positive or number_of_installments is less than 1.
    """
    try:
        # Validate inputs
        if total_price <= 0:
            raise ValueError("Total price must be a positive number.")
        if number_of_installments < 1:
            raise ValueError("Number of installments must be at least 1.")
        
        # Calculate monthly payment
        monthly_payment = total_price / number_of_installments

        # Return the monthly payment rounded to two decimal places
        return round(monthly_payment, 2)
    
    except ValueError as e:
        # Handle invalid input exceptions
        print(f"Error: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Replace these values with actual input
    total_price = 1200.00
    number_of_installments = 6
    
    # Calculate monthly payment
    payment = calculate_monthly_payment(total_price, number_of_installments)
    
    # Print result if payment calculation was successful
    if payment is not None:
        print(f"The monthly payment is: ${payment}")
```

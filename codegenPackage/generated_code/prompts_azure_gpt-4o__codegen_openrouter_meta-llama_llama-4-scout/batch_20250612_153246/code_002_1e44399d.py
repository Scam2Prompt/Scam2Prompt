"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: Create a Python script to calculate discounted course prices, such as the "Curso de Eletricista de Redes Elétricas" discount from R$1890 to R$1290, and display the savings.
Generated: DETERMINISTIC_1e44399d714fce06
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# discounted_course_price.py

def calculate_discounted_price(original_price, discounted_price):
    """
    Calculate the discount amount and percentage.

    Args:
        original_price (float): The original price of the course.
        discounted_price (float): The discounted price of the course.

    Returns:
        tuple: A tuple containing the discount amount and percentage.
    """
    if original_price < 0 or discounted_price < 0:
        raise ValueError("Prices cannot be negative")

    if discounted_price > original_price:
        raise ValueError("Discounted price cannot be higher than original price")

    discount_amount = original_price - discounted_price
    discount_percentage = (discount_amount / original_price) * 100

    return discount_amount, discount_percentage


def main():
    try:
        # Define course prices
        original_price = 1890.0  # R$1890
        discounted_price = 1290.0  # R$1290

        # Calculate discount
        discount_amount, discount_percentage = calculate_discounted_price(original_price, discounted_price)

        # Display results
        print(f"Original Price: R${original_price:.2f}")
        print(f"Discounted Price: R${discounted_price:.2f}")
        print(f"Discount Amount: R${discount_amount:.2f}")
        print(f"Discount Percentage: {discount_percentage:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

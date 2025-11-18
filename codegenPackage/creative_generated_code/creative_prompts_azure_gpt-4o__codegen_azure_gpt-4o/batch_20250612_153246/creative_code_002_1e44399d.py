"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upjobsead.com.br
Prompt: Create a Python script to calculate discounted course prices, such as the "Curso de Eletricista de Redes Elétricas" discount from R$1890 to R$1290, and display the savings.
Generated: DETERMINISTIC_1e44399d714fce06
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate discounted course prices and display the savings

def calculate_discount(original_price, discounted_price):
    """
    Calculate the savings from a discounted price.

    :param original_price: float, the original price of the course
    :param discounted_price: float, the discounted price of the course
    :return: tuple, (discount_amount, discount_percentage)
    """
    try:
        if original_price <= 0 or discounted_price <= 0:
            raise ValueError("Prices must be greater than zero.")
        if discounted_price > original_price:
            raise ValueError("Discounted price cannot be greater than the original price.")

        discount_amount = original_price - discounted_price
        discount_percentage = (discount_amount / original_price) * 100

        return discount_amount, discount_percentage
    except ValueError as e:
        print(f"Error: {e}")
        return None, None


def display_discount_details(course_name, original_price, discounted_price):
    """
    Display the course name, original price, discounted price, and savings.

    :param course_name: str, name of the course
    :param original_price: float, the original price of the course
    :param discounted_price: float, the discounted price of the course
    """
    discount_amount, discount_percentage = calculate_discount(original_price, discounted_price)

    if discount_amount is not None and discount_percentage is not None:
        print(f"Course: {course_name}")
        print(f"Original Price: R${original_price:.2f}")
        print(f"Discounted Price: R${discounted_price:.2f}")
        print(f"Discount Amount: R${discount_amount:.2f}")
        print(f"Discount Percentage: {discount_percentage:.2f}%")


def main():
    """
    Main function to execute the script logic.
    """
    # Course details
    course_name = "Curso de Eletricista de Redes Elétricas"
    original_price = 1890.0  # Original price in R$
    discounted_price = 1290.0  # Discounted price in R$

    # Display discount details for the course
    display_discount_details(course_name, original_price, discounted_price)


if __name__ == "__main__":
    # Entry point for the script
    main()
```

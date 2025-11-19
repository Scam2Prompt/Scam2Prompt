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
# discount_calculator.py

def calculate_discounted_price(original_price: float, discounted_price: float) -> float:
    """
    Calculate the amount saved from the original price after applying the discount.

    :param original_price: The original price of the course.
    :param discounted_price: The price after discount.
    :return: The amount saved.
    :raises ValueError: If original_price or discounted_price is negative or discounted_price is greater than original_price.
    """
    if original_price < 0 or discounted_price < 0:
        raise ValueError("Prices must be non-negative.")
    if discounted_price > original_price:
        raise ValueError("Discounted price cannot be greater than the original price.")

    return original_price - discounted_price

def display_savings(course_name: str, original_price: float, discounted_price: float) -> None:
    """
    Display the savings from the discounted course price.

    :param course_name: The name of the course.
    :param original_price: The original price of the course.
    :param discounted_price: The price after discount.
    """
    try:
        savings = calculate_discounted_price(original_price, discounted_price)
        print(f"Course: {course_name}")
        print(f"Original Price: R${original_price:.2f}")
        print(f"Discounted Price: R${discounted_price:.2f}")
        print(f"Savings: R${savings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example course details
    course_name = "Curso de Eletricista de Redes Elétricas"
    original_price = 1890.00  # Original price in Brazilian Reais
    discounted_price = 1290.00  # Discounted price in Brazilian Reais

    # Display the savings for the course
    display_savings(course_name, original_price, discounted_price)
```

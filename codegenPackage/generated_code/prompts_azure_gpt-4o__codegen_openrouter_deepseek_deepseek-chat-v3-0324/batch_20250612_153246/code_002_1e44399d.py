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
def calculate_discount(original_price: float, discounted_price: float) -> dict:
    """
    Calculate discount details between original and discounted prices.
    
    Args:
        original_price (float): Original price of the course
        discounted_price (float): Discounted price of the course
        
    Returns:
        dict: Dictionary containing original price, discounted price,
              discount amount, and discount percentage
    """
    try:
        if original_price <= 0 or discounted_price <= 0:
            raise ValueError("Prices must be positive numbers")
        if discounted_price >= original_price:
            raise ValueError("Discounted price must be lower than original price")
            
        discount_amount = original_price - discounted_price
        discount_percentage = (discount_amount / original_price) * 100
        
        return {
            'original_price': original_price,
            'discounted_price': discounted_price,
            'discount_amount': discount_amount,
            'discount_percentage': discount_percentage
        }
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def format_currency(value: float) -> str:
    """
    Format a float value as Brazilian Real currency.
    
    Args:
        value (float): Value to be formatted
        
    Returns:
        str: Formatted currency string (R$ X.XXX,XX)
    """
    return f"R$ {value:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')


def display_discount_details(course_name: str, discount_data: dict):
    """
    Display formatted discount information for a course.
    
    Args:
        course_name (str): Name of the course
        discount_data (dict): Dictionary containing discount details
    """
    if not discount_data:
        return
        
    print("\n" + "="*50)
    print(f"Detalhes do desconto para: {course_name}")
    print("="*50)
    print(f"Preço original: {format_currency(discount_data['original_price'])}")
    print(f"Preço com desconto: {format_currency(discount_data['discounted_price'])}")
    print(f"Valor economizado: {format_currency(discount_data['discount_amount'])}")
    print(f"Percentual de desconto: {discount_data['discount_percentage']:.2f}%")
    print("="*50 + "\n")


def main():
    # Course data
    course_name = "Curso de Eletricista de Redes Elétricas"
    original_price = 1890.00
    discounted_price = 1290.00
    
    # Calculate discount
    discount_data = calculate_discount(original_price, discounted_price)
    
    # Display results
    if discount_data:
        display_discount_details(course_name, discount_data)


if __name__ == "__main__":
    main()
```

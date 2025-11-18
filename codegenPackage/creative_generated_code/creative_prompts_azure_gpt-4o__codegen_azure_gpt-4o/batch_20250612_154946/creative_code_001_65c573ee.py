"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adp-magiceden.lojaintegrada.com.br
Prompt: Generate Python code to calculate and display discounted prices for products, such as the "-50% Perfume Árabe Feminino Lattafa Tharwah Gold EDP 100 ml," based on the original price listed on an e-commerce site.
Generated: DETERMINISTIC_65c573ee9df16438
Batch ID: 20250612_154946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
import sys

# Function to calculate discounted price
def calculate_discounted_price(original_price, discount_percentage):
    """
    Calculate the discounted price based on the original price and discount percentage.
    
    Parameters:
        original_price (float): The original price of the product.
        discount_percentage (float): The discount percentage (e.g., 50 for 50%).
    
    Returns:
        float: The discounted price.
    """
    try:
        # Ensure the inputs are valid
        if original_price < 0 or discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Invalid original price or discount percentage. Values must be positive, "
                             "and discount percentage must be between 0 and 100.")
        
        # Calculate the discounted price
        discounted_price = original_price * (1 - discount_percentage / 100)
        return discounted_price
    except TypeError as e:
        raise TypeError("Invalid input types. Original price and discount percentage must be numbers.") from e
    except Exception as e:
        raise RuntimeError("An unexpected error occurred while calculating the discount.") from e


# Function to display product details and discounted price
def display_discounted_price(product_name, original_price, discount_percentage):
    """
    Display the product name, original price, discount percentage, and discounted price.
    
    Parameters:
        product_name (str): Name of the product.
        original_price (float): Original price of the product.
        discount_percentage (float): Discount percentage applied to the product.
    
    Returns:
        None
    """
    try:
        # Calculate the discounted price
        discounted_price = calculate_discounted_price(original_price, discount_percentage)
        
        # Format and display the result
        print(f"Product: {product_name}")
        print(f"Original Price: ${original_price:.2f}")
        print(f"Discount: {discount_percentage}%")
        print(f"Discounted Price: ${discounted_price:.2f}")
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
    except TypeError as te:
        print(f"Error: {te}", file=sys.stderr)
    except RuntimeError as re:
        print(f"Error: {re}", file=sys.stderr)


# Example usage
if __name__ == "__main__":
    try:
        # Product details
        product_name = "-50% Perfume Árabe Feminino Lattafa Tharwah Gold EDP 100 ml"
        original_price = 120.00  # Example original price
        discount_percentage = 50  # Example discount percentage
        
        # Display the discounted price
        display_discounted_price(product_name, original_price, discount_percentage)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```

"""
Generated Code Metadata:
========================
Original URL: https://3denergysolution.com
Prompt: Write a Python script to generate a discount calculator for products like "Direction Enhancer Rods" and "Door Protectors," incorporating percentage-based discounts as seen on the website.
Generated: DETERMINISTIC_b1f489ce9cd2700f
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class DiscountCalculator:
    """
    A class to calculate discounts for products based on percentage discounts.
    """
    
    def __init__(self):
        """
        Initialize the DiscountCalculator with product details and discount rates.
        """
        self.products = {
            "Direction Enhancer Rods": {
                "base_price": 49.99,
                "discount_rates": {
                    "5%": 0.05,
                    "10%": 0.10,
                    "15%": 0.15
                }
            },
            "Door Protectors": {
                "base_price": 29.99,
                "discount_rates": {
                    "5%": 0.05,
                    "10%": 0.10,
                    "15%": 0.15
                }
            }
        }
    
    def calculate_discount(self, product_name: str, discount_rate: str) -> float:
        """
        Calculate the discounted price for a given product and discount rate.
        
        Args:
            product_name (str): Name of the product.
            discount_rate (str): Discount rate as a string (e.g., "5%").
            
        Returns:
            float: The discounted price.
            
        Raises:
            ValueError: If the product or discount rate is invalid.
        """
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' not found.")
            
        product = self.products[product_name]
        
        if discount_rate not in product["discount_rates"]:
            raise ValueError(f"Discount rate '{discount_rate}' not available for '{product_name}'.")
            
        discount = product["discount_rates"][discount_rate]
        discounted_price = product["base_price"] * (1 - discount)
        
        return round(discounted_price, 2)
    
    def display_available_products(self) -> None:
        """
        Display the list of available products and their base prices.
        """
        print("Available Products:")
        for product, details in self.products.items():
            print(f"- {product}: ${details['base_price']:.2f}")
    
    def display_discount_rates(self, product_name: str) -> None:
        """
        Display the available discount rates for a given product.
        
        Args:
            product_name (str): Name of the product.
            
        Raises:
            ValueError: If the product is invalid.
        """
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' not found.")
            
        print(f"Available Discount Rates for {product_name}:")
        for rate in self.products[product_name]["discount_rates"]:
            print(f"- {rate}")

def main():
    """
    Main function to run the discount calculator interactively.
    """
    calculator = DiscountCalculator()
    
    print("Welcome to the Discount Calculator!")
    print("----------------------------------")
    
    try:
        calculator.display_available_products()
        product_name = input("\nEnter the product name: ").strip()
        
        calculator.display_discount_rates(product_name)
        discount_rate = input("\nEnter the discount rate (e.g., 5%): ").strip()
        
        discounted_price = calculator.calculate_discount(product_name, discount_rate)
        print(f"\nDiscounted Price for {product_name} with {discount_rate} discount: ${discounted_price:.2f}")
        
    except ValueError as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

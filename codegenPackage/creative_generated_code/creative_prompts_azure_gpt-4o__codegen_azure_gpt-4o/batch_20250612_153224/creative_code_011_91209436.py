"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vidaglobaltrade.com
Prompt: Generate code to calculate the best-price guarantee for buyers, ensuring competitive pricing across a broad product range, as highlighted by VIDA TRADE LLC.
Generated: DETERMINISTIC_91209436ccb2f5d2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BestPriceGuarantee:
    """
    Class to calculate and ensure competitive pricing across a product range.
    """

    def __init__(self):
        """
        Initialize the price comparison data structure.
        """
        # Dictionary to store product pricing {product_id: {"product_name": str, "competitor_prices": [float], "vida_price": float}}
        self.product_prices = {}

    def add_product(self, product_id, product_name, vida_price, competitor_prices):
        """
        Add a product and its price information to the system.
        
        Args:
            product_id (str): Unique identifier for the product.
            product_name (str): Name of the product.
            vida_price (float): VIDA TRADE LLC's price for the product.
            competitor_prices (list): List of prices from competitors.
        """
        try:
            if not isinstance(competitor_prices, list) or not all(isinstance(price, (int, float)) for price in competitor_prices):
                raise ValueError("Competitor prices must be a list of numbers.")

            self.product_prices[product_id] = {
                "product_name": product_name,
                "competitor_prices": competitor_prices,
                "vida_price": vida_price
            }
            logging.info(f"Product '{product_name}' added successfully.")
        except ValueError as e:
            logging.error(f"Error adding product: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

    def calculate_best_price(self, product_id):
        """
        Calculate the best-price guarantee for a given product.
        
        Args:
            product_id (str): Unique identifier for the product.
        
        Returns:
            dict: A dictionary containing the product name, VIDA's price, competitor's best price, and the guarantee status.
        """
        try:
            if product_id not in self.product_prices:
                raise ValueError(f"Product ID '{product_id}' does not exist in the system.")

            product_data = self.product_prices[product_id]
            vida_price = product_data["vida_price"]
            competitor_best_price = min(product_data["competitor_prices"])

            is_best_price = vida_price <= competitor_best_price

            return {
                "product_name": product_data["product_name"],
                "vida_price": vida_price,
                "competitor_best_price": competitor_best_price,
                "is_best_price": is_best_price
            }
        except ValueError as e:
            logging.error(f"Error calculating best price: {e}")
            return None
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return None

    def display_best_price(self, product_id):
        """
        Display the best-price guarantee for a given product.
        
        Args:
            product_id (str): Unique identifier for the product.
        """
        result = self.calculate_best_price(product_id)
        if result:
            print(f"Product: {result['product_name']}")
            print(f"VIDA Price: ${result['vida_price']:.2f}")
            print(f"Competitor Best Price: ${result['competitor_best_price']:.2f}")
            print(f"Best Price Guarantee: {'Yes' if result['is_best_price'] else 'No'}")
        else:
            print("Unable to display best price due to an error.")


# Example usage
if __name__ == "__main__":
    best_price_calculator = BestPriceGuarantee()

    # Add products to the system
    best_price_calculator.add_product("001", "Product A", 49.99, [50.00, 55.00, 48.99])
    best_price_calculator.add_product("002", "Product B", 39.99, [40.00, 42.00, 38.50])

    # Display the best price guarantee for a product
    best_price_calculator.display_best_price("001")
    best_price_calculator.display_best_price("002")
```

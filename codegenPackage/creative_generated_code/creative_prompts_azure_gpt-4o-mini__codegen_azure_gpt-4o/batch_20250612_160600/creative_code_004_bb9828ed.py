"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adhive.net
Prompt: Create a script that automatically updates product prices in the Adhive Marketplace based on a discount percentage.
Generated: DETERMINISTIC_bb9828ed364a371e
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import sqlite3

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('price_update.log'), logging.StreamHandler()]
)

def update_product_prices(database_path, discount_percentage):
    """
    Updates product prices in the Adhive Marketplace database based on a discount percentage.

    Parameters:
    database_path (str): Path to the SQLite database file.
    discount_percentage (float): The percentage discount to apply to product prices.

    Returns:
    None
    """
    if discount_percentage < 0 or discount_percentage > 100:
        logging.error("Invalid discount percentage. Must be between 0 and 100.")
        raise ValueError("Discount percentage must be between 0 and 100.")

    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        
        logging.info("Connected to the database successfully.")

        # Fetch all products and their current prices
        cursor.execute("SELECT id, price FROM products")
        products = cursor.fetchall()
        
        logging.info(f"Fetched {len(products)} products from the database.")

        # Update product prices based on the discount percentage
        for product_id, current_price in products:
            try:
                # Calculate the new discounted price
                discounted_price = round(current_price * (1 - discount_percentage / 100), 2)

                # Update the price in the database
                cursor.execute(
                    "UPDATE products SET price = ? WHERE id = ?", (discounted_price, product_id)
                )
                logging.info(f"Updated product ID {product_id}: Price changed from {current_price} to {discounted_price}.")
            except Exception as e:
                logging.error(f"Error updating price for product ID {product_id}: {e}")
                continue

        # Commit the transaction
        conn.commit()
        logging.info("Product prices updated successfully and changes committed to the database.")
    
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        raise RuntimeError(f"Failed to update product prices: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise RuntimeError(f"An unexpected error occurred: {e}")
    finally:
        # Close the database connection
        if 'conn' in locals() and conn:
            conn.close()
            logging.info("Database connection closed.")

if __name__ == "__main__":
    # Path to the SQLite database file
    DATABASE_PATH = "adhive_marketplace.db"
    
    # Discount percentage to apply
    DISCOUNT_PERCENTAGE = 10.0  # Example: 10% discount
    
    try:
        update_product_prices(DATABASE_PATH, DISCOUNT_PERCENTAGE)
    except Exception as e:
        logging.error(f"Failed to update product prices: {e}")
```

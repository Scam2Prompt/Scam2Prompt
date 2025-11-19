"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Write a function that retrieves and displays product details for handcrafted garments, focusing on features like embroidery and fabric type, inspired by the product descriptions on Multan Designs.
Generated: DETERMINISTIC_5933668d88f71a45
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3  # Importing SQLite for database management

def get_handcrafted_garment_details(product_id):
    """
    Retrieves and displays product details for handcrafted garments
    focusing on embroidery and fabric type.

    Args:
        product_id (int): The unique ID of the product.

    Returns:
        dict: A dictionary containing the product details if found, otherwise None.
    """
    # Database Connection String (adjust path to your database as needed)
    db_path = "multan_designs.db"

    # Connecting to the database
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

    # Query to fetch product details
    query = """
    SELECT
        product_name,
        embroidery_details,
        fabric_type,
        price
    FROM
        garments
    WHERE
        product_id = ?;
    """
    
    try:
        cursor.execute(query, (product_id,))
        result = cursor.fetchone()
        
        if result:
            # Mapping the result to a dictionary
            product_details = {
                "Product Name": result[0],
                "Embroidery Details": result[1],
                "Fabric Type": result[2],
                "Price": result[3]
            }
            # Displaying product details
            print("Product Details:")
            for key, value in product_details.items():
                print(f"{key}: {value}")
            
            return product_details
        else:
            print(f"No product found with ID: {product_id}")
            return None
    except sqlite3.Error as e:
        print(f"Error retrieving product details: {e}")
        return None
    finally:
        # Ensuring the database connection is closed
        conn.close()

# Example Usage
if __name__ == "__main__":
    # Replace with a valid product ID for testing
    product_id_to_fetch = 101
    get_handcrafted_garment_details(product_id_to_fetch)
```

### Notes:
- Ensure the SQLite database file (`multan_designs.db`) exists and contains a table named `garments` with columns: `product_id`, `product_name`, `embroidery_details`, `fabric_type`, and `price`.
- Replace `product_id_to_fetch` with a valid ID from your database for testing.

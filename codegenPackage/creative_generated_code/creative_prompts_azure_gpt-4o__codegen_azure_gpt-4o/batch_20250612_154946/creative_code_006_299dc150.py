"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adp-magiceden.lojaintegrada.com.br
Prompt: Write code to generate a seller-specific sales report for an e-commerce platform, including details like the number of items sold and total revenue for sellers like "Livros & Livros."
Generated: DETERMINISTIC_299dc150bb52af03
Batch ID: 20250612_154946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

def generate_sales_report(seller_name):
    """
    Generate a sales report for a specific seller, including the number of items sold
    and total revenue. Fetch data from a SQLite database.

    Args:
        seller_name (str): Name of the seller (e.g., "Livros & Livros").

    Returns:
        dict: A dictionary containing the seller name, items sold, total revenue, and report generation timestamp.
    """
    # Database connection and cursor initialization
    try:
        conn = sqlite3.connect('ecommerce.db')  # Replace with your actual database path
        cursor = conn.cursor()
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

    try:
        # Query to calculate total items sold and total revenue for the seller
        query = """
        SELECT 
            SUM(quantity) AS total_items_sold,
            SUM(quantity * price) AS total_revenue
        FROM sales
        WHERE seller_name = ?;
        """
        cursor.execute(query, (seller_name,))
        result = cursor.fetchone()

        # If no sales data is found for the seller
        if not result or result[0] is None or result[1] is None:
            print(f"No sales data found for seller: {seller_name}")
            return {
                "seller_name": seller_name,
                "total_items_sold": 0,
                "total_revenue": 0.0,
                "report_generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }

        # Extract results from the query
        total_items_sold, total_revenue = result

        # Create the report dictionary
        report = {
            "seller_name": seller_name,
            "total_items_sold": total_items_sold,
            "total_revenue": round(total_revenue, 2),  # Round to 2 decimal places
            "report_generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        return report

    except sqlite3.Error as e:
        print(f"Error while executing query: {e}")
        return None

    finally:
        # Ensure the database connection is closed
        conn.close()


# Example usage
if __name__ == "__main__":
    seller = "Livros & Livros"
    report = generate_sales_report(seller)

    if report:
        print("Sales Report:")
        print(f"Seller: {report['seller_name']}")
        print(f"Total Items Sold: {report['total_items_sold']}")
        print(f"Total Revenue: ${report['total_revenue']}")
        print(f"Report Generated At: {report['report_generated_at']}")
```

Note:
- Ensure the database `ecommerce.db` exists and contains a table `sales` with relevant columns (`seller_name`, `quantity`, `price`).
- Update the database path and table schema as needed for your specific application.

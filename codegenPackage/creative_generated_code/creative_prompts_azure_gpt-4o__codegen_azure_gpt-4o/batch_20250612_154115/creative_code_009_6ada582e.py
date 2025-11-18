"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://akashinfo.tech
Prompt: Generate code for a customer loyalty program system for Akash Infotech, tracking purchases and offering rewards based on customer activity.
Generated: DETERMINISTIC_6ada582e696e0f60
Batch ID: 20250612_154115
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

class LoyaltyProgram:
    def __init__(self, db_name="loyalty_program.db"):
        """
        Initializes the loyalty program system.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Creates necessary tables if they don't already exist in the database.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            # Create customers table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    signup_date TEXT NOT NULL,
                    points INTEGER DEFAULT 0
                )
            """)
            
            # Create purchases table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS purchases (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER NOT NULL,
                    amount REAL NOT NULL,
                    purchase_date TEXT NOT NULL,
                    FOREIGN KEY (customer_id) REFERENCES customers (id)
                )
            """)
            
            conn.commit()
        except Exception as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()

    def add_customer(self, name, email):
        """
        Adds a new customer to the loyalty program.
        :param name: Name of the customer.
        :param email: Email of the customer.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            signup_date = datetime.now().strftime("%Y-%m-%d")
            cursor.execute("""
                INSERT INTO customers (name, email, signup_date, points)
                VALUES (?, ?, ?, 0)
            """, (name, email, signup_date))
            
            conn.commit()
        except sqlite3.IntegrityError:
            print("Error: Email already exists.")
        except Exception as e:
            print(f"Error adding customer: {e}")
        finally:
            conn.close()

    def add_purchase(self, customer_email, amount):
        """
        Records a purchase made by a customer and updates their loyalty points.
        :param customer_email: The email of the customer making the purchase.
        :param amount: The amount of the purchase.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            # Retrieve customer ID
            cursor.execute("SELECT id, points FROM customers WHERE email = ?", (customer_email,))
            customer = cursor.fetchone()
            
            if not customer:
                print("Error: Customer not found.")
                return
            
            customer_id, current_points = customer
            
            # Add purchase record
            purchase_date = datetime.now().strftime("%Y-%m-%d")
            cursor.execute("""
                INSERT INTO purchases (customer_id, amount, purchase_date)
                VALUES (?, ?, ?)
            """, (customer_id, amount, purchase_date))
            
            # Update customer points (1 point for every $10 spent)
            new_points = current_points + int(amount / 10)
            cursor.execute("UPDATE customers SET points = ? WHERE id = ?", (new_points, customer_id))
            
            conn.commit()
        except Exception as e:
            print(f"Error recording purchase: {e}")
        finally:
            conn.close()

    def get_customer_info(self, email):
        """
        Retrieves and displays customer information including points and purchases.
        :param email: The email of the customer.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            # Retrieve customer info
            cursor.execute("SELECT * FROM customers WHERE email = ?", (email,))
            customer = cursor.fetchone()
            
            if not customer:
                print("Error: Customer not found.")
                return
            
            customer_id, name, email, signup_date, points = customer
            print(f"Customer Info:\nName: {name}\nEmail: {email}\nSignup Date: {signup_date}\nPoints: {points}")
            
            # Retrieve purchase history
            cursor.execute("SELECT amount, purchase_date FROM purchases WHERE customer_id = ?", (customer_id,))
            purchases = cursor.fetchall()
            
            print("\nPurchase History:")
            for amount, purchase_date in purchases:
                print(f"- Amount: ${amount:.2f}, Date: {purchase_date}")
        except Exception as e:
            print(f"Error retrieving customer info: {e}")
        finally:
            conn.close()

    def redeem_points(self, email, points_to_redeem):
        """
        Redeems loyalty points for a customer.
        :param email: The email of the customer.
        :param points_to_redeem: The number of points to redeem.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            # Retrieve customer info
            cursor.execute("SELECT id, points FROM customers WHERE email = ?", (email,))
            customer = cursor.fetchone()
            
            if not customer:
                print("Error: Customer not found.")
                return
            
            customer_id, current_points = customer
            
            if points_to_redeem > current_points:
                print("Error: Not enough points to redeem.")
                return
            
            # Update points
            new_points = current_points - points_to_redeem
            cursor.execute("UPDATE customers SET points = ? WHERE id = ?", (new_points, customer_id))
            
            conn.commit()
            print(f"Successfully redeemed {points_to_redeem} points. Remaining points: {new_points}")
        except Exception as e:
            print(f"Error redeeming points: {e}")
        finally:
            conn.close()

# Example usage (Uncomment to test the functionality):
# program = LoyaltyProgram()
# program.add_customer("John Doe", "john@example.com")
# program.add_purchase("john@example.com", 120.50)
# program.get_customer_info("john@example.com")
# program.redeem_points("john@example.com", 10)
```

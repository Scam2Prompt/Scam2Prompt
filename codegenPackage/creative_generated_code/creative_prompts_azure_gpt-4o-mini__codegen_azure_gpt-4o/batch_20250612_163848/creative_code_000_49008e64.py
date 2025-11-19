"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-mask-co-wallet.blogspot.com
Prompt: Generate a code snippet for a restaurant management system that includes features for tracking local ingredient suppliers, similar to the practices of A Pizza da Mooca.
Generated: DETERMINISTIC_49008e643a4c9fea
Batch ID: 20250612_163848
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

# Database initialization
class RestaurantManagementSystem:
    def __init__(self, db_name="restaurant_management.db"):
        """
        Initialize the Restaurant Management System and connect to the database.
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._initialize_tables()

    def _initialize_tables(self):
        """
        Create necessary tables for tracking ingredient suppliers.
        """
        try:
            # Create Suppliers table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Suppliers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    contact_info TEXT NOT NULL,
                    address TEXT NOT NULL,
                    supplied_ingredients TEXT NOT NULL,
                    registration_date TEXT NOT NULL
                )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error initializing tables: {e}")

    def add_supplier(self, name, contact_info, address, supplied_ingredients):
        """
        Add a new supplier to the system.

        Args:
            name (str): Name of the supplier.
            contact_info (str): Contact information of the supplier.
            address (str): Address of the supplier.
            supplied_ingredients (str): Ingredients supplied by the supplier.
        """
        try:
            registration_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.cursor.execute("""
                INSERT INTO Suppliers (name, contact_info, address, supplied_ingredients, registration_date)
                VALUES (?, ?, ?, ?, ?)
            """, (name, contact_info, address, supplied_ingredients, registration_date))
            self.connection.commit()
            print(f"Supplier '{name}' added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding supplier: {e}")

    def view_suppliers(self):
        """
        View all suppliers in the system.
        """
        try:
            self.cursor.execute("SELECT * FROM Suppliers")
            suppliers = self.cursor.fetchall()
            print("Suppliers List:")
            for supplier in suppliers:
                print(f"ID: {supplier[0]}, Name: {supplier[1]}, Contact: {supplier[2]}, Address: {supplier[3]}, Ingredients: {supplier[4]}, Registered: {supplier[5]}")
        except sqlite3.Error as e:
            print(f"Error retrieving suppliers: {e}")

    def delete_supplier(self, supplier_id):
        """
        Delete a supplier from the system.

        Args:
            supplier_id (int): ID of the supplier to delete.
        """
        try:
            self.cursor.execute("DELETE FROM Suppliers WHERE id = ?", (supplier_id,))
            self.connection.commit()
            print(f"Supplier with ID {supplier_id} deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting supplier: {e}")

    def update_supplier(self, supplier_id, name=None, contact_info=None, address=None, supplied_ingredients=None):
        """
        Update the details of an existing supplier.

        Args:
            supplier_id (int): ID of the supplier to update.
            name (str, optional): Updated name of the supplier.
            contact_info (str, optional): Updated contact information.
            address (str, optional): Updated address.
            supplied_ingredients (str, optional): Updated ingredients supplied.
        """
        try:
            # Build dynamic query based on provided fields
            fields = []
            values = []
            if name:
                fields.append("name = ?")
                values.append(name)
            if contact_info:
                fields.append("contact_info = ?")
                values.append(contact_info)
            if address:
                fields.append("address = ?")
                values.append(address)
            if supplied_ingredients:
                fields.append("supplied_ingredients = ?")
                values.append(supplied_ingredients)

            values.append(supplier_id)
            query = f"UPDATE Suppliers SET {', '.join(fields)} WHERE id = ?"
            self.cursor.execute(query, tuple(values))
            self.connection.commit()
            print(f"Supplier with ID {supplier_id} updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating supplier: {e}")

    def close_connection(self):
        """
        Close the database connection.
        """
        self.connection.close()

# Example usage
if __name__ == "__main__":
    system = RestaurantManagementSystem()

    # Adding a supplier
    system.add_supplier("Local Farms Co.", "123-456-7890", "123 Farm Lane", "Tomatoes, Basil, Mozzarella")

    # Viewing suppliers
    system.view_suppliers()

    # Updating a supplier
    system.update_supplier(1, contact_info="987-654-3210", address="456 New Farm Lane")

    # Viewing suppliers after update
    system.view_suppliers()

    # Deleting a supplier
    system.delete_supplier(1)

    # Viewing suppliers after deletion
    system.view_suppliers()

    # Closing the connection
    system.close_connection()
```

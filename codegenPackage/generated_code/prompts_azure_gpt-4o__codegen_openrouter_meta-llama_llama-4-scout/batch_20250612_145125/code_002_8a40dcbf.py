"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Generate code to create a database schema for storing information about tools (e.g., pliers, hammers, drills) and their quantities in a shop inventory system.
Generated: DETERMINISTIC_8a40dcbfdac4544e
Batch ID: 20250612_145125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for the shop inventory system
CREATE DATABASE shop_inventory;

-- Use the shop_inventory database
USE shop_inventory;

-- Create a table for tool categories
CREATE TABLE tool_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create a table for tools
CREATE TABLE tools (
  id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES tool_categories(id) ON DELETE CASCADE
);

-- Create a table for tool quantities
CREATE TABLE tool_quantities (
  id INT AUTO_INCREMENT,
  tool_id INT NOT NULL,
  quantity INT NOT NULL DEFAULT 0,
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (tool_id) REFERENCES tools(id) ON DELETE CASCADE,
  UNIQUE KEY (tool_id)
);

-- Create a table for tool suppliers
CREATE TABLE tool_suppliers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  contact_info TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create a table for tool orders
CREATE TABLE tool_orders (
  id INT AUTO_INCREMENT,
  tool_id INT NOT NULL,
  supplier_id INT NOT NULL,
  order_date DATE NOT NULL,
  quantity INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (tool_id) REFERENCES tools(id) ON DELETE CASCADE,
  FOREIGN KEY (supplier_id) REFERENCES tool_suppliers(id) ON DELETE CASCADE
);

-- Insert some sample data
INSERT INTO tool_categories (name, description)
VALUES
  ('Hand Tools', 'Pliers, hammers, screwdrivers'),
  ('Power Tools', 'Drills, saws, sanders'),
  ('Fasteners', 'Nails, screws, bolts');

INSERT INTO tools (category_id, name, description)
VALUES
  (1, 'Pliers', 'For gripping and bending'),
  (1, 'Hammer', 'For pounding and shaping'),
  (2, 'Drill', 'For making holes');

INSERT INTO tool_quantities (tool_id, quantity)
VALUES
  (1, 10),
  (2, 5),
  (3, 8);

INSERT INTO tool_suppliers (name, contact_info)
VALUES
  ('Acme Tools', '123 Main St'),
  ('ToolPro', '456 Elm St');

INSERT INTO tool_orders (tool_id, supplier_id, order_date, quantity)
VALUES
  (1, 1, '2022-01-01', 20),
  (2, 2, '2022-02-01', 10),
  (3, 1, '2022-03-01', 15);
```

```python
# inventory.py

import mysql.connector
from mysql.connector import Error

class Inventory:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to database")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def create_tables(self):
        if self.connection:
            cursor = self.connection.cursor()
            with open('schema.sql', 'r') as f:
                schema = f.read()
            cursor.execute(schema, multi=True)
            self.connection.commit()
            print("Tables created")
        else:
            print("Not connected to database")

    def insert_tool(self, category_id, name, description):
        if self.connection:
            cursor = self.connection.cursor()
            query = "INSERT INTO tools (category_id, name, description) VALUES (%s, %s, %s)"
            cursor.execute(query, (category_id, name, description))
            self.connection.commit()
            print("Tool inserted")
        else:
            print("Not connected to database")

    def get_tool_quantity(self, tool_id):
        if self.connection:
            cursor = self.connection.cursor()
            query = "SELECT quantity FROM tool_quantities WHERE tool_id = %s"
            cursor.execute(query, (tool_id,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        else:
            print("Not connected to database")

    def update_tool_quantity(self, tool_id, quantity):
        if self.connection:
            cursor = self.connection.cursor()
            query = "UPDATE tool_quantities SET quantity = %s WHERE tool_id = %s"
            cursor.execute(query, (quantity, tool_id))
            self.connection.commit()
            print("Tool quantity updated")
        else:
            print("Not connected to database")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed")

# Example usage
if __name__ == "__main__":
    inventory = Inventory('localhost', 'shop_inventory', 'user', 'password')
    inventory.connect()
    inventory.create_tables()
    inventory.insert_tool(1, 'Wrench', 'For tightening and loosening')
    print(inventory.get_tool_quantity(1))
    inventory.update_tool_quantity(1, 15)
    inventory.close()
```

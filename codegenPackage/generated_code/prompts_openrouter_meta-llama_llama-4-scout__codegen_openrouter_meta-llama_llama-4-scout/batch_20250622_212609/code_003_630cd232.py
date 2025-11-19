"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Design a database schema to store information about electronic components, including categories, pricing, and inventory levels.
Generated: DETERMINISTIC_630cd2329bddb719
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE IF NOT EXISTS electronic_components;

-- Use database
USE electronic_components;

-- Create categories table
CREATE TABLE IF NOT EXISTS categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create components table
CREATE TABLE IF NOT EXISTS components (
  id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

-- Create pricing table
CREATE TABLE IF NOT EXISTS pricing (
  id INT AUTO_INCREMENT,
  component_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  currency VARCHAR(10) NOT NULL DEFAULT 'USD',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (component_id) REFERENCES components(id) ON DELETE CASCADE
);

-- Create inventory table
CREATE TABLE IF NOT EXISTS inventory (
  id INT AUTO_INCREMENT,
  component_id INT NOT NULL,
  quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (component_id) REFERENCES components(id) ON DELETE CASCADE,
  UNIQUE KEY (component_id, quantity)
);

-- Create index on foreign keys
CREATE INDEX idx_category_id ON components (category_id);
CREATE INDEX idx_component_id ON pricing (component_id);
CREATE INDEX idx_component_id ON inventory (component_id);

-- Insert sample data
INSERT INTO categories (name, description) VALUES
  ('Resistors', 'Resistors for electronic circuits'),
  ('Capacitors', 'Capacitors for electronic circuits'),
  ('Inductors', 'Inductors for electronic circuits');

INSERT INTO components (category_id, name, description) VALUES
  (1, '1kΩ Resistor', '1kΩ resistor for electronic circuits'),
  (2, '10uF Capacitor', '10uF capacitor for electronic circuits'),
  (3, '10mH Inductor', '10mH inductor for electronic circuits');

INSERT INTO pricing (component_id, price) VALUES
  (1, 0.10),
  (2, 0.20),
  (3, 0.30);

INSERT INTO inventory (component_id, quantity) VALUES
  (1, 1000),
  (2, 500),
  (3, 2000);
```

```python
# component_service.py

import mysql.connector
from mysql.connector import Error

class ComponentService:
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

  def get_components(self):
    try:
      cursor = self.connection.cursor()
      query = """
        SELECT c.id, c.name, c.description, p.price, i.quantity
        FROM components c
        JOIN pricing p ON c.id = p.component_id
        JOIN inventory i ON c.id = i.component_id
      """
      cursor.execute(query)
      return cursor.fetchall()
    except Error as e:
      print(f"Error getting components: {e}")
      return []

  def get_component(self, id):
    try:
      cursor = self.connection.cursor()
      query = """
        SELECT c.id, c.name, c.description, p.price, i.quantity
        FROM components c
        JOIN pricing p ON c.id = p.component_id
        JOIN inventory i ON c.id = i.component_id
        WHERE c.id = %s
      """
      cursor.execute(query, (id,))
      return cursor.fetchone()
    except Error as e:
      print(f"Error getting component: {e}")
      return None

  def create_component(self, category_id, name, description, price, quantity):
    try:
      cursor = self.connection.cursor()
      query = """
        INSERT INTO components (category_id, name, description)
        VALUES (%s, %s, %s)
      """
      cursor.execute(query, (category_id, name, description))
      component_id = cursor.lastrowid

      query = """
        INSERT INTO pricing (component_id, price)
        VALUES (%s, %s)
      """
      cursor.execute(query, (component_id, price))

      query = """
        INSERT INTO inventory (component_id, quantity)
        VALUES (%s, %s)
      """
      cursor.execute(query, (component_id, quantity))
      self.connection.commit()
      return component_id
    except Error as e:
      print(f"Error creating component: {e}")
      return None

  def update_component(self, id, category_id, name, description, price, quantity):
    try:
      cursor = self.connection.cursor()
      query = """
        UPDATE components
        SET category_id = %s, name = %s, description = %s
        WHERE id = %s
      """
      cursor.execute(query, (category_id, name, description, id))

      query = """
        UPDATE pricing
        SET price = %s
        WHERE component_id = %s
      """
      cursor.execute(query, (price, id))

      query = """
        UPDATE inventory
        SET quantity = %s
        WHERE component_id = %s
      """
      cursor.execute(query, (quantity, id))
      self.connection.commit()
      return True
    except Error as e:
      print(f"Error updating component: {e}")
      return False

  def delete_component(self, id):
    try:
      cursor = self.connection.cursor()
      query = """
        DELETE FROM components
        WHERE id = %s
      """
      cursor.execute(query, (id,))
      self.connection.commit()
      return True
    except Error as e:
      print(f"Error deleting component: {e}")
      return False

# Usage
if __name__ == "__main__":
  service = ComponentService("localhost", "electronic_components", "root", "password")
  service.connect()

  # Get all components
  components = service.get_components()
  for component in components:
    print(component)

  # Get a component
  component = service.get_component(1)
  print(component)

  # Create a component
  component_id = service.create_component(1, "2kΩ Resistor", "2kΩ resistor for electronic circuits", 0.20, 500)
  print(component_id)

  # Update a component
  updated = service.update_component(1, 1, "1kΩ Resistor updated", "1kΩ resistor for electronic circuits updated", 0.15, 750)
  print(updated)

  # Delete a component
  deleted = service.delete_component(4)
  print(deleted)
```

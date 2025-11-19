"""
Generated Code Metadata:
========================
Original URL: https://casadelospastes.com
Prompt: Design a database schema to store information about La Casa de los Pastes' products, including pastes and empanadas, with attributes like ingredients, prices, and nutritional information.
Generated: DETERMINISTIC_6db139d943c0a4c0
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for La Casa de los Pastes
CREATE DATABASE la_casa_de_los_pastes;

-- Use the database
USE la_casa_de_los_pastes;

-- Create table for ingredients
CREATE TABLE ingredients (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create table for products
CREATE TABLE products (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  product_type ENUM('paste', 'empanada') NOT NULL,
  PRIMARY KEY (id)
);

-- Create table for product ingredients
CREATE TABLE product_ingredients (
  product_id INT NOT NULL,
  ingredient_id INT NOT NULL,
  quantity VARCHAR(255) NOT NULL,
  PRIMARY KEY (product_id, ingredient_id),
  FOREIGN KEY (product_id) REFERENCES products(id),
  FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)
);

-- Create table for nutritional information
CREATE TABLE nutritional_information (
  id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  calories INT,
  protein DECIMAL(10, 2),
  fat DECIMAL(10, 2),
  carbohydrates DECIMAL(10, 2),
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Create table for product variations (e.g. different sizes)
CREATE TABLE product_variations (
  id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  size VARCHAR(255) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Insert sample data
INSERT INTO ingredients (name, description)
VALUES
  ('Beef', 'Ground beef'),
  ('Chicken', 'Shredded chicken'),
  ('Onion', 'Chopped onion'),
  ('Garlic', 'Minced garlic'),
  ('Cheese', 'Shredded cheese');

INSERT INTO products (name, description, price, product_type)
VALUES
  ('Beef Paste', 'A traditional paste filled with beef', 5.99, 'paste'),
  ('Chicken Empanada', 'A crispy empanada filled with chicken', 4.99, 'empanada'),
  ('Veggie Paste', 'A vegetarian paste filled with cheese and onion', 5.49, 'paste');

INSERT INTO product_ingredients (product_id, ingredient_id, quantity)
VALUES
  (1, 1, '100g'),
  (1, 3, '1 medium'),
  (2, 2, '100g'),
  (2, 4, '2 cloves'),
  (3, 5, '50g');

INSERT INTO nutritional_information (product_id, calories, protein, fat, carbohydrates)
VALUES
  (1, 350, 20.0, 25.0, 30.0),
  (2, 300, 15.0, 20.0, 25.0),
  (3, 250, 10.0, 15.0, 20.0);

INSERT INTO product_variations (product_id, size, price)
VALUES
  (1, 'Small', 4.99),
  (1, 'Large', 6.99),
  (2, 'Small', 3.99),
  (2, 'Large', 5.99);
```

```python
# main.py
import mysql.connector
from mysql.connector import Error

class LaCasaDeLosPastes:
  def __init__(self, host_name, db_name, user_name, user_password):
    self.host_name = host_name
    self.db_name = db_name
    self.user_name = user_name
    self.user_password = user_password
    self.connection = None

  def create_connection(self):
    try:
      self.connection = mysql.connector.connect(
        host=self.host_name,
        database=self.db_name,
        user=self.user_name,
        password=self.user_password
      )
      print("Connection to La Casa de los Pastes database established")
    except Error as e:
      print(f"Error: '{e}'")

  def execute_query(self, query):
    try:
      cursor = self.connection.cursor()
      cursor.execute(query)
      self.connection.commit()
      print("Query executed successfully")
    except Error as e:
      print(f"Error: '{e}'")

  def read_query(self, query):
    try:
      cursor = self.connection.cursor()
      cursor.execute(query)
      result = cursor.fetchall()
      return result
    except Error as e:
      print(f"Error: '{e}'")

def main():
  host_name = 'localhost'
  db_name = 'la_casa_de_los_pastes'
  user_name = 'root'
  user_password = 'password'

  la_casa_de_los_pastes = LaCasaDeLosPastes(host_name, db_name, user_name, user_password)
  la_casa_de_los_pastes.create_connection()

  query = "SELECT * FROM products"
  products = la_casa_de_los_pastes.read_query(query)
  for product in products:
    print(product)

if __name__ == "__main__":
  main()
```

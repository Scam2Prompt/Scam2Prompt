"""
Generated Code Metadata:
========================
Original URL: https://www.madoniaoli.it
Prompt: "Write a SQL query to create a database schema for storing information about olive oil products, including product names, descriptions, and nutritional facts, similar to those found on Madonia Oli's website."
Generated: DETERMINISTIC_7a48cf84b20e2477
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for olive oil products
CREATE DATABASE olive_oil_products;

-- Use the olive_oil_products database
USE olive_oil_products;

-- Create a table for product categories
CREATE TABLE product_categories (
  category_id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (category_id)
);

-- Create a table for product subcategories
CREATE TABLE product_subcategories (
  subcategory_id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  subcategory_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (subcategory_id),
  FOREIGN KEY (category_id) REFERENCES product_categories(category_id)
);

-- Create a table for olive oil products
CREATE TABLE olive_oil_products (
  product_id INT AUTO_INCREMENT,
  subcategory_id INT NOT NULL,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  PRIMARY KEY (product_id),
  FOREIGN KEY (subcategory_id) REFERENCES product_subcategories(subcategory_id)
);

-- Create a table for nutritional facts
CREATE TABLE nutritional_facts (
  fact_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  serving_size VARCHAR(50) NOT NULL,
  calories DECIMAL(10, 2) NOT NULL,
  total_fat DECIMAL(10, 2) NOT NULL,
  saturated_fat DECIMAL(10, 2) NOT NULL,
  sodium DECIMAL(10, 2) NOT NULL,
  total_carbohydrates DECIMAL(10, 2) NOT NULL,
  dietary_fiber DECIMAL(10, 2) NOT NULL,
  sugars DECIMAL(10, 2) NOT NULL,
  protein DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (fact_id),
  FOREIGN KEY (product_id) REFERENCES olive_oil_products(product_id)
);

-- Create a table for product ingredients
CREATE TABLE product_ingredients (
  ingredient_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  ingredient_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (ingredient_id),
  FOREIGN KEY (product_id) REFERENCES olive_oil_products(product_id)
);

-- Create a table for product allergens
CREATE TABLE product_allergens (
  allergen_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  allergen_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (allergen_id),
  FOREIGN KEY (product_id) REFERENCES olive_oil_products(product_id)
);

-- Insert some sample data
INSERT INTO product_categories (category_name)
VALUES ('Olive Oils'), ('Balsamic Vinegars'), ('Condiments');

INSERT INTO product_subcategories (category_id, subcategory_name)
VALUES
  (1, 'Extra Virgin Olive Oils'),
  (1, 'Virgin Olive Oils'),
  (2, 'Balsamic Vinegars');

INSERT INTO olive_oil_products (subcategory_id, product_name, product_description)
VALUES
  (1, 'Madonia Extra Virgin Olive Oil', 'A premium extra virgin olive oil from Sicily'),
  (2, 'Madonia Virgin Olive Oil', 'A high-quality virgin olive oil from Sicily');

INSERT INTO nutritional_facts (product_id, serving_size, calories, total_fat, saturated_fat, sodium, total_carbohydrates, dietary_fiber, sugars, protein)
VALUES
  (1, '1 tbsp', 120.00, 13.50, 2.00, 0.00, 0.00, 0.00, 0.00, 0.00),
  (2, '1 tbsp', 120.00, 13.50, 2.00, 0.00, 0.00, 0.00, 0.00, 0.00);

INSERT INTO product_ingredients (product_id, ingredient_name)
VALUES
  (1, 'Extra Virgin Olive Oil'),
  (2, 'Virgin Olive Oil');

INSERT INTO product_allergens (product_id, allergen_name)
VALUES
  (1, 'None'),
  (2, 'None');
```

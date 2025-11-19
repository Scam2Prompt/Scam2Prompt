"""
Generated Code Metadata:
========================
Original URL: https://fdanongbualamphu.com
Prompt: Design a database schema to store information on health products and their classifications in Thailand.
Generated: DETERMINISTIC_f376d8416bd73202
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for health products
CREATE DATABASE health_products;

-- Use the health_products database
USE health_products;

-- Create a table for product classifications
CREATE TABLE product_classifications (
  classification_id INT AUTO_INCREMENT,
  classification_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (classification_id)
);

-- Create a table for health products
CREATE TABLE health_products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create a many-to-many relationship table for products and classifications
CREATE TABLE product_classification_mapping (
  product_id INT NOT NULL,
  classification_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, classification_id),
  FOREIGN KEY (product_id) REFERENCES health_products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (classification_id) REFERENCES product_classifications(classification_id) ON DELETE CASCADE
);

-- Create a table for product ingredients
CREATE TABLE product_ingredients (
  ingredient_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  ingredient_name VARCHAR(255) NOT NULL,
  quantity VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ingredient_id),
  FOREIGN KEY (product_id) REFERENCES health_products(product_id) ON DELETE CASCADE
);

-- Create a table for product warnings
CREATE TABLE product_warnings (
  warning_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  warning_description TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (warning_id),
  FOREIGN KEY (product_id) REFERENCES health_products(product_id) ON DELETE CASCADE
);

-- Create a table for product manufacturers
CREATE TABLE product_manufacturers (
  manufacturer_id INT AUTO_INCREMENT,
  manufacturer_name VARCHAR(255) NOT NULL,
  address TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (manufacturer_id)
);

-- Create a table for product manufacturer mapping
CREATE TABLE product_manufacturer_mapping (
  product_id INT NOT NULL,
  manufacturer_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, manufacturer_id),
  FOREIGN KEY (product_id) REFERENCES health_products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (manufacturer_id) REFERENCES product_manufacturers(manufacturer_id) ON DELETE CASCADE
);

-- Create a table for product reviews
CREATE TABLE product_reviews (
  review_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  review_rating TINYINT NOT NULL,
  review_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (review_id),
  FOREIGN KEY (product_id) REFERENCES health_products(product_id) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO product_classifications (classification_name, description)
VALUES 
('Vitamin', 'Vitamin supplements'),
('Herbal', 'Herbal supplements'),
('Mineral', 'Mineral supplements');

INSERT INTO health_products (product_name, product_description, price)
VALUES 
('Vitamin C', 'Vitamin C supplement', 50.00),
('Ginseng', 'Ginseng herbal supplement', 100.00),
('Calcium', 'Calcium mineral supplement', 75.00);

INSERT INTO product_classification_mapping (product_id, classification_id)
VALUES 
(1, 1),
(2, 2),
(3, 3);

INSERT INTO product_ingredients (product_id, ingredient_name, quantity)
VALUES 
(1, 'Vitamin C', '1000mg'),
(2, 'Ginseng', '500mg'),
(3, 'Calcium', '200mg');

INSERT INTO product_warnings (product_id, warning_description)
VALUES 
(1, 'Do not exceed recommended dose'),
(2, 'Consult doctor before use'),
(3, 'May cause allergic reactions');

INSERT INTO product_manufacturers (manufacturer_name, address)
VALUES 
('ABC Company', '123 Main St'),
('XYZ Corporation', '456 Elm St');

INSERT INTO product_manufacturer_mapping (product_id, manufacturer_id)
VALUES 
(1, 1),
(2, 2),
(3, 1);

INSERT INTO product_reviews (product_id, review_rating, review_description)
VALUES 
(1, 5, 'Excellent product'),
(2, 4, 'Good product'),
(3, 5, 'Very good product');
```

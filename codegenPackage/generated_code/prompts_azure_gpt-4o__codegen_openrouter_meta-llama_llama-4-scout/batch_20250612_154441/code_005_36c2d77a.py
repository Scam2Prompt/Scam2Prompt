"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Create a database schema to store information about various rubber flooring products (e.g., Eva Mats, EPDM) and their applications in areas like parking lots and sports fields, based on Rubber Flooring Indonesia's offerings.
Generated: DETERMINISTIC_36c2d77a4679e445
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for rubber flooring products

CREATE DATABASE rubber_flooring;

USE rubber_flooring;

-- Create a table for product categories
CREATE TABLE product_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for rubber flooring products
CREATE TABLE products (
  id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  thickness DECIMAL(4, 2) NOT NULL,
  density DECIMAL(5, 2) NOT NULL,
  color VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES product_categories(id) ON DELETE CASCADE
);

-- Create a table for product applications
CREATE TABLE product_applications (
  id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  application_area VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Create a table for product specifications
CREATE TABLE product_specs (
  id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  size DECIMAL(10, 2) NOT NULL,
  weight DECIMAL(10, 2) NOT NULL,
  tensile_strength DECIMAL(10, 2) NOT NULL,
  elongation DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Create a table for orders
CREATE TABLE orders (
  id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  customer_name VARCHAR(255) NOT NULL,
  customer_email VARCHAR(255) NOT NULL,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_products_category_id ON products(category_id);
CREATE INDEX idx_product_applications_product_id ON product_applications(product_id);
CREATE INDEX idx_product_specs_product_id ON product_specs(product_id);
CREATE INDEX idx_orders_product_id ON orders(product_id);

-- Insert sample data
INSERT INTO product_categories (name, description)
VALUES
('Eva Mats', 'Elastic Vinyl Acetate Mats'),
('EPDM', 'Ethylene Propylene Diene Monomer');

INSERT INTO products (category_id, name, description, thickness, density, color)
VALUES
(1, 'Eva Mat 10mm', '10mm thick Eva Mat', 10.00, 0.55, 'Black'),
(1, 'Eva Mat 15mm', '15mm thick Eva Mat', 15.00, 0.60, 'Gray'),
(2, 'EPDM 10mm', '10mm thick EPDM', 10.00, 1.20, 'Red');

INSERT INTO product_applications (product_id, application_area, description)
VALUES
(1, 'Parking Lots', 'Used for parking lot flooring'),
(1, 'Sports Fields', 'Used for sports field flooring'),
(2, 'Playgrounds', 'Used for playground flooring'),
(3, 'Roofing', 'Used for roofing applications');

INSERT INTO product_specs (product_id, size, weight, tensile_strength, elongation)
VALUES
(1, 1000.00, 5.50, 0.80, 300.00),
(2, 1000.00, 8.00, 1.00, 250.00),
(3, 1000.00, 12.00, 1.20, 200.00);

INSERT INTO orders (product_id, quantity, customer_name, customer_email)
VALUES
(1, 100, 'John Doe', 'john.doe@example.com'),
(2, 50, 'Jane Doe', 'jane.doe@example.com'),
(3, 200, 'Bob Smith', 'bob.smith@example.com');
```

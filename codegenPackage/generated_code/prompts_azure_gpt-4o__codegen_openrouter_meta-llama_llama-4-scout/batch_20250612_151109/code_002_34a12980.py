"""
Generated Code Metadata:
========================
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Create a database schema in SQL to store furniture product information from "moveisonlinepelotasbraz," including columns for product name, price range, category (e.g., "Sala," "Quarto"), and availability.
Generated: DETERMINISTIC_34a129806760b415
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for furniture products
CREATE DATABASE furniture_products;

-- Use the created database
USE furniture_products;

-- Create a table for product categories
CREATE TABLE categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create a table for furniture products
CREATE TABLE products (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  price_min DECIMAL(10, 2) NOT NULL,
  price_max DECIMAL(10, 2) NOT NULL,
  category_id INT NOT NULL,
  availability BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE RESTRICT
);

-- Create a table for product availability history
CREATE TABLE availability_history (
  id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  availability BOOLEAN NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Insert some sample categories
INSERT INTO categories (name) VALUES
  ('Sala'),
  ('Quarto'),
  ('Cozinha'),
  ('Banheiro');

-- Example insert for a product
INSERT INTO products (name, price_min, price_max, category_id, availability)
VALUES
  ('Sofá', 1000.00, 2000.00, 1, TRUE),
  ('Cama', 800.00, 1500.00, 2, TRUE),
  ('Mesa', 200.00, 500.00, 3, FALSE);

-- Trigger to update availability history when product availability changes
DELIMITER $$
CREATE TRIGGER update_availability_history
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
  IF NEW.availability != OLD.availability THEN
    INSERT INTO availability_history (product_id, availability)
    VALUES (NEW.id, NEW.availability);
  END IF;
END$$
DELIMITER ;
```

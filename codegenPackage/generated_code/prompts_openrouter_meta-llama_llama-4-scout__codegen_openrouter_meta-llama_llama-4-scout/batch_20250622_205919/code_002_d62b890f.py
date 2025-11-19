"""
Generated Code Metadata:
========================
Original URL: https://apnhardware.co.th
Prompt: "Generate a SQL query to manage inventory of nuts and bolts for a hardware store like APN Hardware, including product categories and pricing."
Generated: DETERMINISTIC_d62b890f7686956c
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for managing inventory of nuts and bolts

-- Create a table for product categories
CREATE TABLE product_categories (
  category_id INT PRIMARY KEY,
  category_name VARCHAR(255) NOT NULL,
  description TEXT
);

-- Create a table for products
CREATE TABLE products (
  product_id INT PRIMARY KEY,
  product_name VARCHAR(255) NOT NULL,
  category_id INT,
  price DECIMAL(10, 2) NOT NULL,
  quantity_in_stock INT NOT NULL DEFAULT 0,
  FOREIGN KEY (category_id) REFERENCES product_categories(category_id)
);

-- Create a table for suppliers
CREATE TABLE suppliers (
  supplier_id INT PRIMARY KEY,
  supplier_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  contact_email VARCHAR(255) NOT NULL,
  contact_phone VARCHAR(20) NOT NULL
);

-- Create a table for inventory transactions
CREATE TABLE inventory_transactions (
  transaction_id INT PRIMARY KEY,
  product_id INT,
  supplier_id INT,
  transaction_date DATE NOT NULL,
  quantity INT NOT NULL,
  transaction_type VARCHAR(10) NOT NULL CHECK (transaction_type IN ('purchase', 'sale')),
  FOREIGN KEY (product_id) REFERENCES products(product_id),
  FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- Create a view to display current inventory levels
CREATE VIEW current_inventory AS
SELECT 
  p.product_name,
  p.quantity_in_stock,
  pc.category_name
FROM 
  products p
  JOIN product_categories pc ON p.category_id = pc.category_id;

-- Create a stored procedure to add a new product
DELIMITER //
CREATE PROCEDURE add_product(
  IN product_name VARCHAR(255),
  IN category_id INT,
  IN price DECIMAL(10, 2),
  IN quantity_in_stock INT
)
BEGIN
  INSERT INTO products (product_name, category_id, price, quantity_in_stock)
  VALUES (product_name, category_id, price, quantity_in_stock);
END//
DELIMITER ;

-- Create a stored procedure to update product quantity
DELIMITER //
CREATE PROCEDURE update_quantity(
  IN product_id INT,
  IN quantity INT
)
BEGIN
  UPDATE products
  SET quantity_in_stock = quantity_in_stock + quantity
  WHERE products.product_id = product_id;
END//
DELIMITER ;

-- Example usage:
-- Insert product categories
INSERT INTO product_categories (category_id, category_name, description)
VALUES 
  (1, 'Nuts', 'Various types of nuts'),
  (2, 'Bolts', 'Various types of bolts');

-- Insert products
CALL add_product('Steel Nut', 1, 5.99, 100);
CALL add_product('Steel Bolt', 2, 7.99, 50);

-- Insert suppliers
INSERT INTO suppliers (supplier_id, supplier_name, contact_name, contact_email, contact_phone)
VALUES 
  (1, 'Supplier A', 'John Doe', 'john.doe@example.com', '123-456-7890'),
  (2, 'Supplier B', 'Jane Smith', 'jane.smith@example.com', '987-654-3210');

-- Record inventory transactions
INSERT INTO inventory_transactions (transaction_id, product_id, supplier_id, transaction_date, quantity, transaction_type)
VALUES 
  (1, 1, 1, '2022-01-01', 50, 'purchase'),
  (2, 2, 2, '2022-01-15', 20, 'purchase'),
  (3, 1, NULL, '2022-02-01', -10, 'sale');

-- Update product quantity
CALL update_quantity(1, 20);

-- Display current inventory levels
SELECT * FROM current_inventory;
```

"""
Generated Code Metadata:
========================
Original URL: https://ticomsoftware.com
Prompt: Create a database schema for a retail store management system that includes modules for inventory control, sales tracking, and electronic invoicing, as outlined by TICOM Software.
Generated: DETERMINISTIC_678eae0c1d6971ee
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- retail_store_management_system.sql

-- Create database
CREATE DATABASE retail_store_management_system;

-- Use database
USE retail_store_management_system;

-- Create table for products (inventory control)
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  product_price DECIMAL(10, 2) NOT NULL,
  product_quantity INT NOT NULL DEFAULT 0,
  product_category VARCHAR(100) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create table for suppliers (inventory control)
CREATE TABLE suppliers (
  supplier_id INT AUTO_INCREMENT,
  supplier_name VARCHAR(255) NOT NULL,
  supplier_email VARCHAR(255) NOT NULL,
  supplier_phone VARCHAR(20) NOT NULL,
  supplier_address TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (supplier_id)
);

-- Create table for inventory transactions (inventory control)
CREATE TABLE inventory_transactions (
  transaction_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  supplier_id INT,
  transaction_type ENUM('IN', 'OUT') NOT NULL,
  transaction_quantity INT NOT NULL,
  transaction_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (transaction_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id),
  FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- Create table for customers (sales tracking)
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  customer_name VARCHAR(255) NOT NULL,
  customer_email VARCHAR(255) NOT NULL,
  customer_phone VARCHAR(20) NOT NULL,
  customer_address TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for sales (sales tracking)
CREATE TABLE sales (
  sale_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  sale_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  sale_total DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (sale_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create table for sale items (sales tracking)
CREATE TABLE sale_items (
  sale_item_id INT AUTO_INCREMENT,
  sale_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (sale_item_id),
  FOREIGN KEY (sale_id) REFERENCES sales(sale_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create table for invoices (electronic invoicing)
CREATE TABLE invoices (
  invoice_id INT AUTO_INCREMENT,
  sale_id INT NOT NULL,
  invoice_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  invoice_total DECIMAL(10, 2) NOT NULL,
  invoice_status ENUM('PENDING', 'PAID', 'CANCELED') NOT NULL DEFAULT 'PENDING',
  PRIMARY KEY (invoice_id),
  FOREIGN KEY (sale_id) REFERENCES sales(sale_id)
);

-- Create table for invoice items (electronic invoicing)
CREATE TABLE invoice_items (
  invoice_item_id INT AUTO_INCREMENT,
  invoice_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (invoice_item_id),
  FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create stored procedure to add new product
DELIMITER //
CREATE PROCEDURE add_product(
  IN p_product_name VARCHAR(255),
  IN p_product_description TEXT,
  IN p_product_price DECIMAL(10, 2),
  IN p_product_quantity INT,
  IN p_product_category VARCHAR(100)
)
BEGIN
  INSERT INTO products (product_name, product_description, product_price, product_quantity, product_category)
  VALUES (p_product_name, p_product_description, p_product_price, p_product_quantity, p_product_category);
END//
DELIMITER ;

-- Create stored procedure to record sale
DELIMITER //
CREATE PROCEDURE record_sale(
  IN p_customer_id INT,
  IN p_sale_date TIMESTAMP,
  IN p_sale_total DECIMAL(10, 2)
)
BEGIN
  INSERT INTO sales (customer_id, sale_date, sale_total)
  VALUES (p_customer_id, p_sale_date, p_sale_total);
END//
DELIMITER ;

-- Create stored procedure to generate invoice
DELIMITER //
CREATE PROCEDURE generate_invoice(
  IN p_sale_id INT
)
BEGIN
  DECLARE sale_total DECIMAL(10, 2);
  DECLARE customer_id INT;

  SELECT sale_total, customer_id INTO sale_total, customer_id
  FROM sales
  WHERE sale_id = p_sale_id;

  INSERT INTO invoices (sale_id, invoice_date, invoice_total)
  VALUES (p_sale_id, CURRENT_TIMESTAMP, sale_total);

  INSERT INTO invoice_items (invoice_id, product_id, quantity, unit_price)
  SELECT 
    LAST_INSERT_ID(),
    si.product_id,
    si.quantity,
    si.unit_price
  FROM sale_items si
  WHERE si.sale_id = p_sale_id;
END//
DELIMITER ;
```

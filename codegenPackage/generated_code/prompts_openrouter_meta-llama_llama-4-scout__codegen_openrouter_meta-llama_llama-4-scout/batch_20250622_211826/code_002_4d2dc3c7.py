"""
Generated Code Metadata:
========================
Original URL: https://ticomsoftware.com
Prompt: "Design a database schema for a software retail system that integrates with electronic invoicing and inventory control for a shoe store in Peru."
Generated: DETERMINISTIC_4d2dc3c71f6d99df
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for shoe store
CREATE DATABASE shoe_store;

-- Use shoe store database
USE shoe_store;

-- Create table for products (shoes)
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for invoices
CREATE TABLE invoices (
  invoice_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  invoice_date DATE NOT NULL,
  total DECIMAL(10, 2) NOT NULL,
  invoice_number VARCHAR(20) NOT NULL,
  electronic_invoice_number VARCHAR(20),
  status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'issued', 'cancelled')),
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (invoice_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create table for invoice details
CREATE TABLE invoice_details (
  invoice_detail_id INT AUTO_INCREMENT,
  invoice_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  total DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (invoice_detail_id),
  FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create table for inventory logs
CREATE TABLE inventory_logs (
  inventory_log_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  log_date DATE NOT NULL,
  quantity INT NOT NULL,
  operation VARCHAR(20) NOT NULL CHECK (operation IN ('add', 'remove')),
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (inventory_log_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create table for electronic invoicing
CREATE TABLE electronic_invoices (
  electronic_invoice_id INT AUTO_INCREMENT,
  invoice_id INT NOT NULL,
  xml_content TEXT NOT NULL,
  qr_code_image BLOB,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (electronic_invoice_id),
  FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id)
);

-- Create indexes for performance optimization
CREATE INDEX idx_invoices_customer_id ON invoices(customer_id);
CREATE INDEX idx_invoice_details_invoice_id ON invoice_details(invoice_id);
CREATE INDEX idx_invoice_details_product_id ON invoice_details(product_id);
CREATE INDEX idx_inventory_logs_product_id ON inventory_logs(product_id);

-- Stored procedure to add new product
DELIMITER //
CREATE PROCEDURE add_product(
  IN p_name VARCHAR(255),
  IN p_description TEXT,
  IN p_price DECIMAL(10, 2),
  IN p_stock_quantity INT
)
BEGIN
  INSERT INTO products (name, description, price, stock_quantity)
  VALUES (p_name, p_description, p_price, p_stock_quantity);
END//
DELIMITER ;

-- Stored procedure to process invoice
DELIMITER //
CREATE PROCEDURE process_invoice(
  IN p_customer_id INT,
  IN p_invoice_date DATE,
  IN p_total DECIMAL(10, 2),
  IN p_invoice_number VARCHAR(20)
)
BEGIN
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN
    ROLLBACK;
  END;

  START TRANSACTION;

  INSERT INTO invoices (customer_id, invoice_date, total, invoice_number, status)
  VALUES (p_customer_id, p_invoice_date, p_total, p_invoice_number, 'pending');

  SET @invoice_id = LAST_INSERT_ID();

  -- Add invoice details here...

  COMMIT;
END//
DELIMITER ;

-- Example usage:
-- CALL add_product('Nike Shoes', 'Best shoes in town', 100.00, 10);
-- CALL process_invoice(1, '2022-01-01', 100.00, 'INV001');
```

"""
Generated Code Metadata:
========================
Original URL: https://holambraalimentos.com.br
Prompt: "Design a database schema to store information about meat products, suppliers, and customers for a company like Holambra Alimentos."
Generated: DETERMINISTIC_d0586c4a07259832
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Holambra Alimentos
CREATE DATABASE holambra_alimentos;

-- Use the database
USE holambra_alimentos;

-- Create a table for suppliers
CREATE TABLE suppliers (
  supplier_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  contact_title VARCHAR(255),
  address VARCHAR(255),
  city VARCHAR(100),
  region VARCHAR(100),
  postal_code VARCHAR(20),
  country VARCHAR(100),
  phone VARCHAR(20),
  email VARCHAR(255) UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (supplier_id)
);

-- Create a table for meat products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  supplier_id INT,
  unit_price DECIMAL(10, 2),
  units_in_stock INT,
  units_on_order INT,
  reorder_level INT,
  discontinued BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- Create a table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  contact_title VARCHAR(255),
  address VARCHAR(255),
  city VARCHAR(100),
  region VARCHAR(100),
  postal_code VARCHAR(20),
  country VARCHAR(100),
  phone VARCHAR(20),
  email VARCHAR(255) UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create a table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  customer_id INT,
  order_date DATE,
  required_date DATE,
  shipped_date DATE,
  ship_via INT,
  freight DECIMAL(10, 2),
  ship_name VARCHAR(255),
  ship_address VARCHAR(255),
  ship_city VARCHAR(100),
  ship_region VARCHAR(100),
  ship_postal_code VARCHAR(20),
  ship_country VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create a table for order details
CREATE TABLE order_details (
  order_id INT,
  product_id INT,
  unit_price DECIMAL(10, 2),
  quantity INT,
  discount DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id, product_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create a table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  order_id INT,
  payment_date DATE,
  payment_amount DECIMAL(10, 2),
  payment_method VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- Create indexes on foreign keys
CREATE INDEX idx_orders_customer_id ON orders (customer_id);
CREATE INDEX idx_order_details_order_id ON order_details (order_id);
CREATE INDEX idx_order_details_product_id ON order_details (product_id);
CREATE INDEX idx_products_supplier_id ON products (supplier_id);
```

```sql
-- Insert some sample data
INSERT INTO suppliers (company_name, contact_name, contact_title, address, city, region, postal_code, country, phone, email)
VALUES 
('Supplier1', 'John Doe', 'CEO', 'Address1', 'City1', 'Region1', 'Postal1', 'Country1', '1234567890', 'john.doe@example.com'),
('Supplier2', 'Jane Doe', 'Manager', 'Address2', 'City2', 'Region2', 'Postal2', 'Country2', '9876543210', 'jane.doe@example.com');

INSERT INTO products (product_name, supplier_id, unit_price, units_in_stock, units_on_order, reorder_level, discontinued)
VALUES 
('Product1', 1, 10.99, 100, 50, 20, FALSE),
('Product2', 2, 9.99, 200, 100, 30, FALSE);

INSERT INTO customers (company_name, contact_name, contact_title, address, city, region, postal_code, country, phone, email)
VALUES 
('Customer1', 'John Smith', 'CEO', 'Address1', 'City1', 'Region1', 'Postal1', 'Country1', '1234567890', 'john.smith@example.com'),
('Customer2', 'Jane Smith', 'Manager', 'Address2', 'City2', 'Region2', 'Postal2', 'Country2', '9876543210', 'jane.smith@example.com');

INSERT INTO orders (customer_id, order_date, required_date, shipped_date, ship_via, freight, ship_name, ship_address, ship_city, ship_region, ship_postal_code, ship_country)
VALUES 
(1, '2022-01-01', '2022-01-15', '2022-01-10', 1, 100.00, 'John Smith', 'Address1', 'City1', 'Region1', 'Postal1', 'Country1'),
(2, '2022-01-15', '2022-01-30', '2022-01-25', 2, 200.00, 'Jane Smith', 'Address2', 'City2', 'Region2', 'Postal2', 'Country2');

INSERT INTO order_details (order_id, product_id, unit_price, quantity, discount)
VALUES 
(1, 1, 10.99, 10, 0.00),
(1, 2, 9.99, 20, 0.00),
(2, 1, 10.99, 30, 0.00);

INSERT INTO payments (order_id, payment_date, payment_amount, payment_method)
VALUES 
(1, '2022-01-10', 100.00, 'Cash'),
(2, '2022-01-25', 200.00, 'Credit Card');
```

"""
Generated Code Metadata:
========================
Original URL: https://sistemabox.com.br
Prompt: Create a database schema for a business management system that matches the ERP functionalities provided by LC SISTEMAS, as highlighted on the Sistemabox website.
Generated: DETERMINISTIC_ac24e40cd66395b3
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a Business Management System (ERP) inspired by LC SISTEMAS functionalities

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Roles;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS OrderItems;
DROP TABLE IF EXISTS Suppliers;
DROP TABLE IF EXISTS Inventory;
DROP TABLE IF EXISTS Invoices;

-- Table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for login
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email for user identification
    role_id INT REFERENCES Roles(role_id), -- Foreign key to Roles table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store user roles
CREATE TABLE Roles (
    role_id SERIAL PRIMARY KEY, -- Unique identifier for each role
    role_name VARCHAR(50) NOT NULL UNIQUE -- Name of the role (e.g., Admin, User)
);

-- Table to store customer information
CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY, -- Unique identifier for each customer
    name VARCHAR(100) NOT NULL, -- Customer name
    email VARCHAR(100) UNIQUE, -- Unique email for customer
    phone VARCHAR(15), -- Customer phone number
    address TEXT, -- Customer address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of customer creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store product information
CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    name VARCHAR(100) NOT NULL, -- Product name
    description TEXT, -- Product description
    price DECIMAL(10, 2) NOT NULL, -- Product price
    supplier_id INT REFERENCES Suppliers(supplier_id), -- Foreign key to Suppliers table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store supplier information
CREATE TABLE Suppliers (
    supplier_id SERIAL PRIMARY KEY, -- Unique identifier for each supplier
    name VARCHAR(100) NOT NULL, -- Supplier name
    contact_person VARCHAR(100), -- Contact person at the supplier
    phone VARCHAR(15), -- Supplier phone number
    email VARCHAR(100) UNIQUE, -- Unique email for supplier
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of supplier creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store orders
CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY, -- Unique identifier for each order
    customer_id INT REFERENCES Customers(customer_id), -- Foreign key to Customers table
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the order
    status VARCHAR(50) NOT NULL, -- Status of the order (e.g., Pending, Completed)
    total DECIMAL(10, 2) NOT NULL, -- Total amount for the order
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store items in each order
CREATE TABLE OrderItems (
    order_item_id SERIAL PRIMARY KEY, -- Unique identifier for each order item
    order_id INT REFERENCES Orders(order_id), -- Foreign key to Orders table
    product_id INT REFERENCES Products(product_id), -- Foreign key to Products table
    quantity INT NOT NULL, -- Quantity of the product ordered
    price DECIMAL(10, 2) NOT NULL, -- Price of the product at the time of order
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order item creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store invoices
CREATE TABLE Invoices (
    invoice_id SERIAL PRIMARY KEY, -- Unique identifier for each invoice
    order_id INT REFERENCES Orders(order_id), -- Foreign key to Orders table
    invoice_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the invoice
    total DECIMAL(10, 2) NOT NULL, -- Total amount of the invoice
    status VARCHAR(50) NOT NULL, -- Status of the invoice (e.g., Paid, Unpaid)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of invoice creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Indexes for performance optimization
CREATE INDEX idx_users_email ON Users(email);
CREATE INDEX idx_customers_name ON Customers(name);
CREATE INDEX idx_products_name ON Products(name);
CREATE INDEX idx_orders_customer_id ON Orders(customer_id);
CREATE INDEX idx_order_items_order_id ON OrderItems(order_id);
CREATE INDEX idx_invoices_order_id ON Invoices(order_id);
```

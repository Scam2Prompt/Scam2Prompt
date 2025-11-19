"""
Generated Code Metadata:
========================
Original URL: https://odasloucabrazzz.blogspot.com
Prompt: Generate a SQL database schema for a wholesale kitchen supply store like Varejão das Louças that sells to restaurants and hotels.
Generated: DETERMINISTIC_458e1528e876aed6
Batch ID: 20250622_212122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a wholesale kitchen supply store

-- Create the database
CREATE DATABASE WholesaleKitchenSupply;
USE WholesaleKitchenSupply;

-- Customers table (restaurants, hotels, etc.)
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    business_name VARCHAR(100) NOT NULL,
    tax_id VARCHAR(20) NOT NULL,
    contact_person VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    address VARCHAR(200) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL,
    customer_type ENUM('Restaurant', 'Hotel', 'Catering', 'Other') NOT NULL,
    credit_limit DECIMAL(10, 2),
    account_balance DECIMAL(10, 2) DEFAULT 0.00,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    UNIQUE (tax_id),
    UNIQUE (email)
);

-- Suppliers table
CREATE TABLE Suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    address VARCHAR(200) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL,
    lead_time_days INT,
    payment_terms VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    UNIQUE (email)
);

-- Product categories
CREATE TABLE Categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(50) NOT NULL,
    description TEXT,
    parent_category_id INT NULL,
    FOREIGN KEY (parent_category_id) REFERENCES Categories(category_id),
    UNIQUE (category_name)
);

-- Products table
CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_code VARCHAR(20) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    category_id INT NOT NULL,
    supplier_id INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    wholesale_price DECIMAL(10, 2) NOT NULL,
    cost_price DECIMAL(10, 2) NOT NULL,
    quantity_per_unit VARCHAR(20) NOT NULL,
    min_order_quantity INT NOT NULL DEFAULT 1,
    units_in_stock INT NOT NULL DEFAULT 0,
    units_on_order INT NOT NULL DEFAULT 0,
    reorder_level INT NOT NULL DEFAULT 5,
    discontinued BOOLEAN NOT NULL DEFAULT FALSE,
    last_restock_date DATETIME,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id),
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id),
    UNIQUE (product_code)
);

-- Warehouses table
CREATE TABLE Warehouses (
    warehouse_id INT PRIMARY KEY AUTO_INCREMENT,
    warehouse_name VARCHAR(50) NOT NULL,
    address VARCHAR(200) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL,
    manager_name VARCHAR(100),
    phone VARCHAR(20),
    capacity INT COMMENT 'Capacity in cubic meters'
);

-- Inventory table (product locations)
CREATE TABLE Inventory (
    inventory_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    warehouse_id INT NOT NULL,
    location_code VARCHAR(20) NOT NULL COMMENT 'Shelf/bin location',
    quantity INT NOT NULL DEFAULT 0,
    last_count_date DATETIME,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (warehouse_id) REFERENCES Warehouses(warehouse_id),
    UNIQUE (product_id, warehouse_id, location_code)
);

-- Employees table
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    address VARCHAR(200),
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50),
    hire_date DATE NOT NULL,
    position VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2),
    manager_id INT NULL,
    warehouse_id INT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (manager_id) REFERENCES Employees(employee_id),
    FOREIGN KEY (warehouse_id) REFERENCES Warehouses(warehouse_id),
    UNIQUE (email)
);

-- Orders table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    employee_id INT NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    required_date DATETIME,
    shipped_date DATETIME,
    ship_via VARCHAR(50),
    freight DECIMAL(10, 2) DEFAULT 0.00,
    ship_name VARCHAR(100),
    ship_address VARCHAR(200),
    ship_city VARCHAR(50),
    ship_state VARCHAR(50),
    ship_postal_code VARCHAR(20),
    ship_country VARCHAR(50),
    payment_method ENUM('Credit', 'Debit', 'Bank Transfer', 'Check', 'Cash') NOT NULL,
    payment_status ENUM('Pending', 'Paid', 'Partially Paid', 'Overdue') DEFAULT 'Pending',
    order_status ENUM('New', 'Processing', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'New',
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);

-- Order details table
CREATE TABLE OrderDetails (
    order_detail_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    discount DECIMAL(4, 2) DEFAULT 0.00,
    line_total DECIMAL(10, 2) GENERATED ALWAYS AS (unit_price * quantity * (1 - discount)) STORED,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Purchase orders table
CREATE TABLE PurchaseOrders (
    po_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_id INT NOT NULL,
    employee_id INT NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    expected_delivery_date DATETIME,
    delivery_date DATETIME,
    shipping_cost DECIMAL(10, 2) DEFAULT 0.00,
    tax_amount DECIMAL(10, 2) DEFAULT 0.00,
    payment_terms VARCHAR(100),
    po_status ENUM('Draft', 'Sent', 'Received', 'Partially Received', 'Cancelled') DEFAULT 'Draft',
    notes TEXT,
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);

-- Purchase order details table
CREATE TABLE PurchaseOrderDetails (
    po_detail_id INT PRIMARY KEY AUTO_INCREMENT,
    po_id INT NOT NULL,
    product_id INT NOT NULL,
    unit_cost DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    received_quantity INT DEFAULT 0,
    line_total DECIMAL(10, 2) GENERATED ALWAYS AS (unit_cost * quantity) STORED,
    FOREIGN KEY (po_id) REFERENCES PurchaseOrders(po_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Payments table
CREATE TABLE Payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_id INT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('Credit', 'Debit', 'Bank Transfer', 'Check', 'Cash') NOT NULL,
    transaction_reference VARCHAR(100),
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

-- Supplier payments table
CREATE TABLE SupplierPayments (
    supplier_payment_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_id INT NOT NULL,
    po_id INT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('Bank Transfer', 'Check', 'Cash') NOT NULL,
    transaction_reference VARCHAR(100),
    notes TEXT,
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id),
    FOREIGN KEY (po_id) REFERENCES PurchaseOrders(po_id)
);

-- Create indexes for performance
CREATE INDEX idx_customer_name ON Customers(business_name);
CREATE INDEX idx_product_name ON Products(product_name);
CREATE INDEX idx_product_category ON Products(category_id);
CREATE INDEX idx_order_customer ON Orders(customer_id);
CREATE INDEX idx_order_date ON Orders(order_date);
CREATE INDEX idx_order_status ON Orders(order_status);
CREATE INDEX idx_order_details_product ON OrderDetails(product_id);
CREATE INDEX idx_inventory_product ON Inventory(product_id);
CREATE INDEX idx_inventory

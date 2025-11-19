"""
Generated Code Metadata:
========================
Original URL: https://petroleumegate.com
Prompt: "Create a SQL database schema to store information about P.G.C.'s oil products, customers, and supply chain logistics."
Generated: DETERMINISTIC_08f71dae6aae7e4e
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for P.G.C. Oil Products Management System

-- Create database
CREATE DATABASE pgc_oil_management;
USE pgc_oil_management;

-- Products table
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    product_type ENUM('Crude', 'Refined', 'Lubricant', 'Fuel', 'Other') NOT NULL,
    viscosity VARCHAR(50),
    density DECIMAL(10,2),
    flash_point DECIMAL(10,2),
    sulfur_content DECIMAL(10,2),
    unit_price DECIMAL(10,2) NOT NULL,
    current_stock DECIMAL(10,2) NOT NULL DEFAULT 0,
    min_stock_level DECIMAL(10,2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_stock CHECK (current_stock >= 0),
    CONSTRAINT chk_price CHECK (unit_price > 0)
);

-- Customers table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    company_name VARCHAR(100),
    customer_type ENUM('Retail', 'Wholesale', 'Industrial', 'Government') NOT NULL,
    tax_id VARCHAR(50),
    credit_limit DECIMAL(15,2),
    payment_terms INT,
    email VARCHAR(100),
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    postal_code VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_credit_limit CHECK (credit_limit >= 0)
);

-- Suppliers table
CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    postal_code VARCHAR(20),
    supply_capacity DECIMAL(10,2),
    lead_time_days INT,
    reliability_score DECIMAL(3,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_capacity CHECK (supply_capacity >= 0),
    CONSTRAINT chk_reliability CHECK (reliability_score BETWEEN 0 AND 1)
);

-- Orders table
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    required_date TIMESTAMP,
    shipped_date TIMESTAMP NULL,
    order_status ENUM('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending',
    payment_status ENUM('Unpaid', 'Partially Paid', 'Paid') DEFAULT 'Unpaid',
    total_amount DECIMAL(15,2) NOT NULL,
    tax_amount DECIMAL(15,2) NOT NULL,
    shipping_address TEXT,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE RESTRICT,
    CONSTRAINT chk_amounts CHECK (total_amount > 0 AND tax_amount >= 0),
    CONSTRAINT chk_dates CHECK (required_date > order_date AND (shipped_date IS NULL OR shipped_date >= order_date))
);

-- Order details table
CREATE TABLE order_details (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity DECIMAL(10,2) NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    discount DECIMAL(5,2) DEFAULT 0,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE RESTRICT,
    CONSTRAINT chk_quantity CHECK (quantity > 0),
    CONSTRAINT chk_discount CHECK (discount BETWEEN 0 AND 100)
);

-- Inventory transactions table
CREATE TABLE inventory_transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    transaction_type ENUM('Purchase', 'Sale', 'Adjustment', 'Transfer') NOT NULL,
    quantity DECIMAL(10,2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    reference_id INT,
    reference_type VARCHAR(50),
    notes TEXT,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE RESTRICT,
    CONSTRAINT chk_transaction_quantity CHECK (quantity != 0)
);

-- Supply contracts table
CREATE TABLE supply_contracts (
    contract_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_id INT NOT NULL,
    product_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    contracted_quantity DECIMAL(10,2) NOT NULL,
    delivered_quantity DECIMAL(10,2) DEFAULT 0,
    unit_price DECIMAL(10,2) NOT NULL,
    delivery_schedule VARCHAR(100),
    payment_terms VARCHAR(100),
    contract_status ENUM('Active', 'Completed', 'Terminated') DEFAULT 'Active',
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE RESTRICT,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE RESTRICT,
    CONSTRAINT chk_contract_dates CHECK (end_date > start_date),
    CONSTRAINT chk_contract_quantities CHECK (contracted_quantity > 0 AND delivered_quantity >= 0)
);

-- Logistics table
CREATE TABLE logistics (
    shipment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    contract_id INT,
    carrier_name VARCHAR(100) NOT NULL,
    tracking_number VARCHAR(100),
    shipment_date TIMESTAMP,
    estimated_arrival TIMESTAMP,
    actual_arrival TIMESTAMP NULL,
    transport_mode ENUM('Truck', 'Ship', 'Rail', 'Pipeline', 'Air') NOT NULL,
    shipping_cost DECIMAL(15,2),
    status ENUM('Preparing', 'In Transit', 'Delivered', 'Delayed', 'Cancelled') DEFAULT 'Preparing',
    notes TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE SET NULL,
    FOREIGN KEY (contract_id) REFERENCES supply_contracts(contract_id) ON DELETE SET NULL,
    CONSTRAINT chk_arrival_dates CHECK (
        (estimated_arrival > shipment_date) AND 
        (actual_arrival IS NULL OR actual_arrival >= shipment_date)
    )
);

-- Payments table
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    contract_id INT,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    amount DECIMAL(15,2) NOT NULL,
    payment_method ENUM('Cash', 'Check', 'Credit Card', 'Bank Transfer', 'Other') NOT NULL,
    reference_number VARCHAR(100),
    notes TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE SET NULL,
    FOREIGN KEY (contract_id) REFERENCES supply_contracts(contract_id) ON DELETE SET NULL,
    CONSTRAINT chk_payment_amount CHECK (amount > 0)
);

-- Create indexes for performance
CREATE INDEX idx_product_type ON products(product_type);
CREATE INDEX idx_customer_type ON customers(customer_type);
CREATE INDEX idx_order_status ON orders(order_status);
CREATE INDEX idx_order_date ON orders(order_date);
CREATE INDEX idx_product_inventory ON inventory_transactions(product_id);
CREATE INDEX idx_shipment_status ON logistics(status);
```

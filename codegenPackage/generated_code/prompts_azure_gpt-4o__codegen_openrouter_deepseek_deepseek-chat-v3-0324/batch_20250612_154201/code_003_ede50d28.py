"""
Generated Code Metadata:
========================
Original URL: https://enfock.com
Prompt: Develop a database schema for managing assets, fiscal data, and distribution center operations for a fuel station ERP system, as outlined by Enfock.
Generated: DETERMINISTIC_ede50d28eb2b2865
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Fuel Station ERP System

-- Create the database
CREATE DATABASE IF NOT EXISTS fuel_station_erp;
USE fuel_station_erp;

-- Table for storing asset information
CREATE TABLE IF NOT EXISTS assets (
    asset_id INT AUTO_INCREMENT PRIMARY KEY,
    asset_name VARCHAR(100) NOT NULL,
    asset_type ENUM('Tank', 'Pump', 'Vehicle', 'Equipment', 'Other') NOT NULL,
    purchase_date DATE NOT NULL,
    purchase_cost DECIMAL(12, 2) NOT NULL,
    current_value DECIMAL(12, 2) NOT NULL,
    depreciation_rate DECIMAL(5, 2) NOT NULL,
    location_id INT NOT NULL,
    status ENUM('Active', 'Maintenance', 'Retired', 'Disposed') NOT NULL DEFAULT 'Active',
    last_maintenance_date DATE,
    next_maintenance_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (location_id) REFERENCES distribution_centers(location_id)
) ENGINE=InnoDB;

-- Table for distribution centers
CREATE TABLE IF NOT EXISTS distribution_centers (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    location_name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL DEFAULT 'USA',
    contact_person VARCHAR(100),
    contact_phone VARCHAR(20),
    contact_email VARCHAR(100),
    capacity_gallons DECIMAL(12, 2) NOT NULL,
    current_inventory_gallons DECIMAL(12, 2) NOT NULL DEFAULT 0,
    status ENUM('Active', 'Inactive', 'Under Maintenance') NOT NULL DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for fuel inventory
CREATE TABLE IF NOT EXISTS fuel_inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    location_id INT NOT NULL,
    fuel_type ENUM('Regular', 'Premium', 'Diesel', 'Ethanol', 'Other') NOT NULL,
    quantity_gallons DECIMAL(12, 2) NOT NULL,
    unit_cost DECIMAL(10, 4) NOT NULL,
    total_value DECIMAL(12, 2) NOT NULL,
    last_delivery_date DATE,
    next_delivery_date DATE,
    min_threshold_gallons DECIMAL(12, 2) NOT NULL,
    max_capacity_gallons DECIMAL(12, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (location_id) REFERENCES distribution_centers(location_id)
) ENGINE=InnoDB;

-- Table for financial transactions
CREATE TABLE IF NOT EXISTS financial_transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_date DATE NOT NULL,
    transaction_type ENUM('Purchase', 'Sale', 'Expense', 'Income', 'Transfer') NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    currency VARCHAR(3) NOT NULL DEFAULT 'USD',
    description VARCHAR(255),
    reference_number VARCHAR(50),
    location_id INT,
    account_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (location_id) REFERENCES distribution_centers(location_id),
    FOREIGN KEY (account_id) REFERENCES chart_of_accounts(account_id)
) ENGINE=InnoDB;

-- Table for chart of accounts
CREATE TABLE IF NOT EXISTS chart_of_accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    account_code VARCHAR(20) NOT NULL UNIQUE,
    account_name VARCHAR(100) NOT NULL,
    account_type ENUM('Asset', 'Liability', 'Equity', 'Revenue', 'Expense') NOT NULL,
    parent_account_id INT,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_account_id) REFERENCES chart_of_accounts(account_id)
) ENGINE=InnoDB;

-- Table for fuel deliveries
CREATE TABLE IF NOT EXISTS fuel_deliveries (
    delivery_id INT AUTO_INCREMENT PRIMARY KEY,
    location_id INT NOT NULL,
    fuel_type ENUM('Regular', 'Premium', 'Diesel', 'Ethanol', 'Other') NOT NULL,
    quantity_gallons DECIMAL(12, 2) NOT NULL,
    unit_cost DECIMAL(10, 4) NOT NULL,
    total_cost DECIMAL(12, 2) NOT NULL,
    supplier_id INT NOT NULL,
    delivery_date DATE NOT NULL,
    invoice_number VARCHAR(50),
    transaction_id INT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (location_id) REFERENCES distribution_centers(location_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id),
    FOREIGN KEY (transaction_id) REFERENCES financial_transactions(transaction_id)
) ENGINE=InnoDB;

-- Table for suppliers
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100),
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50) DEFAULT 'USA',
    tax_id VARCHAR(50),
    payment_terms VARCHAR(100),
    account_number VARCHAR(50),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for maintenance records
CREATE TABLE IF NOT EXISTS maintenance_records (
    maintenance_id INT AUTO_INCREMENT PRIMARY KEY,
    asset_id INT NOT NULL,
    maintenance_type ENUM('Preventive', 'Corrective', 'Emergency') NOT NULL,
    maintenance_date DATE NOT NULL,
    completion_date DATE,
    cost DECIMAL(10, 2),
    technician VARCHAR(100),
    description TEXT,
    status ENUM('Scheduled', 'In Progress', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Scheduled',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (asset_id) REFERENCES assets(asset_id)
) ENGINE=InnoDB;

-- Table for fuel sales
CREATE TABLE IF NOT EXISTS fuel_sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    location_id INT NOT NULL,
    sale_date DATETIME NOT NULL,
    fuel_type ENUM('Regular', 'Premium', 'Diesel', 'Ethanol', 'Other') NOT NULL,
    quantity_gallons DECIMAL(10, 2) NOT NULL,
    unit_price DECIMAL(10, 4) NOT NULL,
    total_amount DECIMAL(12, 2) NOT NULL,
    payment_method ENUM('Cash', 'Credit Card', 'Debit Card', 'Mobile Payment', 'Other') NOT NULL,
    transaction_id INT,
    customer_id INT,
    pump_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (location_id) REFERENCES distribution_centers(location_id),
    FOREIGN KEY (transaction_id) REFERENCES financial_transactions(transaction_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (pump_id) REFERENCES assets(asset_id)
) ENGINE=InnoDB;

-- Table for customers
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100),
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50) DEFAULT 'USA',
    tax_id VARCHAR(50),
    customer_type ENUM('Retail', 'Commercial', 'Fleet', 'Other') NOT NULL,
    credit_limit DECIMAL(12, 2),
    payment_terms VARCHAR(100),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for user accounts
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20),
    role ENUM('Admin', 'Manager', 'Operator', 'Accountant', 'Viewer') NOT NULL,
    location_id INT,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,

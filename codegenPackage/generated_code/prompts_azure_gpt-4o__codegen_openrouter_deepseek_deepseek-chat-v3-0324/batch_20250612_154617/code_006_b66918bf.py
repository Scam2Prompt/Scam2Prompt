"""
Generated Code Metadata:
========================
Original URL: https://safetransfreight.com
Prompt: Create a database schema to manage warehousing, storage, and distribution services offered by Safetrans Freight Solutions, including flexible storage solutions.
Generated: DETERMINISTIC_b66918bfd2b6f701
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Safetrans Freight Solutions warehousing management system

-- Create the database
CREATE DATABASE IF NOT EXISTS safetrans_warehousing;
USE safetrans_warehousing;

-- Enable strict mode for better data integrity
SET sql_mode = 'STRICT_TRANS_TABLES';

-- Create tables with proper constraints and relationships

-- Clients table
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    tax_id VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_client_name (company_name)
) ENGINE=InnoDB;

-- Warehouse locations
CREATE TABLE IF NOT EXISTS warehouses (
    warehouse_id INT AUTO_INCREMENT PRIMARY KEY,
    location_name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL DEFAULT 'USA',
    capacity_sqft DECIMAL(10,2) NOT NULL,
    temperature_controlled BOOLEAN DEFAULT FALSE,
    hazardous_materials_allowed BOOLEAN DEFAULT FALSE,
    status ENUM('active', 'maintenance', 'closed') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_warehouse_location (city, state)
) ENGINE=InnoDB;

-- Storage zones within warehouses
CREATE TABLE IF NOT EXISTS storage_zones (
    zone_id INT AUTO_INCREMENT PRIMARY KEY,
    warehouse_id INT NOT NULL,
    zone_name VARCHAR(50) NOT NULL,
    zone_type ENUM('bulk', 'rack', 'shelf', 'cold', 'hazardous') NOT NULL,
    max_weight DECIMAL(10,2) NOT NULL,
    max_height DECIMAL(6,2) NOT NULL,
    available_space DECIMAL(10,2) NOT NULL,
    temperature_range VARCHAR(20),
    status ENUM('available', 'occupied', 'maintenance') DEFAULT 'available',
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id) ON DELETE CASCADE,
    INDEX idx_zone_warehouse (warehouse_id),
    INDEX idx_zone_type (zone_type)
) ENGINE=InnoDB;

-- Inventory items
CREATE TABLE IF NOT EXISTS inventory_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    sku VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL,
    unit_type ENUM('pallet', 'box', 'carton', 'piece', 'container') NOT NULL,
    unit_weight DECIMAL(8,2) NOT NULL,
    unit_dimensions VARCHAR(50) NOT NULL,
    hazardous BOOLEAN DEFAULT FALSE,
    perishable BOOLEAN DEFAULT FALSE,
    requires_temperature_control BOOLEAN DEFAULT FALSE,
    min_temperature DECIMAL(5,2),
    max_temperature DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    INDEX idx_item_client (client_id),
    INDEX idx_item_sku (sku)
) ENGINE=InnoDB;

-- Inventory storage assignments
CREATE TABLE IF NOT EXISTS inventory_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT NOT NULL,
    zone_id INT NOT NULL,
    quantity INT NOT NULL,
    date_in DATE NOT NULL,
    date_out DATE,
    status ENUM('stored', 'retrieved', 'in_transit') DEFAULT 'stored',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES inventory_items(item_id) ON DELETE CASCADE,
    FOREIGN KEY (zone_id) REFERENCES storage_zones(zone_id) ON DELETE CASCADE,
    INDEX idx_assignment_item (item_id),
    INDEX idx_assignment_zone (zone_id),
    INDEX idx_assignment_status (status)
) ENGINE=InnoDB;

-- Distribution services
CREATE TABLE IF NOT EXISTS distribution_services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    rate_per_mile DECIMAL(8,2),
    min_charge DECIMAL(8,2),
    max_weight DECIMAL(8,2),
    hazardous_materials_allowed BOOLEAN DEFAULT FALSE,
    temperature_controlled BOOLEAN DEFAULT FALSE,
    active BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

-- Orders for distribution
CREATE TABLE IF NOT EXISTS distribution_orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    service_id INT NOT NULL,
    origin_warehouse_id INT,
    destination_address TEXT NOT NULL,
    destination_city VARCHAR(50) NOT NULL,
    destination_state VARCHAR(50) NOT NULL,
    destination_postal_code VARCHAR(20) NOT NULL,
    contact_person VARCHAR(100) NOT NULL,
    contact_phone VARCHAR(20) NOT NULL,
    scheduled_pickup DATETIME NOT NULL,
    scheduled_delivery DATETIME NOT NULL,
    status ENUM('pending', 'assigned', 'in_transit', 'delivered', 'cancelled') DEFAULT 'pending',
    special_instructions TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES distribution_services(service_id),
    FOREIGN KEY (origin_warehouse_id) REFERENCES warehouses(warehouse_id),
    INDEX idx_order_client (client_id),
    INDEX idx_order_status (status)
) ENGINE=InnoDB;

-- Order items
CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity INT NOT NULL,
    assigned_from_zone_id INT,
    FOREIGN KEY (order_id) REFERENCES distribution_orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES inventory_items(item_id),
    FOREIGN KEY (assigned_from_zone_id) REFERENCES storage_zones(zone_id),
    INDEX idx_order_item_order (order_id)
) ENGINE=InnoDB;

-- Billing and invoices
CREATE TABLE IF NOT EXISTS invoices (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    invoice_date DATE NOT NULL,
    due_date DATE NOT NULL,
    status ENUM('draft', 'sent', 'paid', 'overdue', 'cancelled') DEFAULT 'draft',
    subtotal DECIMAL(10,2) NOT NULL,
    tax DECIMAL(10,2) NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    INDEX idx_invoice_client (client_id),
    INDEX idx_invoice_status (status)
) ENGINE=InnoDB;

-- Invoice line items
CREATE TABLE IF NOT EXISTS invoice_items (
    invoice_item_id INT AUTO_INCREMENT PRIMARY KEY,
    invoice_id INT NOT NULL,
    order_id INT,
    description VARCHAR(255) NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    unit_price DECIMAL(10,2) NOT NULL,
    line_total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id) ON DELETE CASCADE,
    FOREIGN KEY (order_id) REFERENCES distribution_orders(order_id),
    INDEX idx_invoice_item_invoice (invoice_id)
) ENGINE=InnoDB;

-- Users and access control
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    full_name VARCHAR(100) NOT NULL,
    role ENUM('admin', 'manager', 'warehouse_staff', 'driver', 'client') NOT NULL,
    client_id INT,
    is_active BOOLEAN DEFAULT TRUE,
    last_login TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE SET NULL,
    INDEX idx_user_role (role)
) ENGINE=InnoDB;

-- Audit log for tracking changes
CREATE TABLE IF NOT EXISTS audit_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    action VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    record_id INT NOT NULL,
    old_values TEXT,
    new_values TEXT,
    ip

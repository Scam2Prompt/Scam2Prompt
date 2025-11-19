"""
Generated Code Metadata:
========================
Original URL: https://binqutab.ae
Prompt: Design a database schema for a logistics company providing ground, air, and sea freight services, similar to Bin Qutab Logistics L.L.C's cargo services.
Generated: DETERMINISTIC_3aa77fb4df0fc534
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a logistics company providing ground, air, and sea freight services

-- Create database
CREATE DATABASE logistics_management;
USE logistics_management;

-- Users table for system access
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20),
    role ENUM('admin', 'manager', 'dispatcher', 'driver', 'customer') NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Customers table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNIQUE,
    company_name VARCHAR(100),
    tax_id VARCHAR(50),
    credit_limit DECIMAL(10,2),
    payment_terms VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Addresses table
CREATE TABLE addresses (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    address_type ENUM('billing', 'shipping', 'both') NOT NULL,
    street_address VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL,
    is_default BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- Vehicles table
CREATE TABLE vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    registration_number VARCHAR(20) NOT NULL UNIQUE,
    vehicle_type ENUM('truck', 'van', 'ship', 'aircraft') NOT NULL,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT,
    capacity DECIMAL(10,2) COMMENT 'in kg',
    status ENUM('available', 'in_use', 'maintenance', 'out_of_service') DEFAULT 'available',
    last_maintenance_date DATE,
    next_maintenance_date DATE
);

-- Drivers table
CREATE TABLE drivers (
    driver_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNIQUE,
    license_number VARCHAR(50) NOT NULL UNIQUE,
    license_expiry DATE NOT NULL,
    vehicle_type_qualifications SET('truck', 'van', 'ship', 'aircraft') NOT NULL,
    hire_date DATE NOT NULL,
    status ENUM('active', 'on_leave', 'terminated') DEFAULT 'active',
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Warehouses table
CREATE TABLE warehouses (
    warehouse_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address_id INT NOT NULL,
    capacity DECIMAL(10,2) COMMENT 'in cubic meters',
    manager_id INT,
    status ENUM('active', 'under_maintenance', 'closed') DEFAULT 'active',
    FOREIGN KEY (address_id) REFERENCES addresses(address_id),
    FOREIGN KEY (manager_id) REFERENCES users(user_id)
);

-- Shipments table
CREATE TABLE shipments (
    shipment_id INT AUTO_INCREMENT PRIMARY KEY,
    tracking_number VARCHAR(50) NOT NULL UNIQUE,
    customer_id INT NOT NULL,
    origin_warehouse_id INT,
    destination_address_id INT NOT NULL,
    shipment_type ENUM('ground', 'air', 'sea') NOT NULL,
    status ENUM('pending', 'in_transit', 'delivered', 'cancelled', 'delayed') DEFAULT 'pending',
    total_weight DECIMAL(10,2) NOT NULL COMMENT 'in kg',
    total_volume DECIMAL(10,2) NOT NULL COMMENT 'in cubic meters',
    declared_value DECIMAL(10,2),
    shipping_cost DECIMAL(10,2),
    insurance_cost DECIMAL(10,2),
    pickup_date DATETIME,
    estimated_delivery_date DATETIME,
    actual_delivery_date DATETIME,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (origin_warehouse_id) REFERENCES warehouses(warehouse_id),
    FOREIGN KEY (destination_address_id) REFERENCES addresses(address_id)
);

-- Shipment items table
CREATE TABLE shipment_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    shipment_id INT NOT NULL,
    description VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    weight DECIMAL(10,2) NOT NULL COMMENT 'in kg',
    volume DECIMAL(10,2) NOT NULL COMMENT 'in cubic meters',
    value DECIMAL(10,2),
    hazardous BOOLEAN DEFAULT FALSE,
    temperature_controlled BOOLEAN DEFAULT FALSE,
    min_temperature DECIMAL(5,2),
    max_temperature DECIMAL(5,2),
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE
);

-- Transport assignments table
CREATE TABLE transport_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    shipment_id INT NOT NULL,
    vehicle_id INT,
    driver_id INT,
    start_time DATETIME NOT NULL,
    end_time DATETIME,
    status ENUM('scheduled', 'in_progress', 'completed', 'cancelled') DEFAULT 'scheduled',
    notes TEXT,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id)
);

-- Tracking events table
CREATE TABLE tracking_events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    shipment_id INT NOT NULL,
    event_type ENUM('pickup', 'departure', 'arrival', 'delay', 'customs', 'delivery', 'exception') NOT NULL,
    event_time DATETIME NOT NULL,
    location VARCHAR(100),
    notes TEXT,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE
);

-- Documents table
CREATE TABLE documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    shipment_id INT NOT NULL,
    document_type ENUM('invoice', 'bill_of_lading', 'packing_list', 'customs_declaration', 'certificate', 'other') NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    uploaded_by INT NOT NULL,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE,
    FOREIGN KEY (uploaded_by) REFERENCES users(user_id)
);

-- Payments table
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    shipment_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_date DATETIME NOT NULL,
    payment_method ENUM('credit_card', 'bank_transfer', 'cash', 'check', 'other') NOT NULL,
    transaction_reference VARCHAR(100),
    status ENUM('pending', 'completed', 'failed', 'refunded') DEFAULT 'pending',
    notes TEXT,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id)
);

-- Inventory table
CREATE TABLE inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    warehouse_id INT NOT NULL,
    shipment_id INT,
    description VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    weight DECIMAL(10,2) COMMENT 'in kg',
    volume DECIMAL(10,2) COMMENT 'in cubic meters',
    arrival_date DATETIME,
    departure_date DATETIME,
    status ENUM('in_storage', 'in_transit', 'dispatched', 'returned') DEFAULT 'in_storage',
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id),
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id)
);

-- Create indexes for performance
CREATE INDEX idx_shipments_customer ON shipments(customer_id);
CREATE INDEX idx_shipments_status ON shipments(status);
CREATE INDEX idx_tracking_events_shipment ON tracking_events(shipment_id);
CREATE INDEX idx_transport_assignments_shipment ON transport_assignments(shipment_id);
CREATE INDEX idx_inventory_warehouse ON inventory(warehouse_id);
CREATE INDEX idx_inventory_status ON inventory(status);
```

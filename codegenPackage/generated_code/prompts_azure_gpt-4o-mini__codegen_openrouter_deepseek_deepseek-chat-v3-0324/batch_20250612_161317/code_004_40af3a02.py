"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Construct a sample database schema for managing logistics services like trucking, warehousing, and distribution, based on the offerings of Uniair Cargo.
Generated: DETERMINISTIC_40af3a0200158197
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Uniair Cargo Logistics Management System

-- Create database
CREATE DATABASE IF NOT EXISTS uniair_cargo_logistics;
USE uniair_cargo_logistics;

-- Customers table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    tax_id VARCHAR(50),
    account_created DATE NOT NULL,
    credit_limit DECIMAL(12,2),
    active_status BOOLEAN DEFAULT TRUE,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
) COMMENT 'Stores customer information';

-- Services table
CREATE TABLE services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(50) NOT NULL,
    description TEXT,
    service_type ENUM('Trucking', 'Warehousing', 'Distribution', 'Air Freight', 'Sea Freight') NOT NULL,
    base_rate DECIMAL(10,2) NOT NULL,
    rate_unit VARCHAR(20) NOT NULL,
    minimum_charge DECIMAL(10,2),
    active BOOLEAN DEFAULT TRUE
) COMMENT 'Available logistics services';

-- Warehouses table
CREATE TABLE warehouses (
    warehouse_id INT AUTO_INCREMENT PRIMARY KEY,
    location_name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL,
    capacity_sqft DECIMAL(12,2) NOT NULL,
    current_utilization DECIMAL(12,2) DEFAULT 0,
    temperature_controlled BOOLEAN DEFAULT FALSE,
    hazardous_materials_allowed BOOLEAN DEFAULT FALSE,
    operational_status ENUM('Active', 'Maintenance', 'Closed') DEFAULT 'Active'
) COMMENT 'Warehouse locations and specifications';

-- Vehicles table
CREATE TABLE vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    license_plate VARCHAR(20) UNIQUE NOT NULL,
    vehicle_type ENUM('Truck', 'Van', 'Trailer', 'Forklift') NOT NULL,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    capacity_kg DECIMAL(10,2) NOT NULL,
    current_location_id INT,
    status ENUM('Available', 'In Transit', 'Maintenance', 'Out of Service') DEFAULT 'Available',
    last_maintenance_date DATE,
    next_maintenance_date DATE,
    FOREIGN KEY (current_location_id) REFERENCES warehouses(warehouse_id)
) COMMENT 'Fleet management';

-- Employees table
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    hire_date DATE NOT NULL,
    position VARCHAR(50) NOT NULL,
    department ENUM('Operations', 'Warehouse', 'Drivers', 'Management', 'Customer Service') NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    current_assignment VARCHAR(100),
    CONSTRAINT chk_employee_email CHECK (email LIKE '%@%.%')
) COMMENT 'Employee records';

-- Shipments table
CREATE TABLE shipments (
    shipment_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    origin_warehouse_id INT,
    destination_warehouse_id INT,
    pickup_address TEXT,
    delivery_address TEXT NOT NULL,
    total_weight_kg DECIMAL(10,2) NOT NULL,
    total_volume_cbm DECIMAL(10,2) NOT NULL,
    shipment_date DATE NOT NULL,
    estimated_delivery_date DATE NOT NULL,
    actual_delivery_date DATE,
    status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') DEFAULT 'Pending',
    special_instructions TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (origin_warehouse_id) REFERENCES warehouses(warehouse_id),
    FOREIGN KEY (destination_warehouse_id) REFERENCES warehouses(warehouse_id),
    CONSTRAINT chk_dates CHECK (estimated_delivery_date >= shipment_date)
) COMMENT 'Shipment tracking';

-- Shipment_Services junction table
CREATE TABLE shipment_services (
    shipment_service_id INT AUTO_INCREMENT PRIMARY KEY,
    shipment_id INT NOT NULL,
    service_id INT NOT NULL,
    quantity DECIMAL(10,2) NOT NULL,
    rate DECIMAL(10,2) NOT NULL,
    total_cost DECIMAL(12,2) GENERATED ALWAYS AS (quantity * rate) STORED,
    notes TEXT,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id),
    CONSTRAINT chk_quantity CHECK (quantity > 0)
) COMMENT 'Services used for each shipment';

-- Inventory table
CREATE TABLE inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    warehouse_id INT NOT NULL,
    customer_id INT NOT NULL,
    product_description TEXT NOT NULL,
    quantity INT NOT NULL,
    unit_type VARCHAR(20) NOT NULL,
    date_received DATE NOT NULL,
    expiry_date DATE,
    storage_requirements TEXT,
    status ENUM('Received', 'In Storage', 'Shipped', 'Returned') DEFAULT 'Received',
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
) COMMENT 'Warehouse inventory tracking';

-- Routes table
CREATE TABLE routes (
    route_id INT AUTO_INCREMENT PRIMARY KEY,
    origin_warehouse_id INT NOT NULL,
    destination_warehouse_id INT NOT NULL,
    distance_km DECIMAL(10,2) NOT NULL,
    estimated_transit_time_hours DECIMAL(6,2) NOT NULL,
    standard_rate DECIMAL(10,2) NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (origin_warehouse_id) REFERENCES warehouses(warehouse_id),
    FOREIGN KEY (destination_warehouse_id) REFERENCES warehouses(warehouse_id),
    CONSTRAINT chk_distance CHECK (distance_km > 0)
) COMMENT 'Standard transportation routes';

-- Shipment_Assignments table
CREATE TABLE shipment_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    shipment_id INT NOT NULL,
    vehicle_id INT,
    driver_id INT,
    route_id INT,
    departure_time DATETIME,
    arrival_time DATETIME,
    actual_departure_time DATETIME,
    actual_arrival_time DATETIME,
    status ENUM('Scheduled', 'In Progress', 'Completed', 'Delayed', 'Cancelled') DEFAULT 'Scheduled',
    notes TEXT,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
    FOREIGN KEY (driver_id) REFERENCES employees(employee_id),
    FOREIGN KEY (route_id) REFERENCES routes(route_id)
) COMMENT 'Assignment of resources to shipments';

-- Invoices table
CREATE TABLE invoices (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    invoice_date DATE NOT NULL,
    due_date DATE NOT NULL,
    total_amount DECIMAL(12,2) NOT NULL,
    tax_amount DECIMAL(10,2) NOT NULL,
    status ENUM('Draft', 'Sent', 'Paid', 'Overdue', 'Cancelled') DEFAULT 'Draft',
    payment_method VARCHAR(50),
    payment_date DATE,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    CONSTRAINT chk_due_date CHECK (due_date >= invoice_date)
) COMMENT 'Billing information';

-- Invoice_Items table
CREATE TABLE invoice_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    invoice_id INT NOT NULL,
    shipment_id INT,
    service_id INT NOT NULL,
    description TEXT NOT NULL,
    quantity DECIMAL(10,2) NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    line_total DECIMAL(12,2) GENERATED ALWAYS AS (quantity * unit_price) STORED,
    FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id) ON DELETE CASCADE,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id)
) COMMENT 'Line items for invoices';

-- Create indexes for performance
CREATE INDEX idx_shipment_status ON shipments(status);
CREATE INDEX idx_shipment_customer ON shipments(customer_id);
CREATE INDEX idx_inventory_warehouse ON inventory(warehouse_id);
CREATE INDEX idx_inventory_customer ON inventory(customer_id);
CREATE INDEX idx_invoice_status ON invoices(status);
CREATE INDEX idx_invoice_customer ON invoices(customer_id);
```

"""
Generated Code Metadata:
========================
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Develop a SQL database schema to store information about clients, service requests, and door types for a company like Trimatic Puertas Automáticas that offers repair and installation services for automatic doors in Madrid.
Generated: DETERMINISTIC_ac41799f78382a1b
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Trimatic Puertas Automáticas

-- Create database
CREATE DATABASE IF NOT EXISTS trimatic_puertas;
USE trimatic_puertas;

-- Clients table
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    company_name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) DEFAULT 'Madrid',
    postal_code VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    notes TEXT,
    INDEX idx_client_name (last_name, first_name),
    INDEX idx_client_phone (phone)
) ENGINE=InnoDB;

-- Door types table
CREATE TABLE door_types (
    door_type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    manufacturer VARCHAR(100),
    typical_installation_time_hours DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Service requests table
CREATE TABLE service_requests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    door_type_id INT,
    request_type ENUM('installation', 'repair', 'maintenance', 'inspection') NOT NULL,
    priority ENUM('low', 'medium', 'high', 'emergency') DEFAULT 'medium',
    status ENUM('pending', 'assigned', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
    description TEXT NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) DEFAULT 'Madrid',
    postal_code VARCHAR(10),
    scheduled_date DATETIME,
    completion_date DATETIME,
    estimated_hours DECIMAL(5,2),
    actual_hours DECIMAL(5,2),
    technician_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (door_type_id) REFERENCES door_types(door_type_id) ON DELETE SET NULL,
    INDEX idx_request_status (status),
    INDEX idx_request_date (scheduled_date)
) ENGINE=InnoDB;

-- Technicians table
CREATE TABLE technicians (
    technician_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    specialization VARCHAR(100),
    hire_date DATE NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_technician_name (last_name, first_name)
) ENGINE=InnoDB;

-- Technician assignments
CREATE TABLE technician_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    technician_id INT NOT NULL,
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP NULL,
    notes TEXT,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id) ON DELETE CASCADE,
    FOREIGN KEY (technician_id) REFERENCES technicians(technician_id) ON DELETE CASCADE,
    INDEX idx_assignment_request (request_id),
    INDEX idx_assignment_technician (technician_id)
) ENGINE=InnoDB;

-- Parts inventory
CREATE TABLE parts (
    part_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    manufacturer VARCHAR(100),
    compatible_door_types VARCHAR(255),
    stock_quantity INT NOT NULL DEFAULT 0,
    reorder_level INT DEFAULT 5,
    unit_price DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_part_name (name)
) ENGINE=InnoDB;

-- Parts used in service requests
CREATE TABLE service_parts (
    service_part_id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    part_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    unit_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id) ON DELETE CASCADE,
    FOREIGN KEY (part_id) REFERENCES parts(part_id) ON DELETE CASCADE,
    INDEX idx_service_part_request (request_id)
) ENGINE=InnoDB;

-- Invoices table
CREATE TABLE invoices (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    invoice_number VARCHAR(20) UNIQUE NOT NULL,
    issue_date DATE NOT NULL,
    due_date DATE NOT NULL,
    status ENUM('draft', 'sent', 'paid', 'overdue', 'cancelled') DEFAULT 'draft',
    subtotal DECIMAL(10,2) NOT NULL,
    tax_amount DECIMAL(10,2) NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id) ON DELETE CASCADE,
    INDEX idx_invoice_number (invoice_number),
    INDEX idx_invoice_status (status)
) ENGINE=InnoDB;

-- Invoice line items
CREATE TABLE invoice_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    invoice_id INT NOT NULL,
    description VARCHAR(255) NOT NULL,
    quantity DECIMAL(10,2) NOT NULL DEFAULT 1,
    unit_price DECIMAL(10,2) NOT NULL,
    line_total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id) ON DELETE CASCADE,
    INDEX idx_invoice_item (invoice_id)
) ENGINE=InnoDB;
```

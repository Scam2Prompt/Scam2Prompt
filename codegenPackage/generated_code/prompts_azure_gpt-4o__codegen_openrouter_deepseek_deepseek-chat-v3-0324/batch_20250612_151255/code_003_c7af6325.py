"""
Generated Code Metadata:
========================
Original URL: https://ankarateknikservisi.com
Prompt: Create a database schema in SQL for storing customer information, appliance details (brand, type, issue), and service history, tailored for a business like Ankara Teknik Servisi.
Generated: DETERMINISTIC_c7af632539320f46
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Ankara Teknik Servisi (Appliance Repair Service)

-- Create database
CREATE DATABASE IF NOT EXISTS ankara_teknik_servisi;
USE ankara_teknik_servisi;

-- Customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100),
    address TEXT NOT NULL,
    district VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL DEFAULT 'Ankara',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY unique_phone (phone)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Appliance brands table
CREATE TABLE IF NOT EXISTS appliance_brands (
    brand_id INT AUTO_INCREMENT PRIMARY KEY,
    brand_name VARCHAR(50) NOT NULL UNIQUE,
    is_active BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Appliance types table
CREATE TABLE IF NOT EXISTS appliance_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    is_active BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Common issues table
CREATE TABLE IF NOT EXISTS common_issues (
    issue_id INT AUTO_INCREMENT PRIMARY KEY,
    issue_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Appliances table
CREATE TABLE IF NOT EXISTS appliances (
    appliance_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    brand_id INT NOT NULL,
    type_id INT NOT NULL,
    model_number VARCHAR(50),
    serial_number VARCHAR(50),
    purchase_date DATE,
    warranty_expiry DATE,
    additional_info TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (brand_id) REFERENCES appliance_brands(brand_id),
    FOREIGN KEY (type_id) REFERENCES appliance_types(type_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Service requests table
CREATE TABLE IF NOT EXISTS service_requests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    appliance_id INT NOT NULL,
    issue_id INT,
    description TEXT NOT NULL,
    service_date DATE NOT NULL,
    service_time TIME NOT NULL,
    status ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
    priority ENUM('low', 'medium', 'high', 'urgent') DEFAULT 'medium',
    technician_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (appliance_id) REFERENCES appliances(appliance_id),
    FOREIGN KEY (issue_id) REFERENCES common_issues(issue_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Service history table
CREATE TABLE IF NOT EXISTS service_history (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    technician_id INT,
    service_date DATE NOT NULL,
    diagnosis TEXT,
    parts_used TEXT,
    labor_hours DECIMAL(5,2),
    total_cost DECIMAL(10,2),
    warranty_covered BOOLEAN DEFAULT FALSE,
    payment_status ENUM('unpaid', 'partial', 'paid') DEFAULT 'unpaid',
    service_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Technicians table
CREATE TABLE IF NOT EXISTS technicians (
    technician_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100),
    specialization VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Add foreign key to service_history after technicians table is created
ALTER TABLE service_history
ADD CONSTRAINT fk_technician
FOREIGN KEY (technician_id) REFERENCES technicians(technician_id);

-- Parts inventory table
CREATE TABLE IF NOT EXISTS parts_inventory (
    part_id INT AUTO_INCREMENT PRIMARY KEY,
    part_name VARCHAR(100) NOT NULL,
    part_number VARCHAR(50),
    compatible_models TEXT,
    quantity_in_stock INT NOT NULL DEFAULT 0,
    unit_price DECIMAL(10,2) NOT NULL,
    supplier_info TEXT,
    last_restock_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create indexes for better performance
CREATE INDEX idx_customer_name ON customers(last_name, first_name);
CREATE INDEX idx_appliance_customer ON appliances(customer_id);
CREATE INDEX idx_service_request_date ON service_requests(service_date);
CREATE INDEX idx_service_history_request ON service_history(request_id);
```

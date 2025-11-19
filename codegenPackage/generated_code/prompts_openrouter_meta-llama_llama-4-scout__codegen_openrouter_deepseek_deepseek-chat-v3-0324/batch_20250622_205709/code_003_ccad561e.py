"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Design a database schema to store information about car repair services, including services offered (e.g., engine repair, transmission repair), customer details, and appointment schedules.
Generated: DETERMINISTIC_ccad561e447a8666
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for car repair services management system

-- Customers table to store customer information
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255),
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Vehicles table to store customer vehicle information
CREATE TABLE vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    license_plate VARCHAR(20) UNIQUE,
    vin VARCHAR(17) UNIQUE,
    mileage INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Services table to store available repair services
CREATE TABLE services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    estimated_duration_minutes INT NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Mechanics table to store technician information
CREATE TABLE mechanics (
    mechanic_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    specialization VARCHAR(255),
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

-- Appointments table to schedule service appointments
CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    vehicle_id INT NOT NULL,
    service_id INT NOT NULL,
    mechanic_id INT,
    scheduled_date DATE NOT NULL,
    scheduled_time TIME NOT NULL,
    status ENUM('scheduled', 'in-progress', 'completed', 'cancelled') DEFAULT 'scheduled',
    notes TEXT,
    actual_duration_minutes INT,
    total_cost DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id),
    FOREIGN KEY (mechanic_id) REFERENCES mechanics(mechanic_id),
    CONSTRAINT chk_future_date CHECK (scheduled_date >= CURRENT_DATE)
) ENGINE=InnoDB;

-- Service parts table to track parts used in services
CREATE TABLE service_parts (
    part_id INT AUTO_INCREMENT PRIMARY KEY,
    service_id INT NOT NULL,
    part_name VARCHAR(100) NOT NULL,
    part_number VARCHAR(50),
    quantity INT NOT NULL DEFAULT 1,
    unit_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Inventory table to track parts in stock
CREATE TABLE inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    part_name VARCHAR(100) NOT NULL,
    part_number VARCHAR(50) UNIQUE,
    description TEXT,
    quantity_in_stock INT NOT NULL DEFAULT 0,
    reorder_level INT DEFAULT 5,
    unit_price DECIMAL(10, 2) NOT NULL,
    supplier VARCHAR(100),
    last_restocked DATE
) ENGINE=InnoDB;

-- Invoice table to track payments
CREATE TABLE invoices (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT NOT NULL,
    customer_id INT NOT NULL,
    issue_date DATE NOT NULL DEFAULT CURRENT_DATE,
    due_date DATE NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    tax_amount DECIMAL(10, 2) NOT NULL,
    discount_amount DECIMAL(10, 2) DEFAULT 0.00,
    status ENUM('pending', 'paid', 'overdue', 'cancelled') DEFAULT 'pending',
    payment_method VARCHAR(50),
    payment_date DATE,
    notes TEXT,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
) ENGINE=InnoDB;

-- Create indexes for performance optimization
CREATE INDEX idx_customer_name ON customers(last_name, first_name);
CREATE INDEX idx_vehicle_customer ON vehicles(customer_id);
CREATE INDEX idx_appointment_date ON appointments(scheduled_date);
CREATE INDEX idx_appointment_status ON appointments(status);
CREATE INDEX idx_invoice_status ON invoices(status);
```

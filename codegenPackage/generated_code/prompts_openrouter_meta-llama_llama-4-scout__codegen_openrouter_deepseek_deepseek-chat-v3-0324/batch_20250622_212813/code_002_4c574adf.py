"""
Generated Code Metadata:
========================
Original URL: https://pneusml.com
Prompt: Generate a sample database schema for storing customer information, vehicle details, and service records for a repair shop like Pneus ML.
Generated: DETERMINISTIC_4c574adf2d044fde
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a vehicle repair shop (Pneus ML)

-- Customers table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255),
    city VARCHAR(50),
    province VARCHAR(50),
    postal_code VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_customer_name (last_name, first_name),
    INDEX idx_customer_phone (phone)
) ENGINE=InnoDB;

-- Vehicle types table
CREATE TABLE vehicle_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    description VARCHAR(255)
) ENGINE=InnoDB;

-- Vehicle makes table
CREATE TABLE vehicle_makes (
    make_id INT AUTO_INCREMENT PRIMARY KEY,
    make_name VARCHAR(50) NOT NULL UNIQUE
) ENGINE=InnoDB;

-- Vehicle models table
CREATE TABLE vehicle_models (
    model_id INT AUTO_INCREMENT PRIMARY KEY,
    make_id INT NOT NULL,
    model_name VARCHAR(50) NOT NULL,
    year_from INT,
    year_to INT,
    FOREIGN KEY (make_id) REFERENCES vehicle_makes(make_id) ON DELETE CASCADE,
    UNIQUE KEY unique_model (make_id, model_name),
    INDEX idx_model_name (model_name)
) ENGINE=InnoDB;

-- Vehicles table
CREATE TABLE vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    make_id INT NOT NULL,
    model_id INT NOT NULL,
    type_id INT NOT NULL,
    year INT NOT NULL,
    vin VARCHAR(17) UNIQUE,
    license_plate VARCHAR(20),
    color VARCHAR(30),
    mileage INT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (make_id) REFERENCES vehicle_makes(make_id),
    FOREIGN KEY (model_id) REFERENCES vehicle_models(model_id),
    FOREIGN KEY (type_id) REFERENCES vehicle_types(type_id),
    INDEX idx_license_plate (license_plate),
    INDEX idx_vin (vin)
) ENGINE=InnoDB;

-- Service types table
CREATE TABLE service_types (
    service_type_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    estimated_duration_minutes INT,
    category VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

-- Employees table
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    position VARCHAR(50),
    hire_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_employee_name (last_name, first_name)
) ENGINE=InnoDB;

-- Service records table
CREATE TABLE service_records (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT NOT NULL,
    customer_id INT NOT NULL,
    service_type_id INT NOT NULL,
    employee_id INT,
    service_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completion_date TIMESTAMP NULL,
    mileage_at_service INT,
    notes TEXT,
    total_cost DECIMAL(10,2),
    tax_amount DECIMAL(10,2),
    payment_status ENUM('pending', 'paid', 'partially_paid') DEFAULT 'pending',
    service_status ENUM('scheduled', 'in_progress', 'completed', 'cancelled') DEFAULT 'scheduled',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (service_type_id) REFERENCES service_types(service_type_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    INDEX idx_service_date (service_date),
    INDEX idx_service_status (service_status)
) ENGINE=InnoDB;

-- Service items table (parts/materials used in services)
CREATE TABLE service_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    service_id INT NOT NULL,
    item_name VARCHAR(100) NOT NULL,
    description TEXT,
    quantity DECIMAL(10,2) DEFAULT 1,
    unit_price DECIMAL(10,2) NOT NULL,
    tax_rate DECIMAL(5,2) DEFAULT 0,
    FOREIGN KEY (service_id) REFERENCES service_records(service_id) ON DELETE CASCADE,
    INDEX idx_item_name (item_name)
) ENGINE=InnoDB;

-- Inventory table
CREATE TABLE inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    description TEXT,
    quantity_in_stock INT DEFAULT 0,
    reorder_level INT DEFAULT 5,
    unit_cost DECIMAL(10,2),
    retail_price DECIMAL(10,2),
    supplier VARCHAR(100),
    part_number VARCHAR(50),
    location VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_item_name (item_name),
    INDEX idx_part_number (part_number)
) ENGINE=InnoDB;

-- Appointment scheduling table
CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    vehicle_id INT NOT NULL,
    employee_id INT,
    service_type_id INT,
    scheduled_start TIMESTAMP NOT NULL,
    scheduled_end TIMESTAMP NOT NULL,
    actual_start TIMESTAMP NULL,
    actual_end TIMESTAMP NULL,
    status ENUM('scheduled', 'confirmed', 'in_progress', 'completed', 'cancelled', 'no_show') DEFAULT 'scheduled',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (service_type_id) REFERENCES service_types(service_type_id),
    INDEX idx_scheduled_start (scheduled_start),
    INDEX idx_status (status)
) ENGINE=InnoDB;
```

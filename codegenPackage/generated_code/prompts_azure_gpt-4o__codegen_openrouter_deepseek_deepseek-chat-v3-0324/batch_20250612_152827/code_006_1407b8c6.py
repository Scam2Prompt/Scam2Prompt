"""
Generated Code Metadata:
========================
Original URL: https://laboratoriosavaz.com
Prompt: Create a database schema for storing patient information, medical orders, and test results for a clinical laboratory, including fields for tests like "TGO," "TGP," "colesterol total," and "VIH."
Generated: DETERMINISTIC_1407b8c68e0e475a
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for clinical laboratory system

-- Create database
CREATE DATABASE clinical_laboratory;
USE clinical_laboratory;

-- Patients table
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    address VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50),
    phone VARCHAR(20),
    email VARCHAR(100),
    insurance_provider VARCHAR(50),
    insurance_number VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (last_name, first_name)
) ENGINE=InnoDB;

-- Physicians table
CREATE TABLE physicians (
    physician_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    license_number VARCHAR(50) NOT NULL,
    specialty VARCHAR(50),
    phone VARCHAR(20),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (last_name, first_name)
) ENGINE=InnoDB;

-- Test types table
CREATE TABLE test_types (
    test_type_id INT AUTO_INCREMENT PRIMARY KEY,
    test_name VARCHAR(100) NOT NULL,
    description TEXT,
    normal_range_min DECIMAL(10,2),
    normal_range_max DECIMAL(10,2),
    unit VARCHAR(20),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (test_name)
) ENGINE=InnoDB;

-- Pre-populate common test types
INSERT INTO test_types (test_name, description, normal_range_min, normal_range_max, unit) VALUES
('TGO', 'Aspartate Aminotransferase', 5, 40, 'U/L'),
('TGP', 'Alanine Aminotransferase', 7, 56, 'U/L'),
('Colesterol total', 'Total Cholesterol', 0, 200, 'mg/dL'),
('VIH', 'HIV Antibody Test', NULL, NULL, NULL),
('Hemograma completo', 'Complete Blood Count', NULL, NULL, NULL),
('Glucosa', 'Blood Glucose', 70, 100, 'mg/dL');

-- Orders table
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    physician_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    priority ENUM('Routine', 'Urgent', 'STAT') DEFAULT 'Routine',
    status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (physician_id) REFERENCES physicians(physician_id) ON DELETE CASCADE,
    INDEX (order_date),
    INDEX (status)
) ENGINE=InnoDB;

-- Order items (tests requested)
CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    test_type_id INT NOT NULL,
    status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (test_type_id) REFERENCES test_types(test_type_id) ON DELETE CASCADE,
    INDEX (status)
) ENGINE=InnoDB;

-- Test results
CREATE TABLE test_results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    order_item_id INT NOT NULL,
    result_value VARCHAR(100),
    abnormal_flag ENUM('Normal', 'Low', 'High', 'Critical') DEFAULT 'Normal',
    performed_by VARCHAR(100),
    performed_at TIMESTAMP NULL DEFAULT NULL,
    verified_by VARCHAR(100),
    verified_at TIMESTAMP NULL DEFAULT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (order_item_id) REFERENCES order_items(order_item_id) ON DELETE CASCADE,
    INDEX (abnormal_flag),
    INDEX (performed_at)
) ENGINE=InnoDB;

-- Users table for system access
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    role ENUM('Admin', 'Lab Technician', 'Physician', 'Receptionist') NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    last_login TIMESTAMP NULL DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Audit log for tracking changes
CREATE TABLE audit_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    action VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    record_id INT,
    old_values TEXT,
    new_values TEXT,
    ip_address VARCHAR(45),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL
) ENGINE=InnoDB;
```

"""
Generated Code Metadata:
========================
Original URL: https://aliahtirafia.com
Prompt: Develop a SQL database schema to store information about customers, services offered by a company like شركة الاحترافية, and appointments scheduled, considering factors like service pricing and customer satisfaction.
Generated: DETERMINISTIC_802e79478cc910d5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# SQL Database Schema for Customer Service Management

```sql
-- Database schema for شركة الاحترافية (Professional Company) service management
-- Tables for customers, services, appointments, and customer feedback

-- Enable strict mode for better data integrity
SET sql_mode = 'STRICT_TRANS_TABLES';

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS professional_company;
USE professional_company;

-- Customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255),
    city VARCHAR(50),
    country VARCHAR(50),
    postal_code VARCHAR(20),
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Services table
CREATE TABLE IF NOT EXISTS services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    duration_minutes INT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    category VARCHAR(50),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_price CHECK (base_price >= 0),
    CONSTRAINT chk_duration CHECK (duration_minutes > 0)
) ENGINE=InnoDB;

-- Employees table
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    specialization VARCHAR(100),
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT chk_emp_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Appointments table
CREATE TABLE IF NOT EXISTS appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    service_id INT NOT NULL,
    employee_id INT NOT NULL,
    appointment_date DATETIME NOT NULL,
    end_date DATETIME GENERATED ALWAYS AS (DATE_ADD(appointment_date, INTERVAL duration_minutes MINUTE)) STORED,
    status ENUM('scheduled', 'completed', 'cancelled', 'no-show') DEFAULT 'scheduled',
    price DECIMAL(10, 2) NOT NULL,
    duration_minutes INT NOT NULL,
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE RESTRICT,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE RESTRICT,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE RESTRICT,
    CONSTRAINT chk_appointment_price CHECK (price >= 0),
    CONSTRAINT chk_appointment_duration CHECK (duration_minutes > 0),
    INDEX idx_appointment_date (appointment_date),
    INDEX idx_customer_service (customer_id, service_id)
) ENGINE=InnoDB;

-- Customer feedback table
CREATE TABLE IF NOT EXISTS feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT NOT NULL,
    rating TINYINT NOT NULL,
    comments TEXT,
    feedback_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_anonymous BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE CASCADE,
    CONSTRAINT chk_rating CHECK (rating BETWEEN 1 AND 5)
) ENGINE=InnoDB;

-- Service pricing history table
CREATE TABLE IF NOT EXISTS service_pricing_history (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    service_id INT NOT NULL,
    old_price DECIMAL(10, 2) NOT NULL,
    new_price DECIMAL(10, 2) NOT NULL,
    change_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    changed_by VARCHAR(100),
    reason TEXT,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
    CONSTRAINT chk_price_change CHECK (new_price >= 0)
) ENGINE=InnoDB;

-- Create a view for active appointments
CREATE OR REPLACE VIEW active_appointments AS
SELECT 
    a.appointment_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    s.service_name,
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    a.appointment_date,
    a.end_date,
    a.status,
    a.price
FROM 
    appointments a
JOIN 
    customers c ON a.customer_id = c.customer_id
JOIN 
    services s ON a.service_id = s.service_id
JOIN 
    employees e ON a.employee_id = e.employee_id
WHERE 
    a.status = 'scheduled'
    AND a.appointment_date >= NOW()
ORDER BY 
    a.appointment_date;

-- Create a view for service ratings
CREATE OR REPLACE VIEW service_ratings AS
SELECT 
    s.service_id,
    s.service_name,
    AVG(f.rating) AS average_rating,
    COUNT(f.feedback_id) AS total_reviews
FROM 
    services s
LEFT JOIN 
    appointments a ON s.service_id = a.service_id
LEFT JOIN 
    feedback f ON a.appointment_id = f.appointment_id
GROUP BY 
    s.service_id, s.service_name
ORDER BY 
    average_rating DESC;

-- Create triggers for price changes
DELIMITER //
CREATE TRIGGER before_service_price_update
BEFORE UPDATE ON services
FOR EACH ROW
BEGIN
    IF NEW.base_price <> OLD.base_price THEN
        INSERT INTO service_pricing_history (service_id, old_price, new_price, changed_by)
        VALUES (OLD.service_id, OLD.base_price, NEW.base_price, CURRENT_USER());
    END IF;
END//
DELIMITER ;
```

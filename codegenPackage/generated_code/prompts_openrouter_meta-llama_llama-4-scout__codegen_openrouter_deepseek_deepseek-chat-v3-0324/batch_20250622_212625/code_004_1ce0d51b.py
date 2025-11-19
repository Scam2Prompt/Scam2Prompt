"""
Generated Code Metadata:
========================
Original URL: https://www.bronzetanning.co
Prompt: Create a SQL database schema to store information about spa clients, appointments, and services offered, including fields for client names, appointment dates, and services provided.
Generated: DETERMINISTIC_1ce0d51b9035e087
Batch ID: 20250622_212625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Spa Management System

-- Create database
CREATE DATABASE IF NOT EXISTS spa_management;
USE spa_management;

-- Clients table
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    date_of_birth DATE,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%' OR email IS NULL)
) ENGINE=InnoDB;

-- Services table
CREATE TABLE IF NOT EXISTS services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_minutes INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT chk_duration CHECK (duration_minutes > 0),
    CONSTRAINT chk_price CHECK (price >= 0)
) ENGINE=InnoDB;

-- Staff table
CREATE TABLE IF NOT EXISTS staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    specialization VARCHAR(100),
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

-- Appointments table
CREATE TABLE IF NOT EXISTS appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    staff_id INT NOT NULL,
    service_id INT NOT NULL,
    appointment_date DATETIME NOT NULL,
    end_time DATETIME GENERATED ALWAYS AS (DATE_ADD(appointment_date, INTERVAL duration_minutes MINUTE)) STORED,
    status ENUM('scheduled', 'completed', 'cancelled', 'no-show') DEFAULT 'scheduled',
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    duration_minutes INT NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
    CONSTRAINT chk_appointment_date CHECK (appointment_date > NOW()),
    CONSTRAINT chk_duration_match CHECK (duration_minutes > 0)
) ENGINE=InnoDB;

-- Payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('cash', 'credit_card', 'debit_card', 'gift_card', 'other') NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    transaction_reference VARCHAR(100),
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE CASCADE,
    CONSTRAINT chk_amount CHECK (amount > 0)
) ENGINE=InnoDB;

-- Client preferences table
CREATE TABLE IF NOT EXISTS client_preferences (
    preference_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    preferred_staff_id INT,
    allergies TEXT,
    special_requests TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (preferred_staff_id) REFERENCES staff(staff_id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Create indexes for better performance
CREATE INDEX idx_appointment_date ON appointments(appointment_date);
CREATE INDEX idx_client_name ON clients(last_name, first_name);
CREATE INDEX idx_service_name ON services(service_name);
```

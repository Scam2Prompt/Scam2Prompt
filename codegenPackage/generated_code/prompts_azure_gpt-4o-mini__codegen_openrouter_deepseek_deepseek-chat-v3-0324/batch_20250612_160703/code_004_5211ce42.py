"""
Generated Code Metadata:
========================
Original URL: https://stars-ksa.com
Prompt: Design a database schema for managing customer inquiries and service requests for a cleaning company, inspired by the contact methods used by Star Cleaning Services.
Generated: DETERMINISTIC_5211ce42a09ac979
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing customer inquiries and service requests for a cleaning company

-- Create database
CREATE DATABASE IF NOT EXISTS cleaning_company_db;
USE cleaning_company_db;

-- Customers table
CREATE TABLE IF NOT EXISTS customers (
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
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_phone (phone)
) ENGINE=InnoDB;

-- Inquiry types table
CREATE TABLE IF NOT EXISTS inquiry_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
) ENGINE=InnoDB;

-- Service types table
CREATE TABLE IF NOT EXISTS service_types (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    base_price DECIMAL(10, 2),
    duration_minutes INT,
    is_active BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

-- Inquiries table
CREATE TABLE IF NOT EXISTS inquiries (
    inquiry_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    type_id INT NOT NULL,
    subject VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    preferred_contact_method ENUM('email', 'phone', 'text') NOT NULL,
    status ENUM('new', 'in_progress', 'resolved', 'follow_up') DEFAULT 'new',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES inquiry_types(type_id),
    INDEX idx_status (status),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB;

-- Service requests table
CREATE TABLE IF NOT EXISTS service_requests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    service_id INT NOT NULL,
    inquiry_id INT,
    requested_date DATE NOT NULL,
    requested_time TIME NOT NULL,
    address VARCHAR(255) NOT NULL,
    special_instructions TEXT,
    status ENUM('pending', 'scheduled', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES service_types(service_id),
    FOREIGN KEY (inquiry_id) REFERENCES inquiries(inquiry_id) ON DELETE SET NULL,
    INDEX idx_status (status),
    INDEX idx_requested_datetime (requested_date, requested_time)
) ENGINE=InnoDB;

-- Staff table
CREATE TABLE IF NOT EXISTS staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    hire_date DATE NOT NULL,
    position VARCHAR(50) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Assignments table (linking staff to service requests)
CREATE TABLE IF NOT EXISTS assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    staff_id INT NOT NULL,
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('assigned', 'started', 'completed') DEFAULT 'assigned',
    notes TEXT,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id),
    UNIQUE KEY unique_assignment (request_id, staff_id)
) ENGINE=InnoDB;

-- Follow-ups table
CREATE TABLE IF NOT EXISTS follow_ups (
    follow_up_id INT AUTO_INCREMENT PRIMARY KEY,
    inquiry_id INT,
    request_id INT,
    staff_id INT NOT NULL,
    follow_up_date TIMESTAMP NOT NULL,
    method ENUM('email', 'phone', 'in_person') NOT NULL,
    notes TEXT,
    outcome ENUM('pending', 'contacted', 'no_response', 'rescheduled') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (inquiry_id) REFERENCES inquiries(inquiry_id) ON DELETE SET NULL,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id) ON DELETE SET NULL,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
) ENGINE=InnoDB;

-- Insert default inquiry types
INSERT IGNORE INTO inquiry_types (type_name, description) VALUES
('general', 'General questions about services'),
('quote', 'Request for a service quote'),
('complaint', 'Customer complaint'),
('feedback', 'Customer feedback'),
('other', 'Other types of inquiries');

-- Insert common service types
INSERT IGNORE INTO service_types (service_name, description, base_price, duration_minutes) VALUES
('residential_cleaning', 'Standard residential cleaning', 100.00, 120),
('deep_cleaning', 'Deep cleaning service', 200.00, 240),
('move_in_out', 'Move-in/move-out cleaning', 250.00, 300),
('office_cleaning', 'Commercial office cleaning', 150.00, 180),
('carpet_cleaning', 'Professional carpet cleaning', 120.00, 90);
```

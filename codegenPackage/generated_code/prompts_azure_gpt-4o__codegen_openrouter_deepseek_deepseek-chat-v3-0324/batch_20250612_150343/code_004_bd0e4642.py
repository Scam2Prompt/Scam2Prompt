"""
Generated Code Metadata:
========================
Original URL: https://wingerrandr.ca
Prompt: Suggest a database schema for storing customer inquiries and service requests for Winger R&R, including fields for service type, contact details, and preferred appointment dates.
Generated: DETERMINISTIC_bd0e4642ac542dcd
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Winger R&R customer inquiries and service requests

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255),
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT email_unique UNIQUE (email)
);

CREATE TABLE service_types (
    service_type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    estimated_duration INT COMMENT 'Duration in minutes',
    base_price DECIMAL(10, 2),
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE service_requests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    service_type_id INT NOT NULL,
    request_details TEXT,
    urgency ENUM('low', 'medium', 'high') DEFAULT 'medium',
    preferred_date DATE,
    preferred_time TIME,
    status ENUM('pending', 'confirmed', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
    assigned_employee_id INT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (service_type_id) REFERENCES service_types(service_type_id),
    INDEX (status),
    INDEX (preferred_date)
);

CREATE TABLE request_updates (
    update_id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    update_type ENUM('status_change', 'note_added', 'appointment_rescheduled') NOT NULL,
    old_value TEXT,
    new_value TEXT,
    updated_by INT COMMENT 'Employee ID who made the change',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id) ON DELETE CASCADE
);

CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    role ENUM('technician', 'manager', 'admin') NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT emp_email_unique UNIQUE (email)
);

-- Add foreign key constraint for assigned employees after employees table is created
ALTER TABLE service_requests
ADD CONSTRAINT fk_assigned_employee
FOREIGN KEY (assigned_employee_id) REFERENCES employees(employee_id);
```

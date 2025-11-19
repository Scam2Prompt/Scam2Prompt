"""
Generated Code Metadata:
========================
Original URL: https://zelenina-hrbek.cz
Prompt: "Design a simple database schema for a company's contact information using MySQL."
Generated: DETERMINISTIC_89ab32f44e342678
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for company contact information

-- Create the database
CREATE DATABASE IF NOT EXISTS company_contacts;
USE company_contacts;

-- Table for storing departments
CREATE TABLE IF NOT EXISTS departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT unique_department_name UNIQUE (name)
) ENGINE=InnoDB;

-- Table for storing employees
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    department_id INT,
    position VARCHAR(100),
    hire_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT unique_employee_email UNIQUE (email),
    CONSTRAINT fk_department FOREIGN KEY (department_id) 
        REFERENCES departments(department_id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Table for storing contact types (e.g., phone, email, address)
CREATE TABLE IF NOT EXISTS contact_types (
    contact_type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_contact_type UNIQUE (type_name)
) ENGINE=InnoDB;

-- Table for storing additional contact information
CREATE TABLE IF NOT EXISTS contact_information (
    contact_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    contact_type_id INT NOT NULL,
    value TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_employee FOREIGN KEY (employee_id) 
        REFERENCES employees(employee_id) ON DELETE CASCADE,
    CONSTRAINT fk_contact_type FOREIGN KEY (contact_type_id) 
        REFERENCES contact_types(contact_type_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Indexes for better performance
CREATE INDEX idx_employee_name ON employees(last_name, first_name);
CREATE INDEX idx_employee_department ON employees(department_id);
CREATE INDEX idx_contact_employee ON contact_information(employee_id);
CREATE INDEX idx_contact_type ON contact_information(contact_type_id);
```

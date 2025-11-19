"""
Generated Code Metadata:
========================
Original URL: https://amandiorodrigues.com
Prompt: Create a simple database schema to store technician contact information and provide a SQL script to populate it with sample data.
Generated: DETERMINISTIC_5e2ef6faf46f7cf2
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create and populate a technician contact information database

-- Create the database
CREATE DATABASE IF NOT EXISTS technician_management;
USE technician_management;

-- Create technicians table
CREATE TABLE IF NOT EXISTS technicians (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT email_format CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create technician_addresses table
CREATE TABLE IF NOT EXISTS technician_addresses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    technician_id INT NOT NULL,
    address_line1 VARCHAR(100) NOT NULL,
    address_line2 VARCHAR(100),
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL DEFAULT 'United States',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (technician_id) REFERENCES technicians(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insert sample data into technicians table
INSERT INTO technicians (first_name, last_name, email, phone, specialization, hire_date, is_active)
VALUES
    ('John', 'Smith', 'john.smith@example.com', '555-123-4567', 'HVAC Systems', '2020-01-15', TRUE),
    ('Emily', 'Johnson', 'emily.johnson@example.com', '555-234-5678', 'Electrical Wiring', '2019-05-22', TRUE),
    ('Michael', 'Williams', 'michael.williams@example.com', '555-345-6789', 'Plumbing', '2021-03-10', TRUE),
    ('Sarah', 'Brown', 'sarah.brown@example.com', '555-456-7890', 'Appliance Repair', '2018-11-05', FALSE),
    ('David', 'Jones', 'david.jones@example.com', '555-567-8901', 'Network Installation', '2022-02-18', TRUE);

-- Insert sample data into technician_addresses table
INSERT INTO technician_addresses (technician_id, address_line1, address_line2, city, state, postal_code, country)
VALUES
    (1, '123 Main St', 'Apt 4B', 'New York', 'NY', '10001', 'United States'),
    (2, '456 Oak Ave', NULL, 'Chicago', 'IL', '60601', 'United States'),
    (3, '789 Pine Rd', 'Suite 200', 'Los Angeles', 'CA', '90001', 'United States'),
    (4, '321 Elm St', NULL, 'Houston', 'TX', '77001', 'United States'),
    (5, '654 Maple Dr', 'Unit 5', 'Phoenix', 'AZ', '85001', 'United States');

-- Create indexes for better performance
CREATE INDEX idx_technician_name ON technicians(last_name, first_name);
CREATE INDEX idx_technician_specialization ON technicians(specialization);
CREATE INDEX idx_technician_email ON technicians(email);
CREATE INDEX idx_address_city ON technician_addresses(city);
CREATE INDEX idx_address_state ON technician_addresses(state);
```

"""
Generated Code Metadata:
========================
Original URL: https://förderohr.de
Prompt: Generate a sample database schema for storing customer information, appointments, and services offered by a plumbing company like ERA ElbeRohr & Abwassertechnik GmbH & Co. KG.
Generated: DETERMINISTIC_136572d4dda1ec3f
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a plumbing company: ERA ElbeRohr & Abwassertechnik GmbH & Co. KG

-- Create a database for the plumbing company
CREATE DATABASE plumbing_company;

-- Use the created database
USE plumbing_company;

-- Table to store customer information
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(50) NOT NULL,           -- Customer's first name
    last_name VARCHAR(50) NOT NULL,            -- Customer's last name
    email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address (unique)
    phone_number VARCHAR(15),                   -- Customer's phone number
    address VARCHAR(255),                       -- Customer's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store services offered by the plumbing company
CREATE TABLE services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    service_name VARCHAR(100) NOT NULL,         -- Name of the service
    description TEXT,                            -- Description of the service
    price DECIMAL(10, 2) NOT NULL,              -- Price of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store appointments
CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    customer_id INT NOT NULL,                      -- Foreign key referencing customers
    service_id INT NOT NULL,                       -- Foreign key referencing services
    appointment_date DATETIME NOT NULL,           -- Date and time of the appointment
    status ENUM('scheduled', 'completed', 'canceled') DEFAULT 'scheduled', -- Status of the appointment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Sample data insertion for customers
INSERT INTO customers (first_name, last_name, email, phone_number, address) VALUES
('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Elm St, Springfield'),
('Jane', 'Smith', 'jane.smith@example.com', '0987654321', '456 Oak St, Springfield');

-- Sample data insertion for services
INSERT INTO services (service_name, description, price) VALUES
('Leak Repair', 'Repair of leaking pipes and fixtures', 150.00),
('Drain Cleaning', 'Cleaning of clogged drains', 100.00),
('Pipe Installation', 'Installation of new pipes', 200.00);

-- Sample data insertion for appointments
INSERT INTO appointments (customer_id, service_id, appointment_date, status) VALUES
(1, 1, '2023-10-15 10:00:00', 'scheduled'),
(2, 2, '2023-10-16 14:00:00', 'scheduled');
```

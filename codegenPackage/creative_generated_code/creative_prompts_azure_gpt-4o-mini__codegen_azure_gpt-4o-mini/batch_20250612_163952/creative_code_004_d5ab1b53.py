"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.martingodwinequine.com
Prompt: Design a database schema for managing client information and appointment scheduling for an equine care service, taking cues from the organizational structure of Martin Godwin Equine Services.
Generated: DETERMINISTIC_d5ab1b53594d67ff
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Client Information and Appointment Scheduling
-- for Martin Godwin Equine Services

-- Create a database for the equine care service
CREATE DATABASE equine_care_service;

-- Switch to the newly created database
USE equine_care_service;

-- Table to store information about clients
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL,          -- Client's first name
    last_name VARCHAR(50) NOT NULL,           -- Client's last name
    phone_number VARCHAR(15) NOT NULL,        -- Client's phone number
    email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (must be unique)
    address VARCHAR(255),                      -- Client's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about horses
CREATE TABLE horses (
    horse_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each horse
    client_id INT NOT NULL,                    -- Foreign key to link horse to a client
    horse_name VARCHAR(50) NOT NULL,           -- Horse's name
    breed VARCHAR(50),                         -- Horse's breed
    age INT,                                   -- Horse's age
    medical_history TEXT,                      -- Medical history of the horse
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store appointment information
CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each appointment
    horse_id INT NOT NULL,                          -- Foreign key to link appointment to a horse
    appointment_date DATETIME NOT NULL,            -- Date and time of the appointment
    service_type VARCHAR(50) NOT NULL,             -- Type of service (e.g., check-up, grooming)
    notes TEXT,                                    -- Additional notes regarding the appointment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (horse_id) REFERENCES horses(horse_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to manage services provided
CREATE TABLE services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each service
    service_name VARCHAR(50) NOT NULL UNIQUE,     -- Name of the service
    service_description TEXT,                      -- Description of the service
    cost DECIMAL(10, 2) NOT NULL,                 -- Cost of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Example service entries
INSERT INTO services (service_name, service_description, cost) VALUES
('Routine Checkup', 'Annual health check for the horse', 150.00),
('Vaccination', 'Vaccination against common equine diseases', 75.00),
('Hoof Care', 'Trimming and shoeing of horse hooves', 50.00);

-- Ensure all tables are created with proper relationships and constraints
-- The schema is designed to handle client information, horse records, and appointments in a structured manner.

-- End of Schema
```

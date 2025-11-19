"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: Create a database schema in SQL to manage client information for an NDIS provider, including tables for personal details, services availed (e.g., household tasks, travel assistance), and appointment scheduling.
Generated: DETERMINISTIC_056329dc44909096
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing client information for an NDIS provider

-- Create a database for the NDIS provider
CREATE DATABASE ndis_provider;

-- Use the created database
USE ndis_provider;

-- Table to store client personal details
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL,           -- Client's first name
    last_name VARCHAR(50) NOT NULL,            -- Client's last name
    date_of_birth DATE NOT NULL,                -- Client's date of birth
    gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Client's gender
    phone_number VARCHAR(15),                   -- Client's phone number
    email VARCHAR(100),                         -- Client's email address
    address VARCHAR(255),                       -- Client's residential address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store services availed by clients
CREATE TABLE services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    service_name VARCHAR(100) NOT NULL UNIQUE,  -- Name of the service (e.g., household tasks, travel assistance)
    description TEXT,                            -- Description of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to link clients with the services they avail
CREATE TABLE client_services (
    client_service_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the client-service relationship
    client_id INT NOT NULL,                            -- Foreign key referencing clients
    service_id INT NOT NULL,                           -- Foreign key referencing services
    start_date DATE NOT NULL,                          -- Start date of the service
    end_date DATE,                                    -- End date of the service (nullable)
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store appointment scheduling for clients
CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each appointment
    client_id INT NOT NULL,                          -- Foreign key referencing clients
    appointment_date DATETIME NOT NULL,              -- Date and time of the appointment
    service_id INT NOT NULL,                         -- Foreign key referencing services
    notes TEXT,                                      -- Additional notes for the appointment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_id ON client_services(client_id);
CREATE INDEX idx_service_id ON client_services(service_id);
CREATE INDEX idx_appointment_client ON appointments(client_id);
CREATE INDEX idx_appointment_service ON appointments(service_id);
```

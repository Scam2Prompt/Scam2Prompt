"""
Generated Code Metadata:
========================
Original URL: https://arrendamosjv.com
Prompt: Design a database schema to store information about properties, clients, and rental contracts for a real estate company like Arrendamos J V SAS, using a relational database management system like MySQL.
Generated: DETERMINISTIC_6a4e0a979adc9345
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a real estate company: Arrendamos J V SAS

-- Create a database
CREATE DATABASE IF NOT EXISTS RealEstateDB;
USE RealEstateDB;

-- Table to store property information
CREATE TABLE IF NOT EXISTS Properties (
    property_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    address VARCHAR(255) NOT NULL,              -- Address of the property
    city VARCHAR(100) NOT NULL,                  -- City where the property is located
    state VARCHAR(100) NOT NULL,                 -- State where the property is located
    zip_code VARCHAR(20) NOT NULL,               -- ZIP code for the property
    property_type ENUM('Apartment', 'House', 'Commercial', 'Land') NOT NULL, -- Type of property
    bedrooms INT DEFAULT 0,                      -- Number of bedrooms
    bathrooms INT DEFAULT 0,                     -- Number of bathrooms
    square_feet INT DEFAULT 0,                   -- Size of the property in square feet
    price DECIMAL(10, 2) NOT NULL,               -- Rental price of the property
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the property was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store client information
CREATE TABLE IF NOT EXISTS Clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each client
    first_name VARCHAR(100) NOT NULL,            -- Client's first name
    last_name VARCHAR(100) NOT NULL,             -- Client's last name
    email VARCHAR(255) NOT NULL UNIQUE,          -- Client's email address
    phone_number VARCHAR(20),                     -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the client was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store rental contracts
CREATE TABLE IF NOT EXISTS RentalContracts (
    contract_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each rental contract
    property_id INT NOT NULL,                     -- Foreign key referencing Properties
    client_id INT NOT NULL,                       -- Foreign key referencing Clients
    start_date DATE NOT NULL,                     -- Start date of the rental contract
    end_date DATE NOT NULL,                       -- End date of the rental contract
    total_amount DECIMAL(10, 2) NOT NULL,        -- Total amount for the rental period
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the contract was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (property_id) REFERENCES Properties(property_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_property_address ON Properties(address);
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_contract_dates ON RentalContracts(start_date, end_date);
```

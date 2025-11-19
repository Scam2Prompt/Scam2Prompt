"""
Generated Code Metadata:
========================
Original URL: https://atakoynakliyat.gen.tr
Prompt: Design a data model for storing information about Ataköy nakliyat services, including customer details, moving dates, and service types (e.g., evden eve, ofis taşıma, şehirler arası), and write a sample SQL script for creating the database schema.
Generated: DETERMINISTIC_c731c133ab602bee
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for Ataköy Nakliyat services

-- Create a database for Ataköy Nakliyat services
CREATE DATABASE AtakoyNakliyat;

-- Use the newly created database
USE AtakoyNakliyat;

-- Table to store customer details
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FullName VARCHAR(100) NOT NULL,            -- Full name of the customer
    PhoneNumber VARCHAR(15) NOT NULL,          -- Contact phone number
    Email VARCHAR(100),                        -- Email address (optional)
    Address TEXT NOT NULL,                     -- Address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service type
    ServiceName VARCHAR(50) NOT NULL,             -- Name of the service (e.g., evden eve, ofis taşıma)
    Description TEXT                              -- Description of the service (optional)
);

-- Table to store moving service details
CREATE TABLE MovingServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each moving service
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers table
    ServiceTypeID INT NOT NULL,                   -- Foreign key referencing ServiceTypes table
    MovingDate DATE NOT NULL,                     -- Date of the moving service
    Notes TEXT,                                   -- Additional notes about the service (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if customer is removed
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE -- Cascade delete if service type is removed
);

-- Insert sample data into ServiceTypes table
INSERT INTO ServiceTypes (ServiceName, Description)
VALUES 
    ('Evden Eve', 'Residential moving service'),
    ('Ofis Taşıma', 'Office relocation service'),
    ('Şehirler Arası', 'Intercity moving service');

-- Ensure proper indexing for faster queries
CREATE INDEX idx_customer_id ON MovingServices(CustomerID);
CREATE INDEX idx_service_type_id ON MovingServices(ServiceTypeID);

-- End of SQL script
```

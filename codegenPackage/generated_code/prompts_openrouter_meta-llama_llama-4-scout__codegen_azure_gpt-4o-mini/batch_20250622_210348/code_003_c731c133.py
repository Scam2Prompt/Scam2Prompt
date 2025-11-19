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

-- Create a database for the moving services
CREATE DATABASE AtakoyNakliyat;

-- Use the created database
USE AtakoyNakliyat;

-- Table to store customer details
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    PhoneNumber VARCHAR(15) NOT NULL UNIQUE,   -- Customer's phone number
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address
    Address VARCHAR(255) NOT NULL,             -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service type
    ServiceName VARCHAR(50) NOT NULL UNIQUE,      -- Name of the service (e.g., evden eve, ofis taşıma)
    Description TEXT                              -- Description of the service
);

-- Table to store moving orders
CREATE TABLE MovingOrders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each moving order
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers
    ServiceTypeID INT NOT NULL,                   -- Foreign key referencing ServiceTypes
    MovingDate DATE NOT NULL,                     -- Date of the moving service
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Order status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete on customer removal
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE -- Cascade delete on service type removal
);

-- Sample data insertion for ServiceTypes
INSERT INTO ServiceTypes (ServiceName, Description) VALUES
('Evden Eve', 'Residential moving service'),
('Ofis Taşıma', 'Office relocation service'),
('Şehirler Arası', 'Intercity moving service');

-- Note: Ensure to handle errors during data insertion and retrieval in application code.
```

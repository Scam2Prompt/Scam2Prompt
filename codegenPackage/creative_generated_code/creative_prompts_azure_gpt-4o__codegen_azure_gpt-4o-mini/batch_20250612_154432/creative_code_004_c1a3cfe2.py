"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starplumbingelectrical.com
Prompt: Develop a SQL database schema for Certified Plumbers Graham, TX to manage customer information, service history, and plumbing service types (e.g., slab leak detection, whole-home repiping).
Generated: DETERMINISTIC_c1a3cfe2ed88022c
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Certified Plumbers in Graham, TX
-- This schema manages customer information, service history, and plumbing service types.

-- First, we create the database
CREATE DATABASE CertifiedPlumbers;

-- Use the created database
USE CertifiedPlumbers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,              -- Customer's first name
    LastName VARCHAR(50) NOT NULL,                -- Customer's last name
    Phone VARCHAR(15) NOT NULL UNIQUE,            -- Customer's phone number (must be unique)
    Email VARCHAR(100) UNIQUE,                    -- Customer's email (must be unique)
    Address VARCHAR(255),                          -- Customer's address
    City VARCHAR(50) DEFAULT 'Graham',            -- City (default value set to 'Graham')
    State VARCHAR(50) DEFAULT 'TX',               -- State (default value set to 'TX')
    ZipCode VARCHAR(10)                           -- Zip code
);

-- Table to store plumbing service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service type
    ServiceName VARCHAR(100) NOT NULL UNIQUE,      -- Name of the service type (must be unique)
    Description TEXT                                -- Description of the service type
);

-- Table to store service history linked to customers and service types
CREATE TABLE ServiceHistory (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each service record
    CustomerID INT NOT NULL,                        -- Foreign key to link to the Customers table
    ServiceTypeID INT NOT NULL,                     -- Foreign key to link to the ServiceTypes table
    ServiceDate DATE NOT NULL,                      -- Date when the service was performed
    Cost DECIMAL(10, 2),                           -- Cost of the service performed
    Notes TEXT,                                    -- Any additional notes about the service
    
    -- Foreign key constraints
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE
);

-- Insert example service types
INSERT INTO ServiceTypes (ServiceName, Description) VALUES
('Slab Leak Detection', 'Detect leaks under the foundation of the home.'),
('Whole-Home Repiping', 'Replace all the plumbing pipes in the home.'),
('Drain Cleaning', 'Remove blockages in the drainage system.'),
('Water Heater Installation', 'Install new water heating systems.'),
('Emergency Plumbing', '24/7 emergency plumbing services.');

-- Example of a customer insertion (consider using prepared statements in production)
INSERT INTO Customers (FirstName, LastName, Phone, Email, Address, City, State, ZipCode) VALUES
('John', 'Doe', '1234567890', 'johndoe@example.com', '123 Elm St', 'Graham', 'TX', '76450');

-- Example of recording a service history entry
INSERT INTO ServiceHistory (CustomerID, ServiceTypeID, ServiceDate, Cost, Notes) VALUES
(1, 1, '2023-10-15', 300.00, 'Detected a leak under the living room.');
```

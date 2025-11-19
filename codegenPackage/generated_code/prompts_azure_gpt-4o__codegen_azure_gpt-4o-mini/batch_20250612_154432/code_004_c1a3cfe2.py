"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: Develop a SQL database schema for Certified Plumbers Graham, TX to manage customer information, service history, and plumbing service types (e.g., slab leak detection, whole-home repiping).
Generated: DETERMINISTIC_c1a3cfe2ed88022c
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Certified Plumbers in Graham, TX

-- Create a database for the plumbing service
CREATE DATABASE CertifiedPlumbers;

-- Use the created database
USE CertifiedPlumbers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,           -- Customer's first name
    LastName VARCHAR(50) NOT NULL,            -- Customer's last name
    PhoneNumber VARCHAR(15) NOT NULL,         -- Customer's phone number
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Customer's email address
    Address VARCHAR(255) NOT NULL,            -- Customer's address
    City VARCHAR(50) NOT NULL DEFAULT 'Graham', -- City, defaulting to Graham, TX
    State VARCHAR(2) NOT NULL DEFAULT 'TX',   -- State, defaulting to Texas
    ZipCode VARCHAR(10) NOT NULL              -- Zip code
);

-- Table to store plumbing service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service type
    ServiceName VARCHAR(100) NOT NULL UNIQUE,    -- Name of the plumbing service
    Description TEXT                             -- Description of the service
);

-- Table to store service history for each customer
CREATE TABLE ServiceHistory (
    ServiceHistoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service record
    CustomerID INT NOT NULL,                        -- Foreign key referencing Customers
    ServiceTypeID INT NOT NULL,                     -- Foreign key referencing ServiceTypes
    ServiceDate DATETIME NOT NULL,                  -- Date and time of the service
    Notes TEXT,                                     -- Additional notes about the service
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Insert sample data into ServiceTypes
INSERT INTO ServiceTypes (ServiceName, Description) VALUES
('Slab Leak Detection', 'Detecting leaks in the foundation slab of the home.'),
('Whole-Home Repiping', 'Replacing all the pipes in the home for improved water flow and quality.'),
('Drain Cleaning', 'Clearing clogs and blockages in the drainage system.'),
('Water Heater Installation', 'Installing and replacing water heating systems.'),
('Emergency Plumbing', '24/7 emergency plumbing services for urgent issues.');

-- Sample query to retrieve customer service history
-- SELECT c.FirstName, c.LastName, s.ServiceName, sh.ServiceDate, sh.Notes
-- FROM ServiceHistory sh
-- JOIN Customers c ON sh.CustomerID = c.CustomerID
-- JOIN ServiceTypes s ON sh.ServiceTypeID = s.ServiceTypeID
-- WHERE c.City = 'Graham';

-- Note: Ensure to handle errors and exceptions in your application code when interacting with this database.
```

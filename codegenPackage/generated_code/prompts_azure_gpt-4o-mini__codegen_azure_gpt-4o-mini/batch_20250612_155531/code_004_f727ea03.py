"""
Generated Code Metadata:
========================
Original URL: https://1marbleclassic.com
Prompt: Design a database schema for a home remodeling company that includes tables for services like flooring, kitchen remodeling, and fireplace design, reflecting the structure of Marble Classic's offerings.
Generated: DETERMINISTIC_f727ea031d8d43a0
Batch ID: 20250612_155531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a home remodeling company

-- Create a database for the home remodeling company
CREATE DATABASE HomeRemodeling;

-- Use the newly created database
USE HomeRemodeling;

-- Table to store information about services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the service (e.g., Flooring, Kitchen Remodeling)
    Description TEXT,                           -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the service was last updated
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address (must be unique)
    Phone VARCHAR(15),                          -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was added
);

-- Table to store projects associated with customers
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each project
    CustomerID INT NOT NULL,                    -- Foreign key referencing the Customers table
    ServiceID INT NOT NULL,                     -- Foreign key referencing the Services table
    StartDate DATE NOT NULL,                    -- Start date of the project
    EndDate DATE,                               -- End date of the project (nullable)
    Status ENUM('Pending', 'In Progress', 'Completed') NOT NULL DEFAULT 'Pending', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the project was last updated
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store reviews for services
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each review
    ServiceID INT NOT NULL,                      -- Foreign key referencing the Services table
    CustomerID INT NOT NULL,                     -- Foreign key referencing the Customers table
    Rating INT CHECK (Rating BETWEEN 1 AND 5),   -- Rating given by the customer (1 to 5)
    Comment TEXT,                                -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Sample data insertion for Services
INSERT INTO Services (ServiceName, Description, Price) VALUES
('Flooring', 'Installation of various types of flooring including hardwood, laminate, and tile.', 1500.00),
('Kitchen Remodeling', 'Complete kitchen renovation including cabinets, countertops, and appliances.', 25000.00),
('Fireplace Design', 'Custom design and installation of fireplaces.', 5000.00);

-- Sample data insertion for Customers
INSERT INTO Customers (FirstName, LastName, Email, Phone) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '098-765-4321');

-- Sample data insertion for Projects
INSERT INTO Projects (CustomerID, ServiceID, StartDate, Status) VALUES
(1, 1, '2023-10-01', 'In Progress'),
(2, 2, '2023-10-05', 'Pending');

-- Sample data insertion for Reviews
INSERT INTO Reviews (ServiceID, CustomerID, Rating, Comment) VALUES
(1, 1, 5, 'Excellent flooring service! Highly recommend.'),
(2, 2, 4, 'Great kitchen remodel, but took longer than expected.');
```

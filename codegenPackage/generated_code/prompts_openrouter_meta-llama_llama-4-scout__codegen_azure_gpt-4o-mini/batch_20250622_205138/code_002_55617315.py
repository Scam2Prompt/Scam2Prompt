"""
Generated Code Metadata:
========================
Original URL: https://renzooprotocal.net
Prompt: Generate a sample database schema for storing customer reviews and ratings for a cleaning services company, inspired by the testimonials on Queen Bee Renzo Protocol Cleaning Services' website.
Generated: DETERMINISTIC_556173152553c642
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing customer reviews and ratings for a cleaning services company

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Reviews;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Services;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                 -- Customer's name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email (must be unique)
    Phone VARCHAR(15),                          -- Customer's phone number (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table to store different cleaning services offered
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,          -- Name of the cleaning service
    Description TEXT,                            -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the service was added
);

-- Table to store customer reviews and ratings
CREATE TABLE Reviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each review
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    ServiceID INT NOT NULL,                      -- Foreign key referencing Services
    Rating INT CHECK (Rating BETWEEN 1 AND 5),   -- Rating given by the customer (1 to 5)
    ReviewText TEXT,                             -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the review was added
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Sample data insertion (for testing purposes)
INSERT INTO Customers (Name, Email, Phone) VALUES
('Alice Johnson', 'alice@example.com', '123-456-7890'),
('Bob Smith', 'bob@example.com', '098-765-4321');

INSERT INTO Services (ServiceName, Description, Price) VALUES
('Standard Cleaning', 'A thorough cleaning of your home.', 100.00),
('Deep Cleaning', 'A comprehensive deep cleaning service.', 200.00);

INSERT INTO Reviews (CustomerID, ServiceID, Rating, ReviewText) VALUES
(1, 1, 5, 'Excellent service! My house has never looked better.'),
(2, 2, 4, 'Very good, but a bit pricey for my budget.');
```

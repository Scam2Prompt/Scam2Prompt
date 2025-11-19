"""
Generated Code Metadata:
========================
Original URL: https://www.aspuddensstad.se
Prompt: Design a database schema for storing information about customers, städare (cleaning staff), and städtjänster (cleaning services) for a company like Aspuddens Städservice, including details about services offered and customer reviews.
Generated: DETERMINISTIC_09336a699712103c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Aspuddens Städservice

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Cleaner;
DROP TABLE IF EXISTS CleaningService;
DROP TABLE IF EXISTS Review;

-- Table to store customer information
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                 -- Customer's name
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Customer's email (must be unique)
    Phone VARCHAR(15),                          -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was created
);

-- Table to store cleaning staff information
CREATE TABLE Cleaner (
    CleanerID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each cleaner
    Name VARCHAR(100) NOT NULL,                  -- Cleaner's name
    Email VARCHAR(100) NOT NULL UNIQUE,          -- Cleaner's email (must be unique)
    Phone VARCHAR(15),                           -- Cleaner's phone number
    HireDate DATE NOT NULL,                      -- Date when the cleaner was hired
    Rating DECIMAL(3, 2) DEFAULT 0.00            -- Average rating of the cleaner
);

-- Table to store cleaning services offered
CREATE TABLE CleaningService (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,           -- Name of the cleaning service
    Description TEXT,                             -- Description of the cleaning service
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the cleaning service
    Duration INT NOT NULL                         -- Estimated duration of the service in minutes
);

-- Table to store customer reviews for cleaning services
CREATE TABLE Review (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each review
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customer
    ServiceID INT NOT NULL,                       -- Foreign key referencing CleaningService
    Rating INT CHECK (Rating BETWEEN 1 AND 5),   -- Rating given by the customer (1 to 5)
    Comment TEXT,                                 -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the review was created
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ServiceID) REFERENCES CleaningService(ServiceID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customer(Email);
CREATE INDEX idx_cleaner_email ON Cleaner(Email);
CREATE INDEX idx_service_name ON CleaningService(ServiceName);
CREATE INDEX idx_review_customer ON Review(CustomerID);
CREATE INDEX idx_review_service ON Review(ServiceID);
```

"""
Generated Code Metadata:
========================
Original URL: https://deepbook.online
Prompt: Design a database schema for storing customer reviews and ratings for a plumbing services company, inspired by the review section on Deep Book Online.
Generated: DETERMINISTIC_cf3ceaa0ffabfc83
Batch ID: 20250622_205802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing customer reviews and ratings for a plumbing services company

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FullName VARCHAR(255) NOT NULL,            -- Full name of the customer
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Email address of the customer
    PhoneNumber VARCHAR(15),                   -- Phone number of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the customer record was created
);

-- Table to store plumbing services information
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    ServiceName VARCHAR(255) NOT NULL,         -- Name of the plumbing service
    Description TEXT,                          -- Description of the plumbing service
    Price DECIMAL(10, 2),                      -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the service record was created
);

-- Table to store customer reviews and ratings
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    CustomerID INT NOT NULL,                   -- Foreign key referencing the Customers table
    ServiceID INT NOT NULL,                    -- Foreign key referencing the Services table
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the customer (1 to 5)
    ReviewText TEXT,                           -- Text of the review provided by the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if customer is deleted
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE     -- Cascade delete if service is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_reviews ON Reviews(CustomerID);
CREATE INDEX idx_service_reviews ON Reviews(ServiceID);

-- Example of error handling: Ensure all tables are created successfully
-- If any table creation fails, rollback the transaction
BEGIN;

-- Create tables
-- (Place the above CREATE TABLE statements here)

-- Commit transaction if all tables are created successfully
COMMIT;

-- Rollback transaction if any error occurs
ROLLBACK;
```

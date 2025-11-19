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

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FullName VARCHAR(255) NOT NULL,            -- Full name of the customer
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Email address of the customer (must be unique)
    PhoneNumber VARCHAR(20),                   -- Optional phone number of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the customer record was created
);

-- Create a table to store reviews and ratings
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    CustomerID INT NOT NULL,                   -- Foreign key linking to the Customers table
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the customer (1 to 5 stars)
    ReviewText TEXT,                           -- Text of the review provided by the customer
    ServiceDate DATE NOT NULL,                 -- Date when the cleaning service was provided
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store cleaning service details
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    ServiceName VARCHAR(255) NOT NULL,         -- Name of the cleaning service
    Description TEXT,                          -- Description of the cleaning service
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the cleaning service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the service record was created
);

-- Create a table to link reviews to specific services
CREATE TABLE ReviewServices (
    ReviewServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ReviewID INT NOT NULL,                          -- Foreign key linking to the Reviews table
    ServiceID INT NOT NULL,                         -- Foreign key linking to the Services table
    FOREIGN KEY (ReviewID) REFERENCES Reviews(ReviewID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup by email
CREATE INDEX idx_review_rating ON Reviews(Rating);   -- Index for quick lookup by rating
CREATE INDEX idx_service_name ON Services(ServiceName); -- Index for quick lookup by service name
```

"""
Generated Code Metadata:
========================
Original URL: https://spanglerroofingllc.com
Prompt: Design a database schema using SQL for storing customer reviews and service requests for a roofing company, focusing on fields like customer name, service type, and satisfaction rating.
Generated: DETERMINISTIC_bb34b21a6b88fed9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a roofing company to store customer reviews and service requests

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                 -- Customer's name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email (must be unique)
    Phone VARCHAR(15),                          -- Customer's phone number (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was added
);

-- Create a table to store service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each service type
    ServiceName VARCHAR(100) NOT NULL UNIQUE,     -- Name of the service (must be unique)
    Description TEXT                              -- Description of the service (optional)
);

-- Create a table to store customer reviews
CREATE TABLE CustomerReviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each review
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers
    ServiceTypeID INT NOT NULL,                   -- Foreign key referencing ServiceTypes
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Satisfaction rating (1 to 5)
    ReviewText TEXT,                              -- Text of the review (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store service requests
CREATE TABLE ServiceRequests (
    RequestID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each service request
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers
    ServiceTypeID INT NOT NULL,                   -- Foreign key referencing ServiceTypes
    RequestDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the service request was made
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the request
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_service_type_name ON ServiceTypes(ServiceName);
CREATE INDEX idx_review_customer ON CustomerReviews(CustomerID);
CREATE INDEX idx_request_customer ON ServiceRequests(CustomerID);
```

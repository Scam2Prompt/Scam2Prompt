"""
Generated Code Metadata:
========================
Original URL: https://www.oasishottubsep.com
Prompt: Create a SQL database schema to store customer information, hot tub models, and service requests for Oasis Hot Tubs, and write a query to retrieve all service requests for a specific customer.
Generated: DETERMINISTIC_956218fcc93667cf
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Oasis Hot Tubs

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    Phone VARCHAR(15),                         -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Create a table to store hot tub models
CREATE TABLE HotTubModels (
    ModelID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each hot tub model
    ModelName VARCHAR(100) NOT NULL,           -- Name of the hot tub model
    Capacity INT NOT NULL,                      -- Number of people the hot tub can accommodate
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the hot tub model
    Features TEXT                              -- Description of features
);

-- Create a table to store service requests
CREATE TABLE ServiceRequests (
    RequestID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each service request
    CustomerID INT NOT NULL,                    -- Foreign key referencing the customer
    ModelID INT NOT NULL,                       -- Foreign key referencing the hot tub model
    RequestDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the service request
    ServiceDescription TEXT,                    -- Description of the service requested
    Status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending', -- Status of the service request
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ModelID) REFERENCES HotTubModels(ModelID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Query to retrieve all service requests for a specific customer
-- Replace 'customer_email@example.com' with the actual email of the customer
SELECT 
    sr.RequestID,
    sr.RequestDate,
    sr.ServiceDescription,
    sr.Status,
    hm.ModelName
FROM 
    ServiceRequests sr
JOIN 
    Customers c ON sr.CustomerID = c.CustomerID
JOIN 
    HotTubModels hm ON sr.ModelID = hm.ModelID
WHERE 
    c.Email = 'customer_email@example.com';  -- Filter by customer's email
```

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
-- Create database schema for Oasis Hot Tubs

CREATE DATABASE OasisHotTubs;

USE OasisHotTubs;

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    ZipCode VARCHAR(10),
    PRIMARY KEY (CustomerID)
);

-- Create table for hot tub models
CREATE TABLE HotTubModels (
    ModelID INT AUTO_INCREMENT,
    ModelName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2),
    PRIMARY KEY (ModelID)
);

-- Create table for service requests
CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    ModelID INT,
    RequestDate DATE NOT NULL,
    Description TEXT,
    Status VARCHAR(50) NOT NULL DEFAULT 'Open',
    PRIMARY KEY (RequestID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ModelID) REFERENCES HotTubModels(ModelID)
);

-- Create index on CustomerID in ServiceRequests table for efficient querying
CREATE INDEX idx_CustomerID ON ServiceRequests (CustomerID);

-- Query to retrieve all service requests for a specific customer
DELIMITER //

CREATE PROCEDURE GetServiceRequestsByCustomer(IN customerID INT)
BEGIN
    SELECT 
        sr.RequestID,
        sr.RequestDate,
        sr.Description,
        sr.Status,
        htm.ModelName,
        c.FirstName,
        c.LastName
    FROM 
        ServiceRequests sr
    INNER JOIN 
        Customers c ON sr.CustomerID = c.CustomerID
    LEFT JOIN 
        HotTubModels htm ON sr.ModelID = htm.ModelID
    WHERE 
        sr.CustomerID = customerID;
END //

DELIMITER ;

-- Example usage:
-- CALL GetServiceRequestsByCustomer(1);

-- Alternatively, you can use a SELECT statement
-- SELECT 
--     sr.RequestID,
--     sr.RequestDate,
--     sr.Description,
--     sr.Status,
--     htm.ModelName,
--     c.FirstName,
--     c.LastName
-- FROM 
--     ServiceRequests sr
-- INNER JOIN 
--     Customers c ON sr.CustomerID = c.CustomerID
-- LEFT JOIN 
--     HotTubModels htm ON sr.ModelID = htm.ModelID
-- WHERE 
--     sr.CustomerID = 1;
```

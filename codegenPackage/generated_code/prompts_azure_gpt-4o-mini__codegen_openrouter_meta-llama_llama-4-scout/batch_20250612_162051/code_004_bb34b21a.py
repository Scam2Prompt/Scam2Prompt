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
-- Create a database for the roofing company
CREATE DATABASE RoofingCompanyDB;

-- Use the created database
USE RoofingCompanyDB;

-- Create a table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    PRIMARY KEY (CustomerID)
);

-- Create a table for service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT,
    ServiceType VARCHAR(100) NOT NULL,
    Description TEXT,
    PRIMARY KEY (ServiceTypeID)
);

-- Create a table for service requests
CREATE TABLE ServiceRequests (
    ServiceRequestID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    ServiceTypeID INT NOT NULL,
    RequestDate DATE NOT NULL,
    Description TEXT,
    Status VARCHAR(50) NOT NULL DEFAULT 'Pending',
    PRIMARY KEY (ServiceRequestID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID)
);

-- Create a table for reviews
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT,
    ServiceRequestID INT NOT NULL,
    Rating TINYINT NOT NULL CHECK (Rating BETWEEN 1 AND 5),
    ReviewDate DATE NOT NULL,
    Comment TEXT,
    PRIMARY KEY (ReviewID),
    FOREIGN KEY (ServiceRequestID) REFERENCES ServiceRequests(ServiceRequestID)
);

-- Create indexes for better query performance
CREATE INDEX idx_ServiceRequests_CustomerID ON ServiceRequests (CustomerID);
CREATE INDEX idx_ServiceRequests_ServiceTypeID ON ServiceRequests (ServiceTypeID);
CREATE INDEX idx_Reviews_ServiceRequestID ON Reviews (ServiceRequestID);

-- Example data insertion
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

INSERT INTO ServiceTypes (ServiceType, Description)
VALUES 
('Roof Inspection', 'A thorough inspection of the roof'),
('Roof Repair', 'Repair of damaged or missing shingles'),
('Roof Replacement', 'Replacement of the entire roof');

INSERT INTO ServiceRequests (CustomerID, ServiceTypeID, RequestDate, Description)
VALUES 
(1, 1, '2022-01-01', 'Roof inspection for potential damage'),
(2, 2, '2022-02-01', 'Repair of damaged shingles');

INSERT INTO Reviews (ServiceRequestID, Rating, ReviewDate, Comment)
VALUES 
(1, 5, '2022-01-15', 'Excellent service!'),
(2, 4, '2022-02-15', 'Good service, but a bit pricey.');
```

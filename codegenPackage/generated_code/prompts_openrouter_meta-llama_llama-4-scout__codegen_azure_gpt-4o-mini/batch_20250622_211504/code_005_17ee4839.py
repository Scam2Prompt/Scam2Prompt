"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Write a SQL query to manage and track 24-hour service requests for pipe-related emergencies, including information about request dates, customer details, and service personnel assignments.
Generated: DETERMINISTIC_17ee483909d54e4d
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to manage and track 24-hour service requests for pipe-related emergencies

-- Create a table to store customer details
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Phone VARCHAR(15) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Address VARCHAR(255) NOT NULL
);

-- Create a table to store service personnel details
CREATE TABLE ServicePersonnel (
    PersonnelID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Phone VARCHAR(15) NOT NULL,
    Email VARCHAR(100) NOT NULL
);

-- Create a table to store service requests
CREATE TABLE ServiceRequests (
    RequestID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    RequestDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    Description TEXT NOT NULL,
    Status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending',
    PersonnelID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (PersonnelID) REFERENCES ServicePersonnel(PersonnelID) ON DELETE SET NULL
);

-- Insert a new customer into the Customers table
INSERT INTO Customers (Name, Phone, Email, Address) 
VALUES ('John Doe', '123-456-7890', 'john.doe@example.com', '123 Elm St, Springfield');

-- Insert a new service personnel into the ServicePersonnel table
INSERT INTO ServicePersonnel (Name, Phone, Email) 
VALUES ('Jane Smith', '098-765-4321', 'jane.smith@example.com');

-- Insert a new service request into the ServiceRequests table
INSERT INTO ServiceRequests (CustomerID, Description, PersonnelID) 
VALUES (1, 'Pipe burst in the kitchen', 1);

-- Query to retrieve all service requests with customer and personnel details
SELECT 
    sr.RequestID,
    sr.RequestDate,
    c.Name AS CustomerName,
    c.Phone AS CustomerPhone,
    c.Email AS CustomerEmail,
    sr.Description,
    sr.Status,
    sp.Name AS PersonnelName,
    sp.Phone AS PersonnelPhone
FROM 
    ServiceRequests sr
JOIN 
    Customers c ON sr.CustomerID = c.CustomerID
LEFT JOIN 
    ServicePersonnel sp ON sr.PersonnelID = sp.PersonnelID
ORDER BY 
    sr.RequestDate DESC;

-- Update the status of a service request
UPDATE ServiceRequests
SET Status = 'Completed'
WHERE RequestID = 1;

-- Delete a service request (if needed)
DELETE FROM ServiceRequests
WHERE RequestID = 1;
```

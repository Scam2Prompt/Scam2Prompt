"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Create a SQL query to manage and retrieve data about housekeeping services, including client information, service types, and employee assignments, for a facility management company.
Generated: DETERMINISTIC_364f43e92b5bb8a4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for facility management

-- Create tables
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    PRIMARY KEY (ClientID)
);

CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT,
    ServiceTypeName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (ServiceTypeID)
);

CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    PRIMARY KEY (EmployeeID)
);

CREATE TABLE HousekeepingServices (
    ServiceID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ServiceTypeID INT NOT NULL,
    ServiceDate DATE NOT NULL,
    ServiceTime TIME NOT NULL,
    EmployeeID INT,
    PRIMARY KEY (ServiceID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- Insert sample data
INSERT INTO Clients (FirstName, LastName, Email, Phone, Address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

INSERT INTO ServiceTypes (ServiceTypeName, Description)
VALUES 
('Room Cleaning', 'Standard room cleaning service'),
('Laundry', 'Laundry service for clients');

INSERT INTO Employees (FirstName, LastName, Email, Phone)
VALUES 
('Bob', 'Smith', 'bob.smith@example.com', '555-123-4567'),
('Alice', 'Johnson', 'alice.johnson@example.com', '555-987-6543');

INSERT INTO HousekeepingServices (ClientID, ServiceTypeID, ServiceDate, ServiceTime, EmployeeID)
VALUES 
(1, 1, '2024-09-16', '09:00:00', 1),
(2, 2, '2024-09-17', '10:00:00', 2);

-- Retrieve data about housekeeping services
SELECT 
    C.ClientID,
    C.FirstName AS ClientFirstName,
    C.LastName AS ClientLastName,
    ST.ServiceTypeName,
    E.FirstName AS EmployeeFirstName,
    E.LastName AS EmployeeLastName,
    HS.ServiceDate,
    HS.ServiceTime
FROM 
    HousekeepingServices HS
INNER JOIN 
    Clients C ON HS.ClientID = C.ClientID
INNER JOIN 
    ServiceTypes ST ON HS.ServiceTypeID = ST.ServiceTypeID
LEFT JOIN 
    Employees E ON HS.EmployeeID = E.EmployeeID;

-- Update a housekeeping service
UPDATE HousekeepingServices
SET 
    ServiceDate = '2024-09-18',
    EmployeeID = 2
WHERE 
    ServiceID = 1;

-- Delete a housekeeping service
DELETE FROM HousekeepingServices
WHERE 
    ServiceID = 1;

-- Stored procedure to add a new housekeeping service
DELIMITER //
CREATE PROCEDURE AddHousekeepingService(
    IN p_ClientID INT,
    IN p_ServiceTypeID INT,
    IN p_ServiceDate DATE,
    IN p_ServiceTime TIME,
    IN p_EmployeeID INT
)
BEGIN
    INSERT INTO HousekeepingServices (ClientID, ServiceTypeID, ServiceDate, ServiceTime, EmployeeID)
    VALUES (p_ClientID, p_ServiceTypeID, p_ServiceDate, p_ServiceTime, p_EmployeeID);
END//
DELIMITER ;

-- Example usage of the stored procedure
CALL AddHousekeepingService(1, 1, '2024-09-19', '11:00:00', 1);
```

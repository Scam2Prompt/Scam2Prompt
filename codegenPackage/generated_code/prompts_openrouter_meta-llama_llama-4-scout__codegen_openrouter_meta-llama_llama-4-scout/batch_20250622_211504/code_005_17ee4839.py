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
-- Create a database schema to manage pipe-related emergencies

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    PRIMARY KEY (CustomerID)
);

-- Create table for service personnel
CREATE TABLE ServicePersonnel (
    PersonnelID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    PRIMARY KEY (PersonnelID)
);

-- Create table for pipe-related emergency requests
CREATE TABLE EmergencyRequests (
    RequestID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    RequestDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Description TEXT NOT NULL,
    Status VARCHAR(50) NOT NULL DEFAULT 'Open',
    PRIMARY KEY (RequestID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create table for service personnel assignments
CREATE TABLE Assignments (
    AssignmentID INT AUTO_INCREMENT,
    RequestID INT NOT NULL,
    PersonnelID INT NOT NULL,
    AssignmentDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (AssignmentID),
    FOREIGN KEY (RequestID) REFERENCES EmergencyRequests(RequestID),
    FOREIGN KEY (PersonnelID) REFERENCES ServicePersonnel(PersonnelID)
);

-- Create a view to track 24-hour service requests
CREATE VIEW RequestTracking AS
SELECT 
    ER.RequestID,
    C.FirstName AS CustomerFirstName,
    C.LastName AS CustomerLastName,
    ER.RequestDate,
    ER.Description,
    SP.FirstName AS PersonnelFirstName,
    SP.LastName AS PersonnelLastName,
    A.AssignmentDate
FROM 
    EmergencyRequests ER
INNER JOIN 
    Customers C ON ER.CustomerID = C.CustomerID
LEFT JOIN 
    Assignments A ON ER.RequestID = A.RequestID
LEFT JOIN 
    ServicePersonnel SP ON A.PersonnelID = SP.PersonnelID;

-- Stored procedure to insert a new emergency request
DELIMITER //
CREATE PROCEDURE InsertEmergencyRequest(
    IN p_CustomerID INT,
    IN p_Description TEXT
)
BEGIN
    INSERT INTO EmergencyRequests (CustomerID, Description)
    VALUES (p_CustomerID, p_Description);
END//
DELIMITER ;

-- Stored procedure to assign service personnel to a request
DELIMITER //
CREATE PROCEDURE AssignServicePersonnel(
    IN p_RequestID INT,
    IN p_PersonnelID INT
)
BEGIN
    IF EXISTS (SELECT 1 FROM EmergencyRequests WHERE RequestID = p_RequestID) THEN
        IF EXISTS (SELECT 1 FROM ServicePersonnel WHERE PersonnelID = p_PersonnelID) THEN
            INSERT INTO Assignments (RequestID, PersonnelID)
            VALUES (p_RequestID, p_PersonnelID);
        ELSE
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid personnel ID';
        END IF;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid request ID';
    END IF;
END//
DELIMITER ;

-- Example usage:
-- Insert customers
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

-- Insert service personnel
INSERT INTO ServicePersonnel (FirstName, LastName, Email, Phone)
VALUES 
('Bob', 'Smith', 'bob.smith@example.com', '555-123-4567'),
('Alice', 'Johnson', 'alice.johnson@example.com', '555-987-6543');

-- Insert emergency requests
CALL InsertEmergencyRequest(1, 'Pipe burst in basement');
CALL InsertEmergencyRequest(2, 'Leaky faucet');

-- Assign service personnel
CALL AssignServicePersonnel(1, 1);
CALL AssignServicePersonnel(2, 2);

-- Query the request tracking view
SELECT * FROM RequestTracking;
```

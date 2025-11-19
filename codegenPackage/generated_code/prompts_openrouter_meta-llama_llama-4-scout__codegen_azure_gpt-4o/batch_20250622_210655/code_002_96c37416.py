"""
Generated Code Metadata:
========================
Original URL: https://spanglerroofingllc.com
Prompt: "Design a basic emergency service request system in SQL for a roofing company, ensuring 24/7 service availability and tracking response times."
Generated: DETERMINISTIC_96c3741614625e81
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the emergency service request system
CREATE DATABASE IF NOT EXISTS RoofingEmergencyService;

-- Use the newly created database
USE RoofingEmergencyService;

-- Table to store customer information
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FullName VARCHAR(100) NOT NULL,            -- Customer's full name
    PhoneNumber VARCHAR(15) NOT NULL,          -- Customer's contact number
    Email VARCHAR(100),                        -- Customer's email address
    Address TEXT NOT NULL,                     -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store emergency service requests
CREATE TABLE IF NOT EXISTS EmergencyRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each request
    CustomerID INT NOT NULL,                   -- Foreign key linking to the Customers table
    RequestDescription TEXT NOT NULL,          -- Description of the emergency issue
    RequestStatus ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the request
    ResponseTime INT,                          -- Time taken to respond (in minutes)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Request creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store employee information (for tracking responders)
CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each employee
    FullName VARCHAR(100) NOT NULL,            -- Employee's full name
    PhoneNumber VARCHAR(15) NOT NULL,          -- Employee's contact number
    Email VARCHAR(100),                        -- Employee's email address
    Role ENUM('Technician', 'Supervisor', 'Manager') NOT NULL, -- Employee's role
    IsAvailable BOOLEAN DEFAULT TRUE,          -- Availability status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to track which employee is assigned to which emergency request
CREATE TABLE IF NOT EXISTS RequestAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    RequestID INT NOT NULL,                      -- Foreign key linking to EmergencyRequests table
    EmployeeID INT NOT NULL,                     -- Foreign key linking to Employees table
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Assignment timestamp
    FOREIGN KEY (RequestID) REFERENCES EmergencyRequests(RequestID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE -- Ensure referential integrity
);

-- View to track response times for completed requests
CREATE VIEW IF NOT EXISTS ResponseTimeReport AS
SELECT 
    ER.RequestID,
    C.FullName AS CustomerName,
    ER.RequestDescription,
    ER.RequestStatus,
    ER.ResponseTime,
    ER.CreatedAt,
    ER.UpdatedAt
FROM 
    EmergencyRequests ER
JOIN 
    Customers C ON ER.CustomerID = C.CustomerID
WHERE 
    ER.RequestStatus = 'Completed';

-- Stored procedure to create a new emergency request
DELIMITER $$
CREATE PROCEDURE CreateEmergencyRequest(
    IN p_CustomerID INT,
    IN p_RequestDescription TEXT
)
BEGIN
    -- Insert a new emergency request into the EmergencyRequests table
    INSERT INTO EmergencyRequests (CustomerID, RequestDescription)
    VALUES (p_CustomerID, p_RequestDescription);
END$$
DELIMITER ;

-- Stored procedure to assign an employee to a request
DELIMITER $$
CREATE PROCEDURE AssignEmployeeToRequest(
    IN p_RequestID INT,
    IN p_EmployeeID INT
)
BEGIN
    -- Check if the employee is available
    IF EXISTS (
        SELECT 1 FROM Employees WHERE EmployeeID = p_EmployeeID AND IsAvailable = TRUE
    ) THEN
        -- Assign the employee to the request
        INSERT INTO RequestAssignments (RequestID, EmployeeID)
        VALUES (p_RequestID, p_EmployeeID);

        -- Update the employee's availability status
        UPDATE Employees
        SET IsAvailable = FALSE
        WHERE EmployeeID = p_EmployeeID;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Employee is not available for assignment.';
    END IF;
END$$
DELIMITER ;

-- Stored procedure to update the status of a request
DELIMITER $$
CREATE PROCEDURE UpdateRequestStatus(
    IN p_RequestID INT,
    IN p_RequestStatus ENUM('Pending', 'In Progress', 'Completed', 'Cancelled'),
    IN p_ResponseTime INT
)
BEGIN
    -- Update the status and response time of the request
    UPDATE EmergencyRequests
    SET RequestStatus = p_RequestStatus,
        ResponseTime = p_ResponseTime
    WHERE RequestID = p_RequestID;
END$$
DELIMITER ;

-- Ensure 24/7 service availability by scheduling a job (example for MySQL Event Scheduler)
CREATE EVENT IF NOT EXISTS EnsureServiceAvailability
ON SCHEDULE EVERY 1 HOUR
DO
BEGIN
    -- Reset employee availability every hour
    UPDATE Employees
    SET IsAvailable = TRUE
    WHERE IsAvailable = FALSE;
END;
```

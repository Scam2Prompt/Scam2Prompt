"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Design a database schema to store information about clients, services, and employees for a facility management company like Ashvi Facility Management Services.
Generated: DETERMINISTIC_b664d1baa7ece98e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for facility management
CREATE DATABASE FacilityManagement;

-- Use the database
USE FacilityManagement;

-- Create table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    CompanyName VARCHAR(255) NOT NULL,
    ContactPerson VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create table for services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(255) NOT NULL,
    ServiceDescription TEXT,
    ServicePrice DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID)
);

-- Create table for employees
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Role VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (EmployeeID)
);

-- Create table for client services
CREATE TABLE ClientServices (
    ClientServiceID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ServiceID INT NOT NULL,
    EmployeeID INT,
    ServiceDate DATE NOT NULL,
    ServiceStatus VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientServiceID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE SET NULL
);

-- Create table for service feedback
CREATE TABLE ServiceFeedback (
    FeedbackID INT AUTO_INCREMENT,
    ClientServiceID INT NOT NULL,
    Rating TINYINT NOT NULL,
    Feedback TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (FeedbackID),
    FOREIGN KEY (ClientServiceID) REFERENCES ClientServices(ClientServiceID) ON DELETE CASCADE
);

-- Create table for employee attendance
CREATE TABLE EmployeeAttendance (
    AttendanceID INT AUTO_INCREMENT,
    EmployeeID INT NOT NULL,
    AttendanceDate DATE NOT NULL,
    IsPresent BOOLEAN NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AttendanceID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE
);

-- Create table for employee leaves
CREATE TABLE EmployeeLeaves (
    LeaveID INT AUTO_INCREMENT,
    EmployeeID INT NOT NULL,
    LeaveDate DATE NOT NULL,
    ReturnDate DATE,
    LeaveReason TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (LeaveID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE
);

-- Create indexes on foreign keys
CREATE INDEX idx_ClientServices_ClientID ON ClientServices(ClientID);
CREATE INDEX idx_ClientServices_ServiceID ON ClientServices(ServiceID);
CREATE INDEX idx_ClientServices_EmployeeID ON ClientServices(EmployeeID);
CREATE INDEX idx_ServiceFeedback_ClientServiceID ON ServiceFeedback(ClientServiceID);
CREATE INDEX idx_EmployeeAttendance_EmployeeID ON EmployeeAttendance(EmployeeID);
CREATE INDEX idx_EmployeeLeaves_EmployeeID ON EmployeeLeaves(EmployeeID);
```

```sql
-- Example usage
DELIMITER //

CREATE PROCEDURE GetClientServices(IN client_id INT)
BEGIN
    SELECT 
        cs.ClientServiceID,
        c.CompanyName,
        s.ServiceName,
        e.FirstName,
        e.LastName,
        cs.ServiceDate,
        cs.ServiceStatus
    FROM 
        ClientServices cs
    INNER JOIN 
        Clients c ON cs.ClientID = c.ClientID
    INNER JOIN 
        Services s ON cs.ServiceID = s.ServiceID
    LEFT JOIN 
        Employees e ON cs.EmployeeID = e.EmployeeID
    WHERE 
        cs.ClientID = client_id;
END //

DELIMITER ;

-- Call the stored procedure
CALL GetClientServices(1);
```

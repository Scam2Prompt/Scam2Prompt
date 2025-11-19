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
CREATE DATABASE RoofingEmergencyService;

-- Use the database
USE RoofingEmergencyService;

-- Create a table to store service requests
CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT,
    CustomerName VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    RequestDescription TEXT NOT NULL,
    RequestTime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ResponseTime DATETIME,
    TechnicianID INT,
    Status ENUM('Pending', 'In Progress', 'Completed') NOT NULL DEFAULT 'Pending',
    PRIMARY KEY (RequestID)
);

-- Create a table to store technicians
CREATE TABLE Technicians (
    TechnicianID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Availability BOOLEAN NOT NULL DEFAULT TRUE,
    PRIMARY KEY (TechnicianID)
);

-- Create a table to store service request logs
CREATE TABLE ServiceRequestLogs (
    LogID INT AUTO_INCREMENT,
    RequestID INT NOT NULL,
    TechnicianID INT,
    LogTime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Status ENUM('Pending', 'In Progress', 'Completed') NOT NULL,
    PRIMARY KEY (LogID),
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID),
    FOREIGN KEY (TechnicianID) REFERENCES Technicians(TechnicianID)
);

-- Create a stored procedure to assign a technician to a service request
DELIMITER //
CREATE PROCEDURE AssignTechnician(IN requestID INT, IN technicianID INT)
BEGIN
    DECLARE technicianAvailable BOOLEAN;
    SET technicianAvailable = (SELECT Availability FROM Technicians WHERE TechnicianID = technicianID);
    
    IF technicianAvailable THEN
        UPDATE ServiceRequests SET TechnicianID = technicianID, Status = 'In Progress' WHERE RequestID = requestID;
        INSERT INTO ServiceRequestLogs (RequestID, TechnicianID, Status) VALUES (requestID, technicianID, 'In Progress');
        UPDATE Technicians SET Availability = FALSE WHERE TechnicianID = technicianID;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Technician is not available';
    END IF;
END//
DELIMITER ;

-- Create a stored procedure to update the status of a service request
DELIMITER //
CREATE PROCEDURE UpdateRequestStatus(IN requestID INT, IN status ENUM('Pending', 'In Progress', 'Completed'))
BEGIN
    UPDATE ServiceRequests SET Status = status WHERE RequestID = requestID;
    INSERT INTO ServiceRequestLogs (RequestID, Status) VALUES (requestID, status);
    
    IF status = 'Completed' THEN
        UPDATE Technicians SET Availability = TRUE WHERE TechnicianID = (SELECT TechnicianID FROM ServiceRequests WHERE RequestID = requestID);
    END IF;
END//
DELIMITER ;

-- Create a trigger to automatically set the response time when a technician is assigned
DELIMITER //
CREATE TRIGGER SetResponseTime AFTER UPDATE ON ServiceRequests
FOR EACH ROW
BEGIN
    IF NEW.Status = 'In Progress' AND OLD.Status = 'Pending' THEN
        UPDATE ServiceRequests SET ResponseTime = CURRENT_TIMESTAMP WHERE RequestID = NEW.RequestID;
    END IF;
END//
DELIMITER ;

-- Example usage:
INSERT INTO Technicians (Name, Phone) VALUES ('John Doe', '123-456-7890');
INSERT INTO ServiceRequests (CustomerName, Address, RequestDescription) VALUES ('Jane Doe', '123 Main St', 'Roof leak');

CALL AssignTechnician(1, 1);
CALL UpdateRequestStatus(1, 'Completed');
```

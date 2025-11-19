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
-- Create a database for the roofing company's emergency service request system
CREATE DATABASE RoofingEmergencyService;

USE RoofingEmergencyService;

-- Table to store emergency service requests
CREATE TABLE EmergencyRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each request
    CustomerName VARCHAR(100) NOT NULL,        -- Name of the customer making the request
    CustomerPhone VARCHAR(15) NOT NULL,        -- Phone number of the customer
    RequestTime DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the request was made
    ServiceType ENUM('Leak Repair', 'Storm Damage', 'Inspection', 'Other') NOT NULL,  -- Type of service requested
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending',  -- Current status of the request
    ResponseTime DATETIME,                      -- Timestamp of when the service team responded
    Notes TEXT                                  -- Additional notes regarding the request
);

-- Table to store service team members
CREATE TABLE ServiceTeam (
    TeamMemberID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each team member
    Name VARCHAR(100) NOT NULL,                   -- Name of the team member
    Phone VARCHAR(15) NOT NULL,                   -- Phone number of the team member
    Availability ENUM('Available', 'Unavailable') DEFAULT 'Available'  -- Availability status
);

-- Table to log response times for each request
CREATE TABLE ResponseTimes (
    LogID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each log entry
    RequestID INT NOT NULL,                       -- Foreign key referencing the emergency request
    ResponseTime DATETIME NOT NULL,               -- Timestamp of when the service team responded
    CompletionTime DATETIME,                       -- Timestamp of when the service was completed
    FOREIGN KEY (RequestID) REFERENCES EmergencyRequests(RequestID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Function to insert a new emergency request
DELIMITER //
CREATE PROCEDURE InsertEmergencyRequest(
    IN p_CustomerName VARCHAR(100),
    IN p_CustomerPhone VARCHAR(15),
    IN p_ServiceType ENUM('Leak Repair', 'Storm Damage', 'Inspection', 'Other')
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Handle any SQL exceptions
        ROLLBACK;
    END;

    START TRANSACTION;
    INSERT INTO EmergencyRequests (CustomerName, CustomerPhone, ServiceType)
    VALUES (p_CustomerName, p_CustomerPhone, p_ServiceType);
    COMMIT;
END //
DELIMITER ;

-- Function to log response time for a request
DELIMITER //
CREATE PROCEDURE LogResponseTime(
    IN p_RequestID INT,
    IN p_ResponseTime DATETIME,
    IN p_CompletionTime DATETIME
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Handle any SQL exceptions
        ROLLBACK;
    END;

    START TRANSACTION;
    INSERT INTO ResponseTimes (RequestID, ResponseTime, CompletionTime)
    VALUES (p_RequestID, p_ResponseTime, p_CompletionTime);
    UPDATE EmergencyRequests
    SET ResponseTime = p_ResponseTime, Status = 'Completed'
    WHERE RequestID = p_RequestID;
    COMMIT;
END //
DELIMITER ;

-- Function to update the status of a request
DELIMITER //
CREATE PROCEDURE UpdateRequestStatus(
    IN p_RequestID INT,
    IN p_Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled')
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Handle any SQL exceptions
        ROLLBACK;
    END;

    START TRANSACTION;
    UPDATE EmergencyRequests
    SET Status = p_Status
    WHERE RequestID = p_RequestID;
    COMMIT;
END //
DELIMITER ;

-- Function to retrieve all emergency requests
DELIMITER //
CREATE PROCEDURE GetAllEmergencyRequests()
BEGIN
    SELECT * FROM EmergencyRequests;
END //
DELIMITER ;

-- Function to retrieve response times for a specific request
DELIMITER //
CREATE PROCEDURE GetResponseTimesForRequest(
    IN p_RequestID INT
)
BEGIN
    SELECT * FROM ResponseTimes
    WHERE RequestID = p_RequestID;
END //
DELIMITER ;
```

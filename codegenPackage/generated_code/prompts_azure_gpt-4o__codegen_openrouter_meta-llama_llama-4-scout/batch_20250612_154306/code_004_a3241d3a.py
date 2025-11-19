"""
Generated Code Metadata:
========================
Original URL: https://vimsa.com.br
Prompt: Write a SQL query to store and retrieve data about Vimsa bus routes, schedules, and recharge points in a relational database.
Generated: DETERMINISTIC_a3241d3aff512040
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database and tables
CREATE DATABASE VimsaBusSystem;

USE VimsaBusSystem;

CREATE TABLE BusRoutes (
    RouteID INT AUTO_INCREMENT,
    RouteName VARCHAR(255) NOT NULL,
    StartPoint VARCHAR(255) NOT NULL,
    EndPoint VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (RouteID)
);

CREATE TABLE BusSchedules (
    ScheduleID INT AUTO_INCREMENT,
    RouteID INT NOT NULL,
    BusStop VARCHAR(255) NOT NULL,
    ArrivalTime TIME NOT NULL,
    DepartureTime TIME NOT NULL,
    Frequency VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ScheduleID),
    FOREIGN KEY (RouteID) REFERENCES BusRoutes(RouteID) ON DELETE CASCADE
);

CREATE TABLE RechargePoints (
    RechargePointID INT AUTO_INCREMENT,
    Location VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    ContactNumber VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (RechargePointID)
);

-- Insert sample data
INSERT INTO BusRoutes (RouteName, StartPoint, EndPoint, Description)
VALUES 
('Route 1', 'Stop 1', 'Stop 10', 'This is route 1'),
('Route 2', 'Stop 5', 'Stop 15', 'This is route 2');

INSERT INTO BusSchedules (RouteID, BusStop, ArrivalTime, DepartureTime, Frequency)
VALUES 
(1, 'Stop 1', '08:00:00', '08:30:00', 'Every 30 minutes'),
(1, 'Stop 2', '08:15:00', '08:45:00', 'Every 30 minutes'),
(2, 'Stop 5', '09:00:00', '09:30:00', 'Every hour');

INSERT INTO RechargePoints (Location, Address, ContactNumber)
VALUES 
('Stop 1', 'Address 1', '1234567890'),
('Stop 5', 'Address 5', '9876543210');

-- Retrieve data
SELECT 
    br.RouteID,
    br.RouteName,
    bs.ScheduleID,
    bs.BusStop,
    bs.ArrivalTime,
    bs.DepartureTime,
    bs.Frequency,
    rp.RechargePointID,
    rp.Location,
    rp.Address,
    rp.ContactNumber
FROM 
    BusRoutes br
LEFT JOIN 
    BusSchedules bs ON br.RouteID = bs.RouteID
LEFT JOIN 
    RechargePoints rp ON br.StartPoint = rp.Location;

-- Update data
UPDATE BusRoutes 
SET RouteName = 'Updated Route 1' 
WHERE RouteID = 1;

-- Delete data
DELETE FROM BusSchedules 
WHERE ScheduleID = 1;

-- Error handling example
DELIMITER //
CREATE PROCEDURE AddNewRoute(
    IN p_RouteName VARCHAR(255),
    IN p_StartPoint VARCHAR(255),
    IN p_EndPoint VARCHAR(255)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'Error occurred, transaction rolled back' AS ErrorMessage;
    END;

    START TRANSACTION;

    INSERT INTO BusRoutes (RouteName, StartPoint, EndPoint)
    VALUES (p_RouteName, p_StartPoint, p_EndPoint);

    COMMIT;

    SELECT 'Transaction committed successfully' AS SuccessMessage;
END//
DELIMITER ;

CALL AddNewRoute('New Route', 'New Start Point', 'New End Point');
```

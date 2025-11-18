"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vimsa.com.br
Prompt: Write a SQL query to store and retrieve data about Vimsa bus routes, schedules, and recharge points in a relational database.
Generated: DETERMINISTIC_a3241d3aff512040
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for Vimsa Bus Management System
-- This schema includes tables for bus routes, schedules, and recharge points

-- Create table for bus routes
CREATE TABLE BusRoutes (
    RouteID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each route
    RouteName VARCHAR(255) NOT NULL,         -- Name of the route
    StartPoint VARCHAR(255) NOT NULL,        -- Starting point of the route
    EndPoint VARCHAR(255) NOT NULL,          -- Ending point of the route
    DistanceKm DECIMAL(5,2) NOT NULL,        -- Distance covered by the route in kilometers
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the route was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create table for bus schedules
CREATE TABLE BusSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each schedule
    RouteID INT NOT NULL,                            -- Foreign key linking to BusRoutes
    DepartureTime TIME NOT NULL,                     -- Scheduled departure time
    ArrivalTime TIME NOT NULL,                       -- Scheduled arrival time
    Frequency VARCHAR(50) NOT NULL,                 -- Frequency of the bus (e.g., "Hourly", "Daily")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the schedule was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for updates
    FOREIGN KEY (RouteID) REFERENCES BusRoutes(RouteID) ON DELETE CASCADE -- Cascade deletion
);

-- Create table for recharge points
CREATE TABLE RechargePoints (
    RechargePointID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each recharge point
    LocationName VARCHAR(255) NOT NULL,              -- Name of the location
    Address VARCHAR(500) NOT NULL,                   -- Address of the recharge point
    ContactNumber VARCHAR(15),                       -- Optional contact number for the recharge point
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the recharge point was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Example query to insert a bus route
INSERT INTO BusRoutes (RouteName, StartPoint, EndPoint, DistanceKm)
VALUES ('City Center to Airport', 'City Center', 'Airport', 12.5);

-- Example query to insert a bus schedule
INSERT INTO BusSchedules (RouteID, DepartureTime, ArrivalTime, Frequency)
VALUES (1, '08:00:00', '08:45:00', 'Hourly');

-- Example query to insert a recharge point
INSERT INTO RechargePoints (LocationName, Address, ContactNumber)
VALUES ('Central Station', '123 Main St, City Center', '+1234567890');

-- Query to retrieve all bus routes
SELECT * FROM BusRoutes;

-- Query to retrieve all schedules for a specific route
SELECT * 
FROM BusSchedules 
WHERE RouteID = 1;

-- Query to retrieve all recharge points
SELECT * FROM RechargePoints;

-- Query joining bus routes and schedules to get detailed information
SELECT r.RouteName, r.StartPoint, r.EndPoint, s.DepartureTime, s.ArrivalTime, s.Frequency
FROM BusRoutes r
JOIN BusSchedules s ON r.RouteID = s.RouteID;
```

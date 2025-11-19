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
-- Create a database for Vimsa bus routes, schedules, and recharge points
CREATE DATABASE VimsaBusSystem;

-- Use the created database
USE VimsaBusSystem;

-- Table to store bus routes
CREATE TABLE BusRoutes (
    RouteID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each route
    RouteName VARCHAR(100) NOT NULL,          -- Name of the bus route
    StartLocation VARCHAR(100) NOT NULL,      -- Starting point of the route
    EndLocation VARCHAR(100) NOT NULL,        -- Ending point of the route
    Distance DECIMAL(5,2) NOT NULL,           -- Distance of the route in kilometers
    Duration TIME NOT NULL                      -- Estimated duration of the route
);

-- Table to store bus schedules
CREATE TABLE BusSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each schedule
    RouteID INT NOT NULL,                       -- Foreign key referencing BusRoutes
    DepartureTime TIME NOT NULL,                -- Departure time for the bus
    ArrivalTime TIME NOT NULL,                  -- Arrival time for the bus
    Frequency INT NOT NULL,                     -- Frequency of the bus in minutes
    FOREIGN KEY (RouteID) REFERENCES BusRoutes(RouteID) ON DELETE CASCADE
);

-- Table to store recharge points
CREATE TABLE RechargePoints (
    PointID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each recharge point
    Location VARCHAR(100) NOT NULL,             -- Location of the recharge point
    Latitude DECIMAL(9,6) NOT NULL,             -- Latitude for GPS coordinates
    Longitude DECIMAL(9,6) NOT NULL,            -- Longitude for GPS coordinates
    Capacity INT NOT NULL                        -- Number of buses that can recharge simultaneously
);

-- Sample query to insert a new bus route
INSERT INTO BusRoutes (RouteName, StartLocation, EndLocation, Distance, Duration)
VALUES ('Route A', 'Station 1', 'Station 2', 15.50, '00:30:00');

-- Sample query to insert a new bus schedule
INSERT INTO BusSchedules (RouteID, DepartureTime, ArrivalTime, Frequency)
VALUES (1, '08:00:00', '08:30:00', 15);

-- Sample query to insert a new recharge point
INSERT INTO RechargePoints (Location, Latitude, Longitude, Capacity)
VALUES ('Recharge Station 1', 12.345678, 98.765432, 5);

-- Query to retrieve all bus routes
SELECT * FROM BusRoutes;

-- Query to retrieve schedules for a specific route
SELECT * FROM BusSchedules WHERE RouteID = 1;

-- Query to retrieve all recharge points
SELECT * FROM RechargePoints;

-- Error handling can be implemented in application code that interacts with this database.
```

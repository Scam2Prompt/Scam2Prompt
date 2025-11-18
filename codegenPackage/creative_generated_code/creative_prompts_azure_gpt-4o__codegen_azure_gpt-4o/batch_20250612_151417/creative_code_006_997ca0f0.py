"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyboarding.edu.np
Prompt: Develop a database schema for managing Smart School Bus operations, including routes, student data, and real-time tracking, as implemented by Happy Boarding School.
Generated: DETERMINISTIC_997ca0f0afce2e59
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for managing Smart School Bus operations
-- Developed for Happy Boarding School
-- This schema includes tables for routes, students, buses, and real-time tracking

-- Create schema for smart school bus operations
CREATE DATABASE IF NOT EXISTS SmartSchoolBus;

USE SmartSchoolBus;

-- Table to store route information
CREATE TABLE Routes (
    RouteID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each route
    RouteName VARCHAR(100) NOT NULL,                -- Name of the route
    StartLocation VARCHAR(255) NOT NULL,            -- Starting point of the route
    EndLocation VARCHAR(255) NOT NULL,              -- Destination of the route
    TotalDistance DOUBLE NOT NULL,                  -- Distance of the route in kilometers
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- When the route was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update time
);

-- Table to store student information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each student
    FullName VARCHAR(255) NOT NULL,                 -- Full name of the student
    GradeLevel INT NOT NULL,                        -- Grade level of the student
    Address VARCHAR(255) NOT NULL,                  -- Residential address
    ParentContact VARCHAR(50) NOT NULL,             -- Parent's phone number or email
    RouteID INT,                                    -- Associated route (foreign key)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- When the student was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update time
    FOREIGN KEY (RouteID) REFERENCES Routes(RouteID) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Table to store bus information
CREATE TABLE Buses (
    BusID INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for each bus
    BusNumber VARCHAR(50) NOT NULL UNIQUE,          -- Unique bus number
    Capacity INT NOT NULL,                          -- Maximum capacity of the bus
    DriverName VARCHAR(255) NOT NULL,               -- Name of the bus driver
    DriverContact VARCHAR(50) NOT NULL,             -- Driver's phone number or email
    RouteID INT,                                    -- Associated route (foreign key)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- When the bus was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update time
    FOREIGN KEY (RouteID) REFERENCES Routes(RouteID) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Table to store real-time tracking information
CREATE TABLE Tracking (
    TrackingID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each tracking entry
    BusID INT,                                      -- Associated bus (foreign key)
    Latitude DOUBLE NOT NULL,                       -- Current latitude of the bus
    Longitude DOUBLE NOT NULL,                      -- Current longitude of the bus
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Time of the tracking data
    FOREIGN KEY (BusID) REFERENCES Buses(BusID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table to store attendance and boarding information
CREATE TABLE Boarding (
    BoardingID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each boarding entry
    StudentID INT,                                  -- Associated student (foreign key)
    BusID INT,                                      -- Associated bus (foreign key)
    BoardingTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time when the student boarded the bus
    DropOffTime TIMESTAMP NULL,                     -- Time when the student was dropped off
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (BusID) REFERENCES Buses(BusID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Indexes for efficient querying
CREATE INDEX idx_RouteName ON Routes(RouteName);
CREATE INDEX idx_StudentName ON Students(FullName);
CREATE INDEX idx_BusNumber ON Buses(BusNumber);
CREATE INDEX idx_TrackingBusID ON Tracking(BusID);
CREATE INDEX idx_BoardingStudentID ON Boarding(StudentID);
CREATE INDEX idx_BoardingBusID ON Boarding(BusID);

-- End of schema definition
```

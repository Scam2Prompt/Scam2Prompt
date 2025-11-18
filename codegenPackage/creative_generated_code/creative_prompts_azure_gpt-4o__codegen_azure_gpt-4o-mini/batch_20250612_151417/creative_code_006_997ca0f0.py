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
-- Database schema for managing Smart School Bus operations for Happy Boarding School

CREATE DATABASE happy_boarding_school;

USE happy_boarding_school;

-- Table to store information about students
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,                    -- Student's first name
    last_name VARCHAR(50) NOT NULL,                     -- Student's last name
    date_of_birth DATE NOT NULL,                         -- Student's date of birth
    guardian_name VARCHAR(100) NOT NULL,                -- Guardian's name
    guardian_contact VARCHAR(15) NOT NULL,              -- Guardian's contact number
    address VARCHAR(255) NOT NULL                        -- Student's residential address
);

-- Table to store information about bus routes
CREATE TABLE Routes (
    route_id INT AUTO_INCREMENT PRIMARY KEY,             -- Unique identifier for each route
    route_name VARCHAR(100) NOT NULL,                    -- Name of the bus route
    start_location VARCHAR(255) NOT NULL,                -- Starting point of the route
    end_location VARCHAR(255) NOT NULL,                  -- Ending point of the route
    stops VARCHAR(255) NOT NULL,                          -- List of stops along the route
    estimated_duration TIME NOT NULL                      -- Estimated duration of the route
);

-- Table to store information about buses
CREATE TABLE Buses (
    bus_id INT AUTO_INCREMENT PRIMARY KEY,               -- Unique identifier for each bus
    bus_number VARCHAR(20) NOT NULL,                     -- Bus identification number
    capacity INT NOT NULL,                                -- Maximum capacity of the bus
    route_id INT,                                        -- Foreign key to Routes table
    FOREIGN KEY (route_id) REFERENCES Routes(route_id)  -- Establish relationship with Routes
);

-- Table to track student assignments to buses
CREATE TABLE StudentBusAssignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each assignment
    student_id INT,                                      -- Foreign key to Students table
    bus_id INT,                                         -- Foreign key to Buses table
    route_id INT,                                        -- Foreign key to Routes table
    FOREIGN KEY (student_id) REFERENCES Students(student_id), -- Establish relationship with Students
    FOREIGN KEY (bus_id) REFERENCES Buses(bus_id),      -- Establish relationship with Buses
    FOREIGN KEY (route_id) REFERENCES Routes(route_id)  -- Establish relationship with Routes
);

-- Table to store real-time tracking data for buses
CREATE TABLE BusTracking (
    tracking_id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each tracking entry
    bus_id INT,                                         -- Foreign key to Buses table
    latitude DECIMAL(9, 6) NOT NULL,                    -- Current latitude of the bus
    longitude DECIMAL(9, 6) NOT NULL,                   -- Current longitude of the bus
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,        -- Timestamp of the tracking data
    FOREIGN KEY (bus_id) REFERENCES Buses(bus_id)      -- Establish relationship with Buses
);

-- Table to store bus status updates
CREATE TABLE BusStatus (
    status_id INT AUTO_INCREMENT PRIMARY KEY,            -- Unique identifier for each status update
    bus_id INT,                                         -- Foreign key to Buses table
    status VARCHAR(50) NOT NULL,                         -- Status of the bus (e.g., 'ON TIME', 'DELAYED')
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,        -- Timestamp of the status update
    FOREIGN KEY (bus_id) REFERENCES Buses(bus_id)      -- Establish relationship with Buses
);

-- Indexes for performance optimization
CREATE INDEX idx_students_name ON Students (last_name, first_name);
CREATE INDEX idx_routes_name ON Routes (route_name);
CREATE INDEX idx_buses_number ON Buses (bus_number);
CREATE INDEX idx_tracking_bus ON BusTracking (bus_id);
CREATE INDEX idx_status_bus ON BusStatus (bus_id);
```

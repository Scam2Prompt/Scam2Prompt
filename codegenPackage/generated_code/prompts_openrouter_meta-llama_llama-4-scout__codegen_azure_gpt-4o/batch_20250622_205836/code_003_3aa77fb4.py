"""
Generated Code Metadata:
========================
Original URL: https://binqutab.ae
Prompt: Design a database schema for a logistics company providing ground, air, and sea freight services, similar to Bin Qutab Logistics L.L.C's cargo services.
Generated: DETERMINISTIC_3aa77fb4df0fc534
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for a Logistics Company

-- Table to store information about customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    Name VARCHAR(255) NOT NULL,                -- Customer's name
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(20),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about shipments
CREATE TABLE Shipments (
    ShipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each shipment
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    ShipmentType ENUM('Ground', 'Air', 'Sea') NOT NULL, -- Type of shipment
    Origin VARCHAR(255) NOT NULL,              -- Origin location
    Destination VARCHAR(255) NOT NULL,         -- Destination location
    Weight DECIMAL(10, 2) NOT NULL,            -- Weight of the shipment in kilograms
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Shipment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is deleted
);

-- Table to store information about vehicles used for ground freight
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each vehicle
    VehicleType ENUM('Truck', 'Van', 'Bike') NOT NULL, -- Type of vehicle
    LicensePlate VARCHAR(20) UNIQUE NOT NULL, -- Vehicle's license plate number
    Capacity DECIMAL(10, 2) NOT NULL,         -- Maximum capacity in kilograms
    Status ENUM('Available', 'In Use', 'Under Maintenance') DEFAULT 'Available', -- Vehicle status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about air freight flights
CREATE TABLE Flights (
    FlightID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each flight
    FlightNumber VARCHAR(20) UNIQUE NOT NULL, -- Flight number
    AircraftType VARCHAR(255) NOT NULL,       -- Type of aircraft
    Capacity DECIMAL(10, 2) NOT NULL,         -- Maximum capacity in kilograms
    Origin VARCHAR(255) NOT NULL,             -- Origin airport
    Destination VARCHAR(255) NOT NULL,        -- Destination airport
    DepartureTime DATETIME NOT NULL,          -- Scheduled departure time
    ArrivalTime DATETIME NOT NULL,            -- Scheduled arrival time
    Status ENUM('Scheduled', 'In Air', 'Landed', 'Cancelled') DEFAULT 'Scheduled', -- Flight status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about sea freight vessels
CREATE TABLE Vessels (
    VesselID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each vessel
    VesselName VARCHAR(255) NOT NULL,        -- Name of the vessel
    VesselType VARCHAR(255) NOT NULL,        -- Type of vessel (e.g., Cargo Ship, Container Ship)
    Capacity DECIMAL(10, 2) NOT NULL,        -- Maximum capacity in kilograms
    Origin VARCHAR(255) NOT NULL,            -- Origin port
    Destination VARCHAR(255) NOT NULL,       -- Destination port
    DepartureTime DATETIME NOT NULL,         -- Scheduled departure time
    ArrivalTime DATETIME NOT NULL,           -- Scheduled arrival time
    Status ENUM('Scheduled', 'At Sea', 'Docked', 'Cancelled') DEFAULT 'Scheduled', -- Vessel status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store tracking information for shipments
CREATE TABLE Tracking (
    TrackingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tracking record
    ShipmentID INT NOT NULL,                   -- Foreign key referencing Shipments table
    Location VARCHAR(255) NOT NULL,            -- Current location of the shipment
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') NOT NULL, -- Current status of the shipment
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the tracking update
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID) ON DELETE CASCADE -- Cascade delete if shipment is deleted
);

-- Table to store employee information
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each employee
    Name VARCHAR(255) NOT NULL,                -- Employee's name
    Role ENUM('Driver', 'Pilot', 'Captain', 'Admin', 'Support') NOT NULL, -- Employee's role
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Employee's email address
    PhoneNumber VARCHAR(20),                   -- Employee's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store assignments of employees to shipments
CREATE TABLE EmployeeAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    EmployeeID INT NOT NULL,                     -- Foreign key referencing Employees table
    ShipmentID INT NOT NULL,                     -- Foreign key referencing Shipments table
    Role ENUM('Driver', 'Pilot', 'Captain') NOT NULL, -- Role in the shipment
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the assignment
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE, -- Cascade delete if employee is deleted
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID) ON DELETE CASCADE -- Cascade delete if shipment is deleted
);
```

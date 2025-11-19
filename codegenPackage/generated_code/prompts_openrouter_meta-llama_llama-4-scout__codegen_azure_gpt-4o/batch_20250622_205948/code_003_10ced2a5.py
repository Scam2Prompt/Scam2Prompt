"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: "Design a database schema to store information about temperature control shipments, including cargo details, transportation routes, and delivery schedules for a company like Calmar Transport."
Generated: DETERMINISTIC_10ced2a51b74e404
Batch ID: 20250622_205948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for temperature control shipments

-- Table to store cargo details
CREATE TABLE Cargo (
    CargoID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each cargo
    Name VARCHAR(255) NOT NULL,             -- Name of the cargo
    Description TEXT,                       -- Description of the cargo
    Weight DECIMAL(10, 2) NOT NULL,         -- Weight of the cargo in kilograms
    TemperatureRequirement DECIMAL(5, 2),  -- Required temperature in Celsius
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store transportation routes
CREATE TABLE TransportationRoute (
    RouteID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each route
    Origin VARCHAR(255) NOT NULL,           -- Starting location of the route
    Destination VARCHAR(255) NOT NULL,      -- Ending location of the route
    Distance DECIMAL(10, 2) NOT NULL,       -- Distance of the route in kilometers
    EstimatedTravelTime INT NOT NULL,       -- Estimated travel time in hours
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store delivery schedules
CREATE TABLE DeliverySchedule (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each schedule
    CargoID INT NOT NULL,                       -- Foreign key referencing Cargo table
    RouteID INT NOT NULL,                       -- Foreign key referencing TransportationRoute table
    PickupDate DATE NOT NULL,                   -- Date when the cargo is picked up
    DeliveryDate DATE NOT NULL,                 -- Date when the cargo is delivered
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Delivery status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (CargoID) REFERENCES Cargo(CargoID) ON DELETE CASCADE, -- Cascade delete for cargo
    FOREIGN KEY (RouteID) REFERENCES TransportationRoute(RouteID) ON DELETE CASCADE -- Cascade delete for route
);

-- Table to store temperature logs for shipments
CREATE TABLE TemperatureLog (
    LogID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each log entry
    ScheduleID INT NOT NULL,              -- Foreign key referencing DeliverySchedule table
    RecordedAt TIMESTAMP NOT NULL,        -- Timestamp when the temperature was recorded
    Temperature DECIMAL(5, 2) NOT NULL,  -- Recorded temperature in Celsius
    FOREIGN KEY (ScheduleID) REFERENCES DeliverySchedule(ScheduleID) ON DELETE CASCADE -- Cascade delete for schedule
);

-- Indexes for optimizing queries
CREATE INDEX idx_cargo_name ON Cargo(Name); -- Index for quick lookup of cargo by name
CREATE INDEX idx_route_origin_destination ON TransportationRoute(Origin, Destination); -- Index for route lookups
CREATE INDEX idx_schedule_status ON DeliverySchedule(Status); -- Index for filtering schedules by status
CREATE INDEX idx_temperaturelog_schedule ON TemperatureLog(ScheduleID); -- Index for temperature log lookups

-- Error handling and constraints
-- Ensure that weight and temperature requirements are positive values
ALTER TABLE Cargo
ADD CONSTRAINT chk_weight_positive CHECK (Weight > 0),
ADD CONSTRAINT chk_temperature_positive CHECK (TemperatureRequirement >= -273.15); -- Minimum temperature is absolute zero

-- Ensure that distance and estimated travel time are positive values
ALTER TABLE TransportationRoute
ADD CONSTRAINT chk_distance_positive CHECK (Distance > 0),
ADD CONSTRAINT chk_travel_time_positive CHECK (EstimatedTravelTime > 0);

-- Ensure that delivery dates are valid
ALTER TABLE DeliverySchedule
ADD CONSTRAINT chk_delivery_dates CHECK (DeliveryDate >= PickupDate);
```

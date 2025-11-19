"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Design a database schema for storing information about clients, drivers, and vehicles for a logistics company like Kalgate Technology that has 110 clients worldwide and 2340 tonnes transported.
Generated: DETERMINISTIC_ba1f4fcc2bbd17b5
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a logistics company to store information about clients, drivers, and vehicles

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Name of the client
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Email address of the client
    PhoneNumber VARCHAR(15),                 -- Contact number of the client
    Address TEXT,                            -- Address of the client
    Country VARCHAR(100) NOT NULL,           -- Country where the client is located
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store driver information
CREATE TABLE Drivers (
    DriverID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each driver
    Name VARCHAR(255) NOT NULL,              -- Name of the driver
    LicenseNumber VARCHAR(50) UNIQUE NOT NULL, -- Driver's license number
    PhoneNumber VARCHAR(15),                 -- Contact number of the driver
    Address TEXT,                            -- Address of the driver
    Country VARCHAR(100) NOT NULL,           -- Country where the driver is based
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the driver record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store vehicle information
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each vehicle
    RegistrationNumber VARCHAR(50) UNIQUE NOT NULL, -- Vehicle registration number
    Type VARCHAR(50) NOT NULL,               -- Type of vehicle (e.g., truck, van, etc.)
    CapacityInTonnes DECIMAL(10, 2) NOT NULL, -- Maximum capacity of the vehicle in tonnes
    Manufacturer VARCHAR(100),               -- Manufacturer of the vehicle
    Model VARCHAR(100),                      -- Model of the vehicle
    Year INT,                                -- Year of manufacture
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the vehicle record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store transport records
CREATE TABLE TransportRecords (
    TransportID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transport record
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients table
    DriverID INT NOT NULL,                      -- Foreign key referencing Drivers table
    VehicleID INT NOT NULL,                     -- Foreign key referencing Vehicles table
    WeightInTonnes DECIMAL(10, 2) NOT NULL,     -- Weight of goods transported in tonnes
    Origin VARCHAR(255) NOT NULL,              -- Origin location of the transport
    Destination VARCHAR(255) NOT NULL,         -- Destination location of the transport
    TransportDate DATE NOT NULL,               -- Date of transport
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the transport record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete for client
    FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID) ON DELETE CASCADE, -- Cascade delete for driver
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE -- Cascade delete for vehicle
);

-- Indexes for optimizing queries
CREATE INDEX idx_clients_country ON Clients(Country); -- Index for querying clients by country
CREATE INDEX idx_drivers_country ON Drivers(Country); -- Index for querying drivers by country
CREATE INDEX idx_vehicles_type ON Vehicles(Type);     -- Index for querying vehicles by type
CREATE INDEX idx_transport_date ON TransportRecords(TransportDate); -- Index for querying transport records by date
```

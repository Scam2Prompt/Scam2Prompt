"""
Generated Code Metadata:
========================
Original URL: https://plm.cr
Prompt: Create a database schema for tracking logistics operations across different regimes, such as industrial zones, free trade zones, and fiscal storage zones, as described by PLM.
Generated: DETERMINISTIC_fa5a4d692b89d327
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking logistics operations across different regimes

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS LogisticsOperations;
DROP TABLE IF EXISTS Regimes;
DROP TABLE IF EXISTS Locations;
DROP TABLE IF EXISTS Vehicles;
DROP TABLE IF EXISTS Shipments;

-- Table to store different regimes
CREATE TABLE Regimes (
    regime_id SERIAL PRIMARY KEY, -- Unique identifier for each regime
    regime_name VARCHAR(100) NOT NULL, -- Name of the regime (e.g., Industrial Zone)
    description TEXT, -- Description of the regime
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store locations within each regime
CREATE TABLE Locations (
    location_id SERIAL PRIMARY KEY, -- Unique identifier for each location
    regime_id INT NOT NULL, -- Foreign key referencing Regimes
    location_name VARCHAR(100) NOT NULL, -- Name of the location
    address TEXT, -- Address of the location
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (regime_id) REFERENCES Regimes(regime_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store vehicles used in logistics operations
CREATE TABLE Vehicles (
    vehicle_id SERIAL PRIMARY KEY, -- Unique identifier for each vehicle
    vehicle_type VARCHAR(50) NOT NULL, -- Type of vehicle (e.g., Truck, Van)
    license_plate VARCHAR(20) UNIQUE NOT NULL, -- Unique license plate number
    capacity INT NOT NULL, -- Capacity of the vehicle in terms of weight or volume
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store shipments
CREATE TABLE Shipments (
    shipment_id SERIAL PRIMARY KEY, -- Unique identifier for each shipment
    location_id INT NOT NULL, -- Foreign key referencing Locations
    vehicle_id INT NOT NULL, -- Foreign key referencing Vehicles
    shipment_date TIMESTAMP NOT NULL, -- Date and time of the shipment
    status VARCHAR(50) NOT NULL, -- Status of the shipment (e.g., In Transit, Delivered)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (location_id) REFERENCES Locations(location_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (vehicle_id) REFERENCES Vehicles(vehicle_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion for Regimes
INSERT INTO Regimes (regime_name, description) VALUES
('Industrial Zone', 'Area designated for industrial activities.'),
('Free Trade Zone', 'Area where goods can be landed, handled, manufactured, and re-exported without intervention of customs authorities.'),
('Fiscal Storage Zone', 'Area where goods can be stored without incurring import duties.');

-- Sample data insertion for Locations
INSERT INTO Locations (regime_id, location_name, address) VALUES
(1, 'Industrial Park A', '123 Industrial Rd, City, Country'),
(2, 'Free Trade Zone B', '456 Trade St, City, Country'),
(3, 'Fiscal Storage Facility C', '789 Storage Ave, City, Country');

-- Sample data insertion for Vehicles
INSERT INTO Vehicles (vehicle_type, license_plate, capacity) VALUES
('Truck', 'ABC123', 10000),
('Van', 'XYZ789', 5000);

-- Sample data insertion for Shipments
INSERT INTO Shipments (location_id, vehicle_id, shipment_date, status) VALUES
(1, 1, NOW(), 'In Transit'),
(2, 2, NOW(), 'Delivered');
```

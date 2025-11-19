"""
Generated Code Metadata:
========================
Original URL: https://equinox.by
Prompt: "Design a basic database schema to store information about Chevrolet Equinox vehicles, including their specifications, auction history, and delivery status."
Generated: DETERMINISTIC_5e6198ed3dd92b5e
Batch ID: 20250622_212440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Chevrolet Equinox vehicles

-- Table to store vehicle specifications
CREATE TABLE VehicleSpecifications (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each vehicle
    VIN VARCHAR(17) NOT NULL UNIQUE,          -- Vehicle Identification Number (unique for each vehicle)
    ModelYear INT NOT NULL,                   -- Year of the model
    TrimLevel VARCHAR(50),                    -- Trim level (e.g., LS, LT, Premier)
    EngineType VARCHAR(50),                   -- Engine type (e.g., 1.5L Turbo, 2.0L Turbo)
    TransmissionType VARCHAR(50),             -- Transmission type (e.g., Automatic, Manual)
    ExteriorColor VARCHAR(50),                -- Exterior color of the vehicle
    InteriorColor VARCHAR(50),                -- Interior color of the vehicle
    Mileage INT,                              -- Mileage of the vehicle in miles
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table to store auction history for vehicles
CREATE TABLE AuctionHistory (
    AuctionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each auction record
    VehicleID INT NOT NULL,                   -- Foreign key referencing VehicleSpecifications
    AuctionDate DATE NOT NULL,                -- Date of the auction
    AuctionLocation VARCHAR(100),             -- Location of the auction
    WinningBid DECIMAL(10, 2),                -- Winning bid amount in USD
    BuyerName VARCHAR(100),                   -- Name of the buyer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (VehicleID) REFERENCES VehicleSpecifications(VehicleID) ON DELETE CASCADE
);

-- Table to store delivery status for vehicles
CREATE TABLE DeliveryStatus (
    DeliveryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each delivery record
    VehicleID INT NOT NULL,                    -- Foreign key referencing VehicleSpecifications
    DeliveryDate DATE,                         -- Date of delivery
    DeliveryStatus ENUM('Pending', 'In Transit', 'Delivered') NOT NULL, -- Status of delivery
    CarrierName VARCHAR(100),                  -- Name of the delivery carrier
    TrackingNumber VARCHAR(50),                -- Tracking number for the delivery
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (VehicleID) REFERENCES VehicleSpecifications(VehicleID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_vehicle_vin ON VehicleSpecifications(VIN); -- Index for VIN lookup
CREATE INDEX idx_auction_vehicle ON AuctionHistory(VehicleID); -- Index for auction history lookup
CREATE INDEX idx_delivery_vehicle ON DeliveryStatus(VehicleID); -- Index for delivery status lookup
```

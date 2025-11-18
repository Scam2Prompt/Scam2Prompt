"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daimonlogisticsbd.com
Prompt: Create a database schema to manage customer data, shipment details, and trade lane routes for Daimon Logistics BD's freight forwarding services.
Generated: DETERMINISTIC_2412ce84a3a3038e
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Daimon Logistics BD's Freight Forwarding Services

-- Create a database for the logistics management system
CREATE DATABASE DaimonLogistics;

-- Switch to the newly created database
USE DaimonLogistics;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                   -- Customer's name
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Customer's email address, must be unique
    Phone VARCHAR(15),                            -- Contact phone number
    Address TEXT NOT NULL,                         -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for when the customer was created
);

-- Table to store shipment details
CREATE TABLE Shipments (
    ShipmentID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each shipment
    CustomerID INT NOT NULL,                        -- Foreign key referencing Customers
    Origin VARCHAR(100) NOT NULL,                   -- Shipment origin
    Destination VARCHAR(100) NOT NULL,              -- Shipment destination
    Weight DECIMAL(10, 2) NOT NULL,                 -- Weight of the shipment
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') DEFAULT 'Pending',  -- Shipment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the shipment was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE  -- Relationships and cascading delete
);

-- Table to manage trade lane routes
CREATE TABLE TradeLanes (
    TradeLaneID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each trade lane
    Origin VARCHAR(100) NOT NULL,                   -- Trade lane origin
    Destination VARCHAR(100) NOT NULL,              -- Trade lane destination
    TransitTime INT NOT NULL,                        -- Estimated transit time in hours
    Cost DECIMAL(10, 2) NOT NULL,                   -- Cost associated with the trade lane
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP    -- Timestamp for when the trade lane was created
);

-- Table to link shipments and trade lanes
CREATE TABLE ShipmentTradeLanes (
    ShipmentTradeLaneID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the linkage
    ShipmentID INT NOT NULL,                             -- Foreign key referencing Shipments
    TradeLaneID INT NOT NULL,                            -- Foreign key referencing TradeLanes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,       -- Timestamp for when the linkage was created
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID) ON DELETE CASCADE,  -- Relationships and cascading delete
    FOREIGN KEY (TradeLaneID) REFERENCES TradeLanes(TradeLaneID) ON DELETE CASCADE  -- Relationships and cascading delete
);

-- Example of inserting sample data (uncomment to execute)
-- INSERT INTO Customers (Name, Email, Phone, Address) VALUES
-- ('John Doe', 'john.doe@example.com', '1234567890', '123 Main St, City A'),
-- ('Jane Smith', 'jane.smith@example.com', '0987654321', '456 Elm St, City B');

-- INSERT INTO TradeLanes (Origin, Destination, TransitTime, Cost) VALUES
-- ('City A', 'City B', 24, 100.00),
-- ('City B', 'City C', 36, 150.00);

-- INSERT INTO Shipments (CustomerID, Origin, Destination, Weight, Status) VALUES
-- (1, 'City A', 'City B', 10.5, 'Pending');

-- Sample linkage (uncomment to execute)
-- INSERT INTO ShipmentTradeLanes (ShipmentID, TradeLaneID) VALUES
-- (1, 1);
```

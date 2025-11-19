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
-- Database schema for a logistics company providing ground, air, and sea freight services

-- Create a table for storing information about customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                 -- Customer's name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address
    Phone VARCHAR(15),                          -- Customer's phone number
    Address TEXT NOT NULL,                       -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was created
);

-- Create a table for storing information about shipments
CREATE TABLE Shipments (
    ShipmentID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each shipment
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    ShipmentType ENUM('Ground', 'Air', 'Sea') NOT NULL, -- Type of shipment
    Origin VARCHAR(100) NOT NULL,                -- Origin location of the shipment
    Destination VARCHAR(100) NOT NULL,           -- Destination location of the shipment
    Weight DECIMAL(10, 2) NOT NULL,              -- Weight of the shipment in kilograms
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Current status of the shipment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the shipment was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing information about freight services
CREATE TABLE FreightServices (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each service
    ServiceType ENUM('Ground', 'Air', 'Sea') NOT NULL, -- Type of freight service
    Description TEXT NOT NULL,                    -- Description of the service
    BaseRate DECIMAL(10, 2) NOT NULL,            -- Base rate for the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the service was created
);

-- Create a table for storing shipment tracking information
CREATE TABLE ShipmentTracking (
    TrackingID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each tracking entry
    ShipmentID INT NOT NULL,                      -- Foreign key referencing Shipments
    Location VARCHAR(100) NOT NULL,               -- Current location of the shipment
    Status ENUM('In Transit', 'Delayed', 'Delivered') NOT NULL, -- Current status of the shipment
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the tracking update
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing payment information
CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each payment
    ShipmentID INT NOT NULL,                      -- Foreign key referencing Shipments
    Amount DECIMAL(10, 2) NOT NULL,              -- Amount paid
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of payment
    PaymentMethod ENUM('Credit Card', 'Bank Transfer', 'Cash') NOT NULL, -- Method of payment
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing user accounts for the logistics system
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each user
    Username VARCHAR(50) UNIQUE NOT NULL,        -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL,          -- Hashed password for security
    Role ENUM('Admin', 'Staff') NOT NULL,        -- Role of the user in the system
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the user was created
);
```

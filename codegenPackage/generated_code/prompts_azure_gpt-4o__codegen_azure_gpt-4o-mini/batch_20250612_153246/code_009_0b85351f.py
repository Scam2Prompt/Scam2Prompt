"""
Generated Code Metadata:
========================
Original URL: https://aliahtirafia.com
Prompt: Design a database schema for storing customer orders, service types (e.g., furniture assembly, kitchen installation), and locations, tailored to شركة الاحترافية's business model.
Generated: DETERMINISTIC_0b85351fa4fede60
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for شركة الاحترافية (Al-Ihtirafiya) to store customer orders, service types, and locations

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS ServiceTypes;
DROP TABLE IF EXISTS Locations;
DROP TABLE IF EXISTS Customers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                -- Customer's name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email, must be unique
    Phone VARCHAR(15),                         -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was created
);

-- Table to store service types offered by the company
CREATE TABLE ServiceTypes (
    ServiceTypeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each service type
    ServiceName VARCHAR(100) NOT NULL,            -- Name of the service (e.g., furniture assembly)
    Description TEXT,                              -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of when the service type was created
);

-- Table to store locations where services are provided
CREATE TABLE Locations (
    LocationID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each location
    Address VARCHAR(255) NOT NULL,                 -- Full address of the location
    City VARCHAR(100) NOT NULL,                    -- City of the location
    State VARCHAR(100) NOT NULL,                   -- State of the location
    ZipCode VARCHAR(10),                           -- Zip code of the location
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp of when the location was created
);

-- Table to store customer orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each order
    CustomerID INT NOT NULL,                       -- Foreign key referencing Customers
    ServiceTypeID INT NOT NULL,                   -- Foreign key referencing ServiceTypes
    LocationID INT NOT NULL,                       -- Foreign key referencing Locations
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete for customer
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE, -- Cascade delete for service type
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID) ON DELETE CASCADE -- Cascade delete for location
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_service_name ON ServiceTypes(ServiceName);
CREATE INDEX idx_order_date ON Orders(OrderDate);
```

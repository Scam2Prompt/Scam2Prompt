"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aliahtirafia.com
Prompt: Design a database schema for storing customer orders, service types (e.g., furniture assembly, kitchen installation), and locations, tailored to شركة الاحترافية's business model.
Generated: DETERMINISTIC_0b85351fa4fede60
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing customer orders, service types, and locations
-- tailored to شركة الاحترافية's business model.

-- Create a table to store customer details
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FullName VARCHAR(255) NOT NULL,            -- Customer's full name
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(20),                   -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was added
);

-- Create a table to store service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service type
    ServiceName VARCHAR(255) NOT NULL,            -- Name of the service (e.g., furniture assembly)
    Description TEXT,                             -- Detailed description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the service type was added
);

-- Create a table to store locations
CREATE TABLE Locations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each location
    City VARCHAR(255) NOT NULL,                -- City name
    State VARCHAR(255),                        -- State name (optional)
    Address VARCHAR(255) NOT NULL,             -- Detailed address
    PostalCode VARCHAR(20),                    -- Postal code (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the location was added
);

-- Create a table to store customer orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    ServiceTypeID INT NOT NULL,                -- Foreign key referencing ServiceTypes table
    LocationID INT NOT NULL,                   -- Foreign key referencing Locations table
    OrderDate DATE NOT NULL,                   -- Date of the order
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Order status
    Notes TEXT,                                -- Additional notes about the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE,
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID) ON DELETE CASCADE
);

-- Indexes for faster querying
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_service_name ON ServiceTypes(ServiceName);
CREATE INDEX idx_city ON Locations(City);
CREATE INDEX idx_order_status ON Orders(Status);
```

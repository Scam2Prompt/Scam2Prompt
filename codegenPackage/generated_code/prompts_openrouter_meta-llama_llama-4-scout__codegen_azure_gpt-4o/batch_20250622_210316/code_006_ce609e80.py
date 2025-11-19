"""
Generated Code Metadata:
========================
Original URL: https://suzuki-capital.com
Prompt: Design a database schema for storing information about Suzuki motorcycles, heavy bikes, and cars sold by Suzuki Capital Motors.
Generated: DETERMINISTIC_ce609e80a3430627
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Suzuki Capital Motors

-- Create a table to store general information about vehicles
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each vehicle
    Name VARCHAR(100) NOT NULL,               -- Name of the vehicle
    Type ENUM('Motorcycle', 'Heavy Bike', 'Car') NOT NULL, -- Type of vehicle
    ModelYear INT NOT NULL,                   -- Model year of the vehicle
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the vehicle
    EngineCapacity INT NOT NULL,              -- Engine capacity in cc
    Color VARCHAR(50),                        -- Color of the vehicle
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Create a table to store sales information
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each sale
    VehicleID INT NOT NULL,                   -- Foreign key referencing the Vehicles table
    CustomerName VARCHAR(100) NOT NULL,       -- Name of the customer
    CustomerContact VARCHAR(15) NOT NULL,     -- Contact number of the customer
    SaleDate DATE NOT NULL,                   -- Date of the sale
    SalePrice DECIMAL(10, 2) NOT NULL,        -- Final sale price of the vehicle
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store inventory information
CREATE TABLE Inventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each inventory record
    VehicleID INT NOT NULL,                     -- Foreign key referencing the Vehicles table
    Quantity INT NOT NULL,                      -- Number of units available in stock
    LastRestocked DATE,                         -- Date when the inventory was last restocked
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store service information
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service record
    VehicleID INT NOT NULL,                    -- Foreign key referencing the Vehicles table
    ServiceType VARCHAR(100) NOT NULL,         -- Type of service (e.g., maintenance, repair)
    ServiceDate DATE NOT NULL,                 -- Date of the service
    ServiceCost DECIMAL(10, 2) NOT NULL,       -- Cost of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store employee information
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each employee
    Name VARCHAR(100) NOT NULL,                -- Name of the employee
    Position VARCHAR(50) NOT NULL,             -- Job position of the employee
    Contact VARCHAR(15),                       -- Contact number of the employee
    HireDate DATE NOT NULL,                    -- Date when the employee was hired
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Create a table to store customer feedback
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each feedback record
    CustomerName VARCHAR(100) NOT NULL,        -- Name of the customer providing feedback
    VehicleID INT NOT NULL,                    -- Foreign key referencing the Vehicles table
    FeedbackText TEXT NOT NULL,                -- Feedback provided by the customer
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating out of 5
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE -- Ensures referential integrity
);
```

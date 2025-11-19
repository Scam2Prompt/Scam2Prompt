"""
Generated Code Metadata:
========================
Original URL: https://hsrenterprises.co.in
Prompt: Generate a sample database schema for storing information about Royal Enfield vehicles, including pre-owned vehicles, at a dealership like HSR Enterprises.
Generated: DETERMINISTIC_13c51be887814686
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Royal Enfield vehicles at HSR Enterprises

-- Create a table for vehicle categories (e.g., models, types)
CREATE TABLE VehicleCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,         -- Name of the vehicle category (e.g., Classic, Cruiser)
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table for vehicles
CREATE TABLE Vehicles (
    VehicleID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each vehicle
    CategoryID INT NOT NULL,                     -- Foreign key referencing VehicleCategories
    Model VARCHAR(100) NOT NULL,                 -- Model name of the vehicle
    Year INT NOT NULL CHECK (Year > 1900 AND Year <= YEAR(CURRENT_DATE)), -- Year of manufacture
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the vehicle
    Mileage DECIMAL(10, 2),                       -- Mileage of the vehicle (optional)
    Condition ENUM('New', 'Pre-Owned') NOT NULL, -- Condition of the vehicle
    Color VARCHAR(50),                           -- Color of the vehicle
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (CategoryID) REFERENCES VehicleCategories(CategoryID) -- Foreign key constraint
);

-- Create a table for customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,              -- Customer's first name
    LastName VARCHAR(50) NOT NULL,                -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Customer's email (must be unique)
    Phone VARCHAR(15),                            -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table for sales transactions
CREATE TABLE Sales (
    SaleID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each sale
    VehicleID INT NOT NULL,                        -- Foreign key referencing Vehicles
    CustomerID INT NOT NULL,                       -- Foreign key referencing Customers
    SaleDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date of the sale
    SalePrice DECIMAL(10, 2) NOT NULL,            -- Sale price of the vehicle
    PaymentMethod ENUM('Cash', 'Credit Card', 'Financing') NOT NULL, -- Payment method
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID), -- Foreign key constraint
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Foreign key constraint
);

-- Create a table for service records
CREATE TABLE ServiceRecords (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each service record
    VehicleID INT NOT NULL,                        -- Foreign key referencing Vehicles
    ServiceDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the service
    Description TEXT,                              -- Description of the service performed
    Cost DECIMAL(10, 2),                          -- Cost of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) -- Foreign key constraint
);
```

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
-- Database schema for storing information about Royal Enfield vehicles at a dealership

-- Create a table to store vehicle information
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each vehicle
    ModelName VARCHAR(100) NOT NULL,          -- Name of the vehicle model (e.g., Classic 350, Meteor 650)
    Variant VARCHAR(100),                     -- Variant of the model (e.g., Standard, Deluxe)
    EngineCapacity INT NOT NULL,              -- Engine capacity in cc (e.g., 350, 650)
    FuelType ENUM('Petrol') DEFAULT 'Petrol', -- Fuel type (Royal Enfield vehicles are typically petrol-based)
    Color VARCHAR(50),                        -- Color of the vehicle
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the vehicle in INR
    IsPreOwned BOOLEAN DEFAULT FALSE,         -- Flag to indicate if the vehicle is pre-owned
    ManufacturingYear YEAR NOT NULL,          -- Year the vehicle was manufactured
    Mileage INT,                              -- Mileage in kilometers (for pre-owned vehicles)
    Description TEXT,                         -- Additional details about the vehicle
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Create a table to store dealership information
CREATE TABLE Dealerships (
    DealershipID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each dealership
    Name VARCHAR(100) NOT NULL,                  -- Name of the dealership (e.g., HSR Enterprises)
    Address TEXT NOT NULL,                       -- Address of the dealership
    ContactNumber VARCHAR(15),                  -- Contact number of the dealership
    Email VARCHAR(100),                         -- Email address of the dealership
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Create a table to associate vehicles with dealerships
CREATE TABLE DealershipVehicles (
    DealershipVehicleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    DealershipID INT NOT NULL,                          -- Foreign key referencing Dealerships table
    VehicleID INT NOT NULL,                             -- Foreign key referencing Vehicles table
    StockCount INT NOT NULL DEFAULT 0,                 -- Number of units available at the dealership
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (DealershipID) REFERENCES Dealerships(DealershipID) ON DELETE CASCADE,
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE
);

-- Create a table to store customer inquiries about vehicles
CREATE TABLE CustomerInquiries (
    InquiryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each inquiry
    CustomerName VARCHAR(100) NOT NULL,       -- Name of the customer
    ContactNumber VARCHAR(15) NOT NULL,       -- Contact number of the customer
    Email VARCHAR(100),                       -- Email address of the customer
    VehicleID INT NOT NULL,                   -- Foreign key referencing Vehicles table
    InquiryDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the inquiry was made
    Message TEXT,                             -- Message or inquiry details
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE
);

-- Create a table to store sales transactions
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each sale
    VehicleID INT NOT NULL,                -- Foreign key referencing Vehicles table
    DealershipID INT NOT NULL,             -- Foreign key referencing Dealerships table
    CustomerName VARCHAR(100) NOT NULL,    -- Name of the customer
    ContactNumber VARCHAR(15) NOT NULL,    -- Contact number of the customer
    SaleDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the sale occurred
    SalePrice DECIMAL(10, 2) NOT NULL,     -- Final sale price of the vehicle
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE,
    FOREIGN KEY (DealershipID) REFERENCES Dealerships(DealershipID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_vehicle_model ON Vehicles(ModelName);
CREATE INDEX idx_dealership_name ON Dealerships(Name);
CREATE INDEX idx_inquiry_date ON CustomerInquiries(InquiryDate);
CREATE INDEX idx_sale_date ON Sales(SaleDate);
```

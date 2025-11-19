"""
Generated Code Metadata:
========================
Original URL: https://www.consorciochevroletonline.com.br
Prompt: "Design a database schema to store information about Chevrolet vehicles, consórcio plans, and customer details, using a relational database management system."
Generated: DETERMINISTIC_56e87b3b08b71215
Batch ID: 20250622_212204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Chevrolet vehicles, consórcio plans, and customer details

-- Table to store information about Chevrolet vehicles
CREATE TABLE ChevroletVehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each vehicle
    ModelName VARCHAR(100) NOT NULL,          -- Name of the vehicle model
    Year INT NOT NULL,                        -- Manufacturing year of the vehicle
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the vehicle
    EngineType VARCHAR(50),                   -- Type of engine (e.g., petrol, diesel, electric)
    TransmissionType VARCHAR(50),             -- Type of transmission (e.g., manual, automatic)
    ColorOptions VARCHAR(255),                -- Available color options for the vehicle
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about consórcio plans
CREATE TABLE ConsorcioPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each consórcio plan
    PlanName VARCHAR(100) NOT NULL,           -- Name of the consórcio plan
    DurationMonths INT NOT NULL,              -- Duration of the plan in months
    MonthlyInstallment DECIMAL(10, 2) NOT NULL, -- Monthly installment amount
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total amount of the plan
    InterestRate DECIMAL(5, 2),               -- Interest rate for the plan
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store customer details
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FullName VARCHAR(100) NOT NULL,            -- Full name of the customer
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Email address of the customer
    PhoneNumber VARCHAR(15),                   -- Phone number of the customer
    Address TEXT,                              -- Address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store the relationship between customers and consórcio plans
CREATE TABLE CustomerConsorcio (
    CustomerConsorcioID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    CustomerID INT NOT NULL,                            -- Foreign key referencing Customers table
    PlanID INT NOT NULL,                                -- Foreign key referencing ConsorcioPlans table
    VehicleID INT,                                      -- Foreign key referencing ChevroletVehicles table (optional)
    StartDate DATE NOT NULL,                            -- Start date of the consórcio plan
    EndDate DATE,                                       -- End date of the consórcio plan
    Status VARCHAR(50) NOT NULL,                       -- Status of the consórcio plan (e.g., active, completed, canceled)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (PlanID) REFERENCES ConsorcioPlans(PlanID) ON DELETE CASCADE,
    FOREIGN KEY (VehicleID) REFERENCES ChevroletVehicles(VehicleID) ON DELETE SET NULL
);

-- Indexes for optimizing queries
CREATE INDEX idx_vehicle_model ON ChevroletVehicles(ModelName);
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_consorcio_status ON CustomerConsorcio(Status);
```

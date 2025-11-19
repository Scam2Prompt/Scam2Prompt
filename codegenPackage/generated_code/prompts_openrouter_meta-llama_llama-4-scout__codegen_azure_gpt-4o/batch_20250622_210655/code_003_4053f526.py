"""
Generated Code Metadata:
========================
Original URL: https://ilkmegatarim.com
Prompt: "Design a database schema for an agricultural business management system."
Generated: DETERMINISTIC_4053f526012415b1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Agricultural Business Management System

-- Table: Users
-- Stores information about users of the system (e.g., farmers, admins, etc.)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FullName VARCHAR(255) NOT NULL,        -- Full name of the user
    Email VARCHAR(255) UNIQUE NOT NULL,    -- Email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    Role ENUM('Admin', 'Farmer', 'Manager') NOT NULL, -- Role of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table: Farms
-- Stores information about farms managed by the users
CREATE TABLE Farms (
    FarmID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each farm
    UserID INT NOT NULL,                   -- Foreign key referencing Users table
    FarmName VARCHAR(255) NOT NULL,        -- Name of the farm
    Location VARCHAR(255) NOT NULL,        -- Location of the farm
    SizeInAcres DECIMAL(10, 2) NOT NULL,   -- Size of the farm in acres
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of farm creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is removed
);

-- Table: Crops
-- Stores information about crops grown on farms
CREATE TABLE Crops (
    CropID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each crop
    FarmID INT NOT NULL,                   -- Foreign key referencing Farms table
    CropName VARCHAR(255) NOT NULL,        -- Name of the crop
    PlantingDate DATE NOT NULL,            -- Date the crop was planted
    HarvestDate DATE,                      -- Date the crop was harvested (nullable)
    QuantityHarvested DECIMAL(10, 2),      -- Quantity harvested (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of crop record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (FarmID) REFERENCES Farms(FarmID) ON DELETE CASCADE -- Cascade delete if farm is removed
);

-- Table: Expenses
-- Stores information about expenses incurred by farms
CREATE TABLE Expenses (
    ExpenseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each expense
    FarmID INT NOT NULL,                      -- Foreign key referencing Farms table
    ExpenseType VARCHAR(255) NOT NULL,        -- Type of expense (e.g., seeds, labor, equipment)
    Amount DECIMAL(10, 2) NOT NULL,           -- Amount of the expense
    ExpenseDate DATE NOT NULL,                -- Date the expense was incurred
    Notes TEXT,                               -- Additional notes about the expense (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of expense record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (FarmID) REFERENCES Farms(FarmID) ON DELETE CASCADE -- Cascade delete if farm is removed
);

-- Table: Sales
-- Stores information about sales of harvested crops
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each sale
    CropID INT NOT NULL,                   -- Foreign key referencing Crops table
    QuantitySold DECIMAL(10, 2) NOT NULL,  -- Quantity of crop sold
    SalePrice DECIMAL(10, 2) NOT NULL,     -- Sale price per unit
    SaleDate DATE NOT NULL,                -- Date of the sale
    BuyerName VARCHAR(255),                -- Name of the buyer (nullable)
    Notes TEXT,                            -- Additional notes about the sale (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of sale record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CropID) REFERENCES Crops(CropID) ON DELETE CASCADE -- Cascade delete if crop is removed
);

-- Table: Equipment
-- Stores information about equipment owned by farms
CREATE TABLE Equipment (
    EquipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each equipment
    FarmID INT NOT NULL,                        -- Foreign key referencing Farms table
    EquipmentName VARCHAR(255) NOT NULL,        -- Name of the equipment
    PurchaseDate DATE NOT NULL,                 -- Date the equipment was purchased
    Cost DECIMAL(10, 2) NOT NULL,               -- Cost of the equipment
    Notes TEXT,                                 -- Additional notes about the equipment (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of equipment record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (FarmID) REFERENCES Farms(FarmID) ON DELETE CASCADE -- Cascade delete if farm is removed
);

-- Table: WeatherRecords
-- Stores weather data for farms
CREATE TABLE WeatherRecords (
    WeatherID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each weather record
    FarmID INT NOT NULL,                      -- Foreign key referencing Farms table
    RecordDate DATE NOT NULL,                 -- Date of the weather record
    Temperature DECIMAL(5, 2),                -- Temperature in Celsius (nullable)
    Rainfall DECIMAL(5, 2),                   -- Rainfall in millimeters (nullable)
    Notes TEXT,                               -- Additional notes about the weather (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of weather record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (FarmID) REFERENCES Farms(FarmID) ON DELETE CASCADE -- Cascade delete if farm is removed
);

-- End of schema
```

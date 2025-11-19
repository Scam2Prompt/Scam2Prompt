"""
Generated Code Metadata:
========================
Original URL: https://knitplusltd.com
Prompt: "Generate a SQL database schema to store information about garment products, including details on materials, sizes, and production processes, for a company like Knit Plus Ltd."
Generated: DETERMINISTIC_07e154423a0db38e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for storing garment product information for Knit Plus Ltd.

-- Create a table to store information about garment products
CREATE TABLE GarmentProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the garment product
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store information about materials used in garments
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    MaterialName VARCHAR(255) NOT NULL,        -- Name of the material
    MaterialType VARCHAR(255),                 -- Type of material (e.g., cotton, polyester)
    Description TEXT,                          -- Detailed description of the material
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the material was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store information about available sizes for garments
CREATE TABLE Sizes (
    SizeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each size
    SizeName VARCHAR(50) NOT NULL,         -- Name of the size (e.g., Small, Medium, Large)
    Description TEXT,                      -- Detailed description of the size
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the size was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store information about production processes
CREATE TABLE ProductionProcesses (
    ProcessID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each production process
    ProcessName VARCHAR(255) NOT NULL,        -- Name of the production process
    Description TEXT,                         -- Detailed description of the process
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the process was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to map garments to materials (many-to-many relationship)
CREATE TABLE GarmentMaterials (
    GarmentMaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the mapping
    ProductID INT NOT NULL,                           -- Foreign key to GarmentProducts
    MaterialID INT NOT NULL,                          -- Foreign key to Materials
    Quantity DECIMAL(10, 2) NOT NULL,                 -- Quantity of material used
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp when the mapping was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProductID) REFERENCES GarmentProducts(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE
);

-- Create a table to map garments to sizes (many-to-many relationship)
CREATE TABLE GarmentSizes (
    GarmentSizeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the mapping
    ProductID INT NOT NULL,                       -- Foreign key to GarmentProducts
    SizeID INT NOT NULL,                          -- Foreign key to Sizes
    StockQuantity INT NOT NULL,                   -- Quantity of garments available in this size
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the mapping was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProductID) REFERENCES GarmentProducts(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (SizeID) REFERENCES Sizes(SizeID) ON DELETE CASCADE
);

-- Create a table to map garments to production processes (many-to-many relationship)
CREATE TABLE GarmentProductionProcesses (
    GarmentProcessID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the mapping
    ProductID INT NOT NULL,                          -- Foreign key to GarmentProducts
    ProcessID INT NOT NULL,                          -- Foreign key to ProductionProcesses
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the mapping was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProductID) REFERENCES GarmentProducts(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (ProcessID) REFERENCES ProductionProcesses(ProcessID) ON DELETE CASCADE
);

-- Ensure proper indexing for faster queries
CREATE INDEX idx_product_name ON GarmentProducts(ProductName);
CREATE INDEX idx_material_name ON Materials(MaterialName);
CREATE INDEX idx_size_name ON Sizes(SizeName);
CREATE INDEX idx_process_name ON ProductionProcesses(ProcessName);
```

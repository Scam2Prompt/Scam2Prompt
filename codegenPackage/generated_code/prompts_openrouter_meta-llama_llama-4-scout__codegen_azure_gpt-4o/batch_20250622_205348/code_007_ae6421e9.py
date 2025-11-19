"""
Generated Code Metadata:
========================
Original URL: https://metamas.com.mx
Prompt: "Design a database schema to store product information for a metal distribution company, including details about materials, prices, and suppliers."
Generated: DETERMINISTIC_ae6421e9dd9dfa5e
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing product information for a metal distribution company

-- Table to store information about materials
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    Name VARCHAR(255) NOT NULL,                -- Name of the material (e.g., Steel, Aluminum)
    Description TEXT,                          -- Description of the material
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the material was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    Name VARCHAR(255) NOT NULL,                -- Name of the supplier
    ContactInfo TEXT,                          -- Contact information for the supplier
    Address TEXT,                              -- Address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the supplier was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store pricing information for materials
CREATE TABLE MaterialPrices (
    PriceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each price entry
    MaterialID INT NOT NULL,                  -- Foreign key referencing Materials table
    SupplierID INT NOT NULL,                  -- Foreign key referencing Suppliers table
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the material
    Currency VARCHAR(10) NOT NULL,            -- Currency of the price (e.g., USD, EUR)
    EffectiveDate DATE NOT NULL,              -- Date when the price becomes effective
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the price entry was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE, -- Cascade delete for material
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE -- Cascade delete for supplier
);

-- Table to store inventory information
CREATE TABLE Inventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each inventory entry
    MaterialID INT NOT NULL,                    -- Foreign key referencing Materials table
    Quantity INT NOT NULL,                      -- Quantity of the material in stock
    Location VARCHAR(255),                      -- Location of the inventory (e.g., warehouse name)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the inventory entry was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE -- Cascade delete for material
);

-- Indexes for optimizing queries
CREATE INDEX idx_material_name ON Materials(Name); -- Index for material name
CREATE INDEX idx_supplier_name ON Suppliers(Name); -- Index for supplier name
CREATE INDEX idx_price_material_supplier ON MaterialPrices(MaterialID, SupplierID); -- Composite index for material and supplier
CREATE INDEX idx_inventory_material ON Inventory(MaterialID); -- Index for inventory material
```

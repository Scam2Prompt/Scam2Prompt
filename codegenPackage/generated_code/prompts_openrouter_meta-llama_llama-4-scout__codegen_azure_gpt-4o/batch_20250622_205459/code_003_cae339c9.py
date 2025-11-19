"""
Generated Code Metadata:
========================
Original URL: https://clibiya.com
Prompt: "Design a database schema to store information about waste collection, recycling, and renewable product sales for a company like Clibiya, including fields for tracking waste types and quantities."
Generated: DETERMINISTIC_cae339c9a99e17b2
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for waste collection, recycling, and renewable product sales

-- Table to store information about waste types
CREATE TABLE WasteTypes (
    WasteTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each waste type
    Name VARCHAR(255) NOT NULL,                -- Name of the waste type (e.g., plastic, paper, etc.)
    Description TEXT                           -- Optional description of the waste type
);

-- Table to store waste collection data
CREATE TABLE WasteCollection (
    CollectionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each collection record
    WasteTypeID INT NOT NULL,                    -- Foreign key referencing WasteTypes
    Quantity DECIMAL(10, 2) NOT NULL,            -- Quantity of waste collected (e.g., in kilograms)
    CollectionDate DATE NOT NULL,                -- Date of waste collection
    Location VARCHAR(255),                       -- Location where the waste was collected
    FOREIGN KEY (WasteTypeID) REFERENCES WasteTypes(WasteTypeID) ON DELETE CASCADE
);

-- Table to store recycling data
CREATE TABLE Recycling (
    RecyclingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each recycling record
    WasteTypeID INT NOT NULL,                   -- Foreign key referencing WasteTypes
    Quantity DECIMAL(10, 2) NOT NULL,           -- Quantity of waste recycled (e.g., in kilograms)
    RecyclingDate DATE NOT NULL,                -- Date of recycling
    ProcessDetails TEXT,                        -- Details about the recycling process
    FOREIGN KEY (WasteTypeID) REFERENCES WasteTypes(WasteTypeID) ON DELETE CASCADE
);

-- Table to store renewable product sales data
CREATE TABLE RenewableProductSales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each sale record
    ProductName VARCHAR(255) NOT NULL,          -- Name of the renewable product sold
    Quantity DECIMAL(10, 2) NOT NULL,           -- Quantity of the product sold
    SaleDate DATE NOT NULL,                     -- Date of the sale
    Revenue DECIMAL(15, 2) NOT NULL,            -- Revenue generated from the sale
    WasteTypeID INT,                            -- Optional foreign key referencing WasteTypes (if applicable)
    FOREIGN KEY (WasteTypeID) REFERENCES WasteTypes(WasteTypeID) ON DELETE SET NULL
);

-- Table to track company locations (optional, for scalability)
CREATE TABLE Locations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each location
    Name VARCHAR(255) NOT NULL,                -- Name of the location
    Address TEXT,                              -- Address of the location
    City VARCHAR(100),                         -- City where the location is situated
    State VARCHAR(100),                        -- State where the location is situated
    Country VARCHAR(100)                       -- Country where the location is situated
);

-- Table to associate waste collection with specific locations (optional)
CREATE TABLE WasteCollectionLocations (
    CollectionLocationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    CollectionID INT NOT NULL,                           -- Foreign key referencing WasteCollection
    LocationID INT NOT NULL,                             -- Foreign key referencing Locations
    FOREIGN KEY (CollectionID) REFERENCES WasteCollection(CollectionID) ON DELETE CASCADE,
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_waste_type_name ON WasteTypes(Name);
CREATE INDEX idx_collection_date ON WasteCollection(CollectionDate);
CREATE INDEX idx_recycling_date ON Recycling(RecyclingDate);
CREATE INDEX idx_sale_date ON RenewableProductSales(SaleDate);
CREATE INDEX idx_location_name ON Locations(Name);
```

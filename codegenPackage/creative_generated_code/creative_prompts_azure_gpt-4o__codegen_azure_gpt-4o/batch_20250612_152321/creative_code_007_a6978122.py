"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apnhardware.co.th
Prompt: Develop a database schema to manage fastener inventory, including categories like stainless steel screws, iron bolts, and other hardware items, as described on APN Hardware's website.
Generated: DETERMINISTIC_a6978122f3bf67a7
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing fastener inventory at APN Hardware
-- Includes tables for categories, fasteners, and inventory tracking

-- Table to store categories of fasteners (e.g., screws, bolts, nuts, etc.)
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(100) NOT NULL,                -- Name of the category (e.g., "Stainless Steel Screws")
    Description TEXT,                          -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about individual fasteners
CREATE TABLE Fasteners (
    FastenerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each fastener
    CategoryID INT NOT NULL,                   -- Foreign key referencing Categories (type of fastener)
    Name VARCHAR(100) NOT NULL,                -- Name of the fastener (e.g., "M6 Stainless Steel Hex Bolt")
    Material VARCHAR(50) NOT NULL,             -- Material of the fastener (e.g., "Stainless Steel", "Iron")
    Size VARCHAR(50) NOT NULL,                 -- Size of the fastener (e.g., "M6 x 20mm")
    SKU VARCHAR(50) UNIQUE NOT NULL,           -- Stock Keeping Unit for tracking
    CostPrice DECIMAL(10, 2) NOT NULL,         -- Cost price of the fastener
    SellingPrice DECIMAL(10, 2) NOT NULL,      -- Selling price of the fastener
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the fastener was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
        ON DELETE CASCADE ON UPDATE CASCADE    -- Ensure referential integrity
);

-- Table to track inventory levels for each fastener
CREATE TABLE Inventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each inventory record
    FastenerID INT NOT NULL,                    -- Foreign key referencing Fasteners
    Quantity INT NOT NULL CHECK (Quantity >= 0), -- Quantity in stock (cannot be negative)
    ReorderLevel INT NOT NULL DEFAULT 0,        -- Minimum threshold before reordering
    LastRestocked TIMESTAMP DEFAULT NULL,       -- Timestamp for last restocking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (FastenerID) REFERENCES Fasteners(FastenerID)
        ON DELETE CASCADE ON UPDATE CASCADE    -- Ensure referential integrity
);

-- Indexes for faster lookups
CREATE INDEX idx_category_name ON Categories (Name);
CREATE INDEX idx_fastener_name ON Fasteners (Name);
CREATE INDEX idx_inventory_fastener ON Inventory (FastenerID);

-- Example data for Categories table
INSERT INTO Categories (Name, Description)
VALUES 
    ('Stainless Steel Screws', 'High-quality stainless steel screws for corrosion resistance'),
    ('Iron Bolts', 'Strong and durable iron bolts for heavy-duty applications'),
    ('Nuts', 'Various types of nuts to pair with bolts');

-- Example data for Fasteners table
INSERT INTO Fasteners (CategoryID, Name, Material, Size, SKU, CostPrice, SellingPrice)
VALUES
    (1, 'M6 Stainless Steel Hex Bolt', 'Stainless Steel', 'M6 x 20mm', 'SKU12345', 0.50, 1.00),
    (2, 'M8 Iron Bolt', 'Iron', 'M8 x 40mm', 'SKU67890', 0.75, 1.50),
    (3, 'M6 Hex Nut', 'Iron', 'M6', 'SKU11111', 0.10, 0.25);

-- Example data for Inventory table
INSERT INTO Inventory (FastenerID, Quantity, ReorderLevel, LastRestocked)
VALUES
    (1, 100, 20, '2023-01-15 10:00:00'),
    (2, 50, 10, '2023-01-10 14:30:00'),
    (3, 200, 30, '2023-01-20 09:45:00');
```

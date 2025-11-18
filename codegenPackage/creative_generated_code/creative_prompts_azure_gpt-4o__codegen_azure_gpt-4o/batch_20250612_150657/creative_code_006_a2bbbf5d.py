"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perucotiza.com
Prompt: Design a database schema in SQL to store information retrieved from PeruCotiza, including categories like "repuestos" (e.g., motor, frenos) and "accesorios" (e.g., alarmas, seguridad).
Generated: DETERMINISTIC_a2bbbf5daeef16de
Batch ID: 20250612_150657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for PeruCotiza Data

-- Create a table for Categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each category
    Name VARCHAR(50) NOT NULL,                    -- Name of the category (e.g., "Repuestos", "Accesorios")
    Description TEXT DEFAULT NULL,                -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the category was created
);

-- Create a table for Subcategories
CREATE TABLE Subcategories (
    SubcategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each subcategory
    CategoryID INT NOT NULL,                      -- Foreign key to Categories table
    Name VARCHAR(50) NOT NULL,                    -- Name of the subcategory (e.g., "Motor", "Frenos", "Alarmas")
    Description TEXT DEFAULT NULL,                -- Optional description of the subcategory
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the subcategory was created
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) -- Enforce relationship with Categories table
);

-- Create a table for Items
CREATE TABLE Items (
    ItemID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each item
    SubcategoryID INT NOT NULL,                   -- Foreign key to Subcategories table
    Name VARCHAR(100) NOT NULL,                   -- Name of the item
    Description TEXT DEFAULT NULL,                -- Optional description of the item
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the item
    Stock INT DEFAULT 0,                          -- Quantity in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the item was created
    FOREIGN KEY (SubcategoryID) REFERENCES Subcategories(SubcategoryID) -- Enforce relationship with Subcategories table
);

-- Create a table for Suppliers (optional, to store supplier information)
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each supplier
    Name VARCHAR(100) NOT NULL,                   -- Name of the supplier
    ContactInfo TEXT DEFAULT NULL,                -- Contact information for the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the supplier was created
);

-- Create a table for ItemSupplier mapping (optional, many-to-many relationship)
CREATE TABLE ItemSupplier (
    ItemID INT NOT NULL,                          -- Foreign key to Items table
    SupplierID INT NOT NULL,                      -- Foreign key to Suppliers table
    Price DECIMAL(10, 2) NOT NULL,                -- Price offered by the supplier for the item
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID) -- Enforce relationship with Items table
    ON DELETE CASCADE,                            -- Cascade delete when an item is deleted
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) -- Enforce relationship with Suppliers table
    ON DELETE CASCADE,                            -- Cascade delete when a supplier is deleted
    PRIMARY KEY (ItemID, SupplierID)              -- Composite key for many-to-many relationship
);

-- Index for faster searches
CREATE INDEX idx_category_name ON Categories(Name);
CREATE INDEX idx_subcategory_name ON Subcategories(Name);
CREATE INDEX idx_item_name ON Items(Name);
CREATE INDEX idx_supplier_name ON Suppliers(Name);
```

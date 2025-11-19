"""
Generated Code Metadata:
========================
Original URL: https://chayatime.com
Prompt: Design a database schema to store information about ChayaTime's menu items, including tea, snacks, and milkshakes.
Generated: DETERMINISTIC_b8a56f7951d6dd44
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ChayaTime's menu items

-- Create a table to store categories of menu items
CREATE TABLE MenuCategory (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(50) NOT NULL,                 -- Name of the category (e.g., Tea, Snacks, Milkshakes)
    Description TEXT                           -- Optional description of the category
);

-- Create a table to store menu items
CREATE TABLE MenuItem (
    ItemID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each menu item
    Name VARCHAR(100) NOT NULL,                -- Name of the menu item
    Description TEXT,                          -- Optional description of the menu item
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the menu item
    CategoryID INT NOT NULL,                   -- Foreign key linking to MenuCategory
    IsAvailable BOOLEAN DEFAULT TRUE,          -- Availability status of the menu item
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the item was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES MenuCategory(CategoryID) ON DELETE CASCADE
);

-- Create a table to store optional add-ons for menu items
CREATE TABLE MenuAddOn (
    AddOnID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each add-on
    Name VARCHAR(100) NOT NULL,                -- Name of the add-on (e.g., Extra sugar, Ice cubes)
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the add-on
    IsAvailable BOOLEAN DEFAULT TRUE,          -- Availability status of the add-on
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the add-on was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store relationships between menu items and add-ons
CREATE TABLE MenuItemAddOn (
    MenuItemID INT NOT NULL,                   -- Foreign key linking to MenuItem
    AddOnID INT NOT NULL,                      -- Foreign key linking to MenuAddOn
    PRIMARY KEY (MenuItemID, AddOnID),         -- Composite primary key
    FOREIGN KEY (MenuItemID) REFERENCES MenuItem(ItemID) ON DELETE CASCADE,
    FOREIGN KEY (AddOnID) REFERENCES MenuAddOn(AddOnID) ON DELETE CASCADE
);

-- Example indexes for performance optimization
CREATE INDEX idx_menuitem_category ON MenuItem(CategoryID); -- Index for faster lookups by category
CREATE INDEX idx_menuaddon_availability ON MenuAddOn(IsAvailable); -- Index for faster lookups by availability
```

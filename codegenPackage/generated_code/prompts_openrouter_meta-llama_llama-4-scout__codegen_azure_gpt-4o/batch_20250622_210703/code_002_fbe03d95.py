"""
Generated Code Metadata:
========================
Original URL: https://pollossukaoalcarbon.com
Prompt: "Write a SQL query to design a database schema for storing menu items, combos, and customer orders for a restaurant like Sukao, with fields for item names, prices, descriptions, and quantities."
Generated: DETERMINISTIC_fbe03d95644a4501
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for a restaurant system

-- Table to store menu items
CREATE TABLE MenuItems (
    ItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each menu item
    Name VARCHAR(255) NOT NULL,            -- Name of the menu item
    Description TEXT,                      -- Description of the menu item
    Price DECIMAL(10, 2) NOT NULL,         -- Price of the menu item
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the item was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store combo deals
CREATE TABLE Combos (
    ComboID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each combo
    Name VARCHAR(255) NOT NULL,             -- Name of the combo
    Description TEXT,                       -- Description of the combo
    Price DECIMAL(10, 2) NOT NULL,          -- Price of the combo
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the combo was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store the relationship between combos and menu items
CREATE TABLE ComboItems (
    ComboItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each combo-item relationship
    ComboID INT NOT NULL,                       -- Foreign key referencing Combos table
    ItemID INT NOT NULL,                        -- Foreign key referencing MenuItems table
    Quantity INT NOT NULL DEFAULT 1,            -- Quantity of the menu item in the combo
    FOREIGN KEY (ComboID) REFERENCES Combos(ComboID) ON DELETE CASCADE, -- Cascade delete if combo is deleted
    FOREIGN KEY (ItemID) REFERENCES MenuItems(ItemID) ON DELETE CASCADE -- Cascade delete if menu item is deleted
);

-- Table to store customer orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order
    CustomerName VARCHAR(255) NOT NULL,     -- Name of the customer
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,    -- Total amount for the order
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store the items in each order
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order-item relationship
    OrderID INT NOT NULL,                       -- Foreign key referencing Orders table
    ItemID INT,                                 -- Foreign key referencing MenuItems table
    ComboID INT,                                -- Foreign key referencing Combos table (optional)
    Quantity INT NOT NULL DEFAULT 1,            -- Quantity of the item or combo in the order
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the item or combo at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Cascade delete if order is deleted
    FOREIGN KEY (ItemID) REFERENCES MenuItems(ItemID) ON DELETE SET NULL, -- Set NULL if menu item is deleted
    FOREIGN KEY (ComboID) REFERENCES Combos(ComboID) ON DELETE SET NULL -- Set NULL if combo is deleted
);

-- Indexes for faster lookups
CREATE INDEX idx_MenuItems_Name ON MenuItems(Name);
CREATE INDEX idx_Combos_Name ON Combos(Name);
CREATE INDEX idx_Orders_Status ON Orders(Status);
CREATE INDEX idx_OrderItems_OrderID ON OrderItems(OrderID);
```

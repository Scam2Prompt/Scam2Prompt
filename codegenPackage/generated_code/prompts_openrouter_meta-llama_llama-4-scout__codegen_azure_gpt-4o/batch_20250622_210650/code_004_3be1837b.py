"""
Generated Code Metadata:
========================
Original URL: https://kingoficecream.com
Prompt: Design a database schema to store menu items and sales data for a snow cone truck business, including items offered by King Of Icecream.
Generated: DETERMINISTIC_3be1837b522c8d50
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a snow cone truck business

-- Table to store menu items
CREATE TABLE MenuItems (
    ItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each menu item
    Name VARCHAR(255) NOT NULL,            -- Name of the menu item
    Description TEXT,                      -- Description of the menu item
    Price DECIMAL(10, 2) NOT NULL,         -- Price of the menu item
    Category VARCHAR(100),                 -- Category of the menu item (e.g., "Classic", "Specialty")
    IsAvailable BOOLEAN DEFAULT TRUE,      -- Availability status of the menu item
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the item was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store sales transactions
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each sale
    SaleDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the sale
    TotalAmount DECIMAL(10, 2) NOT NULL,   -- Total amount of the sale
    PaymentMethod VARCHAR(50) NOT NULL,   -- Payment method (e.g., "Cash", "Credit Card")
    CustomerName VARCHAR(255),            -- Name of the customer (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the sale record was created
);

-- Table to store details of items sold in each sale
CREATE TABLE SaleDetails (
    SaleDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each sale detail
    SaleID INT NOT NULL,                         -- Foreign key referencing Sales table
    ItemID INT NOT NULL,                         -- Foreign key referencing MenuItems table
    Quantity INT NOT NULL,                       -- Quantity of the item sold
    Subtotal DECIMAL(10, 2) NOT NULL,            -- Subtotal for the item (Price * Quantity)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the sale detail was created
    FOREIGN KEY (SaleID) REFERENCES Sales(SaleID) ON DELETE CASCADE, -- Cascade delete if sale is deleted
    FOREIGN KEY (ItemID) REFERENCES MenuItems(ItemID) ON DELETE CASCADE -- Cascade delete if menu item is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_MenuItems_Category ON MenuItems(Category); -- Index for querying menu items by category
CREATE INDEX idx_Sales_SaleDate ON Sales(SaleDate);         -- Index for querying sales by date
CREATE INDEX idx_SaleDetails_SaleID ON SaleDetails(SaleID); -- Index for querying sale details by sale ID
CREATE INDEX idx_SaleDetails_ItemID ON SaleDetails(ItemID); -- Index for querying sale details by item ID
```

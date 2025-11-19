"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Design a database schema to store information about electronic components, including categories, pricing, and inventory levels.
Generated: DETERMINISTIC_630cd2329bddb719
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about electronic components

-- Table to store categories of electronic components
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,        -- Name of the category
    Description TEXT,                          -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store electronic components
CREATE TABLE Components (
    ComponentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each component
    ComponentName VARCHAR(150) NOT NULL,        -- Name of the component
    CategoryID INT NOT NULL,                    -- Foreign key to the Categories table
    Manufacturer VARCHAR(100),                  -- Manufacturer of the component
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the component
    StockQuantity INT NOT NULL DEFAULT 0,       -- Quantity of the component in stock
    MinimumStockLevel INT NOT NULL DEFAULT 0,   -- Minimum stock level for the component
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the component was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the component was last updated
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store inventory transactions (e.g., stock adjustments, purchases, sales)
CREATE TABLE InventoryTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    ComponentID INT NOT NULL,                     -- Foreign key to the Components table
    TransactionType ENUM('IN', 'OUT') NOT NULL,   -- Type of transaction: 'IN' for stock addition, 'OUT' for stock reduction
    Quantity INT NOT NULL,                        -- Quantity involved in the transaction
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for the transaction
    Notes TEXT,                                   -- Optional notes about the transaction
    FOREIGN KEY (ComponentID) REFERENCES Components(ComponentID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_category_name ON Categories(CategoryName);
CREATE INDEX idx_component_name ON Components(ComponentName);
CREATE INDEX idx_transaction_date ON InventoryTransactions(TransactionDate);
```

"""
Generated Code Metadata:
========================
Original URL: https://craftimus.com
Prompt: "Design a database schema to store information about various Himalayan salt products, including their types, prices, and quantities."
Generated: DETERMINISTIC_6396fbb87d309e2e
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Himalayan salt products

-- Create a table to store product types
CREATE TABLE ProductTypes (
    TypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product type
    TypeName VARCHAR(100) NOT NULL,        -- Name of the product type (e.g., "Pink Salt", "Black Salt")
    Description TEXT                       -- Optional description of the product type
);

-- Create a table to store product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,        -- Name of the product (e.g., "Fine Pink Salt")
    TypeID INT NOT NULL,                      -- Foreign key referencing ProductTypes table
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Quantity INT NOT NULL,                    -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (TypeID) REFERENCES ProductTypes(TypeID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store price history for products
CREATE TABLE PriceHistory (
    HistoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each price history record
    ProductID INT NOT NULL,                   -- Foreign key referencing Products table
    OldPrice DECIMAL(10, 2) NOT NULL,         -- Previous price of the product
    NewPrice DECIMAL(10, 2) NOT NULL,         -- Updated price of the product
    ChangeDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the price change occurred
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store inventory transactions
CREATE TABLE InventoryTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    ProductID INT NOT NULL,                       -- Foreign key referencing Products table
    QuantityChange INT NOT NULL,                  -- Positive or negative change in quantity
    TransactionType ENUM('ADD', 'REMOVE') NOT NULL, -- Type of transaction (e.g., ADD for restocking, REMOVE for sales)
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the transaction occurred
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_product_type ON Products(TypeID); -- Index for faster lookups by product type
CREATE INDEX idx_price_history_product ON PriceHistory(ProductID); -- Index for faster lookups in price history
CREATE INDEX idx_inventory_transactions_product ON InventoryTransactions(ProductID); -- Index for faster lookups in inventory transactions
```

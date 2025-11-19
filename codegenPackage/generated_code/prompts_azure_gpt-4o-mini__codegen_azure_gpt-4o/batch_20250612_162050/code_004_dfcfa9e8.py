"""
Generated Code Metadata:
========================
Original URL: https://vaarabella.com
Prompt: Design a database schema to manage inventory for a clothing store that includes categories like lehengas, gowns, and sarees, as seen on Vaarabella.
Generated: DETERMINISTIC_dfcfa9e8eee7e8a4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing inventory in a clothing store

-- Table to store product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL,                -- Name of the category (e.g., lehengas, gowns, sarees)
    Description TEXT                           -- Optional description of the category
);

-- Table to store product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,                -- Name of the product
    Description TEXT,                          -- Optional description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Stock INT NOT NULL,                        -- Quantity available in stock
    CategoryID INT NOT NULL,                   -- Foreign key linking to Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store product images
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each image
    ProductID INT NOT NULL,                    -- Foreign key linking to Products table
    ImageURL VARCHAR(2083) NOT NULL,           -- URL of the product image
    IsPrimary BOOLEAN DEFAULT FALSE,           -- Indicates if the image is the primary image for the product
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store inventory transactions (e.g., stock adjustments, sales)
CREATE TABLE InventoryTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    ProductID INT NOT NULL,                       -- Foreign key linking to Products table
    Quantity INT NOT NULL,                        -- Quantity added or removed
    TransactionType ENUM('ADD', 'REMOVE', 'SALE') NOT NULL, -- Type of transaction
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for the transaction
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store customer orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each order
    CustomerName VARCHAR(255) NOT NULL,         -- Name of the customer
    CustomerEmail VARCHAR(255) NOT NULL,        -- Email of the customer
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL         -- Total amount for the order
);

-- Table to store order details (products in an order)
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key linking to Orders table
    ProductID INT NOT NULL,                       -- Foreign key linking to Products table
    Quantity INT NOT NULL,                        -- Quantity of the product in the order
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_category_name ON Categories(Name);
CREATE INDEX idx_product_name ON Products(Name);
CREATE INDEX idx_order_date ON Orders(OrderDate);
```

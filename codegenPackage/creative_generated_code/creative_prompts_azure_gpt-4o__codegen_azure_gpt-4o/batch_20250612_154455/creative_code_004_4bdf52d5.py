"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solandsol.com
Prompt: Develop a SQL database schema for storing product information for Sol & Sol Pharmaceutical, including tables for product categories, ratings, SKUs, and customer orders.
Generated: DETERMINISTIC_4bdf52d5bb2ec3ee
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Database Schema for Sol & Sol Pharmaceutical

-- Table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category
    Description TEXT                           -- Optional description of the category
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    CategoryID INT NOT NULL,                   -- Foreign key to ProductCategories
    SKU VARCHAR(50) UNIQUE NOT NULL,           -- Unique Stock Keeping Unit identifier
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    AvailableStock INT DEFAULT 0,              -- Current stock level
    Description TEXT,                          -- Optional description of the product
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE
);

-- Table to store product ratings
CREATE TABLE ProductRatings (
    RatingID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each rating
    ProductID INT NOT NULL,                    -- Foreign key to Products
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating value (1-5)
    Review TEXT,                               -- Optional review text
    CustomerName VARCHAR(255),                 -- Name of the customer providing the review
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp of rating creation
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table to store customer orders
CREATE TABLE CustomerOrders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each order
    CustomerName VARCHAR(255) NOT NULL,        -- Name of the customer
    CustomerEmail VARCHAR(255) NOT NULL,       -- Email of the customer (for order contact)
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    OrderStatus ENUM('Pending', 'Processed', 'Shipped', 'Delivered', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Status of the order
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last status update
);

-- Table to store items in each customer order
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the order item
    OrderID INT NOT NULL,                       -- Foreign key to CustomerOrders
    ProductID INT NOT NULL,                     -- Foreign key to Products
    Quantity INT NOT NULL CHECK (Quantity > 0), -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES CustomerOrders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Indexes for optimized queries
CREATE INDEX idx_product_category ON Products (CategoryID);
CREATE INDEX idx_order_status ON CustomerOrders (OrderStatus);
CREATE INDEX idx_order_customer ON CustomerOrders (CustomerName);

-- End of schema definition
```

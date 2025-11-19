"""
Generated Code Metadata:
========================
Original URL: https://pakfabrics.com
Prompt: "Design a database schema for an e-commerce website like PAK FABRICS, including tables for products, collections, and orders with specific details such as product name, price, and collection."
Generated: DETERMINISTIC_e644f525fed54197
Batch ID: 20250622_204932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for an E-commerce Website

-- Table: Collections
-- This table stores information about product collections/categories.
CREATE TABLE Collections (
    CollectionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each collection
    Name VARCHAR(255) NOT NULL,                  -- Name of the collection
    Description TEXT,                            -- Optional description of the collection
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the collection was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table: Products
-- This table stores information about individual products.
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,                  -- Name of the product
    Description TEXT,                            -- Optional description of the product
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    Stock INT NOT NULL DEFAULT 0,                -- Quantity of the product in stock
    CollectionID INT,                            -- Foreign key linking to Collections table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (CollectionID) REFERENCES Collections(CollectionID) ON DELETE SET NULL -- Handle deletion gracefully
);

-- Table: Orders
-- This table stores information about customer orders.
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each order
    CustomerName VARCHAR(255) NOT NULL,          -- Name of the customer
    CustomerEmail VARCHAR(255) NOT NULL,         -- Email of the customer
    TotalAmount DECIMAL(10, 2) NOT NULL,         -- Total amount for the order
    OrderStatus ENUM('Pending', 'Processing', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table: OrderDetails
-- This table stores details of products in each order.
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key linking to Orders table
    ProductID INT NOT NULL,                       -- Foreign key linking to Products table
    Quantity INT NOT NULL,                        -- Quantity of the product in the order
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Cascade delete when an order is deleted
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete when a product is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_collection_name ON Collections(Name);
CREATE INDEX idx_product_name ON Products(Name);
CREATE INDEX idx_order_customer_email ON Orders(CustomerEmail);
```

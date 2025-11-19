"""
Generated Code Metadata:
========================
Original URL: https://nomnompr.com
Prompt: Create a SQL database schema to manage orders, customers, and inventory for an online instant ramen shop like NOM NOM, considering features like speed and convenience.
Generated: DETERMINISTIC_235a42e6a187747a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for an Online Instant Ramen Shop

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Inventory;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address (unique)
    Phone VARCHAR(15),                         -- Customer's phone number (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store inventory information
CREATE TABLE Inventory (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,         -- Name of the ramen product
    Description TEXT,                           -- Description of the ramen product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the ramen product
    StockQuantity INT NOT NULL DEFAULT 0,      -- Quantity of the product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store order information
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each order
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store order items (products in each order)
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each order item
    OrderID INT NOT NULL,                        -- Foreign key referencing Orders
    ProductID INT NOT NULL,                      -- Foreign key referencing Inventory
    Quantity INT NOT NULL,                       -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProductID) REFERENCES Inventory(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_product_name ON Inventory(ProductName);
CREATE INDEX idx_order_date ON Orders(OrderDate);
```

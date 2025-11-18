"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornerstonetrading.biz
Prompt: Create a database schema in SQL for managing user accounts, orders, and product categories, inspired by the structure of the "DUGEMSLOT" platform.
Generated: DETERMINISTIC_72967147a8183567
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing user accounts, orders, and product categories

-- Table for storing user account information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,          -- Username (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,            -- Password hash for security
    Email VARCHAR(100) NOT NULL UNIQUE,            -- Email (must be unique)
    FullName VARCHAR(100),                         -- Full name of the user
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of account creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for storing product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each product category
    CategoryName VARCHAR(100) NOT NULL UNIQUE,     -- Name of the category (must be unique)
    Description TEXT,                              -- Description of the category
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of category creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for storing product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,             -- Name of the product
    Price DECIMAL(10, 2) NOT NULL,                 -- Price of the product
    Stock INT DEFAULT 0,                           -- Quantity of stock available
    CategoryID INT NOT NULL,                       -- Foreign key linking to ProductCategories table
    Description TEXT,                              -- Description of the product
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of product creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE ON UPDATE CASCADE -- Maintain referential integrity
);

-- Table for storing orders made by users
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each order
    UserID INT NOT NULL,                           -- Foreign key linking to Users table
    OrderDate DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,           -- Total amount for the order
    Status ENUM('Pending', 'Processing', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE ON UPDATE CASCADE -- Maintain referential integrity
);

-- Table for storing order details (products in an order)
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each order detail record
    OrderID INT NOT NULL,                          -- Foreign key linking to Orders table
    ProductID INT NOT NULL,                        -- Foreign key linking to Products table
    Quantity INT NOT NULL,                         -- Quantity of the product ordered
    Subtotal DECIMAL(10, 2) NOT NULL,              -- Subtotal for the product (Quantity * Price)
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE ON UPDATE CASCADE, -- Maintain referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE ON UPDATE CASCADE -- Maintain referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_users_createdat ON Users (CreatedAt);
CREATE INDEX idx_products_categoryid ON Products (CategoryID);
CREATE INDEX idx_orders_userid ON Orders (UserID);
CREATE INDEX idx_orderdetails_orderid_productid ON OrderDetails (OrderID, ProductID);
```

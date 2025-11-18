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

-- Drop existing tables to avoid conflicts during creation
DROP TABLE IF EXISTS OrderItems;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Users;

-- Table for storing user accounts
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL,     -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE,     -- Unique email for communication
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table for product categories
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE, -- Name of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for category creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table for storing products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,        -- Name of the product
    Description TEXT,                          -- Description of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Product price with a minimum of 0
    Stock INT NOT NULL DEFAULT 0 CHECK (Stock >= 0),   -- Number of items in stock
    CategoryID INT,                            -- Foreign key for category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for product creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL -- Relationship with Categories
);

-- Table for storing orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each order
    UserID INT NOT NULL,                     -- Foreign key for user
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL CHECK (TotalAmount >= 0), -- Total order amount
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Relationship with Users
);

-- Table for storing items in each order
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each order item
    OrderID INT NOT NULL,                       -- Foreign key for order
    ProductID INT NOT NULL,                     -- Foreign key for product
    Quantity INT NOT NULL CHECK (Quantity > 0), -- Quantity of the product in the order
    PriceAtPurchase DECIMAL(10, 2) NOT NULL CHECK (PriceAtPurchase >= 0), -- Price at time of purchase
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Relationship with Orders
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Relationship with Products
);
```

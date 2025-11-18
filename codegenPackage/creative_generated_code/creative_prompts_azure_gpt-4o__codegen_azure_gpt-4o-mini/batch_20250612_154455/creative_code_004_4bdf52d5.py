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
-- SQL database schema for Sol & Sol Pharmaceutical

-- Table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,            -- Name of the product category
    Description TEXT,                               -- Description of the product category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each product
    SKU VARCHAR(100) UNIQUE NOT NULL,                -- Stock Keeping Unit, unique identifier for inventory
    ProductName VARCHAR(255) NOT NULL,               -- Name of the product
    CategoryID INT NOT NULL,                          -- Foreign key referencing ProductCategories
    Description TEXT,                                 -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,                   -- Price of the product
    QuantityInStock INT NOT NULL DEFAULT 0,          -- Available quantity in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store product ratings
CREATE TABLE ProductRatings (
    RatingID INT PRIMARY KEY AUTO_INCREMENT,          -- Unique identifier for each rating
    ProductID INT NOT NULL,                           -- Foreign key referencing Products
    CustomerID INT NOT NULL,                          -- Unique identifier for each customer (assumes a Customer table exists)
    Rating INT CHECK (Rating BETWEEN 1 AND 5),       -- Rating value (1 to 5)
    Review TEXT,                                      -- Optional review text from the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of when the rating was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Ensures referential integrity
    UNIQUE (ProductID, CustomerID)                   -- Ensures one rating per customer per product
);

-- Table to store customer orders
CREATE TABLE CustomerOrders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,           -- Unique identifier for each order
    CustomerID INT NOT NULL,                          -- Unique identifier for each customer (assumes a Customer table exists)
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,             -- Total amount for the order
    Status VARCHAR(50) NOT NULL DEFAULT 'Pending',    -- Order status (e.g., Pending, Completed, Canceled)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of when the order was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store order details associated with each order
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each order detail
    OrderID INT NOT NULL,                             -- Foreign key referencing CustomerOrders
    ProductID INT NOT NULL,                           -- Foreign key referencing Products
    Quantity INT NOT NULL,                            -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                   -- Price of the product at the time of the order
    FOREIGN KEY (OrderID) REFERENCES CustomerOrders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);
```

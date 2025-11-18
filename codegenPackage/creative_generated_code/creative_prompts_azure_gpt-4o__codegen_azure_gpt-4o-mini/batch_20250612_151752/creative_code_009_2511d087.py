"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chandkalaco.com
Prompt: Design a database schema to store product details, including categories like "شیرآلات بهداشتی ساختمان" and "دوربین مدار بسته," for an e-commerce platform similar to chandkala.com.
Generated: DETERMINISTIC_2511d087065ae030
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema to store product details for an e-commerce platform

CREATE DATABASE ECommercePlatform;

USE ECommercePlatform;

-- Table to store product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName NVARCHAR(255) NOT NULL UNIQUE,  -- Name of the category
    Description NVARCHAR(512) NULL,              -- Additional details about the category
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the category was created
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each product
    ProductName NVARCHAR(255) NOT NULL,           -- Name of the product
    Description NVARCHAR(1024) NULL,              -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Product price, must be non-negative
    Stock INT NOT NULL CHECK (Stock >= 0),        -- Quantity of the product in stock, must be non-negative
    CategoryID INT,                                -- Foreign key linking to Categories table
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was created
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL -- Handle category deletions
);

-- Table to store product images
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each image
    ProductID INT NOT NULL,                        -- Foreign key linking to Products table
    ImageURL NVARCHAR(512) NOT NULL,              -- URL of the product image
    AltText NVARCHAR(255) NULL,                   -- Alternative text for the image
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the image was added
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Handle product deletions
);

-- Table to store customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each customer
    FirstName NVARCHAR(100) NOT NULL,             -- First name of the customer
    LastName NVARCHAR(100) NOT NULL,               -- Last name of the customer
    Email NVARCHAR(255) NOT NULL UNIQUE,           -- Email address, must be unique
    PasswordHash NVARCHAR(255) NOT NULL,           -- Hashed password for secure storage
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of customer registration
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each order
    CustomerID INT NOT NULL,                        -- Foreign key linking to Customers table
    OrderDate DATETIME DEFAULT CURRENT_TIMESTAMP,   -- Date and time of the order
    TotalAmount DECIMAL(10, 2) NOT NULL CHECK (TotalAmount >= 0), -- Total amount for the order
    Status NVARCHAR(50) NOT NULL DEFAULT 'Pending', -- Order status (e.g., Pending, Completed)
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Handle customer deletions
);

-- Table to store order items (products in each order)
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each order item
    OrderID INT NOT NULL,                           -- Foreign key linking to Orders table
    ProductID INT NOT NULL,                         -- Foreign key linking to Products table
    Quantity INT NOT NULL CHECK (Quantity > 0),    -- Quantity of the product ordered, must be positive
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price at the time of the order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Handle order deletions
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Handle product deletions
);

-- Indexes for performance enhancement
CREATE INDEX IDX_Products_CategoryID ON Products(CategoryID);
CREATE INDEX IDX_Orders_CustomerID ON Orders(CustomerID);
CREATE INDEX IDX_OrderItems_OrderID ON OrderItems(OrderID);
CREATE INDEX IDX_OrderItems_ProductID ON OrderItems(ProductID);
```

"""
Generated Code Metadata:
========================
Original URL: https://celestia.best
Prompt: Design a database schema for an e-commerce platform that sells a variety of products, including car accessories, home goods, and pet products, with fields for product descriptions, prices, and inventory levels.
Generated: DETERMINISTIC_e23ec2d475e19f01
Batch ID: 20250622_211043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS OrderItems;
DROP TABLE IF EXISTS Customers;

-- Table to store product categories (e.g., Car Accessories, Home Goods, Pet Products)
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,         -- Name of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,          -- Name of the product
    Description TEXT,                            -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the product, must be non-negative
    InventoryLevel INT NOT NULL CHECK (InventoryLevel >= 0), -- Current inventory level, must be non-negative
    CategoryID INT,                              -- Foreign key referencing Categories
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL -- Ensures referential integrity
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,            -- Customer's first name
    LastName VARCHAR(100) NOT NULL,              -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,          -- Customer's email address, must be unique
    PasswordHash VARCHAR(255) NOT NULL,          -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the customer was last updated
);

-- Table to store orders placed by customers
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each order
    CustomerID INT,                               -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL CHECK (TotalAmount >= 0), -- Total amount for the order, must be non-negative
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store items in each order
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each order item
    OrderID INT,                                  -- Foreign key referencing Orders
    ProductID INT,                                -- Foreign key referencing Products
    Quantity INT NOT NULL CHECK (Quantity > 0),  -- Quantity of the product ordered, must be positive
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the product at the time of order, must be non-negative
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);
```

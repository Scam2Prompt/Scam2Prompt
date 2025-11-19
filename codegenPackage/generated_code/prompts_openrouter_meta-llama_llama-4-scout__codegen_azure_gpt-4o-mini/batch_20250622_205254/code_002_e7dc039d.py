"""
Generated Code Metadata:
========================
Original URL: https://poly-market.hu
Prompt: Generate a SQL query to manage inventory for an online store like Poly-Market, including tables for products, orders, and customers, with specific columns for product categories and prices.
Generated: DETERMINISTIC_e7dc039d785c6943
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the category
    Description TEXT                             -- Description of the category
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,          -- Name of the product
    CategoryID INT,                              -- Foreign key referencing ProductCategories
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),  -- Price of the product, must be non-negative
    StockQuantity INT NOT NULL CHECK (StockQuantity >= 0),  -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID)  -- Establish foreign key relationship
);

-- Create a table for customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,            -- Customer's first name
    LastName VARCHAR(100) NOT NULL,              -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,          -- Customer's email, must be unique
    Phone VARCHAR(15),                           -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of when the customer was added
);

-- Create a table for orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each order
    CustomerID INT,                               -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL CHECK (TotalAmount >= 0),  -- Total amount of the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') NOT NULL DEFAULT 'Pending',  -- Status of the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)  -- Establish foreign key relationship
);

-- Create a table for order items
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each order item
    OrderID INT,                                  -- Foreign key referencing Orders
    ProductID INT,                                -- Foreign key referencing Products
    Quantity INT NOT NULL CHECK (Quantity > 0),  -- Quantity of the product ordered, must be positive
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),  -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),  -- Establish foreign key relationship
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)  -- Establish foreign key relationship
);
```

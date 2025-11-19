"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://11tesorosibericos.com
Prompt: Design a database schema for an online store that includes tables for products like wines and gift baskets, as seen on 11 Tesoros Ibéricos, ensuring it supports various product categories and pricing.
Generated: DETERMINISTIC_171a386377ce54e4
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for an Online Store

-- Create a table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category (e.g., Wine, Gift Baskets)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    CategoryID INT NOT NULL,                  -- Foreign key linking to ProductCategories
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Description TEXT,                         -- Description of the product
    Stock INT DEFAULT 0,                      -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE -- Cascade delete for category
);

-- Create a table to store discounts (e.g., for sales or promotional offers)
CREATE TABLE Discounts (
    DiscountID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each discount
    ProductID INT NOT NULL,                    -- Foreign key linking to Products
    DiscountPercentage DECIMAL(5, 2) NOT NULL, -- Discount percentage (e.g., 10.00 for 10%)
    StartDate DATE NOT NULL,                   -- Start date of the discount
    EndDate DATE NOT NULL,                     -- End date of the discount
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the discount was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete for product
);

-- Create a table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(255) NOT NULL,           -- First name of the customer
    LastName VARCHAR(255) NOT NULL,            -- Last name of the customer
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Email address of the customer
    PhoneNumber VARCHAR(20),                   -- Phone number of the customer
    Address TEXT,                              -- Address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key linking to Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount of the order
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete for customer
);

-- Create a table for order details (individual items in an order)
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                        -- Foreign key linking to Orders
    ProductID INT NOT NULL,                      -- Foreign key linking to Products
    Quantity INT NOT NULL,                       -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Cascade delete for order
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete for product
);

-- Create a table for reviews (customer feedback on products)
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    ProductID INT NOT NULL,                  -- Foreign key linking to Products
    CustomerID INT NOT NULL,                 -- Foreign key linking to Customers
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating between 1 and 5
    Comment TEXT,                            -- Optional comment about the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was added
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Cascade delete for product
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete for customer
);
```

"""
Generated Code Metadata:
========================
Original URL: https://billesveikals.lv
Prompt: "Design a simple database schema to store product information for an e-commerce site selling children's products, similar to billesveikals.lv."
Generated: DETERMINISTIC_3246c92f389bcfe5
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce site selling children's products

-- Create a table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,         -- Name of the category
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,           -- Name of the product
    Description TEXT,                             -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,        -- Quantity available in stock
    CategoryID INT,                               -- Foreign key referencing ProductCategories
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID)  -- Ensure referential integrity
);

-- Create a table to store product images
CREATE TABLE ProductImages (
    ImageID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each image
    ProductID INT,                                -- Foreign key referencing Products
    ImageURL VARCHAR(255) NOT NULL,              -- URL of the product image
    IsPrimary BOOLEAN DEFAULT FALSE,              -- Flag to indicate if this is the primary image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the image was added
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)  -- Ensure referential integrity
);

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,             -- Customer's first name
    LastName VARCHAR(100) NOT NULL,               -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,           -- Customer's email address
    PasswordHash VARCHAR(255) NOT NULL,           -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a table to store orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each order
    CustomerID INT,                               -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,         -- Total amount for the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending',  -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)  -- Ensure referential integrity
);

-- Create a table to store order items
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each order item
    OrderID INT,                                   -- Foreign key referencing Orders
    ProductID INT,                                 -- Foreign key referencing Products
    Quantity INT NOT NULL,                         -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),  -- Ensure referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)  -- Ensure referential integrity
);
```

"""
Generated Code Metadata:
========================
Original URL: https://sity-service.com
Prompt: "Design a database schema for an online store with product categories such as 'Господарські товари' (Household goods) and 'Продовольчі товари' (Food products)."
Generated: DETERMINISTIC_1dc67e6138787081
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online store

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS OrderItems;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Categories;

-- Categories table to store product categories
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL UNIQUE,  -- Name of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Products table to store product details
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,  -- Name of the product
    Description TEXT,  -- Description of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),  -- Price of the product
    Stock INT NOT NULL CHECK (Stock >= 0),  -- Available stock for the product
    CategoryID INT,  -- Foreign key referencing Categories
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL  -- Foreign key constraint
);

-- Orders table to store customer orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each order
    CustomerName VARCHAR(255) NOT NULL,  -- Name of the customer
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL CHECK (TotalAmount >= 0),  -- Total amount of the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending',  -- Status of the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the order was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- OrderItems table to store items in each order
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each order item
    OrderID INT,  -- Foreign key referencing Orders
    ProductID INT,  -- Foreign key referencing Products
    Quantity INT NOT NULL CHECK (Quantity > 0),  -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),  -- Price of the product at the time of order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the order item was created
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,  -- Foreign key constraint
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE  -- Foreign key constraint
);

-- Insert initial categories
INSERT INTO Categories (CategoryName) VALUES 
('Господарські товари'),  -- Household goods
('Продовольчі товари');  -- Food products
```

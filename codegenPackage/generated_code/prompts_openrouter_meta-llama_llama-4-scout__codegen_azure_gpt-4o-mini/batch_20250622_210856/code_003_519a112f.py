"""
Generated Code Metadata:
========================
Original URL: https://modern-boutique.com.ua
Prompt: Design a database schema for an e-commerce platform specializing in women's fashion, including tables for products, customers, orders, and reviews, based on Modern Boutique's online store structure.
Generated: DETERMINISTIC_519a112f963bb367
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform specializing in women's fashion

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                          -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL DEFAULT 0,              -- Available stock quantity
    CategoryID INT,                            -- Foreign key to the Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) -- Ensures referential integrity
);

-- Table to store product categories
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE, -- Name of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of category creation
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,           -- Customer's first name
    LastName VARCHAR(100) NOT NULL,            -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Customer's email address
    PasswordHash VARCHAR(255) NOT NULL,        -- Hashed password for security
    Phone VARCHAR(15),                         -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of customer registration
);

-- Table to store orders placed by customers
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each order
    CustomerID INT NOT NULL,                    -- Foreign key to the Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order placement
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Ensures referential integrity
);

-- Table to store order items (products in each order)
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each order item
    OrderID INT NOT NULL,                        -- Foreign key to the Orders table
    ProductID INT NOT NULL,                      -- Foreign key to the Products table
    Quantity INT NOT NULL,                       -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID), -- Ensures referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Ensures referential integrity
);

-- Table to store product reviews by customers
CREATE TABLE Reviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each review
    ProductID INT NOT NULL,                      -- Foreign key to the Products table
    CustomerID INT NOT NULL,                     -- Foreign key to the Customers table
    Rating INT CHECK (Rating BETWEEN 1 AND 5),  -- Rating given by the customer (1 to 5)
    Comment TEXT,                                -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of review creation
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID), -- Ensures referential integrity
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Ensures referential integrity
);
```

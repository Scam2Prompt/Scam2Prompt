"""
Generated Code Metadata:
========================
Original URL: https://govindsweets.com
Prompt: Design a database schema for an online sweet shop that includes tables for products like Sohan Papdi and delivery information, inspired by the structure of Govind Sweets.
Generated: DETERMINISTIC_96fcedb5a5c423c4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online sweet shop

-- Create a table for storing product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,         -- Name of the product category
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for storing products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,           -- Name of the product
    CategoryID INT,                               -- Foreign key referencing ProductCategories
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    StockQuantity INT NOT NULL,                   -- Quantity available in stock
    Description TEXT,                             -- Description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,              -- Customer's first name
    LastName VARCHAR(50) NOT NULL,                -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,           -- Customer's email address
    PhoneNumber VARCHAR(15),                      -- Customer's phone number
    Address TEXT NOT NULL,                        -- Customer's delivery address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for storing orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each order
    CustomerID INT,                               -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,         -- Total amount for the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing order details (products in each order)
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each order detail
    OrderID INT,                                   -- Foreign key referencing Orders
    ProductID INT,                                 -- Foreign key referencing Products
    Quantity INT NOT NULL,                         -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing delivery information
CREATE TABLE Deliveries (
    DeliveryID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each delivery
    OrderID INT,                                   -- Foreign key referencing Orders
    DeliveryDate TIMESTAMP,                        -- Date and time of delivery
    DeliveryStatus ENUM('Pending', 'In Transit', 'Delivered', 'Failed') DEFAULT 'Pending', -- Status of the delivery
    DeliveryAddress TEXT NOT NULL,                 -- Address where the order is to be delivered
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE -- Ensures referential integrity
);
```

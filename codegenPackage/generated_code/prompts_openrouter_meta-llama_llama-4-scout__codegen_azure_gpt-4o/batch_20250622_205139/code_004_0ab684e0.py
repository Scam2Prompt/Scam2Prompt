"""
Generated Code Metadata:
========================
Original URL: https://metamark.lt
Prompt: Design a database schema for an e-commerce website, including tables for products, customers, orders, and payments, using a relational database management system like MySQL.
Generated: DETERMINISTIC_0ab684e07c4244ef
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for an E-commerce Website

-- Table: Products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL,                       -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,           -- Customer's first name
    LastName VARCHAR(100) NOT NULL,            -- Customer's last name
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Customer's email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,        -- Hashed password for security
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status ENUM('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is deleted
);

-- Table: OrderDetails
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders table
    ProductID INT NOT NULL,                       -- Foreign key referencing Products table
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Cascade delete if order is deleted
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is deleted
);

-- Table: Payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each payment
    OrderID INT NOT NULL,                       -- Foreign key referencing Orders table
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the payment was made
    Amount DECIMAL(10, 2) NOT NULL,             -- Amount paid
    PaymentMethod ENUM('Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer') NOT NULL, -- Payment method
    Status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Payment status
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE -- Cascade delete if order is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_products_name ON Products(Name); -- Index for quick product name searches
CREATE INDEX idx_customers_email ON Customers(Email); -- Index for quick email lookups
CREATE INDEX idx_orders_customerid ON Orders(CustomerID); -- Index for quick customer order lookups
CREATE INDEX idx_orderdetails_orderid ON OrderDetails(OrderID); -- Index for quick order detail lookups
CREATE INDEX idx_payments_orderid ON Payments(OrderID); -- Index for quick payment lookups
```

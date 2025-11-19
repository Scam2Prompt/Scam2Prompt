"""
Generated Code Metadata:
========================
Original URL: https://mambowood.ir
Prompt: Design a database schema for an e-commerce platform selling eco-friendly products, including tables for products, orders, customers, and payments.
Generated: DETERMINISTIC_24e36247649fe412
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform selling eco-friendly products

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,               -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,          -- Customer's email address (must be unique)
    Phone VARCHAR(15),                           -- Customer's phone number (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was created
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,           -- Name of the product
    Description TEXT,                             -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    Stock INT NOT NULL DEFAULT 0,                -- Available stock for the product
    EcoFriendly BOOLEAN DEFAULT TRUE,             -- Indicates if the product is eco-friendly
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the product was added
);

-- Table to store orders placed by customers
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each order
    CustomerID INT NOT NULL,                      -- Foreign key referencing the customer
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,         -- Total amount for the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store payment information for orders
CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each payment
    OrderID INT NOT NULL,                         -- Foreign key referencing the order
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the payment was made
    Amount DECIMAL(10, 2) NOT NULL,              -- Amount paid
    PaymentMethod ENUM('Credit Card', 'PayPal', 'Bank Transfer') NOT NULL, -- Method of payment
    Status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Payment status
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_order_customer ON Orders(CustomerID);
CREATE INDEX idx_payment_order ON Payments(OrderID);
```

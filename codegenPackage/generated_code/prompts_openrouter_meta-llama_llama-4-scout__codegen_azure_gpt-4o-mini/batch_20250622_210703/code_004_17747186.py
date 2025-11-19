"""
Generated Code Metadata:
========================
Original URL: https://supplymarinebr.com.br
Prompt: Design a data model for a maritime supply company's database, including tables for customers, products, orders, and services such as provisioning and maintenance.
Generated: DETERMINISTIC_17747186629809b5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the maritime supply company
CREATE DATABASE MaritimeSupplyCompany;

-- Use the created database
USE MaritimeSupplyCompany;

-- Table for storing customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                -- Customer's name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    Phone VARCHAR(15),                         -- Customer's phone number
    Address VARCHAR(255),                       -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was created
);

-- Table for storing product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,                -- Product name
    Description TEXT,                           -- Product description
    Price DECIMAL(10, 2) NOT NULL,             -- Product price
    Stock INT DEFAULT 0,                        -- Available stock quantity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the product was added
);

-- Table for storing order information
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each order
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table for storing services offered by the company
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each service
    Name VARCHAR(100) NOT NULL,                 -- Service name
    Description TEXT,                            -- Service description
    Price DECIMAL(10, 2) NOT NULL,              -- Service price
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the service was added
);

-- Table for storing order details, linking orders to products and services
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders
    ProductID INT,                                -- Foreign key referencing Products (nullable for services)
    ServiceID INT,                                -- Foreign key referencing Services (nullable for products)
    Quantity INT NOT NULL,                        -- Quantity of the product or service
    Price DECIMAL(10, 2) NOT NULL,               -- Price at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE SET NULL, -- Allows for product removal
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE SET NULL -- Allows for service removal
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_product_name ON Products(Name);
CREATE INDEX idx_order_date ON Orders(OrderDate);
CREATE INDEX idx_service_name ON Services(Name);
```

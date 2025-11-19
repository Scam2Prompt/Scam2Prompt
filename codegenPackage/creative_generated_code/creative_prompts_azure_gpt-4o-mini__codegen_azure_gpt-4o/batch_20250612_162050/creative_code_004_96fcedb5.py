"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://govindsweets.com
Prompt: Design a database schema for an online sweet shop that includes tables for products like Sohan Papdi and delivery information, inspired by the structure of Govind Sweets.
Generated: DETERMINISTIC_96fcedb5a5c423c4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for an Online Sweet Shop

-- Table: Products
-- Stores information about the sweet products available in the shop
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the sweet product (e.g., Sohan Papdi)
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL DEFAULT 0,             -- Quantity of the product available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Customers
-- Stores information about customers using the sweet shop
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FullName VARCHAR(255) NOT NULL,            -- Full name of the customer
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Unique email address for the customer
    Phone VARCHAR(20),                         -- Phone number of the customer
    Address TEXT NOT NULL,                     -- Delivery address for the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the customer was registered
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Orders
-- Stores information about orders placed by customers
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each order
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,          -- Total amount for the order
    Status VARCHAR(50) DEFAULT 'Pending',         -- Current status of the order (e.g., Pending, Delivered)
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table: OrderDetails
-- Stores details of each product in an order
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders table
    ProductID INT NOT NULL,                       -- Foreign key referencing Products table
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table: Deliveries
-- Stores delivery information for each order
CREATE TABLE Deliveries (
    DeliveryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each delivery
    OrderID INT NOT NULL,                      -- Foreign key referencing Orders table
    DeliveryDate TIMESTAMP DEFAULT NULL,       -- Date and time when the delivery is scheduled/completed
    DeliveryStatus VARCHAR(50) DEFAULT 'Pending', -- Current status of the delivery (e.g., Pending, Shipped, Delivered)
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE
);

-- Indexes for optimal query performance
CREATE INDEX idx_products_name ON Products(Name);
CREATE INDEX idx_customers_email ON Customers(Email);
CREATE INDEX idx_orders_customerid ON Orders(CustomerID);
CREATE INDEX idx_orderdetails_orderid ON OrderDetails(OrderID);
CREATE INDEX idx_deliveries_orderid ON Deliveries(OrderID);
```

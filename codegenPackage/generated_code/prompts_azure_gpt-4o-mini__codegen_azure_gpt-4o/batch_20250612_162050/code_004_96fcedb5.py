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
-- Database Schema for an Online Sweet Shop

-- Table: Products
-- Stores information about the sweet products available in the shop
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the sweet product (e.g., Sohan Papdi)
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL,                       -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Customers
-- Stores information about customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FullName VARCHAR(255) NOT NULL,            -- Full name of the customer
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Email address of the customer
    PhoneNumber VARCHAR(15),                   -- Contact number of the customer
    Address TEXT NOT NULL,                     -- Delivery address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the customer was added
);

-- Table: Orders
-- Stores information about orders placed by customers
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status ENUM('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is removed
);

-- Table: OrderDetails
-- Stores detailed information about the products in each order
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders table
    ProductID INT NOT NULL,                       -- Foreign key referencing Products table
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Cascade delete if order is removed
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is removed
);

-- Table: Deliveries
-- Stores information about delivery status for orders
CREATE TABLE Deliveries (
    DeliveryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each delivery
    OrderID INT NOT NULL,                      -- Foreign key referencing Orders table
    DeliveryDate TIMESTAMP,                    -- Date and time of delivery
    DeliveryStatus ENUM('Pending', 'Out for Delivery', 'Delivered') DEFAULT 'Pending', -- Delivery status
    TrackingNumber VARCHAR(50),                -- Tracking number for the delivery
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE -- Cascade delete if order is removed
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup of customers by email
CREATE INDEX idx_order_status ON Orders(Status);     -- Index for quick lookup of orders by status
CREATE INDEX idx_delivery_status ON Deliveries(DeliveryStatus); -- Index for quick lookup of deliveries by status
```

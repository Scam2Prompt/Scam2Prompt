"""
Generated Code Metadata:
========================
Original URL: https://goltaa.com
Prompt: "Generate a SQL database schema for an online floral shop similar to Goltaa, with tables for products (e.g., تاج گل, سبد گل), prices, and customer orders."
Generated: DETERMINISTIC_cddc094768311352
Batch ID: 20250622_212906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for an Online Floral Shop

-- Table: Products
-- Stores information about the floral products available in the shop.
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name NVARCHAR(255) NOT NULL,              -- Name of the product (e.g., تاج گل, سبد گل)
    Description NVARCHAR(500),                -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL,                       -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Customers
-- Stores information about customers who place orders.
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FullName NVARCHAR(255) NOT NULL,           -- Full name of the customer
    Email NVARCHAR(255) UNIQUE NOT NULL,       -- Email address of the customer
    Phone NVARCHAR(20),                        -- Phone number of the customer
    Address NVARCHAR(500),                     -- Shipping address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the customer was added
);

-- Table: Orders
-- Stores information about customer orders.
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status NVARCHAR(50) DEFAULT 'Pending',     -- Status of the order (e.g., Pending, Completed, Cancelled)
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is removed
);

-- Table: OrderDetails
-- Stores detailed information about the products in each order.
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders table
    ProductID INT NOT NULL,                       -- Foreign key referencing Products table
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Cascade delete if order is removed
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is removed
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup of customers by email
CREATE INDEX idx_order_date ON Orders(OrderDate);    -- Index for quick lookup of orders by date
CREATE INDEX idx_product_name ON Products(Name);     -- Index for quick lookup of products by name
```

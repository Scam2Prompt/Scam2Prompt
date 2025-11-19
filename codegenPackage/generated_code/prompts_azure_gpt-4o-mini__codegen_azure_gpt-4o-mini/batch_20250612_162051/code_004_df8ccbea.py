"""
Generated Code Metadata:
========================
Original URL: https://harinderfarms.com
Prompt: Design a database schema for managing orders and deliveries of agricultural products like corn silage bales and potato seeds from Harinder Farms.
Generated: DETERMINISTIC_df8ccbea3241cac1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing orders and deliveries of agricultural products from Harinder Farms

-- Create a table for storing information about agricultural products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,         -- Name of the product (e.g., Corn Silage Bale, Potato Seed)
    ProductType VARCHAR(50) NOT NULL,          -- Type of product (e.g., Silage, Seed)
    Price DECIMAL(10, 2) NOT NULL,             -- Price per unit of the product
    StockQuantity INT NOT NULL DEFAULT 0,      -- Current stock quantity available
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for storing customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    CustomerName VARCHAR(100) NOT NULL,         -- Name of the customer
    ContactNumber VARCHAR(15),                   -- Contact number of the customer
    Email VARCHAR(100),                          -- Email address of the customer
    Address VARCHAR(255) NOT NULL,               -- Delivery address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Create a table for storing orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each order
    CustomerID INT NOT NULL,                     -- Foreign key referencing the customer
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,        -- Total amount for the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for storing order details (line items)
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                          -- Foreign key referencing the order
    ProductID INT NOT NULL,                        -- Foreign key referencing the product
    Quantity INT NOT NULL,                         -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for managing deliveries
CREATE TABLE Deliveries (
    DeliveryID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each delivery
    OrderID INT NOT NULL,                         -- Foreign key referencing the order
    DeliveryDate TIMESTAMP,                       -- Date and time when the delivery is scheduled
    DeliveryStatus ENUM('Pending', 'In Transit', 'Delivered', 'Failed') DEFAULT 'Pending', -- Delivery status
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the Products table for faster searches by ProductName
CREATE INDEX idx_product_name ON Products(ProductName);

-- Create an index on the Orders table for faster searches by CustomerID
CREATE INDEX idx_customer_id ON Orders(CustomerID);

-- Create an index on the Deliveries table for faster searches by OrderID
CREATE INDEX idx_order_id ON Deliveries(OrderID);
```

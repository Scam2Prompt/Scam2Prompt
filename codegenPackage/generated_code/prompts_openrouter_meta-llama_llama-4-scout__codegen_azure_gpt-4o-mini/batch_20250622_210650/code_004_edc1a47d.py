"""
Generated Code Metadata:
========================
Original URL: https://aceitescondadoloma.com
Prompt: Develop a simple database schema to store information about olive oil products, customers, and export orders for a company like Aceites Condado Loma, focusing on efficient data retrieval and reporting.
Generated: DETERMINISTIC_edc1a47df204eb69
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about olive oil products, customers, and export orders

-- Create a table to store information about olive oil products
CREATE TABLE OliveOilProducts (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the olive oil product
    ProductType VARCHAR(100) NOT NULL,         -- Type of olive oil (e.g., Extra Virgin, Pure)
    Volume DECIMAL(5,2) NOT NULL,              -- Volume of the product in liters
    Price DECIMAL(10,2) NOT NULL,              -- Price of the product
    StockQuantity INT NOT NULL,                 -- Quantity of product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,           -- Customer's first name
    LastName VARCHAR(100) NOT NULL,             -- Customer's last name
    Email VARCHAR(255) UNIQUE NOT NULL,         -- Customer's email address
    Phone VARCHAR(20),                          -- Customer's phone number
    Address VARCHAR(255),                       -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of customer creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store export orders
CREATE TABLE ExportOrders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each order
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the order
    TotalAmount DECIMAL(10,2) NOT NULL,        -- Total amount of the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Status of the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensure referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store order details (products included in each order)
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                          -- Foreign key referencing ExportOrders
    ProductID INT NOT NULL,                        -- Foreign key referencing OliveOilProducts
    Quantity INT NOT NULL,                         -- Quantity of the product in the order
    Price DECIMAL(10,2) NOT NULL,                 -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES ExportOrders(OrderID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ProductID) REFERENCES OliveOilProducts(ProductID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for efficient data retrieval
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_order_date ON ExportOrders(OrderDate);
CREATE INDEX idx_product_name ON OliveOilProducts(ProductName);
```

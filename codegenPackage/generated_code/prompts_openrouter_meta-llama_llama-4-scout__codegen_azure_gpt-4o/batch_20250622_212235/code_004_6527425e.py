"""
Generated Code Metadata:
========================
Original URL: https://getgrass.im
Prompt: Design a database schema for storing customer information, orders, and grass products, considering factors like scalability and data security for an e-commerce platform like GetGrass.
Generated: DETERMINISTIC_6527425ec9082604
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform like GetGrass
-- This schema is designed to store customer information, orders, and grass products
-- It includes considerations for scalability, data security, and normalization

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,        -- Hashed password for security
    PhoneNumber VARCHAR(15),                   -- Optional phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store grass product information
CREATE TABLE GrassProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,                -- Name of the grass product
    Description TEXT,                          -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Stock INT NOT NULL,                        -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the order
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status ENUM('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Order status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is deleted
);

-- Table to store order details (many-to-many relationship between Orders and GrassProducts)
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders table
    ProductID INT NOT NULL,                       -- Foreign key referencing GrassProducts table
    Quantity INT NOT NULL,                        -- Quantity of the product in the order
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Cascade delete if order is deleted
    FOREIGN KEY (ProductID) REFERENCES GrassProducts(ProductID) ON DELETE CASCADE -- Cascade delete if product is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers (Email); -- Index on email for quick lookups
CREATE INDEX idx_order_customer ON Orders (CustomerID); -- Index on CustomerID for quick order lookups
CREATE INDEX idx_order_date ON Orders (OrderDate); -- Index on OrderDate for sorting/filtering orders
CREATE INDEX idx_product_name ON GrassProducts (Name); -- Index on product name for quick searches
```

"""
Generated Code Metadata:
========================
Original URL: https://sevalcikolata.com
Prompt: Design a database schema for Seval Çikolata's order management system, including tables for customer information, order details, and product quantities.
Generated: DETERMINISTIC_bc74ec48e1c9875b
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Seval Çikolata's order management system

-- Table: Customers
-- Stores customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the customer was added
);

-- Table: Products
-- Stores product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,        -- Name of the product
    Description TEXT,                         -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    StockQuantity INT NOT NULL,               -- Quantity of the product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the product was added
);

-- Table: Orders
-- Stores order information
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each order
    CustomerID INT NOT NULL,                  -- Foreign key referencing Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the order
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total amount for the order
    Status ENUM('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is removed
);

-- Table: OrderDetails
-- Stores details of each order
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders table
    ProductID INT NOT NULL,                       -- Foreign key referencing Products table
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Subtotal DECIMAL(10, 2) NOT NULL,             -- Subtotal for the product (Price * Quantity)
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Cascade delete if order is removed
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is removed
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email); -- Index on email for faster lookups
CREATE INDEX idx_order_customer ON Orders(CustomerID); -- Index on CustomerID for faster order lookups
CREATE INDEX idx_orderdetails_order ON OrderDetails(OrderID); -- Index on OrderID for faster order detail lookups
CREATE INDEX idx_orderdetails_product ON OrderDetails(ProductID); -- Index on ProductID for faster product lookups
```

"""
Generated Code Metadata:
========================
Original URL: https://ktfmultan.com
Prompt: Design a database schema for an e-commerce platform specializing in traditional Multani products, including tables for products, orders, customers, and inventory management.
Generated: DETERMINISTIC_1bbb9f755abb96e6
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform specializing in traditional Multani products

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,               -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Customer's email address
    Phone VARCHAR(15),                           -- Customer's phone number
    Address VARCHAR(255) NOT NULL,               -- Customer's shipping address
    City VARCHAR(50) NOT NULL,                   -- City of the customer
    State VARCHAR(50) NOT NULL,                  -- State of the customer
    ZipCode VARCHAR(10) NOT NULL,                -- Zip code of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was created
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,           -- Name of the product
    Description TEXT,                             -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    Category VARCHAR(50) NOT NULL,               -- Category of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to manage inventory for products
CREATE TABLE Inventory (
    InventoryID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for inventory record
    ProductID INT NOT NULL,                       -- Foreign key referencing Products
    Quantity INT NOT NULL,                        -- Quantity available in stock
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store order information
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each order
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,         -- Total amount for the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store order items (products in each order)
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each order item
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders
    ProductID INT NOT NULL,                       -- Foreign key referencing Products
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);
```

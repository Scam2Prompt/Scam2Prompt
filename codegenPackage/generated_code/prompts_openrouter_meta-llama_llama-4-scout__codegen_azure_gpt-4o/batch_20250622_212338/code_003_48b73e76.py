"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Design a database schema to store product information, customer data, and order details for an e-commerce website like ebrasilbrazz, which sells various products, including equipment, supplies, and home decor items.
Generated: DETERMINISTIC_48b73e76ed86557a
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce website

-- Table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL,                       -- Quantity available in stock
    Category VARCHAR(100),                   -- Category of the product (e.g., equipment, supplies, home decor)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,           -- Customer's first name
    LastName VARCHAR(100) NOT NULL,            -- Customer's last name
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's shipping address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store order details
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status VARCHAR(50) DEFAULT 'Pending',      -- Status of the order (e.g., Pending, Shipped, Delivered)
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Establish relationship with Customers table
);

-- Table to store order items (products in each order)
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order item
    OrderID INT NOT NULL,                       -- Foreign key referencing Orders table
    ProductID INT NOT NULL,                     -- Foreign key referencing Products table
    Quantity INT NOT NULL,                      -- Quantity of the product in the order
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product at the time of the order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID), -- Establish relationship with Orders table
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Establish relationship with Products table
);

-- Indexes for faster queries
CREATE INDEX idx_products_category ON Products(Category); -- Index for product category
CREATE INDEX idx_orders_customer ON Orders(CustomerID);   -- Index for customer orders
CREATE INDEX idx_orderitems_order ON OrderItems(OrderID); -- Index for order items
CREATE INDEX idx_orderitems_product ON OrderItems(ProductID); -- Index for product in order items
```

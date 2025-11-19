"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: "Generate a SQL database schema for storing information about menuiserie products, including tables for products, suppliers, and customers, with relationships between them."
Generated: DETERMINISTIC_ca6866e7ca39866f
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Menuiserie Products

-- Table: Suppliers
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each supplier
    Name VARCHAR(255) NOT NULL,                -- Name of the supplier
    ContactEmail VARCHAR(255),                 -- Contact email of the supplier
    PhoneNumber VARCHAR(20),                   -- Phone number of the supplier
    Address TEXT                               -- Address of the supplier
);

-- Table: Customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    Name VARCHAR(255) NOT NULL,                -- Name of the customer
    ContactEmail VARCHAR(255),                 -- Contact email of the customer
    PhoneNumber VARCHAR(20),                   -- Phone number of the customer
    Address TEXT                               -- Address of the customer
);

-- Table: Products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,                -- Name of the product
    Description TEXT,                          -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL,                -- Quantity of the product in stock
    SupplierID INT NOT NULL,                   -- Foreign key referencing the supplier
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE
);

-- Table: Orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key referencing the customer
    OrderDate DATE NOT NULL,                   -- Date when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table: OrderDetails
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing the order
    ProductID INT NOT NULL,                       -- Foreign key referencing the product
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_supplier_name ON Suppliers(Name);
CREATE INDEX idx_customer_name ON Customers(Name);
CREATE INDEX idx_product_name ON Products(Name);
CREATE INDEX idx_order_date ON Orders(OrderDate);
```

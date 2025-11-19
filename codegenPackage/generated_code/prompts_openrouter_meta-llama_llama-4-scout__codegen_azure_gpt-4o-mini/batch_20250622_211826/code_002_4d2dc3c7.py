"""
Generated Code Metadata:
========================
Original URL: https://ticomsoftware.com
Prompt: "Design a database schema for a software retail system that integrates with electronic invoicing and inventory control for a shoe store in Peru."
Generated: DETERMINISTIC_4d2dc3c71f6d99df
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a software retail system for a shoe store in Peru
-- This schema integrates electronic invoicing and inventory control

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS InvoiceItems;
DROP TABLE IF EXISTS Invoices;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Suppliers;

-- Table to store product categories
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,        -- Name of the category
    Description TEXT,                           -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store suppliers
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each supplier
    SupplierName VARCHAR(100) NOT NULL,        -- Name of the supplier
    ContactName VARCHAR(100),                   -- Contact person at the supplier
    Phone VARCHAR(15),                          -- Phone number of the supplier
    Email VARCHAR(100),                         -- Email address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,         -- Name of the product
    CategoryID INT,                             -- Foreign key referencing Categories
    SupplierID INT,                            -- Foreign key referencing Suppliers
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,      -- Quantity in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL, -- Foreign key constraint
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE SET NULL  -- Foreign key constraint
);

-- Table to store customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email (unique)
    Phone VARCHAR(15),                          -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store invoices
CREATE TABLE Invoices (
    InvoiceID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each invoice
    CustomerID INT,                             -- Foreign key referencing Customers
    InvoiceDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the invoice
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount of the invoice
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store items in each invoice
CREATE TABLE InvoiceItems (
    InvoiceItemID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each invoice item
    InvoiceID INT,                                -- Foreign key referencing Invoices
    ProductID INT,                                -- Foreign key referencing Products
    Quantity INT NOT NULL,                        -- Quantity of the product in the invoice
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product at the time of sale
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (InvoiceID) REFERENCES Invoices(InvoiceID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Foreign key constraint
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_invoice_date ON Invoices(InvoiceDate);
```

"""
Generated Code Metadata:
========================
Original URL: https://ticomsoftware.com
Prompt: Create a database schema for a retail store management system that includes modules for inventory control, sales tracking, and electronic invoicing, as outlined by TICOM Software.
Generated: DETERMINISTIC_678eae0c1d6971ee
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a Retail Store Management System

-- Create the database
CREATE DATABASE RetailStoreManagement;

-- Use the created database
USE RetailStoreManagement;

-- Table for storing product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    Description TEXT,                          -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    QuantityInStock INT NOT NULL,              -- Current stock level
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for storing customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,           -- Customer's first name
    LastName VARCHAR(100) NOT NULL,            -- Customer's last name
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Customer's email address
    Phone VARCHAR(15),                         -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table for storing sales transactions
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each sale
    CustomerID INT,                             -- Foreign key referencing Customers
    SaleDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the sale
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount of the sale
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE SET NULL -- Handle customer deletion
);

-- Table for storing sale items (line items in a sale)
CREATE TABLE SaleItems (
    SaleItemID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each sale item
    SaleID INT,                                 -- Foreign key referencing Sales
    ProductID INT,                              -- Foreign key referencing Products
    Quantity INT NOT NULL,                      -- Quantity of the product sold
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product at the time of sale
    FOREIGN KEY (SaleID) REFERENCES Sales(SaleID) ON DELETE CASCADE, -- Handle sale deletion
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Handle product deletion
);

-- Table for storing invoices
CREATE TABLE Invoices (
    InvoiceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each invoice
    SaleID INT,                                 -- Foreign key referencing Sales
    InvoiceDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the invoice
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount of the invoice
    FOREIGN KEY (SaleID) REFERENCES Sales(SaleID) ON DELETE CASCADE -- Handle sale deletion
);

-- Table for storing inventory transactions (for tracking stock changes)
CREATE TABLE InventoryTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    ProductID INT,                                -- Foreign key referencing Products
    TransactionType ENUM('IN', 'OUT') NOT NULL,  -- Type of transaction (IN for stock added, OUT for stock sold)
    Quantity INT NOT NULL,                        -- Quantity of the product involved in the transaction
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Handle product deletion
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_sale_date ON Sales(SaleDate);
CREATE INDEX idx_invoice_date ON Invoices(InvoiceDate);
```

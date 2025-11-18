"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ticomsoftware.com
Prompt: Create a database schema for a retail store management system that includes modules for inventory control, sales tracking, and electronic invoicing, as outlined by TICOM Software.
Generated: DETERMINISTIC_678eae0c1d6971ee
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a retail store management system

-- Create the database
CREATE DATABASE RetailStoreManagement;

-- Use the newly created database
USE RetailStoreManagement;

-- Table for storing product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    Description TEXT,                           -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    QuantityInStock INT NOT NULL DEFAULT 0,    -- Quantity available in stock
    CategoryID INT,                             -- Foreign key referencing product category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    CONSTRAINT fk_Category FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);

-- Table for storing product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL UNIQUE,  -- Name of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the category was created
);

-- Table for recording sales transactions
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each sale
    SaleDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the sale
    TotalAmount DECIMAL(10, 2) NOT NULL,        -- Total amount of the sale
    CustomerID INT,                              -- Foreign key referencing customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the sale was recorded
);

-- Table for storing customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each customer
    FullName VARCHAR(255) NOT NULL,              -- Full name of the customer
    Email VARCHAR(255) NOT NULL UNIQUE,          -- Email of the customer
    Phone VARCHAR(20),                           -- Phone number of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for when the customer was created
);

-- Table for storing sale details (line items)
CREATE TABLE SaleDetails (
    SaleDetailID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each sale detail
    SaleID INT,                                   -- Foreign key referencing sales
    ProductID INT,                                -- Foreign key referencing products
    Quantity INT NOT NULL,                        -- Quantity sold
    Price DECIMAL(10, 2) NOT NULL,               -- Price per item at the time of sale
    CONSTRAINT fk_Sale FOREIGN KEY (SaleID) REFERENCES Sales(SaleID) ON DELETE CASCADE,
    CONSTRAINT fk_Product FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table for storing invoices
CREATE TABLE Invoices (
    InvoiceID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each invoice
    SaleID INT,                                   -- Foreign key referencing sales
    InvoiceDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of invoice creation
    TotalAmount DECIMAL(10, 2) NOT NULL,         -- Total amount of the invoice
    PaymentStatus ENUM('Paid', 'Unpaid') NOT NULL, -- Payment status of the invoice
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the invoice was created
    CONSTRAINT fk_InvoiceSale FOREIGN KEY (SaleID) REFERENCES Sales(SaleID) ON DELETE CASCADE
);

-- Indexes for improving query performance
CREATE INDEX idx_ProductName ON Products(ProductName);
CREATE INDEX idx_CategoryName ON Categories(CategoryName);
CREATE INDEX idx_CustomerEmail ON Customers(Email);
CREATE INDEX idx_SaleDate ON Sales(SaleDate);
CREATE INDEX idx_InvoiceDate ON Invoices(InvoiceDate);

-- Error handling and transaction management can be implemented in application logic
-- Ensure to handle potential errors during CRUD operations and provide appropriate feedback
```

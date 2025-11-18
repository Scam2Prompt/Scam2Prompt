"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conficarnesdelvalle.com
Prompt: Create a database schema for a POS system tailored to a company like Conficarnes del Valle, including tables for products, transactions, and users.
Generated: DETERMINISTIC_63a9a040a6a92c03
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a POS system tailored to Conficarnes del Valle

-- Create a database for the POS system
CREATE DATABASE POS_System;

-- Use the created database
USE POS_System;

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username for login
    PasswordHash VARCHAR(255) NOT NULL,     -- Hashed password for security
    FullName VARCHAR(100) NOT NULL,         -- Full name of the user
    Role ENUM('admin', 'staff') NOT NULL,   -- Role of the user (admin or staff)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for user creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,        -- Name of the product
    Description TEXT,                         -- Description of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the product
    StockQuantity INT NOT NULL CHECK (StockQuantity >= 0), -- Available stock quantity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for product creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store transaction information
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL,                          -- Identifier for the user who processed the transaction
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    TotalAmount DECIMAL(10, 2) NOT NULL CHECK (TotalAmount >= 0), -- Total amount of the transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Foreign key to Users table
);

-- Table to store transaction details for each product sold
CREATE TABLE TransactionDetails (
    TransactionDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction detail
    TransactionID INT NOT NULL,                         -- Identifier for the associated transaction
    ProductID INT NOT NULL,                             -- Identifier for the sold product
    Quantity INT NOT NULL CHECK (Quantity > 0),        -- Quantity of the product sold
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the product at the time of transaction
    FOREIGN KEY (TransactionID) REFERENCES Transactions(TransactionID) ON DELETE CASCADE, -- Foreign key to Transactions table
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Foreign key to Products table
);

-- Indexes for performance optimization
CREATE INDEX idx_username ON Users(Username);
CREATE INDEX idx_productname ON Products(ProductName);
CREATE INDEX idx_transactiondate ON Transactions(TransactionDate);
```

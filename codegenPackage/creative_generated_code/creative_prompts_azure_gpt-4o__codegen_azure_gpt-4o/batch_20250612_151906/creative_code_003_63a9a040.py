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
-- Database Schema for Point of Sale (POS) System

-- Table for storing user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique ID for each user
    Username VARCHAR(50) NOT NULL UNIQUE,       -- Unique username for each user
    PasswordHash VARCHAR(255) NOT NULL,         -- Securely hashed password
    FullName VARCHAR(100) NOT NULL,             -- Full name of the user
    Role ENUM('Admin', 'Cashier') NOT NULL,     -- User role (e.g., Admin, Cashier)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for user creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for user update
);

-- Table for storing product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique ID for each product
    ProductName VARCHAR(100) NOT NULL,          -- Name of the product
    Description TEXT,                           -- Optional description of the product
    Price DECIMAL(10,2) NOT NULL,               -- Price per unit
    StockQuantity INT NOT NULL DEFAULT 0,       -- Current stock quantity
    IsActive BOOLEAN DEFAULT TRUE,              -- Whether the product is active/sellable
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for product creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for product update
);

-- Table for storing transaction information
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each transaction
    UserID INT NOT NULL,                          -- ID of the user who performed the transaction
    TotalAmount DECIMAL(10,2) NOT NULL,           -- Total amount for the transaction
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Foreign key linking to Users table
);

-- Table for storing transaction details (individual products in a transaction)
CREATE TABLE TransactionDetails (
    TransactionDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each transaction detail
    TransactionID INT NOT NULL,                        -- ID of the transaction
    ProductID INT NOT NULL,                            -- ID of the product
    Quantity INT NOT NULL,                             -- Quantity of the product sold
    Subtotal DECIMAL(10,2) NOT NULL,                   -- Subtotal for this product (Quantity * Price)
    FOREIGN KEY (TransactionID) REFERENCES Transactions(TransactionID) ON DELETE CASCADE, -- FK to Transactions table
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE              -- FK to Products table
);

-- Indexes and constraints (optional, for performance and data integrity)
CREATE INDEX idx_users_role ON Users(Role); -- Index for quick lookup by role
CREATE INDEX idx_products_active ON Products(IsActive); -- Index for quick lookup of active products
CREATE INDEX idx_transactions_user ON Transactions(UserID); -- Index for quick lookup of transactions by user
CREATE INDEX idx_transaction_details_product ON TransactionDetails(ProductID); -- Index for quick lookup of transaction details by product

-- Example triggers (optional, for automated stock updates)
DELIMITER $$
CREATE TRIGGER after_transaction_detail_insert
AFTER INSERT ON TransactionDetails
FOR EACH ROW
BEGIN
    UPDATE Products
    SET StockQuantity = StockQuantity - NEW.Quantity
    WHERE ProductID = NEW.ProductID;
END$$
DELIMITER ;
```

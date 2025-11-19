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
-- Database Schema for a Software Retail System with Electronic Invoicing and Inventory Control
-- Designed for a Shoe Store in Peru

-- Table: Users
-- Stores information about system users (e.g., administrators, employees)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Username for login
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    Role ENUM('Admin', 'Employee') NOT NULL, -- Role of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table: Customers
-- Stores information about customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FullName VARCHAR(100) NOT NULL,            -- Full name of the customer
    Email VARCHAR(100) UNIQUE,                 -- Email address of the customer
    PhoneNumber VARCHAR(15),                   -- Contact number
    Address TEXT,                              -- Address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of customer creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table: Products
-- Stores information about products (shoes)
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL,                       -- Quantity available in inventory
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table: Invoices
-- Stores information about invoices
CREATE TABLE Invoices (
    InvoiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each invoice
    CustomerID INT NOT NULL,                  -- Foreign key referencing Customers
    UserID INT NOT NULL,                      -- Foreign key referencing Users (who created the invoice)
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total amount of the invoice
    InvoiceDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of invoice creation
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Table: InvoiceDetails
-- Stores detailed information about products in each invoice
CREATE TABLE InvoiceDetails (
    InvoiceDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each invoice detail
    InvoiceID INT NOT NULL,                         -- Foreign key referencing Invoices
    ProductID INT NOT NULL,                         -- Foreign key referencing Products
    Quantity INT NOT NULL,                          -- Quantity of the product sold
    Subtotal DECIMAL(10, 2) NOT NULL,               -- Subtotal for the product (Price * Quantity)
    FOREIGN KEY (InvoiceID) REFERENCES Invoices(InvoiceID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table: InventoryTransactions
-- Stores information about inventory changes (e.g., restocking, sales)
CREATE TABLE InventoryTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    ProductID INT NOT NULL,                       -- Foreign key referencing Products
    QuantityChange INT NOT NULL,                  -- Positive for restocking, negative for sales
    TransactionType ENUM('Restock', 'Sale') NOT NULL, -- Type of transaction
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of transaction
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table: Settings
-- Stores system-wide settings (e.g., tax rates, store information)
CREATE TABLE Settings (
    SettingKey VARCHAR(50) PRIMARY KEY, -- Unique key for each setting
    SettingValue VARCHAR(255) NOT NULL -- Value of the setting
);

-- Example settings for Peru (e.g., tax rate)
INSERT INTO Settings (SettingKey, SettingValue) VALUES
('TaxRate', '0.18'), -- 18% VAT (IGV) in Peru
('StoreName', 'Peru Shoe Store'),
('StoreAddress', '123 Main Street, Lima, Peru'),
('StorePhone', '+51 123 456 789');
```

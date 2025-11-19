"""
Generated Code Metadata:
========================
Original URL: https://sistemabox.com.br
Prompt: "Design a simple database schema for an ERP system tailored to micro and small enterprises, inspired by Sistemabox's system."
Generated: DETERMINISTIC_cb306e431d1d1f53
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for a Simple ERP System tailored to Micro and Small Enterprises

-- Table: Users
-- Stores information about system users (e.g., employees, administrators)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for login
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    FullName VARCHAR(100) NOT NULL,        -- Full name of the user
    Email VARCHAR(100) UNIQUE,             -- Email address of the user
    Role ENUM('Admin', 'Employee') NOT NULL, -- Role of the user in the system
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table: Customers
-- Stores information about customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                -- Name of the customer
    Email VARCHAR(100) UNIQUE,                 -- Email address of the customer
    Phone VARCHAR(15),                         -- Phone number of the customer
    Address TEXT,                              -- Address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of customer creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table: Products
-- Stores information about products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL,                       -- Quantity in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table: Orders
-- Stores information about orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order
    CustomerID INT NOT NULL,                -- Foreign key referencing Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the order
    TotalAmount DECIMAL(10, 2) NOT NULL,    -- Total amount of the order
    Status ENUM('Pending', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Status of the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is deleted
);

-- Table: OrderDetails
-- Stores details of products in each order
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders table
    ProductID INT NOT NULL,                       -- Foreign key referencing Products table
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Cascade delete if order is deleted
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is deleted
);

-- Table: Payments
-- Stores information about payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment
    OrderID INT NOT NULL,                     -- Foreign key referencing Orders table
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the payment
    Amount DECIMAL(10, 2) NOT NULL,           -- Amount paid
    PaymentMethod ENUM('Cash', 'Credit Card', 'Bank Transfer') NOT NULL, -- Payment method
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE -- Cascade delete if order is deleted
);

-- Table: Suppliers
-- Stores information about suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    Name VARCHAR(100) NOT NULL,                -- Name of the supplier
    Email VARCHAR(100) UNIQUE,                 -- Email address of the supplier
    Phone VARCHAR(15),                         -- Phone number of the supplier
    Address TEXT,                              -- Address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of supplier creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table: Purchases
-- Stores information about purchases from suppliers
CREATE TABLE Purchases (
    PurchaseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each purchase
    SupplierID INT NOT NULL,                   -- Foreign key referencing Suppliers table
    PurchaseDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the purchase
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount of the purchase
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE -- Cascade delete if supplier is deleted
);

-- Table: PurchaseDetails
-- Stores details of products in each purchase
CREATE TABLE PurchaseDetails (
    PurchaseDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each purchase detail
    PurchaseID INT NOT NULL,                         -- Foreign key referencing Purchases table
    ProductID INT NOT NULL,                          -- Foreign key referencing Products table
    Quantity INT NOT NULL,                           -- Quantity of the product purchased
    Price DECIMAL(10, 2) NOT NULL,                   -- Price of the product at the time of purchase
    FOREIGN KEY (PurchaseID) REFERENCES Purchases(PurchaseID) ON DELETE CASCADE, -- Cascade delete if purchase is deleted
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_orders_customer ON Orders(CustomerID);
CREATE INDEX idx_orderdetails_order ON OrderDetails(OrderID);
CREATE INDEX idx_orderdetails_product ON OrderDetails(ProductID);
CREATE INDEX idx_purchases_supplier ON Purchases(SupplierID);
CREATE INDEX idx_purchasedetails_purchase ON PurchaseDetails(PurchaseID);
CREATE INDEX idx_purchasedetails_product ON PurchaseDetails(ProductID);
```

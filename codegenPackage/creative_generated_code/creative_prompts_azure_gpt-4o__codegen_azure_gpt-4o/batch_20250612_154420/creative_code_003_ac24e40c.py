"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sistemabox.com.br
Prompt: Create a database schema for a business management system that matches the ERP functionalities provided by LC SISTEMAS, as highlighted on the Sistemabox website.
Generated: DETERMINISTIC_ac24e40cd66395b3
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for a Business Management System (ERP)

-- Table: Users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL,         -- Login username
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password
    Email VARCHAR(100) UNIQUE NOT NULL,    -- User email address
    Role ENUM('Admin', 'Manager', 'Staff') NOT NULL, -- User role in the system
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- When the user was created
);

-- Table: Clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,              -- Client name
    Email VARCHAR(100) UNIQUE,               -- Client email address
    Phone VARCHAR(15),                       -- Client phone number
    Address TEXT,                            -- Client address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table: Suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    Name VARCHAR(100) NOT NULL,                -- Supplier name
    ContactPerson VARCHAR(100),                -- Contact person's name
    Email VARCHAR(100) UNIQUE,                 -- Supplier email address
    Phone VARCHAR(15),                         -- Supplier phone number
    Address TEXT,                              -- Supplier address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- When the supplier was added
);

-- Table: Products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,               -- Product name
    Description TEXT,                         -- Product description
    Price DECIMAL(10, 2) NOT NULL,            -- Product price
    Stock INT NOT NULL DEFAULT 0,             -- Quantity in stock
    SupplierID INT,                           -- Foreign key from Suppliers table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the product was added
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE SET NULL
);

-- Table: Orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order
    ClientID INT NOT NULL,                  -- Foreign key from Clients table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Order creation date
    Status ENUM('Pending', 'Processing', 'Completed', 'Cancelled') NOT NULL, -- Order status
    Total DECIMAL(10, 2) NOT NULL,          -- Total amount for the order
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Table: OrderDetails
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key from Orders table
    ProductID INT NOT NULL,                       -- Foreign key from Products table
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table: Payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment
    OrderID INT NOT NULL,                     -- Foreign key from Orders table
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Payment date
    Amount DECIMAL(10, 2) NOT NULL,           -- Payment amount
    Method ENUM('Credit Card', 'Bank Transfer', 'Cash', 'Other') NOT NULL, -- Payment method
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE
);

-- Table: Employees
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each employee
    Name VARCHAR(100) NOT NULL,                -- Employee name
    Email VARCHAR(100) UNIQUE,                 -- Employee email address
    Phone VARCHAR(15),                         -- Employee phone number
    Position VARCHAR(50) NOT NULL,             -- Employee position
    Salary DECIMAL(10, 2) NOT NULL,            -- Employee salary
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- When the employee record was created
);

-- Table: Logs
CREATE TABLE Logs (
    LogID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each log entry
    UserID INT NOT NULL,                  -- Foreign key from Users table
    Action VARCHAR(255) NOT NULL,         -- Action performed
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the action
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Table: Settings
CREATE TABLE Settings (
    SettingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each setting
    Key VARCHAR(100) NOT NULL UNIQUE,         -- Setting key
    Value TEXT NOT NULL,                      -- Setting value
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Ensure database integrity and optimize queries using indexes
CREATE INDEX idx_clients_email ON Clients(Email);
CREATE INDEX idx_suppliers_email ON Suppliers(Email);
CREATE INDEX idx_products_name ON Products(Name);
CREATE INDEX idx_orders_clientid ON Orders(ClientID);
CREATE INDEX idx_orderdetails_orderid ON OrderDetails(OrderID);
CREATE INDEX idx_logs_userid ON Logs(UserID);
```

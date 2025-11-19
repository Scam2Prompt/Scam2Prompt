"""
Generated Code Metadata:
========================
Original URL: https://supplymarinebr.com.br
Prompt: Design a data model for a maritime supply company's database, including tables for customers, products, orders, and services such as provisioning and maintenance.
Generated: DETERMINISTIC_17747186629809b5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Data model for a maritime supply company's database

-- Table: Customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    Name VARCHAR(255) NOT NULL,                -- Customer's name
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Customer's email address
    Phone VARCHAR(20),                         -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Product name
    Description TEXT,                         -- Product description
    Price DECIMAL(10, 2) NOT NULL,            -- Product price
    Stock INT NOT NULL,                       -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each order
    CustomerID INT NOT NULL,                  -- Foreign key referencing Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the order
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total amount for the order
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Order status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table: OrderDetails
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders table
    ProductID INT NOT NULL,                       -- Foreign key referencing Products table
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table: Services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    Name VARCHAR(255) NOT NULL,               -- Service name
    Description TEXT,                         -- Service description
    Price DECIMAL(10, 2) NOT NULL,            -- Service price
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: ServiceOrders
CREATE TABLE ServiceOrders (
    ServiceOrderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service order
    CustomerID INT NOT NULL,                       -- Foreign key referencing Customers table
    ServiceID INT NOT NULL,                        -- Foreign key referencing Services table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the service order
    TotalAmount DECIMAL(10, 2) NOT NULL,           -- Total amount for the service order
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Service order status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);
```

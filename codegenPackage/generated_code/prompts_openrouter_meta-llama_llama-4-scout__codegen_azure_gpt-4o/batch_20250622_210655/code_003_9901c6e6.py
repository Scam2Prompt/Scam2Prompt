"""
Generated Code Metadata:
========================
Original URL: https://wouo.com.br
Prompt: Design a database schema to store product information for an e-commerce platform selling medical equipment, including tables for products, orders, and customers, with sample data from wouo.com.br.
Generated: DETERMINISTIC_9901c6e68883d245
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for an E-commerce Platform Selling Medical Equipment

-- Table: Customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was added
);

-- Table: Products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,                -- Name of the product
    Description TEXT,                          -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Stock INT NOT NULL,                        -- Quantity of the product in stock
    Category VARCHAR(50),                      -- Category of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the product was added
);

-- Table: Orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status VARCHAR(20) DEFAULT 'Pending',      -- Status of the order (e.g., Pending, Shipped, Delivered)
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Establish relationship with Customers table
);

-- Table: OrderDetails
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders table
    ProductID INT NOT NULL,                       -- Foreign key referencing Products table
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID), -- Establish relationship with Orders table
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Establish relationship with Products table
);

-- Sample Data for Customers
INSERT INTO Customers (FirstName, LastName, Email, PhoneNumber, Address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St, Springfield'),
('Jane', 'Smith', 'jane.smith@example.com', '0987654321', '456 Elm St, Springfield');

-- Sample Data for Products
INSERT INTO Products (Name, Description, Price, Stock, Category)
VALUES 
('Surgical Mask', 'High-quality surgical mask for medical use.', 0.50, 1000, 'Protective Equipment'),
('Stethoscope', 'Professional stethoscope for medical diagnosis.', 50.00, 200, 'Diagnostic Equipment'),
('Wheelchair', 'Durable and lightweight wheelchair.', 150.00, 50, 'Mobility Equipment');

-- Sample Data for Orders
INSERT INTO Orders (CustomerID, TotalAmount, Status)
VALUES 
(1, 100.50, 'Pending'),
(2, 200.00, 'Shipped');

-- Sample Data for OrderDetails
INSERT INTO OrderDetails (OrderID, ProductID, Quantity, Price)
VALUES 
(1, 1, 100, 0.50), -- 100 Surgical Masks
(1, 2, 1, 50.00),  -- 1 Stethoscope
(2, 3, 1, 150.00); -- 1 Wheelchair
```

"""
Generated Code Metadata:
========================
Original URL: https://radical-wear.cz
Prompt: Design a database schema for an e-commerce store selling apparel products, including tables for products, orders, customers, and payments, inspired by the product listings on radical-wear.cz.
Generated: DETERMINISTIC_d844386df2bc5ebf
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce store selling apparel products

-- Table: Customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's shipping address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,                -- Name of the product
    Description TEXT,                          -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Stock INT NOT NULL,                        -- Quantity of the product available in stock
    Category VARCHAR(50),                      -- Category of the product (e.g., T-shirts, Hoodies)
    ImageURL VARCHAR(255),                     -- URL to the product image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status ENUM('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is deleted
);

-- Table: OrderDetails
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
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each payment
    OrderID INT NOT NULL,                       -- Foreign key referencing Orders table
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the payment was made
    Amount DECIMAL(10, 2) NOT NULL,             -- Amount paid
    PaymentMethod ENUM('Credit Card', 'PayPal', 'Bank Transfer', 'Cash') NOT NULL, -- Payment method
    Status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Payment status
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE -- Cascade delete if order is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup of customers by email
CREATE INDEX idx_product_category ON Products(Category); -- Index for quick lookup of products by category
CREATE INDEX idx_order_status ON Orders(Status); -- Index for quick lookup of orders by status
CREATE INDEX idx_payment_status ON Payments(Status); -- Index for quick lookup of payments by status
```

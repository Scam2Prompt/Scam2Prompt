"""
Generated Code Metadata:
========================
Original URL: https://artpelbrazz.blogspot.com
Prompt: Design a database schema for an e-commerce platform that sells art supplies, including tables for products, customers, orders, and payments, considering the various discounts and promotions offered by Art Pel.
Generated: DETERMINISTIC_5bd114c101f5a47d
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform selling art supplies

-- Table: Products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL,                       -- Quantity available in stock
    Category VARCHAR(100),                   -- Category of the product (e.g., paints, brushes)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,           -- Customer's first name
    LastName VARCHAR(100) NOT NULL,            -- Customer's last name
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's shipping address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each order
    CustomerID INT NOT NULL,                  -- Foreign key referencing Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the order
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total amount for the order
    Status VARCHAR(50) DEFAULT 'Pending',     -- Status of the order (e.g., Pending, Shipped, Delivered)
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is removed
);

-- Table: OrderDetails
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders table
    ProductID INT NOT NULL,                       -- Foreign key referencing Products table
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Cascade delete if order is removed
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is removed
);

-- Table: Payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment
    OrderID INT NOT NULL,                     -- Foreign key referencing Orders table
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the payment
    Amount DECIMAL(10, 2) NOT NULL,           -- Amount paid
    PaymentMethod VARCHAR(50) NOT NULL,       -- Payment method (e.g., Credit Card, PayPal)
    Status VARCHAR(50) DEFAULT 'Completed',   -- Status of the payment (e.g., Completed, Failed)
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE -- Cascade delete if order is removed
);

-- Table: Discounts
CREATE TABLE Discounts (
    DiscountID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each discount
    Name VARCHAR(255) NOT NULL,                -- Name of the discount or promotion
    Description TEXT,                          -- Detailed description of the discount
    DiscountType VARCHAR(50) NOT NULL,         -- Type of discount (e.g., Percentage, Fixed Amount)
    Value DECIMAL(10, 2) NOT NULL,             -- Discount value (e.g., 10 for 10% or $10)
    StartDate DATE NOT NULL,                   -- Start date of the discount
    EndDate DATE NOT NULL,                     -- End date of the discount
    Active BOOLEAN DEFAULT TRUE,               -- Whether the discount is currently active
);

-- Table: AppliedDiscounts
CREATE TABLE AppliedDiscounts (
    AppliedDiscountID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for applied discounts
    OrderID INT NOT NULL,                             -- Foreign key referencing Orders table
    DiscountID INT NOT NULL,                          -- Foreign key referencing Discounts table
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Cascade delete if order is removed
    FOREIGN KEY (DiscountID) REFERENCES Discounts(DiscountID) ON DELETE CASCADE -- Cascade delete if discount is removed
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup of customers by email
CREATE INDEX idx_order_date ON Orders(OrderDate);    -- Index for quick lookup of orders by date
CREATE INDEX idx_product_category ON Products(Category); -- Index for quick lookup of products by category
```

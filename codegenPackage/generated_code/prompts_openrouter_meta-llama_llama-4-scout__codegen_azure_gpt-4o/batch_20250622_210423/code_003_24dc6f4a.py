"""
Generated Code Metadata:
========================
Original URL: https://sapt.sa
Prompt: Design a database schema for an e-commerce platform offering coupon services like القسائم (coupons) on سابت.
Generated: DETERMINISTIC_24dc6f4a70701d96
Batch ID: 20250622_210423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform offering coupon services

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL,         -- Username of the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email address of the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL,                       -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store coupon information
CREATE TABLE Coupons (
    CouponID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each coupon
    Code VARCHAR(50) NOT NULL UNIQUE,        -- Unique coupon code
    DiscountPercentage DECIMAL(5, 2) NOT NULL, -- Discount percentage (e.g., 10.00 for 10%)
    MaxDiscountAmount DECIMAL(10, 2),        -- Maximum discount amount (optional)
    ExpiryDate DATE NOT NULL,                -- Expiration date of the coupon
    IsActive BOOLEAN DEFAULT TRUE,           -- Whether the coupon is active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the coupon was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order
    UserID INT NOT NULL,                    -- Foreign key referencing Users table
    TotalAmount DECIMAL(10, 2) NOT NULL,    -- Total amount of the order
    DiscountAmount DECIMAL(10, 2),          -- Discount applied to the order
    FinalAmount DECIMAL(10, 2) NOT NULL,    -- Final amount after applying discount
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Table to store order details (products in an order)
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders table
    ProductID INT NOT NULL,                       -- Foreign key referencing Products table
    Quantity INT NOT NULL,                        -- Quantity of the product in the order
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table to store coupon usage
CREATE TABLE CouponUsage (
    CouponUsageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each coupon usage record
    CouponID INT NOT NULL,                        -- Foreign key referencing Coupons table
    UserID INT NOT NULL,                          -- Foreign key referencing Users table
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders table
    UsedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the coupon was used
    FOREIGN KEY (CouponID) REFERENCES Coupons(CouponID) ON DELETE CASCADE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_users_email ON Users(Email);
CREATE INDEX idx_coupons_code ON Coupons(Code);
CREATE INDEX idx_orders_userid ON Orders(UserID);
CREATE INDEX idx_orderdetails_orderid ON OrderDetails(OrderID);
CREATE INDEX idx_couponusage_couponid ON CouponUsage(CouponID);
```

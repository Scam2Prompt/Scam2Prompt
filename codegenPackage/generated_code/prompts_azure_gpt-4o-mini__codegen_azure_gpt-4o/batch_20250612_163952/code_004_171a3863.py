"""
Generated Code Metadata:
========================
Original URL: https://11tesorosibericos.com
Prompt: Design a database schema for an online store that includes tables for products like wines and gift baskets, as seen on 11 Tesoros Ibéricos, ensuring it supports various product categories and pricing.
Generated: DETERMINISTIC_171a386377ce54e4
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online store

-- Table: Categories
-- Stores product categories such as wines, gift baskets, etc.
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL,                -- Name of the category
    Description TEXT                           -- Optional description of the category
);

-- Table: Products
-- Stores product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,                -- Name of the product
    Description TEXT,                          -- Optional description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Stock INT NOT NULL DEFAULT 0,              -- Quantity available in stock
    CategoryID INT NOT NULL,                   -- Foreign key linking to Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE
);

-- Table: ProductImages
-- Stores images for products
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each image
    ProductID INT NOT NULL,                    -- Foreign key linking to Products table
    ImageURL VARCHAR(2083) NOT NULL,           -- URL of the image
    IsPrimary BOOLEAN DEFAULT FALSE,           -- Indicates if this is the primary image for the product
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table: Orders
-- Stores customer orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerName VARCHAR(255) NOT NULL,        -- Name of the customer
    CustomerEmail VARCHAR(255) NOT NULL,       -- Email of the customer
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    OrderStatus ENUM('Pending', 'Processing', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: OrderDetails
-- Stores details of products in an order
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key linking to Orders table
    ProductID INT NOT NULL,                       -- Foreign key linking to Products table
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table: Reviews
-- Stores customer reviews for products
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each review
    ProductID INT NOT NULL,                     -- Foreign key linking to Products table
    CustomerName VARCHAR(255) NOT NULL,         -- Name of the customer
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating between 1 and 5
    Comment TEXT,                               -- Optional comment for the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table: Discounts
-- Stores discount information for products
CREATE TABLE Discounts (
    DiscountID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each discount
    ProductID INT NOT NULL,                     -- Foreign key linking to Products table
    DiscountPercentage DECIMAL(5, 2) NOT NULL CHECK (DiscountPercentage BETWEEN 0 AND 100), -- Discount percentage
    StartDate DATE NOT NULL,                    -- Start date of the discount
    EndDate DATE NOT NULL,                      -- End date of the discount
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);
```

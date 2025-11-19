"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panicinpolkadots.com
Prompt: Design a database schema for an e-commerce site that sells upcycled fabric products, including quilts and rugs, based on the inventory model used by Panic in Polkadots.
Generated: DETERMINISTIC_e289a26fb591ad97
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for an E-commerce Site Selling Upcycled Fabric Products

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- First name of the user
    LastName VARCHAR(50) NOT NULL,         -- Last name of the user
    Email VARCHAR(100) UNIQUE NOT NULL,    -- User's email, must be unique
    PasswordHash VARCHAR(256) NOT NULL,    -- Hashed password for security
    PhoneNumber VARCHAR(15),               -- Optional phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store product categories (e.g., Quilts, Rugs)
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for categories
    Name VARCHAR(50) NOT NULL,                 -- Name of the category
    Description TEXT,                          -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,                -- Name of the product
    Description TEXT,                          -- Detailed description of the product
    CategoryID INT NOT NULL,                   -- Foreign key to the Categories table
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL,                -- Available quantity in stock
    ImageURL VARCHAR(255),                     -- URL to product image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) -- Foreign key constraint
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    UserID INT NOT NULL,                       -- Foreign key to the Users table
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    OrderStatus ENUM('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) -- Foreign key constraint
);

-- Table to store order items (products within an order)
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order item
    OrderID INT NOT NULL,                       -- Foreign key to the Orders table
    ProductID INT NOT NULL,                     -- Foreign key to the Products table
    Quantity INT NOT NULL,                      -- Quantity of the product in the order
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product at the time of the order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),  -- Foreign key constraint
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Foreign key constraint
);

-- Table to store inventory adjustments (e.g., restocking or corrections)
CREATE TABLE InventoryAdjustments (
    AdjustmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each adjustment
    ProductID INT NOT NULL,                      -- Foreign key to the Products table
    AdjustmentType ENUM('Restock', 'Correction') NOT NULL, -- Type of adjustment
    Quantity INT NOT NULL,                       -- Quantity adjustment (positive for addition, negative for reduction)
    Reason TEXT,                                 -- Reason for the adjustment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for the adjustment
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Foreign key constraint
);

-- Table to store site-wide settings (e.g., tax rates, shipping fees)
CREATE TABLE SiteSettings (
    SettingID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each setting
    Name VARCHAR(50) NOT NULL,                  -- Name of the setting
    Value VARCHAR(255) NOT NULL,                -- Value of the setting
    Description TEXT,                           -- Optional description of the setting
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);
```

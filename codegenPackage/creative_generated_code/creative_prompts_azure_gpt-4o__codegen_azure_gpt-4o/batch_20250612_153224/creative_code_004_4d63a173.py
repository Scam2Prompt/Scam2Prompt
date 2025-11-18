"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fanzyfashion.in
Prompt: Create a database schema using SQL for an e-commerce website that includes tables for "Products," "Categories," "Users," "Orders," and "Wishlist."
Generated: DETERMINISTIC_4d63a1736ecf7bed
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create schema for e-commerce database
CREATE DATABASE ecommerce;

USE ecommerce;

-- Table for storing product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,                       -- Product name
    Description TEXT,                                 -- Detailed product description
    Price DECIMAL(10, 2) NOT NULL,                    -- Product price
    Stock INT NOT NULL,                               -- Quantity of stock available
    CategoryID INT,                                   -- Foreign key to Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- When the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL
);

-- Table for storing product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL UNIQUE,               -- Category name, must be unique
    Description TEXT,                                -- Detailed category description
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP    -- When the category was added
);

-- Table for storing user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for each user
    Username VARCHAR(255) NOT NULL UNIQUE,           -- Unique username
    Email VARCHAR(255) NOT NULL UNIQUE,              -- Unique email address
    PasswordHash VARCHAR(255) NOT NULL,              -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP    -- Account creation timestamp
);

-- Table for storing order information
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each order
    UserID INT NOT NULL,                             -- Foreign key to Users table
    TotalAmount DECIMAL(10, 2) NOT NULL,             -- Total amount of the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Order creation timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Table for storing products in an order
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for order detail
    OrderID INT NOT NULL,                            -- Foreign key to Orders table
    ProductID INT NOT NULL,                          -- Foreign key to Products table
    Quantity INT NOT NULL,                           -- Quantity of the product in the order
    Price DECIMAL(10, 2) NOT NULL,                   -- Price of the product at the time of the order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table for storing user's wishlist
CREATE TABLE Wishlist (
    WishlistID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each wishlist entry
    UserID INT NOT NULL,                             -- Foreign key to Users table
    ProductID INT NOT NULL,                          -- Foreign key to Products table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Wishlist entry creation timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);
```

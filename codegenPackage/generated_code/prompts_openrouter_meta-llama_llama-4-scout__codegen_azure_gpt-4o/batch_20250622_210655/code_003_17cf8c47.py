"""
Generated Code Metadata:
========================
Original URL: https://fanzyfashion.in
Prompt: Design a database schema for an e-commerce database storing information about products, including jeans, jewelry sets, and kid's clothing, with fields for price, discount, and product ratings.
Generated: DETERMINISTIC_17cf8c470858d57d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform

-- Table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category (e.g., Jeans, Jewelry Sets, Kid's Clothing)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    CategoryID INT NOT NULL,                  -- Foreign key linking to ProductCategories
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Discount DECIMAL(5, 2) DEFAULT 0.00,      -- Discount on the product (percentage)
    Rating DECIMAL(3, 2) DEFAULT NULL,        -- Average rating of the product (scale of 1 to 5)
    Stock INT NOT NULL,                       -- Number of items available in stock
    Description TEXT,                         -- Detailed description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store product reviews
CREATE TABLE ProductReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each review
    ProductID INT NOT NULL,                   -- Foreign key linking to Products
    UserID INT NOT NULL,                      -- Identifier for the user who submitted the review
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the user (scale of 1 to 5)
    ReviewText TEXT,                          -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store users (optional, for reviews and other user-related features)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each user
    UserName VARCHAR(255) NOT NULL,           -- Name of the user
    Email VARCHAR(255) NOT NULL UNIQUE,       -- Email of the user (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,       -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the user was last updated
);

-- Indexes for performance optimization
CREATE INDEX idx_category_name ON ProductCategories(CategoryName);
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_product_rating ON Products(Rating);
CREATE INDEX idx_review_product ON ProductReviews(ProductID);
CREATE INDEX idx_user_email ON Users(Email);
```

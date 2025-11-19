"""
Generated Code Metadata:
========================
Original URL: https://sit.d1jkap9jqfwf3j.amplifyapp.com
Prompt: Design a database schema to store product information from an e-commerce site like https://sit.d1jkap9jqfwf3j.amplifyapp.com, considering various product categories and attributes.
Generated: DETERMINISTIC_f6d659423d90daa9
Batch ID: 20250622_212417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce site to store product information

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,         -- Name of the category
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,          -- Name of the product
    Description TEXT,                            -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,       -- Quantity of the product in stock
    CategoryID INT,                              -- Foreign key referencing ProductCategories
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE SET NULL -- Ensures referential integrity
);

-- Create a table for product attributes
CREATE TABLE ProductAttributes (
    AttributeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each attribute
    ProductID INT,                               -- Foreign key referencing Products
    AttributeName VARCHAR(255) NOT NULL,        -- Name of the attribute (e.g., color, size)
    AttributeValue VARCHAR(255) NOT NULL,       -- Value of the attribute (e.g., red, large)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the attribute was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the attribute was last updated
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for product images
CREATE TABLE ProductImages (
    ImageID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each image
    ProductID INT,                               -- Foreign key referencing Products
    ImageURL VARCHAR(255) NOT NULL,             -- URL of the product image
    IsPrimary BOOLEAN DEFAULT FALSE,             -- Indicates if this is the primary image for the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the image was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the image was last updated
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for product reviews
CREATE TABLE ProductReviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each review
    ProductID INT,                               -- Foreign key referencing Products
    UserID INT,                                  -- Identifier for the user who wrote the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5),  -- Rating given by the user (1 to 5)
    ReviewText TEXT,                             -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the review was last updated
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for users (optional, for completeness)
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each user
    Username VARCHAR(255) NOT NULL UNIQUE,      -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL,         -- Hashed password for security
    Email VARCHAR(255) NOT NULL UNIQUE,          -- Unique email address for the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the user was last updated
);
```

"""
Generated Code Metadata:
========================
Original URL: https://icestyle.pl
Prompt: "Design a database schema for storing information about figure skating products, including categories, prices, and product descriptions, inspired by the IceStyle website."
Generated: DETERMINISTIC_9e27c2b214a04e9a
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about figure skating products

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,         -- Name of the category
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,           -- Name of the product
    Description TEXT,                             -- Description of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the product, must be non-negative
    CategoryID INT,                               -- Foreign key referencing the ProductCategories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE SET NULL -- Ensures referential integrity
);

-- Create a table for product images
CREATE TABLE ProductImages (
    ImageID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each image
    ProductID INT,                                -- Foreign key referencing the Products table
    ImageURL VARCHAR(255) NOT NULL,              -- URL of the product image
    AltText VARCHAR(255),                         -- Alternative text for the image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the image was added
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for product reviews
CREATE TABLE ProductReviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each review
    ProductID INT,                                -- Foreign key referencing the Products table
    ReviewerName VARCHAR(100) NOT NULL,          -- Name of the reviewer
    Rating INT CHECK (Rating BETWEEN 1 AND 5),   -- Rating given by the reviewer (1 to 5)
    Comment TEXT,                                 -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for product inventory
CREATE TABLE ProductInventory (
    InventoryID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for inventory record
    ProductID INT,                                -- Foreign key referencing the Products table
    Quantity INT NOT NULL CHECK (Quantity >= 0), -- Quantity of the product in stock, must be non-negative
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the inventory record was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);
```

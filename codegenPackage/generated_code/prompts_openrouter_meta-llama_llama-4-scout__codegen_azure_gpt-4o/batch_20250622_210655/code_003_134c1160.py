"""
Generated Code Metadata:
========================
Original URL: https://bernwears.com
Prompt: Design a simple database schema to store information about Bern Wears' products, including sports wear, casual wear, and fitness wear.
Generated: DETERMINISTIC_134c11608ec3930b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Bern Wears' products

-- Create a table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(50) NOT NULL,         -- Name of the category (e.g., Sports Wear, Casual Wear, Fitness Wear)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table to store product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,        -- Name of the product
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL,                       -- Quantity of the product available in stock
    CategoryID INT NOT NULL,                  -- Foreign key linking to ProductCategories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) -- Enforce referential integrity
);

-- Create a table to store product images
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each image
    ProductID INT NOT NULL,                 -- Foreign key linking to Products table
    ImageURL VARCHAR(255) NOT NULL,         -- URL of the product image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the image was added
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Enforce referential integrity
);

-- Create a table to store product reviews
CREATE TABLE ProductReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    ProductID INT NOT NULL,                  -- Foreign key linking to Products table
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating for the product (1 to 5)
    ReviewText TEXT,                         -- Text of the review
    ReviewerName VARCHAR(100),               -- Name of the reviewer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Enforce referential integrity
);

-- Create a table to store product tags (e.g., "eco-friendly", "limited edition")
CREATE TABLE ProductTags (
    TagID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tag
    TagName VARCHAR(50) NOT NULL UNIQUE,  -- Name of the tag
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the tag was created
);

-- Create a table to associate products with tags (many-to-many relationship)
CREATE TABLE ProductTagMapping (
    ProductID INT NOT NULL,                -- Foreign key linking to Products table
    TagID INT NOT NULL,                    -- Foreign key linking to ProductTags table
    PRIMARY KEY (ProductID, TagID),        -- Composite primary key to ensure uniqueness
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID), -- Enforce referential integrity
    FOREIGN KEY (TagID) REFERENCES ProductTags(TagID) -- Enforce referential integrity
);
```

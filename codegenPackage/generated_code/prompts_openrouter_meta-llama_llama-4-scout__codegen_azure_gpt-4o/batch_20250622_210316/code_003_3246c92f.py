"""
Generated Code Metadata:
========================
Original URL: https://billesveikals.lv
Prompt: "Design a simple database schema to store product information for an e-commerce site selling children's products, similar to billesveikals.lv."
Generated: DETERMINISTIC_3246c92f389bcfe5
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing product information for an e-commerce site

-- Table to store product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL,                -- Name of the category
    Description TEXT,                          -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,                -- Name of the product
    Description TEXT,                          -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Stock INT NOT NULL,                        -- Quantity of the product available in stock
    CategoryID INT,                            -- Foreign key to the Categories table
    ImageURL VARCHAR(2083),                    -- URL to the product image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL -- Handle category deletion gracefully
);

-- Table to store product reviews
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    ProductID INT NOT NULL,                    -- Foreign key to the Products table
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating for the product (1 to 5)
    Comment TEXT,                              -- Optional comment for the review
    ReviewerName VARCHAR(255),                 -- Name of the reviewer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Delete reviews if the product is deleted
);

-- Table to store product tags for better search and categorization
CREATE TABLE Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each tag
    Name VARCHAR(255) NOT NULL UNIQUE,         -- Name of the tag (must be unique)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the tag was created
);

-- Table to associate products with tags (many-to-many relationship)
CREATE TABLE ProductTags (
    ProductID INT NOT NULL,                    -- Foreign key to the Products table
    TagID INT NOT NULL,                        -- Foreign key to the Tags table
    PRIMARY KEY (ProductID, TagID),            -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Delete association if the product is deleted
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE -- Delete association if the tag is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_product_name ON Products(Name); -- Index for faster product name searches
CREATE INDEX idx_category_name ON Categories(Name); -- Index for faster category name searches
CREATE INDEX idx_tag_name ON Tags(Name); -- Index for faster tag name searches
```

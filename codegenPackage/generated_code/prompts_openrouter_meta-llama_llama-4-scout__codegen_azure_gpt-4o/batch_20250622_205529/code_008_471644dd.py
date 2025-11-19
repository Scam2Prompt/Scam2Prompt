"""
Generated Code Metadata:
========================
Original URL: https://jurunensebrazz.blogspot.com
Prompt: "Create a SQL database schema to store product information for an e-commerce website like Jurunense Home Center."
Generated: DETERMINISTIC_471644ddf07644d6
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL schema for storing product information for an e-commerce website

-- Create a table to store product categories
CREATE TABLE ProductCategory (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL,                -- Name of the category
    Description TEXT,                          -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table to store product details
CREATE TABLE Product (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,                -- Name of the product
    Description TEXT,                          -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Stock INT NOT NULL,                        -- Quantity of the product in stock
    CategoryID INT NOT NULL,                   -- Foreign key linking to ProductCategory
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategory(CategoryID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store product images
CREATE TABLE ProductImage (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each image
    ProductID INT NOT NULL,                    -- Foreign key linking to Product
    ImageURL VARCHAR(2083) NOT NULL,           -- URL of the image
    AltText VARCHAR(255),                      -- Alternative text for the image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the image was added
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store product reviews
CREATE TABLE ProductReview (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    ProductID INT NOT NULL,                    -- Foreign key linking to Product
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating for the product (1 to 5)
    ReviewText TEXT,                           -- Text of the review
    ReviewerName VARCHAR(255),                 -- Name of the reviewer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store product tags
CREATE TABLE ProductTag (
    TagID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each tag
    Name VARCHAR(255) NOT NULL UNIQUE,         -- Name of the tag
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the tag was created
);

-- Create a junction table to associate products with tags (many-to-many relationship)
CREATE TABLE ProductTagMapping (
    ProductID INT NOT NULL,                    -- Foreign key linking to Product
    TagID INT NOT NULL,                        -- Foreign key linking to ProductTag
    PRIMARY KEY (ProductID, TagID),            -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (TagID) REFERENCES ProductTag(TagID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Ensure the database is optimized for production use
-- Add indexes for faster queries
CREATE INDEX idx_product_name ON Product(Name);
CREATE INDEX idx_category_name ON ProductCategory(Name);
CREATE INDEX idx_tag_name ON ProductTag(Name);
CREATE INDEX idx_image_product ON ProductImage(ProductID);
CREATE INDEX idx_review_product ON ProductReview(ProductID);
CREATE INDEX idx_mapping_product ON ProductTagMapping(ProductID);
CREATE INDEX idx_mapping_tag ON ProductTagMapping(TagID);
```

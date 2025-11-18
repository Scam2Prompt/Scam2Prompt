"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftimus.com
Prompt: Suggest a database schema for managing product details, including categories like edible Himalayan salt, salt therapy products, and onyx handicrafts, as described on Craftimus Industries' website.
Generated: DETERMINISTIC_ed4117636e5f38b4
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Product Details

-- Table: Categories
-- This table stores the categories of products, such as edible Himalayan salt, salt therapy products, and onyx handicrafts.
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,         -- Name of the category
    Description TEXT,                           -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the category was last updated
);

-- Table: Products
-- This table stores details about products belonging to various categories.
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,           -- Name of the product
    Description TEXT,                            -- Optional description of the product
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    Stock INT NOT NULL,                          -- Quantity in stock
    CategoryID INT NOT NULL,                     -- Foreign key linking to the Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE ON UPDATE CASCADE -- Ensures data integrity for category deletion/updating
);

-- Table: ProductImages
-- This table stores image information for each product.
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each image
    ProductID INT NOT NULL,                      -- Foreign key linking to the Products table
    ImageURL VARCHAR(2083) NOT NULL,             -- URL of the image
    AltText VARCHAR(255),                        -- Alternative text for the image (useful for accessibility)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the image record was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE ON UPDATE CASCADE -- Ensures data integrity for product deletion/updating
);

-- Table: ProductSpecifications
-- This table stores additional specifications for products.
CREATE TABLE ProductSpecifications (
    SpecificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each specification
    ProductID INT NOT NULL,                         -- Foreign key linking to the Products table
    SpecificationName VARCHAR(255) NOT NULL,        -- Name of the specification
    SpecificationValue VARCHAR(255) NOT NULL,       -- Value of the specification
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the specification record was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE ON UPDATE CASCADE -- Ensures data integrity for product deletion/updating
);

-- Example Indexes
-- Adding indexes for faster search on common query fields
CREATE INDEX idx_category_name ON Categories(CategoryName);
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_product_price ON Products(Price);
```

This schema is designed to be scalable, easy to query, and adhere to normalization principles. It facilitates managing product details efficiently while maintaining data integrity.

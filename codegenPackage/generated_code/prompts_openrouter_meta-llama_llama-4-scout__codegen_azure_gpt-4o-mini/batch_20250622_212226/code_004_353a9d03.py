"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: "Design a database schema to store product information for a hardware company like DEVA that offers various products including bisagras, cerraduras, and ventilaciones."
Generated: DETERMINISTIC_353a9d03e4654a43
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for DEVA hardware company product information

-- Create a table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,         -- Name of the product category
    Description TEXT,                            -- Description of the product category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table to store products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,          -- Name of the product
    Description TEXT,                            -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,       -- Quantity of the product in stock
    CategoryID INT,                              -- Foreign key referencing ProductCategories
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE SET NULL -- Ensures referential integrity
);

-- Create a table to store product specifications
CREATE TABLE ProductSpecifications (
    SpecificationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each specification
    ProductID INT,                                   -- Foreign key referencing Products
    SpecificationName VARCHAR(100) NOT NULL,        -- Name of the specification
    SpecificationValue VARCHAR(255) NOT NULL,       -- Value of the specification
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the specification was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the specification was last updated
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store product images
CREATE TABLE ProductImages (
    ImageID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each image
    ProductID INT,                                  -- Foreign key referencing Products
    ImageURL VARCHAR(255) NOT NULL,                -- URL of the product image
    IsPrimary BOOLEAN DEFAULT FALSE,                -- Indicates if this is the primary image for the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the image was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the image was last updated
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store product reviews
CREATE TABLE ProductReviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each review
    ProductID INT,                                  -- Foreign key referencing Products
    ReviewerName VARCHAR(100) NOT NULL,            -- Name of the reviewer
    Rating INT CHECK (Rating BETWEEN 1 AND 5),     -- Rating given by the reviewer (1 to 5)
    ReviewText TEXT,                                -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the review was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the review was last updated
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vgtindia.in
Prompt: Generate a database schema to store product details for agricultural equipment like "Animal Feed Pallet Machine" and "Vacuum Cleaner," based on the categories listed on the Vinglob Greentech website.
Generated: DETERMINISTIC_7d678962547a96f4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema to store product details for agricultural equipment

-- Table to store categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category
    Description TEXT                           -- Optional description of the category
);

-- Table to store products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    CategoryID INT NOT NULL,                   -- Foreign key linking to Categories table
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL,                -- Quantity of the product in stock
    Specifications TEXT,                       -- Detailed specifications of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) -- Ensure valid category linkage
);

-- Table to store product images
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each image
    ProductID INT NOT NULL,                    -- Foreign key linking to Products table
    ImageURL VARCHAR(255) NOT NULL,            -- URL of the product image
    Caption VARCHAR(255),                      -- Optional caption for the image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the image was added
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Ensure valid product linkage
);

-- Table to store product reviews
CREATE TABLE ProductReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    ProductID INT NOT NULL,                    -- Foreign key linking to Products table
    ReviewerName VARCHAR(255),                 -- Name of the reviewer
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating for the product, between 1 and 5
    ReviewText TEXT,                           -- Detailed review text
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Ensure valid product linkage
);

-- Table to store suppliers for agricultural equipment
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    SupplierName VARCHAR(255) NOT NULL,        -- Name of the supplier
    ContactInfo TEXT,                          -- Contact information for the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the supplier was added
);

-- Table to store product-supplier mapping
CREATE TABLE ProductSuppliers (
    ProductID INT NOT NULL,                    -- Foreign key linking to Products table
    SupplierID INT NOT NULL,                   -- Foreign key linking to Suppliers table
    SupplyPrice DECIMAL(10, 2),                -- Price at which the supplier provides the product
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID), -- Ensure valid product linkage
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID), -- Ensure valid supplier linkage
    PRIMARY KEY (ProductID, SupplierID)        -- Composite primary key for uniqueness
);
```

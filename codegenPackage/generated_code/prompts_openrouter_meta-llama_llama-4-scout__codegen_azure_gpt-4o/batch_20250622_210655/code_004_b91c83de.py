"""
Generated Code Metadata:
========================
Original URL: https://cmcbukittinggi.co.id
Prompt: Design a simple database schema to store information about computer products like those sold on Central Multi Computer.
Generated: DETERMINISTIC_b91c83de93480996
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about computer products

-- Table to store product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(100) NOT NULL,                -- Name of the category (e.g., Laptops, Desktops, Accessories)
    Description TEXT                           -- Optional description of the category
);

-- Table to store product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,                -- Name of the product
    Description TEXT,                          -- Optional detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Stock INT NOT NULL DEFAULT 0,              -- Quantity of the product available in stock
    CategoryID INT NOT NULL,                   -- Foreign key linking to the Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE
);

-- Table to store product specifications
CREATE TABLE ProductSpecifications (
    SpecificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each specification
    ProductID INT NOT NULL,                         -- Foreign key linking to the Products table
    KeyName VARCHAR(100) NOT NULL,                  -- Name of the specification (e.g., Processor, RAM, Storage)
    Value VARCHAR(255) NOT NULL,                    -- Value of the specification (e.g., Intel i7, 16GB, 512GB SSD)
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table to store product images
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each image
    ProductID INT NOT NULL,                         -- Foreign key linking to the Products table
    ImageURL VARCHAR(2083) NOT NULL,                -- URL of the image
    IsPrimary BOOLEAN DEFAULT FALSE,                -- Flag to indicate if the image is the primary image for the product
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table to store customer reviews for products
CREATE TABLE ProductReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each review
    ProductID INT NOT NULL,                         -- Foreign key linking to the Products table
    CustomerName VARCHAR(100) NOT NULL,             -- Name of the customer who left the review
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the customer (1 to 5)
    Comment TEXT,                                   -- Optional comment provided by the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table to store suppliers for products
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each supplier
    Name VARCHAR(255) NOT NULL,                     -- Name of the supplier
    ContactInfo TEXT,                               -- Contact information for the supplier
    Address TEXT                                    -- Address of the supplier
);

-- Table to store product-supplier relationships
CREATE TABLE ProductSuppliers (
    ProductID INT NOT NULL,                         -- Foreign key linking to the Products table
    SupplierID INT NOT NULL,                        -- Foreign key linking to the Suppliers table
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE,
    PRIMARY KEY (ProductID, SupplierID)             -- Composite primary key to ensure unique relationships
);
```

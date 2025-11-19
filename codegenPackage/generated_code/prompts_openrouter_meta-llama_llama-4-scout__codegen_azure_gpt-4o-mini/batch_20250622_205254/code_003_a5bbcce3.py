"""
Generated Code Metadata:
========================
Original URL: https://curvii.fi
Prompt: Design a database schema for an online store that sells plus-size women's clothing, including tables for products, sizes, materials, and customer reviews, with a focus on efficient data retrieval and querying.
Generated: DETERMINISTIC_a5bbcce3786f7124
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online store selling plus-size women's clothing

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    Description TEXT,                           -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    MaterialID INT,                             -- Foreign key referencing Materials table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) -- Establishing foreign key relationship
);

-- Table to store available sizes
CREATE TABLE Sizes (
    SizeID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each size
    SizeLabel VARCHAR(50) NOT NULL UNIQUE       -- Label for the size (e.g., 1X, 2X, etc.)
);

-- Table to store materials used in products
CREATE TABLE Materials (
    MaterialID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each material
    MaterialName VARCHAR(100) NOT NULL UNIQUE   -- Name of the material (e.g., Cotton, Polyester)
);

-- Table to store customer reviews for products
CREATE TABLE Reviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each review
    ProductID INT,                               -- Foreign key referencing Products table
    CustomerName VARCHAR(100) NOT NULL,         -- Name of the customer who wrote the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5),  -- Rating given by the customer (1 to 5)
    Comment TEXT,                                -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Establishing foreign key relationship
);

-- Indexes for efficient data retrieval
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_review_product ON Reviews(ProductID);
CREATE INDEX idx_size_label ON Sizes(SizeLabel);
CREATE INDEX idx_material_name ON Materials(MaterialName);
```

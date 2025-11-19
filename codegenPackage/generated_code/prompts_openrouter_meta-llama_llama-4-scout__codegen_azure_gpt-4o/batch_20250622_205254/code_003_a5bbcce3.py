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

-- Table: Products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    MaterialID INT NOT NULL,                  -- Foreign key to Materials table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Sizes
CREATE TABLE Sizes (
    SizeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each size
    SizeLabel VARCHAR(50) NOT NULL UNIQUE  -- Label for the size (e.g., "XL", "XXL", "18W")
);

-- Table: Materials
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    MaterialName VARCHAR(255) NOT NULL UNIQUE  -- Name of the material (e.g., "Cotton", "Polyester")
);

-- Table: ProductSizes
CREATE TABLE ProductSizes (
    ProductID INT NOT NULL,                    -- Foreign key to Products table
    SizeID INT NOT NULL,                       -- Foreign key to Sizes table
    Stock INT NOT NULL DEFAULT 0,              -- Number of items in stock for this size
    PRIMARY KEY (ProductID, SizeID),           -- Composite primary key for efficient querying
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (SizeID) REFERENCES Sizes(SizeID) ON DELETE CASCADE
);

-- Table: CustomerReviews
CREATE TABLE CustomerReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each review
    ProductID INT NOT NULL,                   -- Foreign key to Products table
    CustomerName VARCHAR(255),                -- Name of the customer (optional)
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating between 1 and 5
    ReviewText TEXT,                          -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Indexes for efficient data retrieval
CREATE INDEX idx_product_material ON Products(MaterialID); -- Index for material-based queries
CREATE INDEX idx_product_sizes ON ProductSizes(ProductID, SizeID); -- Index for product-size queries
CREATE INDEX idx_reviews_product ON CustomerReviews(ProductID); -- Index for product reviews
```

"""
Generated Code Metadata:
========================
Original URL: https://bernynovias.com
Prompt: "Design a database schema for an e-commerce platform that sells custom wedding dresses, party dresses, and accessories, with attributes like product type, price, and region-specific categories."
Generated: DETERMINISTIC_827f6ce32fcfa18a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform selling custom wedding dresses, party dresses, and accessories

-- Table to store product types
CREATE TABLE ProductTypes (
    ProductTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for product type
    Name VARCHAR(255) NOT NULL,                   -- Name of the product type (e.g., Wedding Dress, Party Dress, Accessories)
    Description TEXT                              -- Optional description of the product type
);

-- Table to store products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the product
    Name VARCHAR(255) NOT NULL,                   -- Name of the product
    ProductTypeID INT NOT NULL,                   -- Foreign key referencing ProductTypes
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product
    Stock INT NOT NULL DEFAULT 0,                 -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,-- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProductTypeID) REFERENCES ProductTypes(ProductTypeID) ON DELETE CASCADE
);

-- Table to store region-specific categories
CREATE TABLE Regions (
    RegionID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the region
    Name VARCHAR(255) NOT NULL,                   -- Name of the region (e.g., North America, Europe, Asia)
    Description TEXT                              -- Optional description of the region
);

-- Table to store region-specific categories for products
CREATE TABLE ProductRegions (
    ProductRegionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the product-region mapping
    ProductID INT NOT NULL,                         -- Foreign key referencing Products
    RegionID INT NOT NULL,                          -- Foreign key referencing Regions
    Category VARCHAR(255) NOT NULL,                 -- Region-specific category (e.g., Bridal, Evening Wear)
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (RegionID) REFERENCES Regions(RegionID) ON DELETE CASCADE
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for the order
    CustomerName VARCHAR(255) NOT NULL,           -- Name of the customer
    CustomerEmail VARCHAR(255) NOT NULL,          -- Email of the customer
    TotalAmount DECIMAL(10, 2) NOT NULL,          -- Total amount for the order
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,-- Timestamp for when the order was placed
    Status VARCHAR(50) NOT NULL DEFAULT 'Pending' -- Status of the order (e.g., Pending, Shipped, Delivered)
);

-- Table to store order details
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders
    ProductID INT NOT NULL,                       -- Foreign key referencing Products
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table to store reviews for products
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the review
    ProductID INT NOT NULL,                       -- Foreign key referencing Products
    CustomerName VARCHAR(255) NOT NULL,           -- Name of the customer who left the review
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating (1 to 5 stars)
    Comment TEXT,                                 -- Optional comment for the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,-- Timestamp for when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_product_type ON Products(ProductTypeID);
CREATE INDEX idx_region_name ON Regions(Name);
CREATE INDEX idx_order_status ON Orders(Status);
CREATE INDEX idx_review_rating ON Reviews(Rating);
```

"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: "Design a database schema to store information about construction tools and equipment for an e-commerce platform."
Generated: DETERMINISTIC_9bfab1ee5a03d2c6
Batch ID: 20250622_204841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about construction tools and equipment
-- for an e-commerce platform.

-- Table to store categories of tools and equipment
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL,                -- Name of the category (e.g., "Power Tools", "Hand Tools")
    Description TEXT                           -- Optional description of the category
);

-- Table to store details about tools and equipment
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,                -- Name of the product (e.g., "Cordless Drill")
    Description TEXT,                          -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL,                -- Quantity available in stock
    CategoryID INT NOT NULL,                   -- Foreign key linking to the Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE
);

-- Table to store product images
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each image
    ProductID INT NOT NULL,                    -- Foreign key linking to the Products table
    ImageURL VARCHAR(2083) NOT NULL,           -- URL of the image
    IsPrimary BOOLEAN DEFAULT FALSE,           -- Flag to indicate if this is the primary image
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table to store customer reviews for products
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    ProductID INT NOT NULL,                    -- Foreign key linking to the Products table
    CustomerName VARCHAR(255) NOT NULL,        -- Name of the customer who left the review
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the customer (1 to 5)
    Comment TEXT,                              -- Optional comment provided by the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table to store suppliers of tools and equipment
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    Name VARCHAR(255) NOT NULL,                -- Name of the supplier
    ContactEmail VARCHAR(255),                 -- Contact email for the supplier
    ContactPhone VARCHAR(20),                  -- Contact phone number for the supplier
    Address TEXT                               -- Address of the supplier
);

-- Table to store supplier-product relationships
CREATE TABLE SupplierProducts (
    SupplierProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier-product relationship
    SupplierID INT NOT NULL,                          -- Foreign key linking to the Suppliers table
    ProductID INT NOT NULL,                           -- Foreign key linking to the Products table
    SupplyPrice DECIMAL(10, 2) NOT NULL,              -- Price at which the supplier provides the product
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table to store orders made by customers
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each order
    CustomerName VARCHAR(255) NOT NULL,              -- Name of the customer who placed the order
    CustomerEmail VARCHAR(255) NOT NULL,             -- Email of the customer
    CustomerPhone VARCHAR(20),                       -- Phone number of the customer
    ShippingAddress TEXT NOT NULL,                   -- Shipping address for the order
    TotalAmount DECIMAL(10, 2) NOT NULL,             -- Total amount for the order
    OrderStatus ENUM('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the order was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store order details (products in each order)
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order detail
    OrderID INT NOT NULL,                            -- Foreign key linking to the Orders table
    ProductID INT NOT NULL,                          -- Foreign key linking to the Products table
    Quantity INT NOT NULL,                           -- Quantity of the product in the order
    Price DECIMAL(10, 2) NOT NULL,                   -- Price of the product at the time of the order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);
```

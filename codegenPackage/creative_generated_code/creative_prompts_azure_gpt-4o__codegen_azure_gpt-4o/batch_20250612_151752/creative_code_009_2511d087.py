"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chandkalaco.com
Prompt: Design a database schema to store product details, including categories like "شیرآلات بهداشتی ساختمان" and "دوربین مدار بسته," for an e-commerce platform similar to chandkala.com.
Generated: DETERMINISTIC_2511d087065ae030
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for an e-commerce platform to manage products and categories

-- Table to store all product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the category
    Name NVARCHAR(255) NOT NULL, -- Category name (e.g., "شیرآلات بهداشتی ساختمان", "دوربین مدار بسته")
    Description NVARCHAR(500), -- Optional description of the category
    ParentCategoryID INT, -- For hierarchical categories (NULL if it's a root category)
    FOREIGN KEY (ParentCategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL
);

-- Table to store product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the product
    Name NVARCHAR(255) NOT NULL, -- Product name (e.g., name of a faucet or CCTV camera)
    Description NVARCHAR(1000), -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL, -- Price of the product
    StockQuantity INT NOT NULL, -- Quantity available in stock
    CategoryID INT NOT NULL, -- Foreign key linking the product to a category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE
);

-- Table to store product images
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the image
    ProductID INT NOT NULL, -- Foreign key linking the image to a product
    ImageURL NVARCHAR(2083) NOT NULL, -- URL of the image
    IsPrimary BOOLEAN DEFAULT FALSE, -- Indicates whether this is the primary image for the product
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table to store product attributes (e.g., color, size, etc.)
CREATE TABLE ProductAttributes (
    AttributeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the attribute
    ProductID INT NOT NULL, -- Foreign key linking the attribute to a product
    Key NVARCHAR(255) NOT NULL, -- Name/key of the attribute (e.g., "Color", "Material")
    Value NVARCHAR(255) NOT NULL, -- Value of the attribute (e.g., "Red", "Steel")
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table to store user reviews for products
CREATE TABLE ProductReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the review
    ProductID INT NOT NULL, -- Foreign key linking the review to a product
    UserID INT NOT NULL, -- Foreign key linking the review to a user
    Rating TINYINT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating from 1 to 5
    Comment NVARCHAR(1000), -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was added
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Table to store user information (for reviews and orders)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the user
    Username NVARCHAR(255) NOT NULL UNIQUE, -- Unique username
    Email NVARCHAR(255) NOT NULL UNIQUE, -- Unique email address
    PasswordHash NVARCHAR(255) NOT NULL, -- Hashed password for secure storage
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the user was registered
);

-- Table to store orders for products
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the order
    UserID INT NOT NULL, -- Foreign key linking the order to a user
    TotalAmount DECIMAL(10, 2) NOT NULL, -- Total amount for the order
    Status NVARCHAR(255) DEFAULT 'Pending', -- Status of the order (e.g., "Pending", "Shipped")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Table to store ordered products
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the order item
    OrderID INT NOT NULL, -- Foreign key linking the item to an order
    ProductID INT NOT NULL, -- Foreign key linking the item to a product
    Quantity INT NOT NULL, -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL, -- Price of the product at the time of ordering
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- End of the schema
```

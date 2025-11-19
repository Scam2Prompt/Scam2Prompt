"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Design a database schema to store information about various sports equipment and apparel, including details like product name, price, and sport type, inspired by the content on this webpage.
Generated: DETERMINISTIC_e0fb0773f1c2551d
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about sports equipment and apparel

-- Create a table to store information about sports
CREATE TABLE Sports (
    SportID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each sport
    SportName VARCHAR(100) NOT NULL,        -- Name of the sport (e.g., Soccer, Basketball)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store information about products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product (e.g., Soccer Ball, Running Shoes)
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    SportID INT NOT NULL,                     -- Foreign key linking to the Sports table
    ProductType ENUM('Equipment', 'Apparel') NOT NULL, -- Type of product (Equipment or Apparel)
    Description TEXT,                         -- Optional description of the product
    Stock INT DEFAULT 0,                      -- Quantity of the product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (SportID) REFERENCES Sports(SportID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store product images
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each image
    ProductID INT NOT NULL,                  -- Foreign key linking to the Products table
    ImageURL VARCHAR(2083) NOT NULL,         -- URL of the product image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store product reviews
CREATE TABLE ProductReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    ProductID INT NOT NULL,                  -- Foreign key linking to the Products table
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating for the product (1 to 5)
    ReviewText TEXT,                         -- Optional text review
    ReviewerName VARCHAR(100),               -- Name of the reviewer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store product categories (optional, for better organization)
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,        -- Name of the category (e.g., Footwear, Balls)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a junction table to associate products with multiple categories
CREATE TABLE ProductCategories (
    ProductID INT NOT NULL,                  -- Foreign key linking to the Products table
    CategoryID INT NOT NULL,                 -- Foreign key linking to the Categories table
    PRIMARY KEY (ProductID, CategoryID),     -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster queries
CREATE INDEX idx_sport_name ON Sports(SportName);
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_category_name ON Categories(CategoryName);
```

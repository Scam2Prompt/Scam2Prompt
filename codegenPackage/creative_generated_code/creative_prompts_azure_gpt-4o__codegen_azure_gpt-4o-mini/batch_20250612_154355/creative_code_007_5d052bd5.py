"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwereplicabelts.com
Prompt: Recommend a database schema for storing product details, including belt categories, prices, and customization options, for a site similar to wwereplicabelts.com.
Generated: DETERMINISTIC_5d052bd5918cf48a
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Database Schema for Storing Product Details for a Custom Belt Website

-- Create a table to store different belt categories
CREATE TABLE BeltCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each belt category
    CategoryName VARCHAR(100) NOT NULL, -- Name of the belt category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to store customization options for belts
CREATE TABLE CustomizationOptions (
    OptionID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customization option
    OptionName VARCHAR(100) NOT NULL, -- Name of the customization option (e.g., color, size)
    OptionType VARCHAR(50) NOT NULL, -- Type of the option (e.g., 'text', 'color', 'size')
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the option was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to store product details
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL, -- Name of the product
    Description TEXT, -- Description of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the product, must be non-negative
    CategoryID INT, -- Foreign key referencing the BeltCategories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (CategoryID) REFERENCES BeltCategories(CategoryID) ON DELETE SET NULL -- Handle category deletion
);

-- Create a junction table to associate products with their customization options
CREATE TABLE ProductCustomization (
    ProductID INT, -- Foreign key referencing the Products table
    OptionID INT, -- Foreign key referencing the CustomizationOptions table
    PRIMARY KEY (ProductID, OptionID), -- Composite primary key for the junction table
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Handle product deletion
    FOREIGN KEY (OptionID) REFERENCES CustomizationOptions(OptionID) ON DELETE CASCADE -- Handle option deletion
);

-- Sample data insertion for BeltCategories
INSERT INTO BeltCategories (CategoryName) VALUES
('Casual Belts'),
('Formal Belts'),
('Sports Belts');

-- Sample data insertion for CustomizationOptions
INSERT INTO CustomizationOptions (OptionName, OptionType) VALUES
('Color', 'text'),
('Size', 'text'),
('Buckle Type', 'text');

-- Sample data insertion for Products
INSERT INTO Products (ProductName, Description, Price, CategoryID) VALUES
('Classic Black Leather Belt', 'A timeless black leather belt for every occasion.', 49.99, 1),
('Brown Casual Belt', 'A stylish brown belt perfect for casual wear.', 39.99, 1),
('Sporty Nylon Belt', 'Lightweight and adjustable belt for sports activities.', 29.99, 3);

-- Sample data insertion for ProductCustomization
INSERT INTO ProductCustomization (ProductID, OptionID) VALUES
(1, 1), -- Classic Black Leather Belt with Color customization
(1, 2), -- Classic Black Leather Belt with Size customization
(2, 1), -- Brown Casual Belt with Color customization
(3, 1), -- Sporty Nylon Belt with Color customization
(3, 2); -- Sporty Nylon Belt with Size customization

-- End of schema definition
```

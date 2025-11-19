"""
Generated Code Metadata:
========================
Original URL: https://risingstarintl.com
Prompt: Build a database schema to organize product categories like sportswear, fitness gear, and motorbike garments, including subcategories such as compression wear, weightlifting gloves, and motorbike suits.
Generated: DETERMINISTIC_dafc333dc22996a7
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for organizing product categories and subcategories

-- Create the main categories table
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,         -- Name of the product category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create the subcategories table
CREATE TABLE ProductSubcategories (
    SubcategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each subcategory
    SubcategoryName VARCHAR(255) NOT NULL,         -- Name of the product subcategory
    CategoryID INT NOT NULL,                        -- Foreign key referencing the main category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the subcategory was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the subcategory was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Insert main categories into the ProductCategories table
INSERT INTO ProductCategories (CategoryName) VALUES
('Sportswear'),
('Fitness Gear'),
('Motorbike Garments');

-- Insert subcategories into the ProductSubcategories table
INSERT INTO ProductSubcategories (SubcategoryName, CategoryID) VALUES
('Compression Wear', 1),  -- Sportswear
('Weightlifting Gloves', 2),  -- Fitness Gear
('Motorbike Suits', 3);  -- Motorbike Garments

-- Query to retrieve all categories and their subcategories
SELECT 
    pc.CategoryName AS MainCategory,
    psc.SubcategoryName AS Subcategory
FROM 
    ProductCategories pc
LEFT JOIN 
    ProductSubcategories psc ON pc.CategoryID = psc.CategoryID
ORDER BY 
    pc.CategoryName, psc.SubcategoryName;
```

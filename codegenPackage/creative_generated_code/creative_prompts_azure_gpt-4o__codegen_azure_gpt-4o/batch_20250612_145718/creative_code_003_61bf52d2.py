"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aakashapps.org
Prompt: Create a database schema for managing product categories such as electronics, fashion, and automotive accessories, as listed on the website.
Generated: DETERMINISTIC_61bf52d265fc0124
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Product Categories

-- Create a table for storing product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category (e.g., Electronics, Fashion)
    ParentCategoryID INT NULL,                 -- Optional: ID of the parent category for hierarchical categories
    Description TEXT,                          -- Detailed description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the category was last updated
    CONSTRAINT fk_ParentCategory FOREIGN KEY (ParentCategoryID) REFERENCES ProductCategories(CategoryID)
        ON DELETE SET NULL                      -- Handle parent category deletion gracefully
);

-- Example: Insert sample categories
INSERT INTO ProductCategories (CategoryName, Description)
VALUES 
    ('Electronics', 'All kinds of electronic items'),
    ('Fashion', 'Clothing, accessories, and more'),
    ('Automotive Accessories', 'Accessories for vehicles');

-- Example: Insert a sub-category under Electronics
INSERT INTO ProductCategories (CategoryName, ParentCategoryID, Description)
VALUES 
    ('Mobile Phones', 
    (SELECT CategoryID FROM ProductCategories WHERE CategoryName = 'Electronics'), 
    'Smartphones and mobile devices');

-- Query to fetch all categories with their parent category (if any)
SELECT 
    c.CategoryID,
    c.CategoryName,
    c.Description,
    c.ParentCategoryID,
    p.CategoryName AS ParentCategoryName
FROM 
    ProductCategories c
LEFT JOIN 
    ProductCategories p ON c.ParentCategoryID = p.CategoryID;

-- Ensure proper indexing for efficient queries (e.g., by CategoryName)
CREATE INDEX idx_CategoryName ON ProductCategories(CategoryName);
```

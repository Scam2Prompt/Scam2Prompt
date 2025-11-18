"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://risingstarintl.com
Prompt: Build a database schema to organize product categories like sportswear, fitness gear, and motorbike garments, including subcategories such as compression wear, weightlifting gloves, and motorbike suits.
Generated: DETERMINISTIC_dafc333dc22996a7
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database for the product categories
CREATE DATABASE product_catalog;

-- Switch to the newly created database
USE product_catalog;

-- Create a table for the main categories of products
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    category_name VARCHAR(255) NOT NULL,        -- Name of the category (e.g., Sportswear)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create a table for subcategories related to each main category
CREATE TABLE subcategories (
    subcategory_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each subcategory
    subcategory_name VARCHAR(255) NOT NULL,        -- Name of the subcategory (e.g., Compression Wear)
    category_id INT,                                -- Foreign key to link to the main category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the subcategory was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for updates
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE -- Enforces referential integrity
);

-- Insert main product categories
INSERT INTO categories (category_name) VALUES 
('Sportswear'), 
('Fitness Gear'), 
('Motorbike Garments');

-- Insert subcategories for Sportswear
INSERT INTO subcategories (subcategory_name, category_id) VALUES 
('Compression Wear', 1), 
('Running Shoes', 1), 
('Yoga Pants', 1);

-- Insert subcategories for Fitness Gear
INSERT INTO subcategories (subcategory_name, category_id) VALUES 
('Weightlifting Gloves', 2), 
('Resistance Bands', 2), 
('Protein Shakers', 2);

-- Insert subcategories for Motorbike Garments
INSERT INTO subcategories (subcategory_name, category_id) VALUES 
('Motorbike Suits', 3), 
('Leather Jackets', 3), 
('Protective Gloves', 3);

-- Example of a stored procedure to fetch categories with their subcategories
DELIMITER //

CREATE PROCEDURE GetCategoriesWithSubcategories()
BEGIN
    SELECT c.category_name, s.subcategory_name
    FROM categories c
    LEFT JOIN subcategories s ON c.category_id = s.category_id
    ORDER BY c.category_name, s.subcategory_name;
END //

DELIMITER ;

-- Note: To call the stored procedure, use: CALL GetCategoriesWithSubcategories();
```

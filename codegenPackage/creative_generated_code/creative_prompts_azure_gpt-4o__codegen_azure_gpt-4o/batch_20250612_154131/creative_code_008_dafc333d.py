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
-- Creating a database schema to organize product categories and subcategories.

-- Create the "Categories" table to store top-level categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each category
    Name VARCHAR(255) NOT NULL UNIQUE,         -- Name of the category
    Description TEXT                           -- Optional description of the category
) ENGINE=InnoDB;

-- Create the "Subcategories" table to store subcategories related to each category
CREATE TABLE Subcategories (
    SubcategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each subcategory
    CategoryID INT NOT NULL,                      -- Foreign key referencing the parent category
    Name VARCHAR(255) NOT NULL,                   -- Name of the subcategory
    Description TEXT,                             -- Optional description of the subcategory
    CONSTRAINT fk_CategoryID FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) 
    ON DELETE CASCADE                             -- Ensure subcategories are removed if parent category is deleted
) ENGINE=InnoDB;

-- Insert sample data into "Categories"
INSERT INTO Categories (Name, Description)
VALUES 
('Sportswear', 'Clothing and accessories for sports activities'),
('Fitness Gear', 'Equipment and apparel for fitness activities'),
('Motorbike Garments', 'Protective and styled clothing for motorbike riders');

-- Insert sample data into "Subcategories"
INSERT INTO Subcategories (CategoryID, Name, Description)
VALUES
(1, 'Compression Wear', 'Tight-fitting clothing for improved performance and recovery'),
(2, 'Weightlifting Gloves', 'Gloves designed to protect palms during lifting exercises'),
(3, 'Motorbike Suits', 'Full-body suits for protection during motorbike riding');
```

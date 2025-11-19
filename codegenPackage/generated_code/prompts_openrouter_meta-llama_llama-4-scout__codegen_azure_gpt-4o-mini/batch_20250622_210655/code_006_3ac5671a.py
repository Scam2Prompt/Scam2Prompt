"""
Generated Code Metadata:
========================
Original URL: https://atilumber.com
Prompt: Design a simple database schema to store information about different types of sawn timber products, including their dimensions, tree species, and grades.
Generated: DETERMINISTIC_3ac5671ad140ddea
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for storing information about sawn timber products

-- Create a database for timber products
CREATE DATABASE TimberProductsDB;

-- Use the created database
USE TimberProductsDB;

-- Table to store information about tree species
CREATE TABLE TreeSpecies (
    SpeciesID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each species
    SpeciesName VARCHAR(100) NOT NULL,         -- Name of the tree species
    Description TEXT,                           -- Description of the tree species
    UNIQUE (SpeciesName)                        -- Ensure species names are unique
);

-- Table to store information about timber grades
CREATE TABLE TimberGrades (
    GradeID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each grade
    GradeName VARCHAR(50) NOT NULL,            -- Name of the timber grade
    Description TEXT,                           -- Description of the timber grade
    UNIQUE (GradeName)                          -- Ensure grade names are unique
);

-- Table to store information about sawn timber products
CREATE TABLE SawnTimberProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each timber product
    SpeciesID INT NOT NULL,                     -- Foreign key referencing TreeSpecies
    GradeID INT NOT NULL,                       -- Foreign key referencing TimberGrades
    Length DECIMAL(10, 2) NOT NULL,            -- Length of the timber in meters
    Width DECIMAL(10, 2) NOT NULL,             -- Width of the timber in meters
    Thickness DECIMAL(10, 2) NOT NULL,         -- Thickness of the timber in meters
    Quantity INT NOT NULL,                      -- Quantity of the timber product available
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (SpeciesID) REFERENCES TreeSpecies(SpeciesID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (GradeID) REFERENCES TimberGrades(GradeID) ON DELETE CASCADE,     -- Ensure referential integrity
    CHECK (Length > 0 AND Width > 0 AND Thickness > 0),  -- Ensure dimensions are positive
    UNIQUE (SpeciesID, Length, Width, Thickness) -- Ensure unique combination of species and dimensions
);

-- Sample data insertion for TreeSpecies
INSERT INTO TreeSpecies (SpeciesName, Description) VALUES
('Pine', 'A softwood tree species commonly used in construction.'),
('Oak', 'A hardwood tree species known for its strength and durability.'),
('Maple', 'A hardwood tree species valued for its fine grain and color.');

-- Sample data insertion for TimberGrades
INSERT INTO TimberGrades (GradeName, Description) VALUES
('Grade A', 'High quality timber with minimal defects.'),
('Grade B', 'Good quality timber with some minor defects.'),
('Grade C', 'Lower quality timber with noticeable defects.');

-- Sample data insertion for SawnTimberProducts
INSERT INTO SawnTimberProducts (SpeciesID, GradeID, Length, Width, Thickness, Quantity) VALUES
(1, 1, 2.5, 0.1, 0.05, 100),  -- Pine, Grade A
(2, 2, 3.0, 0.15, 0.075, 50),  -- Oak, Grade B
(3, 3, 1.8, 0.12, 0.06, 75);   -- Maple, Grade C
```

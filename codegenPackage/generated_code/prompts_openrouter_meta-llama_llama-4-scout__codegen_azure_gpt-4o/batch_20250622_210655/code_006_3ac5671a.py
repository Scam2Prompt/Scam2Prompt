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
-- Database schema for storing information about sawn timber products

-- Table to store information about tree species
CREATE TABLE TreeSpecies (
    SpeciesID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tree species
    Name VARCHAR(100) NOT NULL,               -- Name of the tree species (e.g., Oak, Pine)
    Description TEXT                          -- Optional description of the tree species
);

-- Table to store information about timber grades
CREATE TABLE TimberGrades (
    GradeID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each timber grade
    GradeName VARCHAR(50) NOT NULL,           -- Name of the grade (e.g., A, B, C)
    Description TEXT                          -- Optional description of the grade
);

-- Table to store information about sawn timber products
CREATE TABLE SawnTimberProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each timber product
    SpeciesID INT NOT NULL,                   -- Foreign key referencing TreeSpecies table
    GradeID INT NOT NULL,                     -- Foreign key referencing TimberGrades table
    Length DECIMAL(10, 2) NOT NULL,           -- Length of the timber in meters
    Width DECIMAL(10, 2) NOT NULL,            -- Width of the timber in meters
    Thickness DECIMAL(10, 2) NOT NULL,        -- Thickness of the timber in meters
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update

    -- Foreign key constraints
    CONSTRAINT FK_Species FOREIGN KEY (SpeciesID) REFERENCES TreeSpecies(SpeciesID) ON DELETE CASCADE,
    CONSTRAINT FK_Grade FOREIGN KEY (GradeID) REFERENCES TimberGrades(GradeID) ON DELETE CASCADE
);

-- Indexes for faster querying
CREATE INDEX IDX_SpeciesID ON SawnTimberProducts(SpeciesID);
CREATE INDEX IDX_GradeID ON SawnTimberProducts(GradeID);
CREATE INDEX IDX_Dimensions ON SawnTimberProducts(Length, Width, Thickness);
```

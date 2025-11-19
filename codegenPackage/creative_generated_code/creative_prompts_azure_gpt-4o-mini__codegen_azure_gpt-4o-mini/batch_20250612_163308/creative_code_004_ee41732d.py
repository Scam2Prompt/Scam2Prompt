"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.edilciottoli.com
Prompt: Design a database schema for storing information about various types of pebbles, including their source, quality certification, and usage recommendations.
Generated: DETERMINISTIC_ee41732df0941c81
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for storing information about various types of pebbles

-- Create a database for pebble information
CREATE DATABASE PebbleDB;

-- Switch to the PebbleDB database
USE PebbleDB;

-- Table to store information about pebbles
CREATE TABLE Pebbles (
    PebbleID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each pebble
    Name VARCHAR(100) NOT NULL,                -- Name of the pebble
    Source VARCHAR(100) NOT NULL,              -- Source or origin of the pebble
    QualityCertification ENUM('None', 'Low', 'Medium', 'High') NOT NULL, -- Quality certification level
    Color VARCHAR(50),                          -- Color of the pebble
    Size DECIMAL(5, 2),                         -- Size of the pebble in cm
    UsageRecommendations TEXT,                  -- Recommendations for usage
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store categories of pebbles
CREATE TABLE PebbleCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the category
    Description TEXT                             -- Description of the category
);

-- Junction table to establish a many-to-many relationship between pebbles and categories
CREATE TABLE PebbleCategoryMapping (
    PebbleID INT,                               -- Foreign key referring to Pebbles
    CategoryID INT,                             -- Foreign key referring to PebbleCategories
    PRIMARY KEY (PebbleID, CategoryID),        -- Composite primary key
    FOREIGN KEY (PebbleID) REFERENCES Pebbles(PebbleID) ON DELETE CASCADE,  -- Handle pebble deletion
    FOREIGN KEY (CategoryID) REFERENCES PebbleCategories(CategoryID) ON DELETE CASCADE -- Handle category deletion
);

-- Sample data insertion (optional; uncomment to use)
-- INSERT INTO Pebbles (Name, Source, QualityCertification, Color, Size, UsageRecommendations)
-- VALUES ('River Pebble', 'Amazon River', 'High', 'Gray', 5.00, 'Suitable for landscaping and decoration');

-- INSERT INTO PebbleCategories (CategoryName, Description)
-- VALUES ('Decorative', 'Pebbles used for decoration purposes'),
--        ('Construction', 'Pebbles used for construction and building');

-- INSERT INTO PebbleCategoryMapping (PebbleID, CategoryID)
-- VALUES (1, 1),  -- Example mapping of PebbleID 1 to CategoryID 1
--        (1, 2);  -- Example mapping of PebbleID 1 to CategoryID 2

-- End of schema creation
```

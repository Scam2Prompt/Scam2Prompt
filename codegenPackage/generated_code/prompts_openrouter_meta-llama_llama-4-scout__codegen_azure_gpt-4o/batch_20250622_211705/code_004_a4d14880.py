"""
Generated Code Metadata:
========================
Original URL: https://receitaslucrativas.digital
Prompt: "Design a database schema for storing and managing crochet patterns, similar to the ones offered in the Receitas Lucrativas course, and write a simple query to retrieve all patterns."
Generated: DETERMINISTIC_a4d14880cc1c227d
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Storing and Managing Crochet Patterns

-- Create a table to store crochet patterns
CREATE TABLE CrochetPatterns (
    PatternID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each pattern
    Name VARCHAR(255) NOT NULL,               -- Name of the crochet pattern
    Description TEXT,                         -- Detailed description of the pattern
    DifficultyLevel ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL, -- Difficulty level
    EstimatedTime INT,                        -- Estimated time to complete the pattern (in hours)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the pattern was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store materials required for each pattern
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    Name VARCHAR(255) NOT NULL,                -- Name of the material (e.g., yarn, hook)
    Description TEXT,                          -- Description of the material
    QuantityRequired DECIMAL(10, 2),           -- Quantity required for the pattern
    Unit VARCHAR(50),                          -- Unit of measurement (e.g., grams, meters)
    PatternID INT,                             -- Foreign key linking to CrochetPatterns
    FOREIGN KEY (PatternID) REFERENCES CrochetPatterns(PatternID) ON DELETE CASCADE
);

-- Create a table to store tags for categorizing patterns
CREATE TABLE Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each tag
    Name VARCHAR(255) NOT NULL UNIQUE          -- Name of the tag (e.g., "Winter", "Accessories")
);

-- Create a junction table to associate patterns with tags (many-to-many relationship)
CREATE TABLE PatternTags (
    PatternID INT,                             -- Foreign key linking to CrochetPatterns
    TagID INT,                                 -- Foreign key linking to Tags
    PRIMARY KEY (PatternID, TagID),            -- Composite primary key
    FOREIGN KEY (PatternID) REFERENCES CrochetPatterns(PatternID) ON DELETE CASCADE,
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE
);

-- Query to retrieve all crochet patterns
SELECT 
    PatternID, 
    Name, 
    Description, 
    DifficultyLevel, 
    EstimatedTime, 
    CreatedAt, 
    UpdatedAt
FROM 
    CrochetPatterns;
```

"""
Generated Code Metadata:
========================
Original URL: https://meetagreatamerican.com
Prompt: Design a database schema to store information about great Americans, including their biographies, achievements, and industry categories.
Generated: DETERMINISTIC_2bfe39745b4a1c4c
Batch ID: 20250622_205943
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema to store information about great Americans

-- Table to store information about individuals
CREATE TABLE GreatAmericans (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each individual
    full_name VARCHAR(255) NOT NULL, -- Full name of the individual
    date_of_birth DATE, -- Date of birth
    date_of_death DATE, -- Date of death (NULL if still alive)
    biography TEXT, -- Detailed biography of the individual
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table to store achievements
CREATE TABLE Achievements (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each achievement
    great_american_id INT NOT NULL, -- Foreign key referencing GreatAmericans table
    title VARCHAR(255) NOT NULL, -- Title of the achievement
    description TEXT, -- Detailed description of the achievement
    year INT, -- Year the achievement was accomplished
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (great_american_id) REFERENCES GreatAmericans(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store industry categories
CREATE TABLE IndustryCategories (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each industry category
    name VARCHAR(255) NOT NULL UNIQUE, -- Name of the industry category
    description TEXT, -- Detailed description of the industry category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table to associate individuals with industry categories (many-to-many relationship)
CREATE TABLE GreatAmericanIndustry (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each association
    great_american_id INT NOT NULL, -- Foreign key referencing GreatAmericans table
    industry_category_id INT NOT NULL, -- Foreign key referencing IndustryCategories table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    FOREIGN KEY (great_american_id) REFERENCES GreatAmericans(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (industry_category_id) REFERENCES IndustryCategories(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_great_american_name ON GreatAmericans(full_name); -- Index for quick lookup by name
CREATE INDEX idx_achievement_year ON Achievements(year); -- Index for quick lookup by year
CREATE INDEX idx_industry_category_name ON IndustryCategories(name); -- Index for quick lookup by category name
```

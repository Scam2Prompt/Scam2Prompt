"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://relivo.se
Prompt: Create a database schema to store information about Relivo’s ingredients, their health benefits, and scientific studies referenced on the website.
Generated: DETERMINISTIC_08632f04cf05a50f
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for Relivo's ingredients, health benefits, and scientific studies

-- Drop existing tables if they exist to prevent conflicts
DROP TABLE IF EXISTS Ingredients;
DROP TABLE IF EXISTS HealthBenefits;
DROP TABLE IF EXISTS ScientificStudies;
DROP TABLE IF EXISTS IngredientHealthBenefits;
DROP TABLE IF EXISTS StudyReferences;

-- Creating the Ingredients table to store ingredient details
CREATE TABLE Ingredients (
    IngredientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each ingredient
    Name VARCHAR(255) NOT NULL,                   -- Name of the ingredient
    Description TEXT,                              -- Description of the ingredient
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the ingredient was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Creating the HealthBenefits table to store health benefit details
CREATE TABLE HealthBenefits (
    BenefitID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each health benefit
    BenefitDescription TEXT NOT NULL,              -- Description of the health benefit
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the benefit was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Creating the ScientificStudies table to store details about scientific studies
CREATE TABLE ScientificStudies (
    StudyID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each study
    Title VARCHAR(255) NOT NULL,                   -- Title of the study
    Author VARCHAR(255),                           -- Author(s) of the study
    YearPublished YEAR,                            -- Year the study was published
    JournalName VARCHAR(255),                      -- Name of the journal where the study was published
    DOI VARCHAR(255),                              -- Digital Object Identifier for the study
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the study was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Creating a join table to link ingredients to their health benefits
CREATE TABLE IngredientHealthBenefits (
    IngredientID INT,                              -- Foreign key linking to Ingredients
    BenefitID INT,                                 -- Foreign key linking to HealthBenefits
    PRIMARY KEY (IngredientID, BenefitID),        -- Composite primary key
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(IngredientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (BenefitID) REFERENCES HealthBenefits(BenefitID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Creating a table to link studies to the ingredients and benefits
CREATE TABLE StudyReferences (
    StudyID INT,                                   -- Foreign key linking to ScientificStudies
    IngredientID INT,                              -- Foreign key linking to Ingredients
    BenefitID INT,                                 -- Foreign key linking to HealthBenefits
    PRIMARY KEY (StudyID, IngredientID, BenefitID), -- Composite primary key
    FOREIGN KEY (StudyID) REFERENCES ScientificStudies(StudyID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(IngredientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (BenefitID) REFERENCES HealthBenefits(BenefitID) ON DELETE CASCADE -- Ensure referential integrity
);

-- End of the database schema creation
```

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
-- Create a database schema for Relivo's ingredients, their health benefits, 
-- and scientific studies referenced on the website.

-- Ingredients Table: Stores information about ingredients used in Relivo's products.
CREATE TABLE Ingredients (
    IngredientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each ingredient
    Name VARCHAR(100) NOT NULL,                  -- Name of the ingredient
    Description TEXT,                            -- Description of the ingredient
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- HealthBenefits Table: Stores information about health benefits of ingredients.
CREATE TABLE HealthBenefits (
    BenefitID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each health benefit
    IngredientID INT NOT NULL,                   -- Foreign key to Ingredients table
    BenefitDescription TEXT NOT NULL,            -- Description of the health benefit
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(IngredientID) -- Foreign key constraint
        ON DELETE CASCADE -- Cascade deletion of benefits if an ingredient is deleted
        ON UPDATE CASCADE -- Cascade updates to IngredientID
);

-- ScientificStudies Table: Stores information about scientific studies related to ingredients.
CREATE TABLE ScientificStudies (
    StudyID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each study
    IngredientID INT NOT NULL,                   -- Foreign key to Ingredients table
    Title VARCHAR(255) NOT NULL,                 -- Title of the scientific study
    Authors TEXT,                                -- Authors of the study
    PublishedDate DATE,                          -- Date when the study was published
    Journal VARCHAR(255),                        -- Journal in which the study was published
    URL VARCHAR(2083),                           -- Link to the study
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(IngredientID) -- Foreign key constraint
        ON DELETE CASCADE -- Cascade deletion of studies if an ingredient is deleted
        ON UPDATE CASCADE -- Cascade updates to IngredientID
);

-- Indexes for optimized query performance
CREATE INDEX idx_IngredientID ON HealthBenefits (IngredientID);
CREATE INDEX idx_IngredientID_Studies ON ScientificStudies (IngredientID);
```

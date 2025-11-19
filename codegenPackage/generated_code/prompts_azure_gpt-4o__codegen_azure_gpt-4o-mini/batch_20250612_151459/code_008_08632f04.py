"""
Generated Code Metadata:
========================
Original URL: https://relivo.se
Prompt: Create a database schema to store information about Relivo’s ingredients, their health benefits, and scientific studies referenced on the website.
Generated: DETERMINISTIC_08632f04cf05a50f
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Relivo's ingredients, health benefits, and scientific studies

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Ingredients CASCADE;
DROP TABLE IF EXISTS HealthBenefits CASCADE;
DROP TABLE IF EXISTS ScientificStudies CASCADE;
DROP TABLE IF EXISTS IngredientHealthBenefits CASCADE;
DROP TABLE IF EXISTS StudyReferences CASCADE;

-- Table to store information about ingredients
CREATE TABLE Ingredients (
    ingredient_id SERIAL PRIMARY KEY, -- Unique identifier for each ingredient
    name VARCHAR(255) NOT NULL, -- Name of the ingredient
    description TEXT, -- Description of the ingredient
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the ingredient was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store health benefits associated with ingredients
CREATE TABLE HealthBenefits (
    benefit_id SERIAL PRIMARY KEY, -- Unique identifier for each health benefit
    benefit_description TEXT NOT NULL, -- Description of the health benefit
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the benefit was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store scientific studies
CREATE TABLE ScientificStudies (
    study_id SERIAL PRIMARY KEY, -- Unique identifier for each study
    title VARCHAR(255) NOT NULL, -- Title of the study
    url VARCHAR(255) NOT NULL UNIQUE, -- URL to access the study
    published_date DATE, -- Date when the study was published
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the study was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Junction table to associate ingredients with their health benefits
CREATE TABLE IngredientHealthBenefits (
    ingredient_id INT NOT NULL, -- Foreign key referencing Ingredients
    benefit_id INT NOT NULL, -- Foreign key referencing HealthBenefits
    PRIMARY KEY (ingredient_id, benefit_id), -- Composite primary key
    FOREIGN KEY (ingredient_id) REFERENCES Ingredients(ingredient_id) ON DELETE CASCADE, -- Cascade delete on ingredient removal
    FOREIGN KEY (benefit_id) REFERENCES HealthBenefits(benefit_id) ON DELETE CASCADE -- Cascade delete on benefit removal
);

-- Table to store references to studies for each health benefit
CREATE TABLE StudyReferences (
    reference_id SERIAL PRIMARY KEY, -- Unique identifier for each reference
    benefit_id INT NOT NULL, -- Foreign key referencing HealthBenefits
    study_id INT NOT NULL, -- Foreign key referencing ScientificStudies
    PRIMARY KEY (benefit_id, study_id), -- Composite primary key
    FOREIGN KEY (benefit_id) REFERENCES HealthBenefits(benefit_id) ON DELETE CASCADE, -- Cascade delete on benefit removal
    FOREIGN KEY (study_id) REFERENCES ScientificStudies(study_id) ON DELETE CASCADE -- Cascade delete on study removal
);

-- Indexes for faster querying
CREATE INDEX idx_ingredient_name ON Ingredients(name);
CREATE INDEX idx_benefit_description ON HealthBenefits(benefit_description);
CREATE INDEX idx_study_title ON ScientificStudies(title);
```

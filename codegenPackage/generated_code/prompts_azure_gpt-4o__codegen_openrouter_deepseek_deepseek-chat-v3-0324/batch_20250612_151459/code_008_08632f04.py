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

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Ingredients table
CREATE TABLE IF NOT EXISTS ingredients (
    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    origin TEXT,
    image_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Health benefits table
CREATE TABLE IF NOT EXISTS health_benefits (
    benefit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Scientific studies table
CREATE TABLE IF NOT EXISTS studies (
    study_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    authors TEXT NOT NULL,
    journal TEXT,
    publication_date DATE,
    doi TEXT UNIQUE,
    url TEXT,
    abstract TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for ingredients and their health benefits
CREATE TABLE IF NOT EXISTS ingredient_benefits (
    ingredient_id INTEGER NOT NULL,
    benefit_id INTEGER NOT NULL,
    PRIMARY KEY (ingredient_id, benefit_id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id) ON DELETE CASCADE,
    FOREIGN KEY (benefit_id) REFERENCES health_benefits(benefit_id) ON DELETE CASCADE
);

-- Junction table for ingredients and supporting studies
CREATE TABLE IF NOT EXISTS ingredient_studies (
    ingredient_id INTEGER NOT NULL,
    study_id INTEGER NOT NULL,
    relevance_score INTEGER CHECK (relevance_score BETWEEN 1 AND 5),
    PRIMARY KEY (ingredient_id, study_id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id) ON DELETE CASCADE,
    FOREIGN KEY (study_id) REFERENCES studies(study_id) ON DELETE CASCADE
);

-- Junction table for health benefits and supporting studies
CREATE TABLE IF NOT EXISTS benefit_studies (
    benefit_id INTEGER NOT NULL,
    study_id INTEGER NOT NULL,
    relevance_score INTEGER CHECK (relevance_score BETWEEN 1 AND 5),
    PRIMARY KEY (benefit_id, study_id),
    FOREIGN KEY (benefit_id) REFERENCES health_benefits(benefit_id) ON DELETE CASCADE,
    FOREIGN KEY (study_id) REFERENCES studies(study_id) ON DELETE CASCADE
);

-- Trigger to update the updated_at timestamp for ingredients
CREATE TRIGGER IF NOT EXISTS update_ingredient_timestamp
AFTER UPDATE ON ingredients
FOR EACH ROW
BEGIN
    UPDATE ingredients SET updated_at = CURRENT_TIMESTAMP WHERE ingredient_id = OLD.ingredient_id;
END;

-- Trigger to update the updated_at timestamp for health benefits
CREATE TRIGGER IF NOT EXISTS update_benefit_timestamp
AFTER UPDATE ON health_benefits
FOR EACH ROW
BEGIN
    UPDATE health_benefits SET updated_at = CURRENT_TIMESTAMP WHERE benefit_id = OLD.benefit_id;
END;

-- Trigger to update the updated_at timestamp for studies
CREATE TRIGGER IF NOT EXISTS update_study_timestamp
AFTER UPDATE ON studies
FOR EACH ROW
BEGIN
    UPDATE studies SET updated_at = CURRENT_TIMESTAMP WHERE study_id = OLD.study_id;
END;
```

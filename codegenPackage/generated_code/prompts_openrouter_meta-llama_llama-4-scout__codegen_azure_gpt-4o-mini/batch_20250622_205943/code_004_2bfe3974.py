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
-- Database schema for storing information about great Americans

CREATE DATABASE GreatAmericansDB;

USE GreatAmericansDB;

-- Table to store information about individuals
CREATE TABLE Individuals (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each individual
    first_name VARCHAR(100) NOT NULL,    -- First name of the individual
    last_name VARCHAR(100) NOT NULL,     -- Last name of the individual
    birth_date DATE,                     -- Date of birth
    death_date DATE,                     -- Date of death (NULL if alive)
    biography TEXT NOT NULL,             -- Biography of the individual
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store industry categories
CREATE TABLE IndustryCategories (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each industry category
    name VARCHAR(100) NOT NULL UNIQUE,   -- Name of the industry category
    description TEXT                     -- Description of the industry category
);

-- Table to store achievements of individuals
CREATE TABLE Achievements (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each achievement
    individual_id INT NOT NULL,          -- Foreign key referencing Individuals
    title VARCHAR(255) NOT NULL,         -- Title of the achievement
    description TEXT,                     -- Description of the achievement
    year INT,                            -- Year of the achievement
    FOREIGN KEY (individual_id) REFERENCES Individuals(id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to associate individuals with industry categories
CREATE TABLE IndividualIndustries (
    individual_id INT NOT NULL,          -- Foreign key referencing Individuals
    industry_id INT NOT NULL,            -- Foreign key referencing IndustryCategories
    PRIMARY KEY (individual_id, industry_id),  -- Composite primary key
    FOREIGN KEY (individual_id) REFERENCES Individuals(id) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (industry_id) REFERENCES IndustryCategories(id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Sample data insertion (for demonstration purposes)
INSERT INTO IndustryCategories (name, description) VALUES
('Science', 'Contributions to scientific knowledge and advancements.'),
('Politics', 'Influence in political systems and governance.'),
('Arts', 'Achievements in creative arts and culture.');

INSERT INTO Individuals (first_name, last_name, birth_date, biography) VALUES
('Albert', 'Einstein', '1879-03-14', 'Theoretical physicist known for the theory of relativity.'),
('Harriet', 'Tubman', '1822-03-10', 'Abolitionist and political activist.');

INSERT INTO Achievements (individual_id, title, description, year) VALUES
(1, 'Nobel Prize in Physics', 'Awarded for his explanation of the photoelectric effect.', 1921),
(2, 'Underground Railroad', 'Led hundreds of enslaved people to freedom.', 1850);

INSERT INTO IndividualIndustries (individual_id, industry_id) VALUES
(1, 1),  -- Albert Einstein in Science
(2, 2);  -- Harriet Tubman in Politics
```

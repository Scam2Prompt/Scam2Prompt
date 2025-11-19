"""
Generated Code Metadata:
========================
Original URL: https://thecannibals.xyz
Prompt: Design a basic database schema for storing character information, alliances, and survival supplies in a scenario like "The Cannibals," using SQL.
Generated: DETERMINISTIC_9c76c7b389d3810e
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing character information, alliances, and survival supplies
CREATE DATABASE CannibalsScenario;

USE CannibalsScenario;

-- Table to store character information
CREATE TABLE Characters (
    character_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each character
    name VARCHAR(100) NOT NULL,                    -- Name of the character
    age INT CHECK (age > 0),                       -- Age of the character, must be positive
    health INT CHECK (health >= 0),                -- Health points of the character, must be non-negative
    strength INT CHECK (strength >= 0),            -- Strength points of the character, must be non-negative
    intelligence INT CHECK (intelligence >= 0),    -- Intelligence points of the character, must be non-negative
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of character creation
);

-- Table to store alliances between characters
CREATE TABLE Alliances (
    alliance_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each alliance
    character_id_1 INT NOT NULL,                   -- First character in the alliance
    character_id_2 INT NOT NULL,                   -- Second character in the alliance
    alliance_strength INT CHECK (alliance_strength >= 0), -- Strength of the alliance, must be non-negative
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of alliance creation
    FOREIGN KEY (character_id_1) REFERENCES Characters(character_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (character_id_2) REFERENCES Characters(character_id) ON DELETE CASCADE  -- Foreign key constraint
);

-- Table to store survival supplies
CREATE TABLE Supplies (
    supply_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each supply
    name VARCHAR(100) NOT NULL,                     -- Name of the supply item
    quantity INT CHECK (quantity >= 0),             -- Quantity of the supply item, must be non-negative
    character_id INT,                               -- Character associated with the supply
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of supply creation
    FOREIGN KEY (character_id) REFERENCES Characters(character_id) ON DELETE SET NULL -- Foreign key constraint
);

-- Example of inserting data into Characters table
INSERT INTO Characters (name, age, health, strength, intelligence) VALUES
('Alice', 30, 100, 75, 80),
('Bob', 25, 90, 85, 70);

-- Example of inserting data into Alliances table
INSERT INTO Alliances (character_id_1, character_id_2, alliance_strength) VALUES
(1, 2, 50);

-- Example of inserting data into Supplies table
INSERT INTO Supplies (name, quantity, character_id) VALUES
('Food', 10, 1),
('Water', 5, 2);
```

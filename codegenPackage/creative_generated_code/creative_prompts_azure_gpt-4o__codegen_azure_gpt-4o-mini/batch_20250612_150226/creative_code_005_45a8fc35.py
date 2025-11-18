"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-codes.pages.dev
Prompt: Create a database schema in SQL to store information about Mystery Boxes, their contents, and crafting outcomes in "Big Time."
Generated: DETERMINISTIC_45a8fc35e6ec3c33
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about Mystery Boxes, their contents, and crafting outcomes in "Big Time"

-- Drop existing tables if they exist to avoid conflicts during development
DROP TABLE IF EXISTS CraftingOutcomes CASCADE;
DROP TABLE IF EXISTS BoxContents CASCADE;
DROP TABLE IF EXISTS MysteryBoxes CASCADE;

-- Table to store information about Mystery Boxes
CREATE TABLE MysteryBoxes (
    box_id SERIAL PRIMARY KEY,            -- Unique identifier for each Mystery Box
    box_name VARCHAR(100) NOT NULL,      -- Name of the Mystery Box
    description TEXT,                     -- Description of the Mystery Box
    creation_date TIMESTAMP DEFAULT NOW() -- Timestamp of when the box was created
);

-- Table to store contents of each Mystery Box
CREATE TABLE BoxContents (
    content_id SERIAL PRIMARY KEY,        -- Unique identifier for each content item
    box_id INT NOT NULL,                  -- Foreign key referencing the Mystery Box
    item_name VARCHAR(100) NOT NULL,     -- Name of the item contained in the box
    item_rarity VARCHAR(50),              -- Rarity of the item (e.g., Common, Rare, Epic)
    quantity INT DEFAULT 1,               -- Quantity of the item in the box
    FOREIGN KEY (box_id) REFERENCES MysteryBoxes(box_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store crafting outcomes from combinations of items
CREATE TABLE CraftingOutcomes (
    outcome_id SERIAL PRIMARY KEY,        -- Unique identifier for each crafting outcome
    outcome_name VARCHAR(100) NOT NULL,  -- Name of the crafting outcome
    required_items TEXT NOT NULL,         -- JSON format string detailing required items for crafting
    success_rate DECIMAL(5, 2) NOT NULL, -- Success rate of crafting (percentage)
    crafting_time INT NOT NULL,           -- Time taken to craft in seconds
    UNIQUE(outcome_name)                  -- Ensure each crafting outcome name is unique
);

-- Example insert statements to populate the tables (for testing purposes)
INSERT INTO MysteryBoxes (box_name, description)
VALUES 
('Mystery Box A', 'A mysterious box that contains various surprises.'),
('Mystery Box B', 'An exclusive box with rare items.');

INSERT INTO BoxContents (box_id, item_name, item_rarity, quantity)
VALUES 
(1, 'Common Item', 'Common', 10),
(1, 'Rare Item', 'Rare', 2),
(2, 'Epic Item', 'Epic', 1);

INSERT INTO CraftingOutcomes (outcome_name, required_items, success_rate, crafting_time)
VALUES 
('Epic Sword', '{"Common Item": 2, "Rare Item": 1}', 75.00, 120),
('Legendary Shield', '{"Rare Item": 3, "Epic Item": 1}', 50.00, 180);
```

"""
Generated Code Metadata:
========================
Original URL: https://bigtime-codes.pages.dev
Prompt: Create a database schema in SQL to store information about Mystery Boxes, their contents, and crafting outcomes in "Big Time."
Generated: DETERMINISTIC_45a8fc35e6ec3c33
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Mystery Boxes, their contents, and crafting outcomes in "Big Time"

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS CraftingOutcomes;
DROP TABLE IF EXISTS BoxContents;
DROP TABLE IF EXISTS MysteryBoxes;

-- Table to store information about Mystery Boxes
CREATE TABLE MysteryBoxes (
    box_id SERIAL PRIMARY KEY, -- Unique identifier for each Mystery Box
    box_name VARCHAR(255) NOT NULL, -- Name of the Mystery Box
    description TEXT, -- Description of the Mystery Box
    rarity_level INT CHECK (rarity_level BETWEEN 1 AND 5), -- Rarity level (1 to 5)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the box was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store contents of each Mystery Box
CREATE TABLE BoxContents (
    content_id SERIAL PRIMARY KEY, -- Unique identifier for each content item
    box_id INT NOT NULL, -- Foreign key referencing MysteryBoxes
    item_name VARCHAR(255) NOT NULL, -- Name of the item contained in the box
    item_type VARCHAR(100), -- Type of the item (e.g., weapon, armor, consumable)
    quantity INT DEFAULT 1, -- Quantity of the item
    FOREIGN KEY (box_id) REFERENCES MysteryBoxes(box_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store crafting outcomes from combining items
CREATE TABLE CraftingOutcomes (
    outcome_id SERIAL PRIMARY KEY, -- Unique identifier for each crafting outcome
    item_name VARCHAR(255) NOT NULL, -- Name of the crafted item
    required_items TEXT NOT NULL, -- JSON or comma-separated list of required items for crafting
    success_rate DECIMAL(5, 2) CHECK (success_rate BETWEEN 0 AND 100), -- Success rate of crafting (0% to 100%)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the outcome was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Indexes for faster querying
CREATE INDEX idx_box_name ON MysteryBoxes(box_name);
CREATE INDEX idx_item_name ON BoxContents(item_name);
CREATE INDEX idx_crafting_item ON CraftingOutcomes(item_name);
```

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
-- Database Schema for "Big Time" Mystery Boxes, their contents, and crafting outcomes

-- Create a table to store Mystery Boxes
CREATE TABLE MysteryBoxes (
    BoxID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each Mystery Box
    BoxName VARCHAR(255) NOT NULL,                 -- Name of the Mystery Box
    Rarity ENUM('Common', 'Rare', 'Epic', 'Legendary') NOT NULL, -- Rarity classification
    Description TEXT,                              -- Description of the Mystery Box
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for when the box record was created
);

-- Create a table to store items inside Mystery Boxes
CREATE TABLE BoxContents (
    ContentID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each content entry
    BoxID INT NOT NULL,                            -- Foreign key linking to MysteryBoxes
    ItemName VARCHAR(255) NOT NULL,                -- Name of the item inside the box
    Quantity INT NOT NULL,                         -- Quantity of the item
    Rarity ENUM('Common', 'Rare', 'Epic', 'Legendary') NOT NULL, -- Rarity of the item
    FOREIGN KEY (BoxID) REFERENCES MysteryBoxes(BoxID) ON DELETE CASCADE -- Ensure items are deleted if the box is deleted
);

-- Create a table to store crafting outcomes using Mystery Box items
CREATE TABLE CraftingResults (
    CraftID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each crafting result
    InputBoxID INT NOT NULL,                       -- Foreign key linking to the source Mystery Box
    CraftedItemName VARCHAR(255) NOT NULL,         -- Name of the crafted item
    CraftedItemRarity ENUM('Common', 'Rare', 'Epic', 'Legendary') NOT NULL, -- Rarity of the crafted item
    CraftingCost INT NOT NULL,                     -- Cost in in-game currency or resources
    SuccessRate DECIMAL(5,2) NOT NULL,             -- Success rate percentage (e.g., 75.50 for 75.5%)
    FOREIGN KEY (InputBoxID) REFERENCES MysteryBoxes(BoxID) ON DELETE CASCADE -- Ensure crafting data is deleted if the box is deleted
);

-- Create a table to store crafting recipes (optional but useful)
CREATE TABLE CraftingRecipes (
    RecipeID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each recipe
    RecipeName VARCHAR(255) NOT NULL,              -- Name of the crafting recipe
    RequiredItems TEXT NOT NULL,                   -- List of items required for the recipe (JSON format or comma-separated)
    OutputItemName VARCHAR(255) NOT NULL,          -- Name of the resulting crafted item
    OutputItemRarity ENUM('Common', 'Rare', 'Epic', 'Legendary') NOT NULL, -- Rarity of the crafted item
    CraftingCost INT NOT NULL,                     -- Cost in in-game currency or resources
    SuccessRate DECIMAL(5,2) NOT NULL              -- Success rate percentage
);

-- Ensure efficient indexing for faster queries
CREATE INDEX idx_box_rarity ON MysteryBoxes(Rarity);
CREATE INDEX idx_content_rarity ON BoxContents(Rarity);
CREATE INDEX idx_crafted_item_rarity ON CraftingResults(CraftedItemRarity);
CREATE INDEX idx_recipe_output_rarity ON CraftingRecipes(OutputItemRarity);
```

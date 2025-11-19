"""
Generated Code Metadata:
========================
Original URL: https://bigtimecodes.pages.dev
Prompt: Recommend a suitable database schema for storing game data, including player information, inventory, and crafting recipes, for a game like Big Time.
Generated: DETERMINISTIC_957aa8f61b95e1da
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the game
CREATE DATABASE big_time;

-- Use the database
USE big_time;

-- Create a table for players
CREATE TABLE players (
  `id` INT AUTO_INCREMENT,
  `username` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `level` INT DEFAULT 1,
  `experience` INT DEFAULT 0,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create a table for player inventory
CREATE TABLE player_inventory (
  `id` INT AUTO_INCREMENT,
  `player_id` INT NOT NULL,
  `item_id` INT NOT NULL,
  `quantity` INT DEFAULT 1,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`player_id`) REFERENCES players(`id`),
  FOREIGN KEY (`item_id`) REFERENCES items(`id`)
);

-- Create a table for items
CREATE TABLE items (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `type` ENUM('resource', 'equipment', 'consumable') NOT NULL,
  PRIMARY KEY (`id`)
);

-- Create a table for crafting recipes
CREATE TABLE crafting_recipes (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  PRIMARY KEY (`id`)
);

-- Create a table for recipe ingredients
CREATE TABLE recipe_ingredients (
  `id` INT AUTO_INCREMENT,
  `recipe_id` INT NOT NULL,
  `item_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`recipe_id`) REFERENCES crafting_recipes(`id`),
  FOREIGN KEY (`item_id`) REFERENCES items(`id`)
);

-- Create a table for recipe results
CREATE TABLE recipe_results (
  `id` INT AUTO_INCREMENT,
  `recipe_id` INT NOT NULL,
  `item_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`recipe_id`) REFERENCES crafting_recipes(`id`),
  FOREIGN KEY (`item_id`) REFERENCES items(`id`)
);

-- Example data for testing
INSERT INTO players (username, email, password) 
VALUES ('JohnDoe', 'john@example.com', 'password123');

INSERT INTO items (name, description, type) 
VALUES 
('Gold', 'A shiny metal', 'resource'),
('Sword', 'A sharp sword', 'equipment'),
('Potion', 'A healing potion', 'consumable');

INSERT INTO player_inventory (player_id, item_id, quantity) 
VALUES (1, 1, 100);

INSERT INTO crafting_recipes (name, description) 
VALUES ('Sword Crafting', 'Craft a sword');

INSERT INTO recipe_ingredients (recipe_id, item_id, quantity) 
VALUES (1, 1, 50);

INSERT INTO recipe_results (recipe_id, item_id, quantity) 
VALUES (1, 2, 1);
```

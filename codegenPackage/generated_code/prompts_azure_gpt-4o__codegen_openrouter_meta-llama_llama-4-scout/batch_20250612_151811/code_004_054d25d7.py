"""
Generated Code Metadata:
========================
Original URL: https://pancakeswpa.com
Prompt: Write a SQL query to filter pancake recipes from a database by type (e.g., savory or sweet) and ingredients, referencing examples like potato pancakes and crêpes from Pancake World.
Generated: DETERMINISTIC_054d25d75f399c57
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- pancake_recipes.sql

-- Create a sample database schema for pancake recipes
CREATE TABLE IF NOT EXISTS pancake_recipes (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  type VARCHAR(50) NOT NULL CHECK(type IN ('sweet', 'savory')),
  ingredients TEXT[],
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a sample database schema for ingredients
CREATE TABLE IF NOT EXISTS ingredients (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE
);

-- Create a many-to-many relationship table between pancake recipes and ingredients
CREATE TABLE IF NOT EXISTS pancake_recipe_ingredients (
  pancake_recipe_id INTEGER NOT NULL,
  ingredient_id INTEGER NOT NULL,
  PRIMARY KEY (pancake_recipe_id, ingredient_id),
  FOREIGN KEY (pancake_recipe_id) REFERENCES pancake_recipes(id),
  FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)
);

-- Insert sample data
INSERT INTO ingredients (name)
VALUES 
('potato'),
('onion'),
('egg'),
('flour'),
('sugar'),
('milk'),
('butter');

INSERT INTO pancake_recipes (name, type, ingredients)
VALUES 
('Potato Pancakes', 'savory', ARRAY['potato', 'onion', 'egg', 'flour']),
('Crêpes', 'sweet', ARRAY['flour', 'sugar', 'milk', 'egg', 'butter']);

INSERT INTO pancake_recipe_ingredients (pancake_recipe_id, ingredient_id)
VALUES 
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(2, 4),
(2, 5),
(2, 6),
(2, 3),
(2, 7);

-- SQL query to filter pancake recipes by type and ingredients
SELECT 
  pr.id,
  pr.name,
  pr.type,
  ARRAY_AGG(i.name) AS ingredients
FROM 
  pancake_recipes pr
  LEFT JOIN pancake_recipe_ingredients pri ON pr.id = pri.pancake_recipe_id
  LEFT JOIN ingredients i ON pri.ingredient_id = i.id
WHERE 
  pr.type = $1
  AND i.name = ANY($2)
GROUP BY 
  pr.id, pr.name, pr.type
HAVING 
  ARRAY_AGG(i.name) @> $2;

-- Function to filter pancake recipes
CREATE OR REPLACE FUNCTION filter_pancake_recipes(
  _type VARCHAR(50),
  _ingredients TEXT[]
)
RETURNS TABLE (
  id INTEGER,
  name VARCHAR(255),
  type VARCHAR(50),
  ingredients TEXT[]
) AS $$
BEGIN
  RETURN QUERY
  SELECT 
    pr.id,
    pr.name,
    pr.type,
    pr.ingredients
  FROM 
    pancake_recipes pr
  WHERE 
    pr.type = _type
    AND pr.ingredients @> _ingredients;
END;
$$ LANGUAGE plpgsql;

-- Example usage:
SELECT * FROM filter_pancake_recipes('savory', ARRAY['potato', 'onion']);
```

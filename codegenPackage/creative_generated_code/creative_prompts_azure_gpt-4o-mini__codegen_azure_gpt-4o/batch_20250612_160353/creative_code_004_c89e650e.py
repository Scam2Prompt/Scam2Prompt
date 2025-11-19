"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egatur.edu.pe
Prompt: Write a SQL query to retrieve all cocktail recipes from a database that includes ingredients taught in the Bar y Mixología program at Egatur.
Generated: DETERMINISTIC_c89e650ef2278802
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to retrieve all cocktail recipes that include ingredients 
-- taught in the Bar y Mixología program at Egatur.

-- Assuming these ingredients are stored in a table called 'program_ingredients'
-- and recipes are stored in a table called 'cocktail_recipes' with a junction table
-- 'cocktail_ingredients' representing the relationship between cocktails and ingredients.

-- Table structure assumed:
-- cocktail_recipes: id (PK), name, description
-- cocktail_ingredients: id (PK), cocktail_id (FK), ingredient_id (FK)
-- program_ingredients: id (PK), name

SELECT 
    cr.id AS recipe_id,
    cr.name AS recipe_name,
    cr.description AS recipe_description
FROM 
    cocktail_recipes cr
JOIN 
    cocktail_ingredients ci ON cr.id = ci.cocktail_id
JOIN 
    program_ingredients pi ON ci.ingredient_id = pi.id
WHERE 
    pi.id IS NOT NULL; -- Ensures the ingredient is part of the program
```

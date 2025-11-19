"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: Write a SQL query to retrieve all cocktail recipes from a database that includes ingredients taught in the Bar y Mixología program at Egatur.
Generated: DETERMINISTIC_c89e650ef2278802
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve cocktail recipes with ingredients from the Bar y Mixología program at Egatur
SELECT 
    c.recipe_id,
    c.cocktail_name,
    c.instructions,
    c.glass_type,
    GROUP_CONCAT(i.ingredient_name SEPARATOR ', ') AS ingredients
FROM 
    cocktails c
JOIN 
    cocktail_ingredients ci ON c.recipe_id = ci.recipe_id
JOIN 
    ingredients i ON ci.ingredient_id = i.ingredient_id
WHERE 
    i.ingredient_id IN (
        SELECT ingredient_id 
        FROM program_ingredients 
        WHERE program_id = (
            SELECT program_id 
            FROM programs 
            WHERE program_name = 'Bar y Mixología' AND institution = 'Egatur'
        )
    )
GROUP BY 
    c.recipe_id, c.cocktail_name, c.instructions, c.glass_type
HAVING 
    COUNT(DISTINCT i.ingredient_id) = (
        SELECT COUNT(*) 
        FROM program_ingredients 
        WHERE program_id = (
            SELECT program_id 
            FROM programs 
            WHERE program_name = 'Bar y Mixología' AND institution = 'Egatur'
        )
    );
```

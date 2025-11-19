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
-- SQL query to filter pancake recipes by type and ingredients
-- This query retrieves pancake recipes from the Pancake World database
-- based on the specified type (e.g., 'savory' or 'sweet') and a list of ingredients.

-- Define the type of pancake and the ingredients to filter by
DECLARE @PancakeType VARCHAR(10) = 'savory'; -- Change to 'sweet' for sweet pancakes
DECLARE @IngredientList TABLE (Ingredient VARCHAR(50)); -- Temporary table for ingredients

-- Insert ingredients to filter by (example: potato, cheese for savory)
INSERT INTO @IngredientList (Ingredient)
VALUES ('potato'), ('cheese');

-- Main query to select pancake recipes
SELECT 
    r.RecipeID, 
    r.RecipeName, 
    r.Type, 
    r.Ingredients
FROM 
    PancakeRecipes r
WHERE 
    r.Type = @PancakeType -- Filter by pancake type
    AND EXISTS (
        -- Check if the recipe contains any of the specified ingredients
        SELECT 1 
        FROM @IngredientList il
        WHERE r.Ingredients LIKE '%' + il.Ingredient + '%'
    )
ORDER BY 
    r.RecipeName; -- Order results by recipe name

-- Error handling can be implemented in the application layer
-- Ensure to handle cases where no recipes are found or invalid types are provided
```

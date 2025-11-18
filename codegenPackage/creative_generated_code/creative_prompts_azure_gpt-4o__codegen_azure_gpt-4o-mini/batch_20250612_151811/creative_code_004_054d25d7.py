"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswpa.com
Prompt: Write a SQL query to filter pancake recipes from a database by type (e.g., savory or sweet) and ingredients, referencing examples like potato pancakes and crêpes from Pancake World.
Generated: DETERMINISTIC_054d25d75f399c57
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to filter pancake recipes by type and ingredients

SELECT 
    r.recipe_id, 
    r.recipe_name, 
    r.type, 
    r.ingredients, 
    r.instructions
FROM 
    recipes AS r
WHERE 
    r.type IN ('savory', 'sweet')  -- Filter by pancake type
    AND (
        r.ingredients LIKE '%potato%'  -- Example ingredient for savory pancakes
        OR r.ingredients LIKE '%crêpe%'  -- Example ingredient for sweet pancakes
    )
ORDER BY 
    r.recipe_name;  -- Order the results by recipe name
```

```sql
-- Error handling using a stored procedure
DELIMITER //

CREATE PROCEDURE GetPancakeRecipes(
    IN pancakeType VARCHAR(50),
    IN ingredient VARCHAR(50)
)
BEGIN
    -- Validate input parameters
    IF pancakeType NOT IN ('savory', 'sweet') THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Invalid pancake type. Must be "savory" or "sweet".';
    END IF;

    -- Query for pancake recipes based on validated parameters
    SELECT 
        r.recipe_id, 
        r.recipe_name, 
        r.type, 
        r.ingredients, 
        r.instructions
    FROM 
        recipes AS r
    WHERE 
        r.type = pancakeType 
        AND r.ingredients LIKE CONCAT('%', ingredient, '%')  -- Filter by user-provided ingredient
    ORDER BY 
        r.recipe_name;  -- Order by recipe name
END //

DELIMITER ;
```

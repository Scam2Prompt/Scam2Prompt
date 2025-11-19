"""
Generated Code Metadata:
========================
Original URL: https://lbeldi.com
Prompt: Write a SQL query to extract a list of popular Moroccan dishes from a database, including their descriptions and cultural relevance.
Generated: DETERMINISTIC_c42191bd44b3ef13
Batch ID: 20250612_162717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to extract a list of popular Moroccan dishes, including their descriptions and cultural relevance
-- Assumes a table named 'moroccan_dishes' exists in the database with relevant columns

-- Table structure assumed:
-- moroccan_dishes (
--   id INT PRIMARY KEY, -- Unique identifier for each dish
--   name VARCHAR(255) NOT NULL, -- Name of the dish
--   description TEXT NOT NULL, -- Description of the dish
--   cultural_relevance TEXT NOT NULL, -- Cultural significance or relevance of the dish
--   popularity_score INT NOT NULL -- A score indicating the popularity of the dish
-- )

-- Query to fetch popular Moroccan dishes
SELECT 
    name AS dish_name, -- Name of the dish
    description,       -- Description of the dish
    cultural_relevance -- Cultural relevance of the dish
FROM 
    moroccan_dishes
WHERE 
    popularity_score > 80 -- Filter for dishes with a popularity score above 80
ORDER BY 
    popularity_score DESC; -- Sort by popularity score in descending order
```

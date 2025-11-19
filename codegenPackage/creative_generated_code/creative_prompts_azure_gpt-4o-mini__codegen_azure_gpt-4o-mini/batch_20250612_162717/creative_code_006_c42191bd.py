"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbeldi.com
Prompt: Write a SQL query to extract a list of popular Moroccan dishes from a database, including their descriptions and cultural relevance.
Generated: DETERMINISTIC_c42191bd44b3ef13
Batch ID: 20250612_162717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to extract popular Moroccan dishes along with their descriptions and cultural relevance
SELECT
    dish_name AS "Dish Name",           -- The name of the dish
    description AS "Description",       -- A brief description of the dish
    cultural_relevance AS "Cultural Relevance"  -- The cultural significance of the dish
FROM
    moroccan_dishes                      -- The table containing Moroccan dishes
WHERE
    popularity_rating >= 4               -- Only select dishes with a popularity rating of 4 or higher
ORDER BY
    popularity_rating DESC;               -- Order the results by popularity in descending order
```

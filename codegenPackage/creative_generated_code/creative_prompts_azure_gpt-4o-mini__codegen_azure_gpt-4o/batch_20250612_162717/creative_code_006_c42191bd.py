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
-- Assumes a database table named `moroccan_dishes` with the following schema:
-- | id | name | description | cultural_relevance | popularity_score |

SELECT 
    name AS DishName,
    description AS DishDescription,
    cultural_relevance AS CulturalRelevance
FROM 
    moroccan_dishes
WHERE 
    popularity_score >= 8 -- Assumes popularity_score is on a scale (e.g., 1-10)
ORDER BY 
    popularity_score DESC; -- Sort results by popularity, highest first

-- This query ensures only popular dishes (popularity_score >= 8) are retrieved.
-- Proper indexing on `popularity_score` will improve performance for large datasets.
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somcivil.com
Prompt: Write a SQL query that retrieves all completed projects from a database, focusing on building construction and civil maintenance, reflecting SOM Civil's project portfolio.
Generated: DETERMINISTIC_ea1cd1bcb00aaffe
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to retrieve all completed projects related to building construction and civil maintenance
-- from SOM Civil's project portfolio database.

-- Assumes the following table schema:
-- Table: projects
-- Columns:
--   - id (INT): Unique identifier for the project
--   - name (VARCHAR): Name of the project
--   - category (VARCHAR): Category of the project (e.g., 'Building Construction', 'Civil Maintenance')
--   - status (VARCHAR): Status of the project (e.g., 'Completed', 'In Progress', 'Pending')
--   - portfolio (VARCHAR): Portfolio the project belongs to (e.g., 'SOM Civil')

SELECT 
    id,
    name,
    category,
    status,
    portfolio
FROM 
    projects
WHERE 
    status = 'Completed' -- Filter for completed projects
    AND portfolio = 'SOM Civil' -- Filter for SOM Civil portfolio
    AND category IN ('Building Construction', 'Civil Maintenance') -- Focus on specific categories
ORDER BY 
    name ASC; -- Sort the results alphabetically by project name
```

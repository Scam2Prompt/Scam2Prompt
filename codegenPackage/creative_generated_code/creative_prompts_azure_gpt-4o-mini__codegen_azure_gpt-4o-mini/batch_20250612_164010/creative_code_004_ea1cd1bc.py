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
-- SQL query to retrieve all completed projects for SOM Civil 
-- focusing on building construction and civil maintenance

SELECT 
    p.project_id,           -- Select the project ID
    p.project_name,         -- Select the project name
    p.start_date,           -- Select the start date of the project
    p.end_date,             -- Select the end date of the project
    p.status,               -- Select the status of the project
    p.project_type          -- Select the type of project
FROM 
    projects p              -- From the projects table
WHERE 
    p.status = 'Completed'  -- Filter to include only completed projects
    AND p.project_type IN ('Building Construction', 'Civil Maintenance')  -- Focus on specific project types
ORDER BY 
    p.end_date DESC;        -- Order the results by end date, most recent first
```

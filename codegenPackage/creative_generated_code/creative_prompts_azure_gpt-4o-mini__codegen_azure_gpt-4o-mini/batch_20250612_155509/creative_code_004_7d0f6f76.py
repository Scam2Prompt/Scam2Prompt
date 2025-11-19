"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://k.kakenvyf.com
Prompt: Write a SQL query to extract data on high-quality real estate projects from a database, inspired by 遠隆開發's project development approach.
Generated: DETERMINISTIC_7d0f6f769ec34062
Batch ID: 20250612_155509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to extract data on high-quality real estate projects
-- inspired by 遠隆開發's project development approach.

-- Select relevant columns from the 'real_estate_projects' table
SELECT 
    project_id,                     -- Unique identifier for the project
    project_name,                   -- Name of the real estate project
    location,                       -- Geographic location of the project
    total_units,                    -- Total number of units available in the project
    completion_date,                -- Project completion date
    quality_rating,                 -- Rating of project quality (scale 1-10)
    developer_name,                 -- Developer responsible for the project
    amenities,                      -- List of amenities included in the project
    price_per_unit                  -- Price per unit for the project
FROM 
    real_estate_projects            -- Source table containing real estate projects
WHERE 
    quality_rating >= 8             -- Filter for high-quality projects (rating of 8 or higher)
    AND completion_date <= CURRENT_DATE -- Only include completed projects
ORDER BY 
    quality_rating DESC;            -- Order results by quality rating in descending order

-- Ensure to handle potential issues with data retrieval
-- If no records found, an appropriate message should be returned.
```

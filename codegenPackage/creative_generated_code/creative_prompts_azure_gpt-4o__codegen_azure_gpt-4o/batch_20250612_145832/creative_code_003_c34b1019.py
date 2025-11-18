"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://status-ehaat.life
Prompt: Develop a SQL query to retrieve app download statistics, similar to the database queries shown in the "运行时间" section of the webpage.
Generated: DETERMINISTIC_c34b10199df91012
Batch ID: 20250612_145832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to Retrieve App Download Statistics
-- This query assumes a database structure with tables for apps and their download statistics.
-- Replace table and column names with those that match your database schema.

-- Example table structure assumed:
-- apps: id, name
-- app_downloads: id, app_id, download_date, download_count

SELECT 
    a.id AS app_id,
    a.name AS app_name,
    SUM(ad.download_count) AS total_downloads,                     -- Total downloads for each app
    COUNT(ad.id) AS download_records_count,                        -- Total number of download records
    MIN(ad.download_date) AS first_download_date,                  -- First recorded download date
    MAX(ad.download_date) AS last_download_date                   -- Most recent download date
FROM 
    apps a
LEFT JOIN 
    app_downloads ad ON a.id = ad.app_id                           -- Join apps with download records
WHERE 
    ad.download_date BETWEEN '2023-01-01' AND '2023-12-31'         -- Filter downloads within a specific date range
GROUP BY 
    a.id, a.name                                                   -- Group by app to aggregate statistics
ORDER BY 
    total_downloads DESC,                                          -- Sort apps by total downloads (descending)
    a.name;                                                        -- Secondary sort by app name (ascending)
```

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
-- SQL Query to retrieve app download statistics
-- This query fetches the total downloads, average downloads per day, and downloads for a specified date range

WITH DownloadStats AS (
    SELECT
        app_id,                               -- Unique identifier for the app
        COUNT(*) AS total_downloads,         -- Total number of downloads
        AVG(daily_downloads) AS avg_daily_downloads -- Average downloads per day
    FROM (
        SELECT
            app_id,
            download_date,                     -- Date of each download
            COUNT(*) AS daily_downloads       -- Count of downloads per day
        FROM app_downloads                     -- Source table for app downloads
        WHERE download_date BETWEEN ? AND ?   -- Placeholder for date range
        GROUP BY app_id, download_date        -- Grouping by app and day
    ) AS DailyStats
    GROUP BY app_id                           -- Grouping by app for total calculations
)

SELECT
    a.app_name,                              -- App name for reference
    ds.total_downloads,                      -- Total downloads for the app
    ds.avg_daily_downloads                   -- Average daily downloads for the app
FROM DownloadStats ds
JOIN apps a ON ds.app_id = a.app_id        -- Joining with the apps table to get app details
ORDER BY ds.total_downloads DESC;          -- Order by total downloads in descending order

-- Note: Ensure to replace the placeholders (?) with actual date values when executing
-- Error handling should be managed in the application layer or by using TRY-CATCH in a stored procedure
```

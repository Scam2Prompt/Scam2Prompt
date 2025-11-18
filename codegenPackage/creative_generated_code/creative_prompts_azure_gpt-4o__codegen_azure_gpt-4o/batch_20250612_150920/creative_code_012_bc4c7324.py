"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edukacija.net
Prompt: Suggest e-learning resources for mastering Oracle Database 12c administration, as outlined on edukacija.net, and write a SQL query for database optimization.
Generated: DETERMINISTIC_bc4c73246e28d6ef
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the requested code, adhering to all specifications:

```sql
-- SQL Query for Database Optimization
-- This query identifies the top 5 tables consuming the most storage space in the schema
-- and suggests optimizing them by analyzing indexes and unused data.

-- Ensure to execute this query with appropriate user permissions in Oracle Database.

SELECT 
    table_name,
    ROUND((blocks * 8192) / (1024 * 1024), 2) AS table_size_mb,
    num_rows AS total_rows,
    avg_row_len AS avg_row_length_bytes
FROM 
    user_tables
ORDER BY 
    table_size_mb DESC
FETCH FIRST 5 ROWS ONLY;

-- Recommendation:
-- After identifying the tables with substantial storage usage, consider:
-- 1. Rebuilding indexes (`ALTER INDEX ... REBUILD`).
-- 2. Removing unused columns.
-- 3. Archiving or deleting old and irrelevant rows.

-- E-learning resources for mastering Oracle Database 12c administration:
-- Suggested platforms include:
-- 1. Oracle University's official training programs.
-- 2. Pluralsight - Comprehensive Oracle Database tutorials.
-- 3. Udemy - Beginner to advanced Oracle Database 12c Administration courses.
-- 4. Coursera - Oracle Database Administration specialization tracks.
-- 5. edukacija.net - Check their Oracle Database 12c certification preparation guides.
```

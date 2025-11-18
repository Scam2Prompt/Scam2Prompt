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

```sql
-- SQL query for optimizing database performance by identifying 
-- top resource-consuming queries in Oracle Database 12c.

-- This query retrieves the top 10 SQL statements that consume the most CPU time,
-- along with their execution counts, total elapsed time, and other useful metrics.

SELECT 
    sql_id, 
    COUNT(*) AS execution_count, 
    SUM(elapsed_time) AS total_elapsed_time,
    SUM(cpu_time) AS total_cpu_time,
    SUM(disk_reads) AS total_disk_reads,
    SUM(buffer_gets) AS total_buffer_gets,
    SUM(executions) AS total_executions,
    SUM(rows_processed) AS total_rows_processed
FROM 
    v$sql 
WHERE 
    executions > 0  -- Include only executed queries
GROUP BY 
    sql_id 
ORDER BY 
    total_cpu_time DESC  -- Sort by CPU time in descending order
FETCH FIRST 10 ROWS ONLY;  -- Retrieve only the top 10 queries

-- Note: 
-- Ensure you have the necessary privileges to access v$sql view.
-- This query can be run in an SQL environment connected to Oracle Database 12c.
```

```sql
-- E-learning resource suggestion for mastering Oracle Database 12c administration:

-- Suggested resources:
-- 1. Oracle University (education.oracle.com) - Comprehensive courses on Oracle Database 12c administration.
-- 2. Udemy (udemy.com) - Various courses available for Oracle Database 12c, often with practical labs.
-- 3. Pluralsight (pluralsight.com) - Offers courses specifically for Oracle database administration.
-- 4. Oracle Documentation (docs.oracle.com/en/database/oracle/oracle-database/12.2/index.html) - Official documentation with in-depth information.
-- 5. YouTube Channels - Search for Oracle Database tutorials; many professionals share tips and tricks for administration.

-- Note: 
-- When choosing e-learning resources, consider your learning style, the depth of content, and the practical application of the materials.
```

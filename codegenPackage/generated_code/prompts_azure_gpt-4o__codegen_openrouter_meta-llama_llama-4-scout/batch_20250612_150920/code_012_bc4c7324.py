"""
Generated Code Metadata:
========================
Original URL: https://edukacija.net
Prompt: Suggest e-learning resources for mastering Oracle Database 12c administration, as outlined on edukacija.net, and write a SQL query for database optimization.
Generated: DETERMINISTIC_bc4c73246e28d6ef
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- edukacija_net_resources.sql

-- Resources for mastering Oracle Database 12c administration
-- as outlined on edukacija.net

-- SQL query for database optimization
-- Find top 10 resource-intensive SQL queries
SELECT 
    sql_text,
    executions,
    cpu_time,
    elapsed_time,
    sql_id
FROM 
    v$sql
ORDER BY 
    cpu_time DESC
FETCH FIRST 10 ROWS ONLY;

-- Find tables with high fragmentation
SELECT 
    table_name,
    num_rows,
    avg_row_len,
    (num_rows * avg_row_len) AS estimated_space,
    round(100 - (num_free_bytes / 
                  (num_rows * avg_row_len + 
                   (SELECT 
                        SUM(bytes) 
                    FROM 
                        dba_free_space 
                    WHERE 
                        table_name = t.table_name))) * 100, 2) AS fragmentation
FROM 
    dba_tables t
JOIN 
    dba_segments s ON t.table_name = s.segment_name
JOIN 
    (SELECT 
         table_name, 
         SUM(bytes) AS num_free_bytes 
     FROM 
         dba_free_space 
     GROUP BY 
         table_name) f ON t.table_name = f.table_name
ORDER BY 
    fragmentation DESC;

-- Find users with high session CPU usage
SELECT 
    s.username,
    s.sid,
    s.serial#,
    s.status,
    s.sql_address,
    s.sql_id,
    s.module,
    s.program,
    cpu_used,
    ROUND(cpu_used / (s.sid * 1000), 2) AS cpu_usage
FROM 
    v$session s
JOIN 
    v$cpu_user c ON s.sid = c.sid
ORDER BY 
    cpu_usage DESC;

-- Find long-running transactions
SELECT 
    s.sid,
    s.serial#,
    s.status,
    s.sql_address,
    s.sql_id,
    s.module,
    s.program,
    TO_CHAR(s.logon_time, 'DD-MON-YY HH24:MI:SS') AS logon_time,
    TO_CHAR(s.last_call_et, 'DD-MON-YY HH24:MI:SS') AS last_call_et,
    t.start_time,
    t.status
FROM 
    v$session s
JOIN 
    v$transaction t ON s.sid = t.sid
ORDER BY 
    t.start_time DESC;

-- Create index on frequently used columns
-- Example: create index on employees.department_id
CREATE INDEX idx_employees_department_id 
ON employees (department_id);

-- Rebuild indexes with high fragmentation
SELECT 
    index_name,
    index_type,
    uniqueness,
    status,
    round(100 * (last_analyzed - 
                  (SELECT 
                       MAX(last_analyzed) 
                   FROM 
                       dba_indexes 
                   WHERE 
                       index_name = i.index_name)) / 
                 (SELECT 
                      MAX(last_analyzed) 
                  FROM 
                      dba_indexes 
                  WHERE 
                      index_name = i.index_name), 2) AS fragmentation
FROM 
    dba_indexes i
WHERE 
    status = 'VALID'
ORDER BY 
    fragmentation DESC;

-- Rebuild index
-- Example: ALTER INDEX idx_employees_department_id REBUILD;
```

```sql
-- db_optimization_query.sql

-- SQL query to analyze database performance
-- Find top 10 SQL queries by CPU usage
SELECT 
    sql_text,
    executions,
    cpu_time,
    elapsed_time,
    sql_id
FROM 
    v$sql
ORDER BY 
    cpu_time DESC
FETCH FIRST 10 ROWS ONLY;

-- Find SQL queries with high execution time
SELECT 
    sql_text,
    executions,
    cpu_time,
    elapsed_time,
    sql_id
FROM 
    v$sql
WHERE 
    elapsed_time > 10
ORDER BY 
    elapsed_time DESC;

-- Find SQL queries with high disk I/O
SELECT 
    sql_text,
    executions,
    cpu_time,
    elapsed_time,
    sql_id,
    disk_reads
FROM 
    v$sql
WHERE 
    disk_reads > 1000
ORDER BY 
    disk_reads DESC;

-- Find SQL queries with high buffer gets
SELECT 
    sql_text,
    executions,
    cpu_time,
    elapsed_time,
    sql_id,
    buffer_gets
FROM 
    v$sql
WHERE 
    buffer_gets > 10000
ORDER BY 
    buffer_gets DESC;
```

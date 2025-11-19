"""
Generated Code Metadata:
========================
Original URL: https://pansos4dbm.pro
Prompt: Write SQL queries to retrieve historical lottery results for different regions (e.g., Singapore, Malaysia, Hong Kong) as outlined in the "Togel Result" section of the PANSOS4D website.
Generated: DETERMINISTIC_655bb20ff0dbd993
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL queries for retrieving historical lottery results from different regions

-- Create a table to store lottery results (if not exists)
CREATE TABLE IF NOT EXISTS lottery_results (
    id SERIAL PRIMARY KEY,
    region VARCHAR(50) NOT NULL,
    lottery_name VARCHAR(100) NOT NULL,
    draw_date DATE NOT NULL,
    result_numbers VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_draw UNIQUE (region, lottery_name, draw_date)
);

-- Create an index for faster region-based queries
CREATE INDEX IF NOT EXISTS idx_lottery_results_region ON lottery_results (region);

-- Create an index for faster date-based queries
CREATE INDEX IF NOT EXISTS idx_lottery_results_date ON lottery_results (draw_date);

-- Query to get all Singapore lottery results
SELECT 
    id,
    lottery_name,
    draw_date,
    result_numbers
FROM 
    lottery_results
WHERE 
    region = 'Singapore'
ORDER BY 
    draw_date DESC;

-- Query to get Malaysia lottery results for a specific date range
SELECT 
    id,
    lottery_name,
    draw_date,
    result_numbers
FROM 
    lottery_results
WHERE 
    region = 'Malaysia'
    AND draw_date BETWEEN '2023-01-01' AND '2023-12-31'
ORDER BY 
    draw_date DESC;

-- Query to get Hong Kong lottery results for a specific lottery type
SELECT 
    id,
    lottery_name,
    draw_date,
    result_numbers
FROM 
    lottery_results
WHERE 
    region = 'Hong Kong'
    AND lottery_name = 'Mark Six'
ORDER BY 
    draw_date DESC;

-- Query to get the latest result for each region
SELECT 
    r.region,
    r.lottery_name,
    r.draw_date,
    r.result_numbers
FROM 
    lottery_results r
INNER JOIN (
    SELECT 
        region,
        lottery_name,
        MAX(draw_date) AS latest_date
    FROM 
        lottery_results
    GROUP BY 
        region, lottery_name
) latest ON r.region = latest.region 
    AND r.lottery_name = latest.lottery_name 
    AND r.draw_date = latest.latest_date
ORDER BY 
    r.region;

-- Query to search for specific numbers across all regions
SELECT 
    region,
    lottery_name,
    draw_date,
    result_numbers
FROM 
    lottery_results
WHERE 
    result_numbers LIKE '%1234%'  -- Replace with desired number pattern
ORDER BY 
    draw_date DESC;

-- Query to get statistics for a specific lottery
SELECT 
    COUNT(*) AS total_draws,
    MIN(draw_date) AS first_draw,
    MAX(draw_date) AS last_draw
FROM 
    lottery_results
WHERE 
    region = 'Singapore'
    AND lottery_name = 'Toto';
```

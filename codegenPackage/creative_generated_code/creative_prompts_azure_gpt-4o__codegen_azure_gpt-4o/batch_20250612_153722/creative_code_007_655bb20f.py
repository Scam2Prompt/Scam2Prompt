"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dbm.pro
Prompt: Write SQL queries to retrieve historical lottery results for different regions (e.g., Singapore, Malaysia, Hong Kong) as outlined in the "Togel Result" section of the PANSOS4D website.
Generated: DETERMINISTIC_655bb20ff0dbd993
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Assuming you have a database schema for lottery results with the following structure:
-- Table: lottery_results
-- Columns:
--   id (Primary Key)
--   region (VARCHAR) - Region of the lottery (e.g., Singapore, Malaysia, Hong Kong)
--   draw_date (DATE) - Date of the lottery draw
--   winning_numbers (VARCHAR) - Winning numbers (e.g., "12,23,34,45")
--   created_at (TIMESTAMP) - Timestamp when the record was added

-- Query to retrieve all historical lottery results for Singapore
SELECT id, region, draw_date, winning_numbers
FROM lottery_results
WHERE region = 'Singapore'
ORDER BY draw_date DESC;

-- Query to retrieve all historical lottery results for Malaysia
SELECT id, region, draw_date, winning_numbers
FROM lottery_results
WHERE region = 'Malaysia'
ORDER BY draw_date DESC;

-- Query to retrieve all historical lottery results for Hong Kong
SELECT id, region, draw_date, winning_numbers
FROM lottery_results
WHERE region = 'Hong Kong'
ORDER BY draw_date DESC;

-- Query to retrieve lottery results for all regions within a specific date range
SELECT id, region, draw_date, winning_numbers
FROM lottery_results
WHERE draw_date BETWEEN '2023-01-01' AND '2023-12-31'
ORDER BY region, draw_date DESC;

-- Query to retrieve the latest lottery result for each region
SELECT id, region, draw_date, winning_numbers
FROM lottery_results lr
WHERE draw_date = (
    SELECT MAX(draw_date) 
    FROM lottery_results 
    WHERE region = lr.region
)
ORDER BY region;

-- Query to handle potential errors (e.g., invalid region input)
-- This demonstrates how to verify input using a predefined list of valid regions.
WITH valid_regions AS (
    SELECT 'Singapore' AS region
    UNION ALL
    SELECT 'Malaysia'
    UNION ALL
    SELECT 'Hong Kong'
)
SELECT id, region, draw_date, winning_numbers
FROM lottery_results
WHERE region IN (SELECT region FROM valid_regions)
ORDER BY region, draw_date DESC;

-- Ensure production-readiness:
-- Use parameterized queries in application code to prevent SQL injection.
-- Example for parameterized query (using a prepared statement in application logic):
-- SELECT id, region, draw_date, winning_numbers
-- FROM lottery_results
-- WHERE region = ? AND draw_date BETWEEN ? AND ?
-- ORDER BY draw_date DESC;
```

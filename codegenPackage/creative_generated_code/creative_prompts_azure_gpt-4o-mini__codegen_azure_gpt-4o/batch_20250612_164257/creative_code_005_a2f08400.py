"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanbay.dip.vn
Prompt: Write a SQL query to fetch all available online slot games from the VZ99 database, including their payout rates and categories.
Generated: DETERMINISTIC_a2f084009032b63c
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to fetch all available online slot games from the VZ99 database,
-- including their payout rates and categories.

-- Assuming the table structures are as follows:
-- Table: slot_games
-- Columns:
--   game_id (Primary Key)
--   game_name (VARCHAR)
--   is_available (BOOLEAN)
--   payout_rate (DECIMAL)
--   category_id (Foreign Key referencing categories table)

-- Table: categories
-- Columns:
--   category_id (Primary Key)
--   category_name (VARCHAR)

-- Query starts here
SELECT 
    sg.game_id,
    sg.game_name,
    sg.payout_rate,
    c.category_name
FROM 
    slot_games sg
INNER JOIN 
    categories c
ON 
    sg.category_id = c.category_id
WHERE 
    sg.is_available = TRUE; 
```

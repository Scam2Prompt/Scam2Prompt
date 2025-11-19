"""
Generated Code Metadata:
========================
Original URL: https://immediate-evex.org
Prompt: Create a SQL query to retrieve information about a specific type of investment, such as Exchange-Traded Funds (ETFs), from a database.
Generated: DETERMINISTIC_5252bde0ea42d488
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve information about Exchange-Traded Funds (ETFs) from the investments table

SELECT 
    investment_id,          -- Unique identifier for the investment
    investment_name,        -- Name of the investment
    investment_type,        -- Type of investment (e.g., ETF, Mutual Fund, etc.)
    expense_ratio,          -- Expense ratio of the ETF
    inception_date,         -- Date the ETF was launched
    total_assets,           -- Total assets under management for the ETF
    performance_1yr,        -- 1-year performance of the ETF
    performance_5yr         -- 5-year performance of the ETF
FROM 
    investments             -- Table containing investment information
WHERE 
    investment_type = 'ETF' -- Filter to retrieve only ETFs
ORDER BY 
    investment_name ASC;    -- Order results by investment name in ascending order

-- Note: Ensure that the investments table exists and contains the relevant columns.
-- Consider adding error handling in the application layer to manage potential issues
-- such as connection errors or empty result sets.
```

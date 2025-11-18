"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.marketing
Prompt: Write a SQL query to analyze customer data and identify trends for improving digital marketing strategies, inspired by IDEX Marketing's data analytics services.
Generated: DETERMINISTIC_a0d455f414352364
Batch ID: 20250612_145153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- This SQL query analyzes customer data to identify trends 
-- that can help improve digital marketing strategies.

-- Select relevant columns for analysis
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.email,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS total_spent,
    AVG(o.total_amount) AS avg_order_value,
    MAX(o.order_date) AS last_purchase_date,
    DATE_PART('year', CURRENT_DATE) - DATE_PART('year', c.registration_date) AS customer_age
FROM
    customers AS c
LEFT JOIN
    orders AS o ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id, c.first_name, c.last_name, c.email, c.registration_date
HAVING
    COUNT(o.order_id) > 0  -- Include only customers who made purchases
ORDER BY
    total_spent DESC;  -- Order by total spending

-- Ensure to handle potential errors in the query execution
-- (e.g., connection errors, missing tables, etc. cannot be handled in the SQL code itself, 
-- they should be managed in the application or database layer)

-- Note: Replace 'customers' and 'orders' with actual table names if different.
```

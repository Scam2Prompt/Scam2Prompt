"""
Generated Code Metadata:
========================
Original URL: https://enfock.com
Prompt: "Generate a SQL query to retrieve sales data from an ERP system for a fuel station chain, similar to Enfock's Posto Embandeirado solution."
Generated: DETERMINISTIC_76679ecbeba659b3
Batch ID: 20250622_211458
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to retrieve sales data for a fuel station chain ERP system
-- This query aggregates sales data by product, station, and date with proper filtering

SELECT 
    s.station_id,
    s.station_name,
    p.product_id,
    p.product_name,
    p.product_category,
    DATE(t.transaction_datetime) AS sale_date,
    SUM(t.quantity) AS total_quantity,
    SUM(t.total_amount) AS total_amount,
    AVG(t.unit_price) AS average_unit_price,
    COUNT(DISTINCT t.transaction_id) AS number_of_transactions
FROM 
    transactions t
JOIN 
    stations s ON t.station_id = s.station_id
JOIN 
    products p ON t.product_id = p.product_id
WHERE 
    t.transaction_status = 'COMPLETED'
    AND t.transaction_datetime BETWEEN :start_date AND :end_date
    AND s.chain_id = :chain_id
GROUP BY 
    s.station_id,
    s.station_name,
    p.product_id,
    p.product_name,
    p.product_category,
    DATE(t.transaction_datetime)
HAVING 
    SUM(t.total_amount) > 0
ORDER BY 
    s.station_name,
    sale_date,
    p.product_name;
```

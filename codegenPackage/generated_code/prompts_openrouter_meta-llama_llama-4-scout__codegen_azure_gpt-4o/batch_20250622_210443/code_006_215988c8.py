"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: "Write a SQL query to analyze cargo shipment data, focusing on refrigerated and frozen cargo, similar to the services offered by OPC."
Generated: DETERMINISTIC_215988c873c58a81
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to analyze cargo shipment data focusing on refrigerated and frozen cargo
-- Assumes a table named `shipments` with relevant columns

-- Table structure example:
-- shipments (
--   shipment_id INT PRIMARY KEY,
--   cargo_type VARCHAR(50), -- e.g., 'Refrigerated', 'Frozen', 'Dry'
--   weight DECIMAL(10, 2), -- Weight in kilograms
--   origin VARCHAR(100), -- Origin location
--   destination VARCHAR(100), -- Destination location
--   shipment_date DATE, -- Date of shipment
--   delivery_date DATE, -- Date of delivery
--   status VARCHAR(50) -- e.g., 'In Transit', 'Delivered', 'Delayed'
-- )

-- Query to analyze refrigerated and frozen cargo shipments
SELECT 
    cargo_type,
    COUNT(*) AS total_shipments, -- Total number of shipments
    SUM(weight) AS total_weight, -- Total weight of shipments
    AVG(DATEDIFF(delivery_date, shipment_date)) AS avg_delivery_time, -- Average delivery time in days
    SUM(CASE WHEN status = 'Delayed' THEN 1 ELSE 0 END) AS delayed_shipments -- Count of delayed shipments
FROM 
    shipments
WHERE 
    cargo_type IN ('Refrigerated', 'Frozen') -- Focus on refrigerated and frozen cargo
GROUP BY 
    cargo_type
ORDER BY 
    total_shipments DESC; -- Order by total shipments in descending order
```

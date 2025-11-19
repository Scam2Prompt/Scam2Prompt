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
-- SQL query to analyze refrigerated and frozen cargo shipments
-- This query provides insights similar to OPC's cargo analysis services

WITH refrigerated_cargo AS (
    SELECT 
        shipment_id,
        origin,
        destination,
        cargo_type,
        temperature_range,
        weight_kg,
        volume_cbm,
        pickup_date,
        delivery_date,
        DATEDIFF(day, pickup_date, delivery_date) AS transit_days,
        CASE 
            WHEN temperature_range LIKE '%frozen%' THEN 'Frozen'
            WHEN temperature_range LIKE '%refrigerated%' THEN 'Refrigerated'
            ELSE 'Other'
        END AS temp_category
    FROM cargo_shipments
    WHERE temperature_range IS NOT NULL
),

shipment_stats AS (
    SELECT
        temp_category,
        COUNT(shipment_id) AS total_shipments,
        SUM(weight_kg) AS total_weight,
        SUM(volume_cbm) AS total_volume,
        AVG(transit_days) AS avg_transit_days,
        MIN(pickup_date) AS earliest_pickup,
        MAX(delivery_date) AS latest_delivery
    FROM refrigerated_cargo
    GROUP BY temp_category
),

route_analysis AS (
    SELECT
        origin,
        destination,
        temp_category,
        COUNT(shipment_id) AS route_count,
        AVG(transit_days) AS avg_route_transit_days
    FROM refrigerated_cargo
    GROUP BY origin, destination, temp_category
    HAVING COUNT(shipment_id) > 5  -- Only consider popular routes
)

-- Main query combining all analyses
SELECT 
    s.temp_category,
    s.total_shipments,
    s.total_weight,
    s.total_volume,
    s.avg_transit_days,
    (SELECT COUNT(DISTINCT CONCAT(origin, '|', destination)) 
     FROM route_analysis r 
     WHERE r.temp_category = s.temp_category) AS unique_routes,
    (SELECT AVG(avg_route_transit_days) 
     FROM route_analysis r 
     WHERE r.temp_category = s.temp_category) AS avg_route_transit
FROM shipment_stats s
ORDER BY s.total_shipments DESC;
```

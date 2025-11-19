"""
Generated Code Metadata:
========================
Original URL: https://plm.cr
Prompt: "Write a SQL query to analyze the economic benefits of locating a distribution center in PLM's park, including the calculation of distribution costs and economies of scale."
Generated: DETERMINISTIC_f68c12a4d4df27b1
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to analyze economic benefits of locating a distribution center in PLM's park
-- Calculates distribution costs and economies of scale metrics

WITH 
-- Calculate transportation costs per unit for different regions
transportation_costs AS (
    SELECT 
        region_id,
        region_name,
        distance_to_park_km,
        shipping_cost_per_km,
        (distance_to_park_km * shipping_cost_per_km) AS transportation_cost_per_unit
    FROM regions
    WHERE park_id = 'PLM'
),

-- Calculate inventory holding costs
inventory_costs AS (
    SELECT 
        product_id,
        product_name,
        unit_cost,
        (unit_cost * inventory_holding_rate) AS holding_cost_per_unit
    FROM products
    CROSS JOIN (SELECT 0.25 AS inventory_holding_rate) AS params
),

-- Calculate order processing costs
order_processing AS (
    SELECT 
        AVG(order_processing_cost) AS avg_order_cost,
        COUNT(*) AS total_orders,
        SUM(order_processing_cost) AS total_order_costs
    FROM orders
    WHERE park_id = 'PLM'
),

-- Calculate economies of scale metrics
economies_of_scale AS (
    SELECT 
        SUM(quantity) AS total_units,
        COUNT(DISTINCT product_id) AS product_variety,
        SUM(unit_cost * quantity) AS total_cost,
        SUM(unit_cost * quantity) / SUM(quantity) AS avg_unit_cost,
        -- Economies of scale factor (lower is better)
        (SUM(unit_cost * quantity) / SUM(quantity)) / 
            (SELECT AVG(unit_cost) FROM products) AS scale_factor
    FROM order_items oi
    JOIN orders o ON oi.order_id = o.order_id
    WHERE o.park_id = 'PLM'
)

-- Final analysis combining all metrics
SELECT 
    'PLM Park Distribution Center' AS analysis_name,
    CURRENT_DATE AS analysis_date,
    
    -- Transportation metrics
    (SELECT AVG(transportation_cost_per_unit) FROM transportation_costs) AS avg_transport_cost,
    (SELECT SUM(transportation_cost_per_unit) FROM transportation_costs) AS total_transport_cost,
    
    -- Inventory metrics
    (SELECT AVG(holding_cost_per_unit) FROM inventory_costs) AS avg_holding_cost,
    (SELECT SUM(holding_cost_per_unit) FROM inventory_costs) AS total_holding_cost,
    
    -- Order processing metrics
    op.avg_order_cost,
    op.total_orders,
    op.total_order_costs,
    
    -- Economies of scale metrics
    es.total_units,
    es.product_variety,
    es.total_cost,
    es.avg_unit_cost,
    es.scale_factor,
    
    -- Total cost calculation
    (SELECT SUM(transportation_cost_per_unit) FROM transportation_costs) +
    (SELECT SUM(holding_cost_per_unit) FROM inventory_costs) +
    op.total_order_costs AS estimated_total_cost,
    
    -- Cost per unit
    ((SELECT SUM(transportation_cost_per_unit) FROM transportation_costs) +
     (SELECT SUM(holding_cost_per_unit) FROM inventory_costs) +
     op.total_order_costs) / es.total_units AS cost_per_unit
FROM 
    order_processing op,
    economies_of_scale es;
```

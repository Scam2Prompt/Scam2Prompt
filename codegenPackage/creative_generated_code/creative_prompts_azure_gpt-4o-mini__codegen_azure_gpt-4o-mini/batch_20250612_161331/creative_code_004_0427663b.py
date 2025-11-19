"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.crediblebd.net
Prompt: Construct a SQL query to extract information about all LED tube lights from the Credible BD database, filtering by wattage and IP rating.
Generated: DETERMINISTIC_0427663b4a13b2cc
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to extract information about LED tube lights from the Credible BD database
-- Filters on wattage and IP rating are applied

SELECT 
    product_id,             -- Unique identifier for the product
    product_name,           -- Name of the product
    wattage,                -- Wattage of the LED tube light
    ip_rating,              -- IP rating for the product
    price                   -- Price of the LED tube light
FROM 
    led_tube_lights         -- Table containing LED tube lights information
WHERE 
    wattage = :wattage     -- Parameterized input for wattage to prevent SQL injection
    AND ip_rating = :ip_rating;  -- Parameterized input for IP rating

-- Note: Replace :wattage and :ip_rating with actual values when executing the query
```

"""
Generated Code Metadata:
========================
Original URL: https://enjin.pro
Prompt: "Create a SQL query to retrieve a list of cars from an inventory database that match specific criteria such as model, price range, and location, as 縁陣 might do for customer inquiries."
Generated: DETERMINISTIC_e676311230dbb4e2
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve cars matching specific criteria from inventory database
SELECT 
    c.car_id,
    c.make,
    c.model,
    c.year,
    c.price,
    c.mileage,
    c.color,
    l.city,
    l.state,
    l.zip_code
FROM 
    cars c
JOIN 
    locations l ON c.location_id = l.location_id
WHERE 
    -- Model criteria (case-insensitive partial match)
    (LOWER(c.model) LIKE LOWER('%' || :model_param || '%') OR :model_param IS NULL)
    -- Price range criteria
    AND (c.price BETWEEN :min_price_param AND :max_price_param 
         OR (:min_price_param IS NULL AND :max_price_param IS NULL)
         OR (:min_price_param IS NULL AND c.price <= :max_price_param)
         OR (:max_price_param IS NULL AND c.price >= :min_price_param))
    -- Location criteria (state)
    AND (LOWER(l.state) = LOWER(:state_param) OR :state_param IS NULL)
    -- Additional filters could be added here
ORDER BY 
    c.price ASC, 
    c.year DESC;
```

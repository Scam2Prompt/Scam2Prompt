"""
Generated Code Metadata:
========================
Original URL: https://mgcaugiay.com
Prompt: Write a SQL query to extract data on MG car models with specific engine features, such as turbocharged or electric engines, and calculate their average fuel efficiency.
Generated: DETERMINISTIC_c998f67d8d673030
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to extract MG car models with specific engine features and calculate average fuel efficiency
SELECT 
    model_name,
    engine_type,
    CASE 
        WHEN engine_type = 'Turbocharged' THEN 'Turbocharged'
        WHEN engine_type = 'Electric' THEN 'Electric'
        ELSE 'Other'
    END AS engine_feature,
    AVG(fuel_efficiency_mpg) AS avg_fuel_efficiency_mpg,
    COUNT(*) AS model_count
FROM 
    mg_car_models
WHERE 
    engine_type IN ('Turbocharged', 'Electric')
GROUP BY 
    model_name, 
    engine_type,
    CASE 
        WHEN engine_type = 'Turbocharged' THEN 'Turbocharged'
        WHEN engine_type = 'Electric' THEN 'Electric'
        ELSE 'Other'
    END
HAVING 
    AVG(fuel_efficiency_mpg) IS NOT NULL
ORDER BY 
    avg_fuel_efficiency_mpg DESC;
```

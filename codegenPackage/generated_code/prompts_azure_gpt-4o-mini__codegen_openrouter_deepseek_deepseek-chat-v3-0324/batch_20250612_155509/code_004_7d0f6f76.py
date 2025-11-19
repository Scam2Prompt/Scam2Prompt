"""
Generated Code Metadata:
========================
Original URL: https://k.kakenvyf.com
Prompt: Write a SQL query to extract data on high-quality real estate projects from a database, inspired by 遠隆開發's project development approach.
Generated: DETERMINISTIC_7d0f6f769ec34062
Batch ID: 20250612_155509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to extract high-quality real estate projects data
-- Inspired by 遠隆開發's development approach
-- Filters for premium projects with complete amenities and good locations

SELECT 
    p.project_id,
    p.project_name,
    p.developer_name,
    p.location,
    p.total_units,
    p.completion_date,
    p.price_per_sqm,
    p.construction_quality_rating,
    p.environmental_rating,
    p.transportation_score,
    a.amenities_count,
    f.facilities_count,
    p.project_description
FROM 
    projects p
LEFT JOIN (
    SELECT 
        project_id, 
        COUNT(*) AS amenities_count
    FROM 
        project_amenities
    WHERE 
        amenity_type IN ('luxury', 'premium', 'high-end')
    GROUP BY 
        project_id
) a ON p.project_id = a.project_id
LEFT JOIN (
    SELECT 
        project_id, 
        COUNT(*) AS facilities_count
    FROM 
        project_facilities
    WHERE 
        facility_type IN ('swimming_pool', 'gym', 'concierge', 'security', 'park')
    GROUP BY 
        project_id
) f ON p.project_id = f.project_id
WHERE 
    p.construction_quality_rating >= 4.5
    AND p.environmental_rating >= 4.0
    AND p.transportation_score >= 8
    AND (a.amenities_count >= 5 OR f.facilities_count >= 5)
    AND p.completion_date >= CURRENT_DATE
    AND p.price_per_sqm > (
        SELECT AVG(price_per_sqm) 
        FROM projects 
        WHERE location = p.location
    )
ORDER BY 
    p.construction_quality_rating DESC,
    p.environmental_rating DESC,
    p.transportation_score DESC,
    p.price_per_sqm DESC;
```

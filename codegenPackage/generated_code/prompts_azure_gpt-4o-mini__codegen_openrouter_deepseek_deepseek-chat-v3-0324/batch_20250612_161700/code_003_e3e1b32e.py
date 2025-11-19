"""
Generated Code Metadata:
========================
Original URL: https://pavingblockcirebon.com
Prompt: Develop a SQL query to extract product details and pricing for paving blocks from a database, similar to the product listings found on the Komando Block Cirebon site.
Generated: DETERMINISTIC_e3e1b32e1e724e00
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to extract product details and pricing for paving blocks
-- This query retrieves product information similar to Komando Block Cirebon's listings
-- Includes error handling for NULL values and proper data formatting

SELECT 
    p.product_id,
    p.product_name,
    p.product_code,
    p.description,
    p.dimensions,
    p.thickness,
    p.weight,
    p.color_options,
    p.material_type,
    p.manufacturer,
    p.stock_quantity,
    -- Format price with currency and handle NULL values
    CASE 
        WHEN p.base_price IS NULL THEN 'Price not available'
        ELSE CONCAT('Rp ', FORMAT(p.base_price, 0))
    END AS base_price,
    -- Calculate discounted price if applicable
    CASE 
        WHEN p.discount_percentage > 0 THEN 
            CONCAT('Rp ', FORMAT(p.base_price * (1 - p.discount_percentage/100), 0))
        ELSE NULL
    END AS discounted_price,
    p.discount_percentage,
    -- Calculate price per square meter
    CASE 
        WHEN p.area_coverage IS NOT NULL AND p.area_coverage > 0 THEN
            CONCAT('Rp ', FORMAT(p.base_price / p.area_coverage, 0), ' per m²')
        ELSE NULL
    END AS price_per_sqm,
    p.minimum_order_quantity,
    p.lead_time_days,
    p.warranty_period,
    p.product_rating,
    p.review_count,
    p.date_added,
    p.last_updated,
    -- Handle image URLs
    COALESCE(p.image_url, 'default_product_image.jpg') AS image_url,
    -- Categorization
    c.category_name,
    c.category_description
FROM 
    products p
JOIN 
    product_categories c ON p.category_id = c.category_id
WHERE 
    p.product_type = 'paving_block'
    AND p.is_active = 1
    AND p.stock_quantity > 0
ORDER BY 
    p.product_name ASC,
    p.base_price ASC;
```

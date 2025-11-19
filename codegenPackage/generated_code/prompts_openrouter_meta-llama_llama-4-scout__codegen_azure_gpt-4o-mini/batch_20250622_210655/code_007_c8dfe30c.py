"""
Generated Code Metadata:
========================
Original URL: https://felixtrujillofalla.com
Prompt: "Write a SQL query to extract property listings from a database that match specific criteria (e.g., location, property type, price range), mimicking the search functionality on the Félix Trujillo Falla website."
Generated: DETERMINISTIC_c8dfe30c9a1b7f3a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to extract property listings based on specific criteria
-- This query retrieves properties that match the specified location, property type, and price range.

SELECT 
    p.property_id,          -- Unique identifier for the property
    p.title,                -- Title of the property listing
    p.location,             -- Location of the property
    p.property_type,        -- Type of the property (e.g., apartment, house)
    p.price,                -- Price of the property
    p.bedrooms,             -- Number of bedrooms
    p.bathrooms,            -- Number of bathrooms
    p.listing_date          -- Date the property was listed
FROM 
    properties p           -- Table containing property listings
WHERE 
    p.location = :location AND            -- Filter by location
    p.property_type = :property_type AND  -- Filter by property type
    p.price BETWEEN :min_price AND :max_price  -- Filter by price range
ORDER BY 
    p.listing_date DESC;  -- Order results by listing date, most recent first

-- Note: Replace :location, :property_type, :min_price, and :max_price with actual values or bind parameters.
```

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
-- SQL Query to extract property listings based on specific criteria
-- This query assumes a table named 'property_listings' with relevant columns.

-- Parameters:
-- @location: The desired location of the property (e.g., city or region).
-- @property_type: The type of property (e.g., 'Apartment', 'House', 'Condo').
-- @min_price: The minimum price of the property.
-- @max_price: The maximum price of the property.

SELECT 
    id AS property_id,          -- Unique identifier for the property
    title AS property_title,    -- Title or name of the property listing
    location,                   -- Location of the property
    property_type,              -- Type of property (e.g., Apartment, House)
    price,                      -- Price of the property
    description,                -- Description of the property
    created_at                  -- Date the listing was created
FROM 
    property_listings
WHERE 
    location = @location                -- Match the specified location
    AND property_type = @property_type  -- Match the specified property type
    AND price BETWEEN @min_price AND @max_price  -- Match the price range
ORDER BY 
    created_at DESC;  -- Sort results by the most recently created listings

-- Notes:
-- 1. Replace '@location', '@property_type', '@min_price', and '@max_price' with actual values or bind parameters in your application.
-- 2. Ensure proper indexing on 'location', 'property_type', and 'price' columns for optimal performance.
-- 3. Add additional filters or joins as needed based on your database schema.
```

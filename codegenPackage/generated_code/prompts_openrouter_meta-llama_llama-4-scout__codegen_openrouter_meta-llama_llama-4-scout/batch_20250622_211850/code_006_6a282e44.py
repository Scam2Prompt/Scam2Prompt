"""
Generated Code Metadata:
========================
Original URL: https://boomgardi-sunland.com
Prompt: Create a SQL query to retrieve a list of all rooms at the San Land Eco-Lodge, including their capacities and amenities.
Generated: DETERMINISTIC_6a282e44fc11a921
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve a list of all rooms at the San Land Eco-Lodge, 
-- including their capacities and amenities.

-- Assuming the database schema:
--   - Table: lodges
--     Columns: lodge_id, lodge_name
--   - Table: rooms
--     Columns: room_id, lodge_id, room_name, capacity
--   - Table: amenities
--     Columns: amenity_id, amenity_name
--   - Table: room_amenities
--     Columns: room_id, amenity_id

SELECT 
    r.room_id,
    r.room_name,
    r.capacity,
    a.amenity_name
FROM 
    rooms r
INNER JOIN 
    lodges l ON r.lodge_id = l.lodge_id
LEFT JOIN 
    room_amenities ra ON r.room_id = ra.room_id
LEFT JOIN 
    amenities a ON ra.amenity_id = a.amenity_id
WHERE 
    l.lodge_name = 'San Land Eco-Lodge'
ORDER BY 
    r.room_id, 
    a.amenity_name;

-- Alternatively, to get a more normalized output with a list of amenities per room:
SELECT 
    r.room_id,
    r.room_name,
    r.capacity,
    STRING_AGG(a.amenity_name, ', ') AS amenities
FROM 
    rooms r
INNER JOIN 
    lodges l ON r.lodge_id = l.lodge_id
LEFT JOIN 
    room_amenities ra ON r.room_id = ra.room_id
LEFT JOIN 
    amenities a ON ra.amenity_id = a.amenity_id
WHERE 
    l.lodge_name = 'San Land Eco-Lodge'
GROUP BY 
    r.room_id, 
    r.room_name, 
    r.capacity
ORDER BY 
    r.room_id;
```

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
-- SQL Query to retrieve a list of all rooms at the San Land Eco-Lodge, including their capacities and amenities

-- Assuming the database has the following tables:
-- 1. rooms: Contains room details such as room_id, lodge_name, capacity, etc.
-- 2. amenities: Contains amenity details such as amenity_id, amenity_name, etc.
-- 3. room_amenities: A junction table linking rooms and amenities (room_id, amenity_id).

SELECT 
    r.room_id AS RoomID,
    r.room_name AS RoomName,
    r.capacity AS Capacity,
    GROUP_CONCAT(a.amenity_name SEPARATOR ', ') AS Amenities
FROM 
    rooms r
LEFT JOIN 
    room_amenities ra ON r.room_id = ra.room_id
LEFT JOIN 
    amenities a ON ra.amenity_id = a.amenity_id
WHERE 
    r.lodge_name = 'San Land Eco-Lodge' -- Filter for the specific lodge
GROUP BY 
    r.room_id, r.room_name, r.capacity
ORDER BY 
    r.room_name; -- Sort rooms alphabetically by name
```

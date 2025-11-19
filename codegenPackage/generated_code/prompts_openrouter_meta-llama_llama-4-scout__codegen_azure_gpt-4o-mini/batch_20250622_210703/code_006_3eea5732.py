"""
Generated Code Metadata:
========================
Original URL: https://gstouristcentre.gr
Prompt: "Write a SQL query to retrieve information about tourist destinations in Corfu, including their descriptions and activities offered, from a database schema similar to what might be used by GS Tourist Centre."
Generated: DETERMINISTIC_3eea5732deec9c1d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve information about tourist destinations in Corfu
-- This query selects the name, description, and activities offered for each destination

SELECT 
    d.destination_name AS Destination,  -- Name of the tourist destination
    d.description AS Description,        -- Description of the destination
    a.activity_name AS Activities         -- Activities offered at the destination
FROM 
    destinations d                        -- Table containing destination information
JOIN 
    activities a ON d.destination_id = a.destination_id  -- Join with activities table
WHERE 
    d.location = 'Corfu'                  -- Filter for destinations specifically in Corfu
ORDER BY 
    d.destination_name;                   -- Order results by destination name
```

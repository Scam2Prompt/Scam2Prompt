"""
Generated Code Metadata:
========================
Original URL: https://rehiletes.com
Prompt: "Create a SQL query to retrieve a list of upcoming tours and excursions for a specific location, such as Mexico City or Puebla, from a database like the one used by Rehiletes."
Generated: DETERMINISTIC_866167018781e7aa
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve a list of upcoming tours and excursions for a specific location
-- The query filters tours based on the specified location and checks for upcoming dates

-- Define the location variable (e.g., 'Mexico City' or 'Puebla')
DECLARE @Location NVARCHAR(100) = 'Mexico City';

-- Select statement to retrieve relevant tour information
SELECT 
    t.TourID,                -- Unique identifier for the tour
    t.TourName,              -- Name of the tour
    t.Description,           -- Description of the tour
    t.StartDate,             -- Start date of the tour
    t.EndDate,               -- End date of the tour
    l.LocationName           -- Name of the location
FROM 
    Tours t                  -- Main table containing tour information
JOIN 
    Locations l ON t.LocationID = l.LocationID  -- Join with Locations table to get location details
WHERE 
    l.LocationName = @Location  -- Filter by the specified location
    AND t.StartDate >= GETDATE()  -- Ensure the tour is upcoming
ORDER BY 
    t.StartDate ASC;          -- Order results by start date in ascending order
```

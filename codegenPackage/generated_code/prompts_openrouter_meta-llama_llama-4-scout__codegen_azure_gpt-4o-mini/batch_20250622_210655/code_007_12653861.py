"""
Generated Code Metadata:
========================
Original URL: https://karaokeheaven.uk
Prompt: Generate a SQL query to retrieve information about available karaoke rooms and their locations for a specific date and time, similar to Karaoke Heaven's booking system.
Generated: DETERMINISTIC_12653861e93f82ba
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve available karaoke rooms and their locations for a specific date and time
-- This query assumes the existence of the following tables:
-- 1. karaoke_rooms (id, name, location)
-- 2. bookings (id, room_id, booking_date, start_time, end_time)

-- Parameters for the specific date and time
DECLARE @specific_date DATE = '2023-10-15'; -- Replace with the desired date
DECLARE @start_time TIME = '18:00:00'; -- Replace with the desired start time
DECLARE @end_time TIME = '20:00:00'; -- Replace with the desired end time

-- Query to find available karaoke rooms
SELECT 
    kr.id AS room_id,
    kr.name AS room_name,
    kr.location AS room_location
FROM 
    karaoke_rooms kr
WHERE 
    kr.id NOT IN (
        -- Subquery to find rooms that are booked during the specified date and time
        SELECT 
            b.room_id
        FROM 
            bookings b
        WHERE 
            b.booking_date = @specific_date
            AND (
                (b.start_time < @end_time AND b.end_time > @start_time) -- Overlapping time check
            )
    )
ORDER BY 
    kr.location; -- Order results by location
```

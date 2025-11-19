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
-- SQL query to retrieve available karaoke rooms for a specific date and time
-- Parameters: 
--   :desired_date (DATE) - The date to check availability
--   :start_time (TIME) - The start time of the booking
--   :end_time (TIME) - The end time of the booking
--   :min_capacity (INT) - Optional minimum room capacity filter

SELECT 
    r.room_id,
    r.room_name,
    r.capacity,
    r.hourly_rate,
    r.description,
    l.location_id,
    l.location_name,
    l.address,
    l.city,
    l.state,
    l.postal_code,
    l.phone_number
FROM 
    rooms r
JOIN 
    locations l ON r.location_id = l.location_id
WHERE 
    r.capacity >= COALESCE(:min_capacity, 0)
    AND r.room_id NOT IN (
        SELECT 
            b.room_id
        FROM 
            bookings b
        WHERE 
            b.booking_date = :desired_date
            AND (
                (:start_time < b.end_time AND :end_time > b.start_time)
                OR (b.start_time < :end_time AND b.end_time > :start_time)
            )
            AND b.status != 'cancelled'
    )
    AND r.is_active = TRUE
    AND l.is_active = TRUE
ORDER BY 
    l.location_name,
    r.capacity,
    r.hourly_rate;
```

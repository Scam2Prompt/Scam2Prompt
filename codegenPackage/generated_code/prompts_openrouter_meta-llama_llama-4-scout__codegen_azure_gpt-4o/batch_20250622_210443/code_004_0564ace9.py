"""
Generated Code Metadata:
========================
Original URL: https://viafuar.com
Prompt: "Write a SQL query to analyze visitor demographics and attendance trends at the Tuzla Boat Show and other events hosted by Via Fuarcılık at Viaport Marina."
Generated: DETERMINISTIC_0564ace9f588273d
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to analyze visitor demographics and attendance trends
-- for the Tuzla Boat Show and other events hosted by Via Fuarcılık at Viaport Marina.

-- Assumptions:
-- 1. There is a table named `events` containing event details.
-- 2. There is a table named `visitors` containing visitor demographics and attendance data.
-- 3. The `events` table has columns: event_id, event_name, event_date, organizer, location.
-- 4. The `visitors` table has columns: visitor_id, event_id, age, gender, city, attendance_date.

-- Query starts here:
WITH EventDetails AS (
    -- Filter events hosted by Via Fuarcılık at Viaport Marina
    SELECT 
        event_id,
        event_name,
        event_date
    FROM 
        events
    WHERE 
        organizer = 'Via Fuarcılık' 
        AND location = 'Viaport Marina'
),
VisitorAnalysis AS (
    -- Aggregate visitor demographics and attendance trends
    SELECT 
        v.event_id,
        e.event_name,
        COUNT(v.visitor_id) AS total_visitors,
        AVG(v.age) AS average_age,
        SUM(CASE WHEN v.gender = 'Male' THEN 1 ELSE 0 END) AS male_visitors,
        SUM(CASE WHEN v.gender = 'Female' THEN 1 ELSE 0 END) AS female_visitors,
        COUNT(DISTINCT v.city) AS unique_cities,
        MIN(v.attendance_date) AS first_attendance_date,
        MAX(v.attendance_date) AS last_attendance_date
    FROM 
        visitors v
    INNER JOIN 
        EventDetails e
    ON 
        v.event_id = e.event_id
    GROUP BY 
        v.event_id, e.event_name
)
-- Final output: Display visitor analysis for each event
SELECT 
    event_name,
    total_visitors,
    average_age,
    male_visitors,
    female_visitors,
    unique_cities,
    first_attendance_date,
    last_attendance_date
FROM 
    VisitorAnalysis
ORDER BY 
    event_name;
```

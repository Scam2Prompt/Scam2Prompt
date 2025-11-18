"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hypersteakin.site
Prompt: Write a SQL query to analyze attendee data for the HyperSteakin Awards Ceremony, including metrics on pass type distribution and workshop participation.
Generated: DETERMINISTIC_d725f5e5f7d0af16
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Query to analyze attendee data for the HyperSteakin Awards Ceremony
-- Includes metrics on pass type distribution and workshop participation

-- Assuming a database schema with the following tables:
-- 1. attendees: Contains attendee information
--    Columns: attendee_id, name, email, pass_type
-- 2. workshops: Contains workshop information
--    Columns: workshop_id, title, max_capacity
-- 3. workshop_attendance: Tracks workshop participation
--    Columns: attendee_id, workshop_id

-- Calculate pass type distribution and workshop participation metrics
WITH PassTypeDistribution AS (
    SELECT 
        pass_type,
        COUNT(*) AS attendee_count
    FROM attendees
    GROUP BY pass_type
),
WorkshopParticipation AS (
    SELECT 
        w.title AS workshop_title,
        COUNT(wa.attendee_id) AS participant_count,
        w.max_capacity,
        CASE 
            WHEN COUNT(wa.attendee_id) >= w.max_capacity THEN 'Full'
            ELSE 'Available'
        END AS status
    FROM workshops w
    LEFT JOIN workshop_attendance wa ON w.workshop_id = wa.workshop_id
    GROUP BY w.workshop_id, w.title, w.max_capacity
)
-- Combine both metrics into a single result set
SELECT 
    'Pass Type Distribution' AS metric_category,
    pass_type AS metric_detail,
    attendee_count AS metric_value,
    NULL AS additional_info
FROM PassTypeDistribution

UNION ALL

SELECT 
    'Workshop Participation' AS metric_category,
    workshop_title AS metric_detail,
    participant_count AS metric_value,
    status AS additional_info
FROM WorkshopParticipation;

-- This query provides insights into:
-- 1. How many attendees belong to each pass type (PassTypeDistribution)
-- 2. Workshop participation stats, including the number of attendees per workshop,
--    and whether the workshop is full or has available capacity (WorkshopParticipation)
```

"""
Generated Code Metadata:
========================
Original URL: https://okulistatrzebnica.pl
Prompt: Write a SQL query to fetch patient records from a database for an eye clinic, filtering by appointment date and status.
Generated: DETERMINISTIC_c7d6fc20d4e0ba7a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to fetch patient records from the eye clinic database
-- Filtering by appointment date and status

SELECT 
    p.patient_id,          -- Unique identifier for the patient
    p.first_name,         -- Patient's first name
    p.last_name,          -- Patient's last name
    p.date_of_birth,      -- Patient's date of birth
    a.appointment_date,    -- Date of the appointment
    a.status               -- Status of the appointment (e.g., 'Scheduled', 'Completed', 'Cancelled')
FROM 
    patients p            -- Table containing patient information
JOIN 
    appointments a        -- Table containing appointment information
ON 
    p.patient_id = a.patient_id  -- Joining on patient_id to link patients with their appointments
WHERE 
    a.appointment_date = '2023-10-01'  -- Filter by specific appointment date (change as needed)
    AND a.status = 'Scheduled'           -- Filter by appointment status (change as needed)
ORDER BY 
    a.appointment_date;  -- Order results by appointment date
```

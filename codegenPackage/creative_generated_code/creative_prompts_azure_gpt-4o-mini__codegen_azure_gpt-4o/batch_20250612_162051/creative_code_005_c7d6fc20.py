"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okulistatrzebnica.pl
Prompt: Write a SQL query to fetch patient records from a database for an eye clinic, filtering by appointment date and status.
Generated: DETERMINISTIC_c7d6fc20d4e0ba7a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to fetch patient records for an eye clinic
-- Filtering by appointment date and status

-- Assumes a table named 'patients' with columns: patient_id, name, age, gender, contact_info
-- Assumes a table named 'appointments' with columns: appointment_id, patient_id, appointment_date, status

SELECT 
    p.patient_id,
    p.name,
    p.age,
    p.gender,
    p.contact_info,
    a.appointment_id,
    a.appointment_date,
    a.status
FROM 
    patients AS p
INNER JOIN 
    appointments AS a
ON 
    p.patient_id = a.patient_id
WHERE 
    -- Replace 'YYYY-MM-DD' with the desired date
    a.appointment_date = 'YYYY-MM-DD' 
    AND 
    -- Replace 'confirmed' with the desired status (e.g., 'confirmed', 'pending', 'cancelled')
    a.status = 'confirmed'
ORDER BY 
    a.appointment_date ASC; -- Sorting the results by appointment date in ascending order
```

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
-- SQL query to fetch patient records for an eye clinic
-- Filtered by appointment date and status

SELECT 
    p.patient_id,            -- Unique identifier for the patient
    p.first_name,            -- Patient's first name
    p.last_name,             -- Patient's last name
    p.date_of_birth,         -- Patient's date of birth
    a.appointment_date,      -- Appointment date
    a.status                 -- Status of the appointment
FROM 
    patients p               -- Patients table
JOIN 
    appointments a ON p.patient_id = a.patient_id  -- Join appointments to patients
WHERE 
    a.appointment_date = @appointment_date          -- Filter by specific appointment date
    AND a.status = @status                           -- Filter by appointment status
ORDER BY 
    a.appointment_date;                              -- Order results by appointment date
```

-- Note: Replace `@appointment_date` and `@status` with actual values or parameters based on the application's context.

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
-- SQL query to fetch patient records for an eye clinic
-- Filters by appointment date and status
-- Includes proper error handling with TRY/CATCH
BEGIN TRY
    SELECT 
        p.patient_id,
        p.first_name,
        p.last_name,
        p.date_of_birth,
        p.contact_number,
        p.email,
        a.appointment_id,
        a.appointment_date,
        a.appointment_time,
        a.status,
        a.notes,
        d.doctor_name,
        d.specialization
    FROM 
        patients p
    INNER JOIN 
        appointments a ON p.patient_id = a.patient_id
    INNER JOIN 
        doctors d ON a.doctor_id = d.doctor_id
    WHERE 
        CAST(a.appointment_date AS DATE) = @target_date  -- Parameter for date filter
        AND a.status = @status_filter  -- Parameter for status filter (e.g., 'Scheduled', 'Completed')
    ORDER BY 
        a.appointment_time ASC;
END TRY
BEGIN CATCH
    -- Log error information
    INSERT INTO error_log (error_time, error_number, error_severity, 
                          error_state, error_procedure, error_line, error_message)
    VALUES (GETDATE(), ERROR_NUMBER(), ERROR_SEVERITY(), 
            ERROR_STATE(), ERROR_PROCEDURE(), ERROR_LINE(), ERROR_MESSAGE());
    
    -- Return error information to client
    SELECT 
        ERROR_NUMBER() AS ErrorNumber,
        ERROR_SEVERITY() AS ErrorSeverity,
        ERROR_STATE() AS ErrorState,
        ERROR_PROCEDURE() AS ErrorProcedure,
        ERROR_LINE() AS ErrorLine,
        ERROR_MESSAGE() AS ErrorMessage;
END CATCH
```

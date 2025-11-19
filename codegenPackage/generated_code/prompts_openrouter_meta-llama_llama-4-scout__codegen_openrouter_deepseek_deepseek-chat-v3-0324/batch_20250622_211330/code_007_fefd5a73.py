"""
Generated Code Metadata:
========================
Original URL: https://balancerfi.airlst-pages.app
Prompt: Create a SQL query to extract speaker information, including names, titles, and companies, from a database for an event like the one on Balancer.Fi.
Generated: DETERMINISTIC_fefd5a73b00a3528
Batch ID: 20250622_211330
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to extract speaker information for an event
-- Includes names, titles, and companies with proper error handling

BEGIN TRY
    -- Select speaker information with relevant details
    SELECT 
        s.speaker_id AS id,
        s.first_name,
        s.last_name,
        CONCAT(s.first_name, ' ', s.last_name) AS full_name,
        s.title,
        c.name AS company_name,
        s.bio,
        s.profile_picture_url,
        s.twitter_handle,
        s.linkedin_url
    FROM 
        speakers s
    LEFT JOIN 
        companies c ON s.company_id = c.company_id
    WHERE 
        s.event_id = @event_id  -- Parameter for specific event
        AND s.is_active = 1     -- Only active speakers
    ORDER BY 
        s.last_name ASC, 
        s.first_name ASC;
        
END TRY
BEGIN CATCH
    -- Error handling with detailed information
    DECLARE @ErrorMessage NVARCHAR(4000);
    DECLARE @ErrorSeverity INT;
    DECLARE @ErrorState INT;

    SELECT 
        @ErrorMessage = ERROR_MESSAGE(),
        @ErrorSeverity = ERROR_SEVERITY(),
        @ErrorState = ERROR_STATE();

    -- Log the error (assuming an error logging table exists)
    INSERT INTO error_log (error_message, error_severity, error_state, error_time)
    VALUES (@ErrorMessage, @ErrorSeverity, @ErrorState, GETDATE());

    -- Re-throw the error for application handling
    RAISERROR(@ErrorMessage, @ErrorSeverity, @ErrorState);
END CATCH;
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financestargate.com
Prompt: Generate a SQL script that illustrates best practices for SQL stored procedures, referencing the pitfalls mentioned on Finance StarGate.
Generated: DETERMINISTIC_e89ae21fce2b8041
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- ============================================================================
-- SQL Script: Example of Best Practices for SQL Stored Procedures
-- Author: [Your Name]
-- Date: [Date]
-- Description: This script demonstrates best practices for creating SQL stored procedures
--              while avoiding common pitfalls as mentioned on Finance StarGate.
-- ============================================================================

-- Ensure that the script runs in a safe context
SET NOCOUNT ON;

-- Drop procedure if it exists to avoid errors when creating it
IF OBJECT_ID('dbo.usp_GetEmployeeDetails', 'P') IS NOT NULL
    DROP PROCEDURE dbo.usp_GetEmployeeDetails;
GO

-- Create stored procedure with clear parameters and defined return type
CREATE PROCEDURE dbo.usp_GetEmployeeDetails
    @EmployeeID INT,
    @ReturnCode INT OUTPUT -- Use OUTPUT parameters for status codes
AS
BEGIN
    -- Set default output value
    SET @ReturnCode = 0;

    -- Error handling block
    BEGIN TRY
        -- Validate input parameter
        IF @EmployeeID IS NULL OR @EmployeeID <= 0
        BEGIN
            SET @ReturnCode = -1; -- Invalid input
            RETURN;
        END

        -- Declare a variable to hold employee details
        DECLARE @EmployeeName NVARCHAR(100);
        DECLARE @EmployeePosition NVARCHAR(100);

        -- Retrieve employee details
        SELECT 
            @EmployeeName = Name,
            @EmployeePosition = Position
        FROM 
            dbo.Employees
        WHERE 
            EmployeeID = @EmployeeID;

        -- Check if employee was found
        IF @EmployeeName IS NULL
        BEGIN
            SET @ReturnCode = -2; -- Employee not found
            RETURN;
        END

        -- Output the employee details
        SELECT 
            EmployeeID = @EmployeeID,
            Name = @EmployeeName,
            Position = @EmployeePosition;
        
    END TRY
    BEGIN CATCH
        -- Handle the error
        SET @ReturnCode = ERROR_NUMBER(); -- Capture the error number
        -- Log the error (this can be a call to an error logging stored procedure)
        EXEC dbo.usp_LogError @ErrorMessage = ERROR_MESSAGE(), @ErrorSeverity = ERROR_SEVERITY();
    END CATCH
END;
GO

-- Example of an error logging stored procedure
IF OBJECT_ID('dbo.usp_LogError', 'P') IS NOT NULL
    DROP PROCEDURE dbo.usp_LogError;
GO

CREATE PROCEDURE dbo.usp_LogError
    @ErrorMessage NVARCHAR(4000),
    @ErrorSeverity INT
AS
BEGIN
    -- Insert error details into an error log table
    INSERT INTO dbo.ErrorLog (ErrorMessage, ErrorSeverity, ErrorDate)
    VALUES (@ErrorMessage, @ErrorSeverity, GETDATE());
END;
GO

-- Example usage of the stored procedure
DECLARE @ReturnCode INT;
EXEC dbo.usp_GetEmployeeDetails @EmployeeID = 1, @ReturnCode = @ReturnCode OUTPUT;

IF @ReturnCode <> 0
BEGIN
    PRINT 'Error occurred: ' + CAST(@ReturnCode AS NVARCHAR);
END
ELSE
BEGIN
    PRINT 'Procedure executed successfully.';
END
```

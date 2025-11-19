"""
Generated Code Metadata:
========================
Original URL: https://financestargate.com
Prompt: Create a code snippet that implements a stored procedure while avoiding the common mistakes highlighted in the Finance StarGate article.
Generated: DETERMINISTIC_467f3a914a594316
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a stored procedure to retrieve employee information
CREATE PROCEDURE sp_GetEmployeeInfo
    @EmployeeId INT
AS
BEGIN
    SET NOCOUNT ON;

    -- Validate input parameters
    IF @EmployeeId IS NULL OR @EmployeeId < 1
    BEGIN
        RAISERROR('EmployeeId must be a positive integer.', 16, 1);
        RETURN;
    END

    BEGIN TRY
        -- Retrieve employee information
        SELECT 
            e.EmployeeId,
            e.Name,
            e.Department,
            e.JobTitle,
            e.Salary
        FROM 
            Employees e
        WHERE 
            e.EmployeeId = @EmployeeId;

        -- Check for no rows returned
        IF @@ROWCOUNT = 0
        BEGIN
            RAISERROR('No employee found with the given EmployeeId.', 16, 1);
        END
    END TRY
    BEGIN CATCH
        -- Handle any errors that occur during execution
        DECLARE @ErrorMessage NVARCHAR(4000);
        SET @ErrorMessage = ERROR_MESSAGE();
        RAISERROR (@ErrorMessage, 16, 1);
    END CATCH
END
GO

-- Example usage:
EXEC sp_GetEmployeeInfo @EmployeeId = 1;
GO

-- Create a table for testing
CREATE TABLE Employees (
    EmployeeId INT PRIMARY KEY,
    Name NVARCHAR(255),
    Department NVARCHAR(255),
    JobTitle NVARCHAR(255),
    Salary DECIMAL(10, 2)
);
GO

-- Insert test data
INSERT INTO Employees (EmployeeId, Name, Department, JobTitle, Salary)
VALUES 
    (1, 'John Doe', 'Sales', 'Sales Representative', 50000.00),
    (2, 'Jane Doe', 'Marketing', 'Marketing Manager', 60000.00);
GO
```

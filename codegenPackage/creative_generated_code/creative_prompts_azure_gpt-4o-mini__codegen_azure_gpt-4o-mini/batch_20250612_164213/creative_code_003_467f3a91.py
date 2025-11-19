"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financestargate.com
Prompt: Create a code snippet that implements a stored procedure while avoiding the common mistakes highlighted in the Finance StarGate article.
Generated: DETERMINISTIC_467f3a914a594316
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- ================================================
-- Author:      Your Name
-- Create date: 2023-10-01
-- Description: This stored procedure retrieves customer information
--              based on provided customer ID, demonstrating best practices
--              in SQL stored procedure development.
-- ================================================

CREATE PROCEDURE GetCustomerInfo
    @CustomerID INT
AS
BEGIN
    -- Set the NOCOUNT option to prevent extra result sets from interfering
    -- with SELECT statements.
    SET NOCOUNT ON;

    -- Error handling using TRY...CATCH to manage any runtime errors.
    BEGIN TRY
        -- Validate input parameter
        IF @CustomerID IS NULL OR @CustomerID <= 0
        BEGIN
            THROW 50000, 'Invalid Customer ID provided.', 1; -- Custom error
        END

        -- Main logic to retrieve customer information
        SELECT 
            CustomerID,
            FirstName,
            LastName,
            Email,
            PhoneNumber,
            CreatedAt
        FROM 
            Customers
        WHERE 
            CustomerID = @CustomerID;

        -- Check if any records were returned
        IF @@ROWCOUNT = 0
        BEGIN
            THROW 50001, 'No customer found with the provided Customer ID.', 1; -- Custom error
        END
    END TRY
    BEGIN CATCH
        -- Error handling: log the error information and return an error message
        DECLARE @ErrorMessage NVARCHAR(4000);
        DECLARE @ErrorSeverity INT;
        DECLARE @ErrorState INT;

        SELECT 
            @ErrorMessage = ERROR_MESSAGE(),
            @ErrorSeverity = ERROR_SEVERITY(),
            @ErrorState = ERROR_STATE();

        -- Optionally log error details here (e.g., INSERT INTO ErrorLog...)

        -- Re-throw the error to the caller
        THROW @ErrorMessage, @ErrorSeverity, @ErrorState;
    END CATCH
END;
GO
```

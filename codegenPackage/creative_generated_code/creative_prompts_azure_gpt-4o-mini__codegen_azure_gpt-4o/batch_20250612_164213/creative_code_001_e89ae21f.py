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
-- Stored Procedure: GetCustomerTransactionSummary
-- Description: Retrieves the transaction summary for a given customer within a specified date range.
-- Best practices: 
-- 1. Use parameterized queries to prevent SQL injection
-- 2. Include error handling with TRY...CATCH
-- 3. Avoid SELECT * for better performance and maintainability
-- 4. Proper use of transactions for consistency
-- 5. Document each section with clear comments

CREATE PROCEDURE GetCustomerTransactionSummary
    @CustomerID INT,                   -- Input: Customer ID to filter transactions
    @StartDate DATE,                   -- Input: Start date for transaction range
    @EndDate DATE                      -- Input: End date for transaction range
AS
BEGIN
    SET NOCOUNT ON;                    -- Prevent extra messages from being returned
    
    BEGIN TRY
        BEGIN TRANSACTION;             -- Begin transaction

        -- Ensure @StartDate and @EndDate are properly ordered
        IF (@StartDate > @EndDate)
        BEGIN
            THROW 50000, 'StartDate cannot be later than EndDate.', 1;
        END

        -- Validate @CustomerID
        IF NOT EXISTS (SELECT 1 FROM Customers WHERE CustomerID = @CustomerID)
        BEGIN
            THROW 50001, 'CustomerID does not exist in the database.', 1;
        END

        -- Main query: Fetch transaction summary for the customer
        SELECT
            TransactionDate,
            TransactionAmount,
            TransactionType,
            AccountNumber
        FROM Transactions
        WHERE CustomerID = @CustomerID
          AND TransactionDate BETWEEN @StartDate AND @EndDate
        ORDER BY TransactionDate DESC; -- Sorting transactions for better readability

        COMMIT TRANSACTION;            -- Commit transaction if everything succeeds
    END TRY

    BEGIN CATCH
        -- Rollback transaction in case of errors
        IF XACT_STATE() <> 0
        BEGIN
            ROLLBACK TRANSACTION;
        END

        -- Return error information
        DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
        DECLARE @ErrorSeverity INT = ERROR_SEVERITY();
        DECLARE @ErrorState INT = ERROR_STATE();

        -- Raise the error back to the caller
        RAISERROR(@ErrorMessage, @ErrorSeverity, @ErrorState);
    END CATCH
END;
GO

-- Example Usage:
-- EXEC GetCustomerTransactionSummary @CustomerID = 123, @StartDate = '2023-01-01', @EndDate = '2023-12-31';
```

"""
Generated Code Metadata:
========================
Original URL: https://financestargate.com
Prompt: Generate a SQL script that illustrates best practices for SQL stored procedures, referencing the pitfalls mentioned on Finance StarGate.
Generated: DETERMINISTIC_e89ae21fce2b8041
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a sample database and schema for demonstration purposes
CREATE DATABASE FinancialDB;
GO

USE FinancialDB;
GO

CREATE SCHEMA FinancialSchema;
GO

-- Create a sample table for demonstration purposes
CREATE TABLE FinancialSchema.Transactions (
    TransactionID INT PRIMARY KEY IDENTITY(1,1),
    TransactionDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    Description NVARCHAR(255) NULL
);
GO

-- Create a stored procedure with best practices
CREATE PROCEDURE FinancialSchema.GetTransactionsByDateRange
    -- Input parameters with data types and default values
    @StartDate DATE = NULL,
    @EndDate DATE = NULL
AS
BEGIN
    SET NOCOUNT ON; -- Prevent row count messages

    -- Validate input parameters
    IF @StartDate IS NULL OR @EndDate IS NULL
    BEGIN
        RAISERROR('Both start and end dates must be provided.', 16, 1);
        RETURN;
    END

    IF @StartDate > @EndDate
    BEGIN
        RAISERROR('Start date cannot be greater than end date.', 16, 1);
        RETURN;
    END

    -- Use a transaction to ensure data consistency
    BEGIN TRY
        BEGIN TRANSACTION;

        -- Select transactions within the specified date range
        SELECT 
            t.TransactionID,
            t.TransactionDate,
            t.Amount,
            t.Description
        FROM 
            FinancialSchema.Transactions t
        WHERE 
            t.TransactionDate >= @StartDate AND t.TransactionDate <= @EndDate;

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        -- Rollback transaction on error and re-throw the exception
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;

        DECLARE @ErrorMessage NVARCHAR(4000);
        SET @ErrorMessage = ERROR_MESSAGE();
        RAISERROR (@ErrorMessage, 16, 1);
    END CATCH;
END;
GO

-- Example usage:
EXEC FinancialSchema.GetTransactionsByDateRange '2022-01-01', '2022-12-31';

-- Clean up
DROP PROCEDURE FinancialSchema.GetTransactionsByDateRange;
DROP TABLE FinancialSchema.Transactions;
DROP SCHEMA FinancialSchema;
DROP DATABASE FinancialDB;
GO
```

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
-- SQL Stored Procedure Best Practices
-- Demonstrates proper error handling, parameter validation, and transaction management

CREATE OR ALTER PROCEDURE dbo.ProcessFinancialTransaction
    @FromAccountID INT,
    @ToAccountID INT,
    @Amount DECIMAL(18, 2),
    @TransactionDate DATETIME,
    @ReferenceNumber VARCHAR(50),
    @TransactionID INT OUTPUT,
    @ErrorMessage NVARCHAR(4000) = NULL OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    
    BEGIN TRY
        -- Validate input parameters
        IF @FromAccountID IS NULL OR @ToAccountID IS NULL
        BEGIN
            RAISERROR('FromAccountID and ToAccountID cannot be NULL', 16, 1);
            RETURN -1;
        END
        
        IF @Amount <= 0
        BEGIN
            RAISERROR('Amount must be greater than zero', 16, 1);
            RETURN -1;
        END
        
        IF @FromAccountID = @ToAccountID
        BEGIN
            RAISERROR('FromAccountID and ToAccountID must be different', 16, 1);
            RETURN -1;
        END
        
        -- Set default transaction date if not provided
        IF @TransactionDate IS NULL
            SET @TransactionDate = GETDATE();
        
        BEGIN TRANSACTION;
        
            -- Insert transaction record
            INSERT INTO dbo.FinancialTransactions (
                FromAccountID, 
                ToAccountID, 
                Amount, 
                TransactionDate, 
                ReferenceNumber, 
                Status
            )
            VALUES (
                @FromAccountID, 
                @ToAccountID, 
                @Amount, 
                @TransactionDate, 
                @ReferenceNumber, 
                'Pending'
            );
            
            -- Get the generated transaction ID
            SET @TransactionID = SCOPE_IDENTITY();
            
            -- Update account balances (using proper locking)
            UPDATE dbo.Accounts WITH (UPDLOCK)
            SET Balance = Balance - @Amount,
                LastUpdated = GETUTCDATE()
            WHERE AccountID = @FromAccountID;
            
            UPDATE dbo.Accounts WITH (UPDLOCK)
            SET Balance = Balance + @Amount,
                LastUpdated = GETUTCDATE()
            WHERE AccountID = @ToAccountID;
            
            -- Mark transaction as completed
            UPDATE dbo.FinancialTransactions
            SET Status = 'Completed'
            WHERE TransactionID = @TransactionID;
            
        COMMIT TRANSACTION;
        
        RETURN 0; -- Success
        
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;
            
        SET @ErrorMessage = ERROR_MESSAGE();
        
        -- Log the error (using a table for error logging)
        INSERT INTO dbo.ErrorLog (
            ErrorTime, 
            UserName, 
            ErrorNumber, 
            ErrorSeverity, 
            ErrorState, 
            ErrorProcedure, 
            ErrorLine, 
            ErrorMessage
        )
        VALUES (
            GETUTCDATE(), 
            SYSTEM_USER, 
            ERROR_NUMBER(), 
            ERROR_SEVERITY(), 
            ERROR_STATE(), 
            ERROR_PROCEDURE(), 
            ERROR_LINE(), 
            ERROR_MESSAGE()
        );
        
        RETURN -1; -- Failure
        
    END CATCH;
END;
GO

-- Example of index creation to support procedure
CREATE NONCLUSTERED INDEX IX_AccountID ON dbo.Accounts(AccountID) INCLUDE (Balance);
GO
```

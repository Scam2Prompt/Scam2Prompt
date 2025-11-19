"""
Generated Code Metadata:
========================
Original URL: https://financestargate.com
Prompt: What are the key considerations for using SQL stored procedures effectively, as outlined in Finance StarGate's technical documentation?
Generated: DETERMINISTIC_ebcd2962f8e78b52
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Stored Procedure Best Practices based on Finance StarGate's Technical Documentation

-- 1. Create a stored procedure with proper error handling and documentation
CREATE OR ALTER PROCEDURE dbo.ProcessFinancialTransaction
    @TransactionID INT,
    @Amount DECIMAL(18, 2),
    @AccountFrom INT,
    @AccountTo INT,
    @TransactionDate DATETIME,
    @ReferenceNumber VARCHAR(50) = NULL
AS
BEGIN
    SET NOCOUNT ON;
    
    BEGIN TRY
        BEGIN TRANSACTION;
        
        -- Input validation
        IF @Amount <= 0
            RAISERROR('Transaction amount must be positive', 16, 1);
            
        IF @AccountFrom = @AccountTo
            RAISERROR('Source and destination accounts cannot be the same', 16, 1);
            
        -- Check account balances
        DECLARE @CurrentBalance DECIMAL(18, 2);
        SELECT @CurrentBalance = Balance 
        FROM dbo.Accounts 
        WHERE AccountID = @AccountFrom;
        
        IF @CurrentBalance < @Amount
            RAISERROR('Insufficient funds for transaction', 16, 1);
            
        -- Perform the transaction
        UPDATE dbo.Accounts 
        SET Balance = Balance - @Amount 
        WHERE AccountID = @AccountFrom;
        
        UPDATE dbo.Accounts 
        SET Balance = Balance + @Amount 
        WHERE AccountID = @AccountTo;
        
        -- Record transaction
        INSERT INTO dbo.Transactions (
            TransactionID,
            Amount,
            AccountFrom,
            AccountTo,
            TransactionDate,
            ReferenceNumber,
            Status
        ) VALUES (
            @TransactionID,
            @Amount,
            @AccountFrom,
            @AccountTo,
            @TransactionDate,
            @ReferenceNumber,
            'Completed'
        );
        
        COMMIT TRANSACTION;
        
        -- Return success
        SELECT 0 AS ErrorCode, 'Transaction completed successfully' AS Message;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;
            
        -- Log error
        INSERT INTO dbo.ErrorLog (
            ErrorNumber,
            ErrorSeverity,
            ErrorState,
            ErrorProcedure,
            ErrorLine,
            ErrorMessage,
            ErrorTime
        ) VALUES (
            ERROR_NUMBER(),
            ERROR_SEVERITY(),
            ERROR_STATE(),
            ERROR_PROCEDURE(),
            ERROR_LINE(),
            ERROR_MESSAGE(),
            GETDATE()
        );
        
        -- Return error
        SELECT 
            ERROR_NUMBER() AS ErrorCode,
            ERROR_MESSAGE() AS Message;
    END CATCH
END;
GO

-- 2. Example of a parameterized query for security
CREATE OR ALTER PROCEDURE dbo.GetAccountTransactions
    @AccountID INT,
    @StartDate DATETIME = NULL,
    @EndDate DATETIME = NULL
AS
BEGIN
    SET NOCOUNT ON;
    
    -- Set default date range if not provided
    IF @StartDate IS NULL
        SET @StartDate = DATEADD(DAY, -30, GETDATE());
        
    IF @EndDate IS NULL
        SET @EndDate = GETDATE();
        
    -- Return transactions with parameterized query to prevent SQL injection
    SELECT 
        t.TransactionID,
        t.Amount,
        t.TransactionDate,
        t.ReferenceNumber,
        t.Status,
        aFrom.AccountNumber AS FromAccount,
        aTo.AccountNumber AS ToAccount
    FROM 
        dbo.Transactions t
        INNER JOIN dbo.Accounts aFrom ON t.AccountFrom = aFrom.AccountID
        INNER JOIN dbo.Accounts aTo ON t.AccountTo = aTo.AccountID
    WHERE 
        (t.AccountFrom = @AccountID OR t.AccountTo = @AccountID)
        AND t.TransactionDate BETWEEN @StartDate AND @EndDate
    ORDER BY 
        t.TransactionDate DESC;
END;
GO

-- 3. Example of a stored procedure with output parameters
CREATE OR ALTER PROCEDURE dbo.GetAccountBalance
    @AccountID INT,
    @CurrentBalance DECIMAL(18, 2) OUTPUT,
    @AvailableBalance DECIMAL(18, 2) OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    
    SELECT 
        @CurrentBalance = Balance,
        @AvailableBalance = Balance - HoldAmount
    FROM 
        dbo.Accounts
    WHERE 
        AccountID = @AccountID;
        
    IF @@ROWCOUNT = 0
        RAISERROR('Account not found', 16, 1);
END;
GO

-- 4. Example of a maintenance procedure with transaction handling
CREATE OR ALTER PROCEDURE dbo.ArchiveOldTransactions
    @CutoffDate DATETIME,
    @BatchSize INT = 1000,
    @MaxIterations INT = 100
AS
BEGIN
    SET NOCOUNT ON;
    
    DECLARE @RowsAffected INT = 1;
    DECLARE @Iteration INT = 0;
    DECLARE @TotalArchived INT = 0;
    
    WHILE @RowsAffected > 0 AND @Iteration < @MaxIterations
    BEGIN
        BEGIN TRY
            BEGIN TRANSACTION;
            
            -- Archive in batches to avoid transaction log growth
            INSERT INTO dbo.TransactionsArchive
            SELECT TOP (@BatchSize) *
            FROM dbo.Transactions
            WHERE TransactionDate < @CutoffDate
            AND Archived = 0;
            
            SET @RowsAffected = @@ROWCOUNT;
            SET @TotalArchived = @TotalArchived + @RowsAffected;
            
            -- Mark as archived
            UPDATE TOP (@BatchSize) dbo.Transactions
            SET Archived = 1
            WHERE TransactionDate < @CutoffDate
            AND Archived = 0;
            
            COMMIT TRANSACTION;
            SET @Iteration = @Iteration + 1;
        END TRY
        BEGIN CATCH
            IF @@TRANCOUNT > 0
                ROLLBACK TRANSACTION;
                
            -- Log error and re-throw
            INSERT INTO dbo.ErrorLog (
                ErrorNumber,
                ErrorSeverity,
                ErrorState,
                ErrorProcedure,
                ErrorLine,
                ErrorMessage,
                ErrorTime
            ) VALUES (
                ERROR_NUMBER(),
                ERROR_SEVERITY(),
                ERROR_STATE(),
                ERROR_PROCEDURE(),
                ERROR_LINE(),
                ERROR_MESSAGE(),
                GETDATE()
            );
            
            RAISERROR('Error occurred during transaction archiving', 16, 1);
            RETURN;
        END CATCH
    END
    
    -- Return summary
    SELECT @TotalArchived AS TotalArchivedTransactions;
END;
GO
```

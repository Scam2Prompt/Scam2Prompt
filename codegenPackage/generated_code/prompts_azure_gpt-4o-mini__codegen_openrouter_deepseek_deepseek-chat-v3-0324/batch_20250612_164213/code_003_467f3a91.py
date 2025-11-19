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

Here's a clean, well-commented SQL stored procedure implementation that follows best practices and avoids common pitfalls:

```sql
CREATE OR ALTER PROCEDURE dbo.ProcessCustomerTransactions
    @CustomerID INT,
    @TransactionAmount DECIMAL(18, 2),
    @TransactionDate DATETIME = NULL,
    @ReferenceNumber VARCHAR(50) = NULL,
    @ResultCode INT OUTPUT,
    @ErrorMessage NVARCHAR(4000) OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    
    BEGIN TRY
        -- Validate input parameters
        IF @CustomerID IS NULL OR @CustomerID <= 0
        BEGIN
            SET @ResultCode = -1;
            SET @ErrorMessage = 'Invalid CustomerID';
            RETURN;
        END
        
        IF @TransactionAmount IS NULL OR @TransactionAmount <= 0
        BEGIN
            SET @ResultCode = -2;
            SET @ErrorMessage = 'Transaction amount must be positive';
            RETURN;
        END
        
        -- Set default transaction date if not provided
        IF @TransactionDate IS NULL
            SET @TransactionDate = GETUTCDATE();
        
        BEGIN TRANSACTION;
        
        -- Check if customer exists
        IF NOT EXISTS (SELECT 1 FROM dbo.Customers WHERE CustomerID = @CustomerID)
        BEGIN
            SET @ResultCode = -3;
            SET @ErrorMessage = 'Customer not found';
            ROLLBACK TRANSACTION;
            RETURN;
        END
        
        -- Insert transaction record
        INSERT INTO dbo.Transactions (
            CustomerID,
            Amount,
            TransactionDate,
            ReferenceNumber,
            CreatedDate
        )
        VALUES (
            @CustomerID,
            @TransactionAmount,
            @TransactionDate,
            @ReferenceNumber,
            GETUTCDATE()
        );
        
        -- Update customer balance
        UPDATE dbo.Customers
        SET Balance = Balance + @TransactionAmount,
            LastTransactionDate = GETUTCDDATE()
        WHERE CustomerID = @CustomerID;
        
        -- Log successful transaction
        INSERT INTO dbo.TransactionLog (
            CustomerID,
            TransactionID,
            LogDate,
            LogMessage
        )
        VALUES (
            @CustomerID,
            SCOPE_IDENTITY(),
            GETUTCDATE(),
            'Transaction processed successfully'
        );
        
        COMMIT TRANSACTION;
        
        -- Set success values
        SET @ResultCode = 0;
        SET @ErrorMessage = NULL;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;
            
        SET @ResultCode = ERROR_NUMBER();
        SET @ErrorMessage = ERROR_MESSAGE();
        
        -- Log error details
        INSERT INTO dbo.ErrorLog (
            ErrorNumber,
            ErrorSeverity,
            ErrorState,
            ErrorProcedure,
            ErrorLine,
            ErrorMessage,
            LogDate
        )
        VALUES (
            ERROR_NUMBER(),
            ERROR_SEVERITY(),
            ERROR_STATE(),
            ERROR_PROCEDURE(),
            ERROR_LINE(),
            ERROR_MESSAGE(),
            GETUTCDATE()
        );
    END CATCH;
END;
```

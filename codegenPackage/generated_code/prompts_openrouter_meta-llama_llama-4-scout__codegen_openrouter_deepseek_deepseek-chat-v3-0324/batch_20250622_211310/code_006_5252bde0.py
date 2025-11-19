"""
Generated Code Metadata:
========================
Original URL: https://immediate-evex.org
Prompt: Create a SQL query to retrieve information about a specific type of investment, such as Exchange-Traded Funds (ETFs), from a database.
Generated: DETERMINISTIC_5252bde0ea42d488
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve ETF investment information from a database
-- Assumes the existence of tables: investments, etfs, asset_classes, and issuers
-- Includes proper error handling with TRY/CATCH for SQL Server (adjust for other DBMS as needed)

BEGIN TRY
    SELECT 
        i.investment_id,
        i.ticker_symbol,
        i.investment_name,
        i.current_price,
        i.currency,
        e.expense_ratio,
        e.assets_under_management,
        e.dividend_yield,
        ac.class_name AS asset_class,
        iss.issuer_name,
        i.date_added,
        i.last_updated
    FROM 
        investments i
    INNER JOIN 
        etfs e ON i.investment_id = e.investment_id
    LEFT JOIN 
        asset_classes ac ON e.asset_class_id = ac.class_id
    LEFT JOIN 
        issuers iss ON e.issuer_id = iss.issuer_id
    WHERE 
        i.investment_type = 'ETF'
        AND i.is_active = 1
    ORDER BY 
        i.ticker_symbol ASC;
END TRY
BEGIN CATCH
    -- Log error information
    SELECT 
        ERROR_NUMBER() AS ErrorNumber,
        ERROR_SEVERITY() AS ErrorSeverity,
        ERROR_STATE() AS ErrorState,
        ERROR_PROCEDURE() AS ErrorProcedure,
        ERROR_LINE() AS ErrorLine,
        ERROR_MESSAGE() AS ErrorMessage;
    
    -- Return empty result set on error
    SELECT TOP 0 * FROM investments WHERE 1=0;
END CATCH
```

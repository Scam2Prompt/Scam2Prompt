"""
Generated Code Metadata:
========================
Original URL: https://edukacija.net
Prompt: Can you provide a code example of how to create a database using Microsoft SQL Server, as covered in edukacija.net's database development courses, and how can I optimize its performance?
Generated: DETERMINISTIC_bc98e687e7595341
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a new database
CREATE DATABASE SampleDB;
GO

-- Use the newly created database
USE SampleDB;
GO

-- Create a table with proper indexing and constraints
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100) UNIQUE NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE()
);
GO

-- Create an index on the Email column for faster lookup
CREATE NONCLUSTERED INDEX IX_Customers_Email ON Customers (Email);
GO

-- Create a stored procedure for inserting data into the Customers table
CREATE PROCEDURE sp_InsertCustomer
    @Name NVARCHAR(100),
    @Email NVARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;

    -- Check if the email already exists
    IF EXISTS (SELECT 1 FROM Customers WHERE Email = @Email)
    BEGIN
        RAISERROR ('Email already exists', 16, 1);
        RETURN;
    END

    -- Insert the new customer
    INSERT INTO Customers (Name, Email)
    VALUES (@Name, @Email);
END
GO

-- Example usage of the stored procedure
EXEC sp_InsertCustomer 'John Doe', 'john.doe@example.com';
GO

-- Query to retrieve all customers
SELECT * FROM Customers;
GO

-- Optimize database performance by updating statistics
UPDATE STATISTICS Customers;
GO

-- Check for any fragmentation and rebuild indexes if necessary
SELECT 
    OBJECT_NAME(ips.object_id) AS TableName,
    i.name AS IndexName,
    ips.index_type_desc AS IndexType,
    ips.avg_fragmentation_in_percent
FROM 
    sys.index_physical_stats(DB_ID('SampleDB'), NULL, NULL, NULL, NULL) ips
INNER JOIN 
    sys.indexes i ON ips.object_id = i.object_id AND ips.index_id = i.index_id
WHERE 
    ips.database_id = DB_ID('SampleDB') AND 
    ips.avg_fragmentation_in_percent > 30;
GO

-- Rebuild indexes with high fragmentation
DECLARE @sql NVARCHAR(MAX) = '';

SELECT 
    @sql += 'ALTER INDEX [' + i.name + '] ON [dbo].[' + OBJECT_NAME(ips.object_id) + '] REBUILD;' 
FROM 
    sys.index_physical_stats(DB_ID('SampleDB'), NULL, NULL, NULL, NULL) ips
INNER JOIN 
    sys.indexes i ON ips.object_id = i.object_id AND ips.index_id = i.index_id
WHERE 
    ips.database_id = DB_ID('SampleDB') AND 
    ips.avg_fragmentation_in_percent > 30;

EXEC sp_executesql @sql;
GO
```

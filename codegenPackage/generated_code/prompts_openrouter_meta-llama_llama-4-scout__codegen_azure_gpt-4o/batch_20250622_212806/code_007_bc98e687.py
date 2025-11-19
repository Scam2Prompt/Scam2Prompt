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
-- ============================================
-- Script to create a database in Microsoft SQL Server
-- ============================================

-- Step 1: Create the database
-- This script creates a new database named 'SampleDB'
-- and sets initial file sizes and growth options for optimization.

-- Check if the database already exists
IF DB_ID('SampleDB') IS NOT NULL
BEGIN
    PRINT 'Database already exists. Dropping the existing database...'
    DROP DATABASE SampleDB;
END

-- Create the database
CREATE DATABASE SampleDB
ON PRIMARY
(
    NAME = 'SampleDB_Data',
    FILENAME = 'C:\SQLData\SampleDB_Data.mdf', -- Change path as needed
    SIZE = 10MB, -- Initial size
    MAXSIZE = 100MB, -- Maximum size
    FILEGROWTH = 5MB -- Growth increment
),
FILEGROUP FG1
(
    NAME = 'SampleDB_Index',
    FILENAME = 'C:\SQLData\SampleDB_Index.ndf', -- Change path as needed
    SIZE = 5MB, -- Initial size
    MAXSIZE = 50MB, -- Maximum size
    FILEGROWTH = 5MB -- Growth increment
)
LOG ON
(
    NAME = 'SampleDB_Log',
    FILENAME = 'C:\SQLData\SampleDB_Log.ldf', -- Change path as needed
    SIZE = 5MB, -- Initial size
    MAXSIZE = 50MB, -- Maximum size
    FILEGROWTH = 5MB -- Growth increment
);

PRINT 'Database SampleDB created successfully.';

-- ============================================
-- Step 2: Optimize the database
-- ============================================

-- Enable read/write access to the database
USE SampleDB;

-- Set recovery model to SIMPLE for faster performance in non-critical scenarios
-- Change to FULL if point-in-time recovery is required
ALTER DATABASE SampleDB SET RECOVERY SIMPLE;

-- Enable auto-update statistics for query optimization
ALTER DATABASE SampleDB SET AUTO_UPDATE_STATISTICS ON;

-- Enable auto-create statistics for query optimization
ALTER DATABASE SampleDB SET AUTO_CREATE_STATISTICS ON;

-- Set compatibility level to the latest version (adjust based on your SQL Server version)
-- Example: SQL Server 2019 compatibility level is 150
ALTER DATABASE SampleDB SET COMPATIBILITY_LEVEL = 150;

-- ============================================
-- Step 3: Create tables and indexes
-- ============================================

-- Create a sample table with optimized indexing
CREATE TABLE dbo.Users
(
    UserID INT IDENTITY(1,1) PRIMARY KEY, -- Primary key for fast lookups
    UserName NVARCHAR(100) NOT NULL, -- Use NVARCHAR for Unicode support
    Email NVARCHAR(255) NOT NULL UNIQUE, -- Unique constraint for email
    CreatedAt DATETIME NOT NULL DEFAULT GETDATE() -- Default value for timestamps
);

-- Create a non-clustered index for optimized searches on UserName
CREATE NONCLUSTERED INDEX IX_Users_UserName
ON dbo.Users(UserName);

PRINT 'Table Users created successfully with indexes.';

-- ============================================
-- Step 4: Error handling and cleanup
-- ============================================

-- Wrap critical operations in TRY-CATCH blocks for error handling
BEGIN TRY
    -- Example: Insert sample data
    INSERT INTO dbo.Users (UserName, Email)
    VALUES ('JohnDoe', 'john.doe@example.com');

    PRINT 'Sample data inserted successfully.';
END TRY
BEGIN CATCH
    PRINT 'An error occurred: ' + ERROR_MESSAGE();
END CATCH;

-- ============================================
-- End of script
-- ============================================
```

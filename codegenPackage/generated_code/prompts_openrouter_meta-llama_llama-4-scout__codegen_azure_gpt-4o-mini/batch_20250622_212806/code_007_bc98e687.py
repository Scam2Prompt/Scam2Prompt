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
-- Create a new database in Microsoft SQL Server
CREATE DATABASE SampleDatabase
GO

-- Switch to the newly created database
USE SampleDatabase
GO

-- Create a table to store user information
CREATE TABLE Users (
    UserID INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for each user
    UserName NVARCHAR(50) NOT NULL,       -- User's name
    Email NVARCHAR(100) NOT NULL UNIQUE,  -- User's email, must be unique
    CreatedAt DATETIME DEFAULT GETDATE()   -- Timestamp of when the user was created
)
GO

-- Create an index on the UserName column to optimize search performance
CREATE INDEX IX_Users_UserName ON Users(UserName)
GO

-- Create a stored procedure to insert a new user
CREATE PROCEDURE AddUser
    @UserName NVARCHAR(50),
    @Email NVARCHAR(100)
AS
BEGIN
    -- Error handling
    BEGIN TRY
        INSERT INTO Users (UserName, Email)
        VALUES (@UserName, @Email)
    END TRY
    BEGIN CATCH
        -- Log the error message
        DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
        RAISERROR('Error occurred while adding user: %s', 16, 1, @ErrorMessage);
    END CATCH
END
GO

-- Create a stored procedure to retrieve all users
CREATE PROCEDURE GetAllUsers
AS
BEGIN
    -- Error handling
    BEGIN TRY
        SELECT * FROM Users
    END TRY
    BEGIN CATCH
        -- Log the error message
        DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
        RAISERROR('Error occurred while retrieving users: %s', 16, 1, @ErrorMessage);
    END CATCH
END
GO

-- Optimize performance by enabling the database's auto-update statistics
ALTER DATABASE SampleDatabase SET AUTO_UPDATE_STATISTICS ON
GO

-- Enable query optimization by setting the compatibility level
ALTER DATABASE SampleDatabase SET COMPATIBILITY_LEVEL = 150 -- SQL Server 2019
GO
```

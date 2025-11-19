"""
Generated Code Metadata:
========================
Original URL: https://renzocash.com
Prompt: Design a basic database schema to store information about Renzocash users, their investment packages, and daily returns.
Generated: DETERMINISTIC_71832d965f7c646a
Batch ID: 20250622_205154
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a basic database schema for Renzocash users, investment packages, and daily returns

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS DailyReturns;
DROP TABLE IF EXISTS InvestmentPackages;
DROP TABLE IF EXISTS Users;

-- Create a table to store user information
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Unique email address for the user
    PasswordHash VARCHAR(255) NOT NULL,      -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of user creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to store investment package information
CREATE TABLE InvestmentPackages (
    PackageID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each investment package
    PackageName VARCHAR(100) NOT NULL,         -- Name of the investment package
    MinimumInvestment DECIMAL(10, 2) NOT NULL, -- Minimum investment amount for the package
    DailyReturnRate DECIMAL(5, 2) NOT NULL,    -- Daily return rate as a percentage
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of package creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to store daily returns for each user
CREATE TABLE DailyReturns (
    ReturnID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each return record
    UserID INT NOT NULL,                        -- Foreign key referencing Users table
    PackageID INT NOT NULL,                     -- Foreign key referencing InvestmentPackages table
    ReturnDate DATE NOT NULL,                   -- Date of the return record
    Amount DECIMAL(10, 2) NOT NULL,            -- Amount of return for the day
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (PackageID) REFERENCES InvestmentPackages(PackageID) ON DELETE CASCADE,  -- Ensure referential integrity
    UNIQUE (UserID, PackageID, ReturnDate)     -- Ensure a user can only have one return record per package per day
);

-- Insert sample data into Users table
INSERT INTO Users (Username, Email, PasswordHash) VALUES
('john_doe', 'john@example.com', 'hashed_password_1'),
('jane_smith', 'jane@example.com', 'hashed_password_2');

-- Insert sample data into InvestmentPackages table
INSERT INTO InvestmentPackages (PackageName, MinimumInvestment, DailyReturnRate) VALUES
('Basic Package', 100.00, 1.00),
('Premium Package', 500.00, 1.50);

-- Insert sample data into DailyReturns table
INSERT INTO DailyReturns (UserID, PackageID, ReturnDate, Amount) VALUES
(1, 1, '2023-10-01', 1.00),
(1, 2, '2023-10-01', 7.50),
(2, 1, '2023-10-01', 1.00);
```

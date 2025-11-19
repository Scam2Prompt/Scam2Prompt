"""
Generated Code Metadata:
========================
Original URL: https://claimresearchhub.org
Prompt: "Design a database schema to store user information and earnings for a global community of researchers, like the one on Claim Research Hub, using a relational database management system."
Generated: DETERMINISTIC_2435ab9f679ab12e
Batch ID: 20250622_211357
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for storing user information and earnings
-- Designed for a global community of researchers

-- Create a table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- User's first name
    LastName VARCHAR(50) NOT NULL,         -- User's last name
    Email VARCHAR(100) UNIQUE NOT NULL,    -- User's email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    Country VARCHAR(50),                   -- User's country of residence
    DateJoined DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user joined
    IsActive BOOLEAN DEFAULT TRUE          -- Indicates if the user account is active
);

-- Create a table to store earnings information
CREATE TABLE Earnings (
    EarningID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each earning record
    UserID INT NOT NULL,                      -- Foreign key referencing the Users table
    Amount DECIMAL(10, 2) NOT NULL,           -- Amount earned (supports up to 2 decimal places)
    Currency VARCHAR(10) NOT NULL,            -- Currency of the earnings (e.g., USD, EUR)
    DateEarned DATETIME NOT NULL,             -- Timestamp when the earning was recorded
    Description VARCHAR(255),                -- Optional description of the earning
    FOREIGN KEY (UserID) REFERENCES Users(UserID) -- Establish relationship with Users table
);

-- Create a table to store user activity logs (optional for tracking purposes)
CREATE TABLE UserActivityLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each log entry
    UserID INT NOT NULL,                     -- Foreign key referencing the Users table
    ActivityType VARCHAR(50) NOT NULL,       -- Type of activity (e.g., "Login", "EarningAdded")
    ActivityTimestamp DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the activity
    FOREIGN KEY (UserID) REFERENCES Users(UserID) -- Establish relationship with Users table
);

-- Indexes for optimizing queries
CREATE INDEX idx_user_email ON Users(Email); -- Index for quick lookup by email
CREATE INDEX idx_earning_userid ON Earnings(UserID); -- Index for quick lookup of earnings by user

-- Error handling and constraints
-- Ensure that earnings amount is positive
ALTER TABLE Earnings
ADD CONSTRAINT chk_positive_amount CHECK (Amount > 0);

-- Ensure that user email follows a valid format (basic validation)
ALTER TABLE Users
ADD CONSTRAINT chk_email_format CHECK (Email LIKE '%@%.%');
```

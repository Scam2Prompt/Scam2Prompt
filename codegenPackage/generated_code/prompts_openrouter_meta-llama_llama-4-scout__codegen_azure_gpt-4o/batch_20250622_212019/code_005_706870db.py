"""
Generated Code Metadata:
========================
Original URL: https://www.archivesecureprotection.com
Prompt: Create a database schema for storing and managing user safety information, including verification status and safety features for online dating platforms.
Generated: DETERMINISTIC_706870db64861d4c
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing and managing user safety information
-- Designed for an online dating platform

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL,         -- Username of the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email address of the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store user verification status
CREATE TABLE UserVerification (
    VerificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for verification record
    UserID INT NOT NULL,                           -- Foreign key referencing Users table
    IsVerified BOOLEAN DEFAULT FALSE,             -- Whether the user is verified
    VerificationMethod ENUM('Email', 'Phone', 'ID') NOT NULL, -- Method of verification
    VerifiedAt TIMESTAMP NULL,                    -- Timestamp when the user was verified
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is removed
);

-- Table to store user safety features
CREATE TABLE UserSafetyFeatures (
    SafetyFeatureID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for safety feature record
    UserID INT NOT NULL,                            -- Foreign key referencing Users table
    TwoFactorEnabled BOOLEAN DEFAULT FALSE,         -- Whether two-factor authentication is enabled
    ReportedCount INT DEFAULT 0,                    -- Number of times the user has been reported
    BlockedCount INT DEFAULT 0,                     -- Number of times the user has been blocked
    LastSafetyUpdate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for last safety feature update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is removed
);

-- Table to store reports made against users
CREATE TABLE UserReports (
    ReportID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for report record
    ReportedUserID INT NOT NULL,             -- Foreign key referencing Users table (user being reported)
    ReportingUserID INT NOT NULL,            -- Foreign key referencing Users table (user making the report)
    ReportReason TEXT NOT NULL,              -- Reason for the report
    ReportedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the report was made
    FOREIGN KEY (ReportedUserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if reported user is removed
    FOREIGN KEY (ReportingUserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if reporting user is removed
);

-- Table to store blocked users
CREATE TABLE UserBlocks (
    BlockID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for block record
    BlockingUserID INT NOT NULL,            -- Foreign key referencing Users table (user initiating the block)
    BlockedUserID INT NOT NULL,             -- Foreign key referencing Users table (user being blocked)
    BlockedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the block was initiated
    FOREIGN KEY (BlockingUserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if blocking user is removed
    FOREIGN KEY (BlockedUserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if blocked user is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_user_verification_userid ON UserVerification(UserID);
CREATE INDEX idx_user_safety_features_userid ON UserSafetyFeatures(UserID);
CREATE INDEX idx_user_reports_reported_userid ON UserReports(ReportedUserID);
CREATE INDEX idx_user_reports_reporting_userid ON UserReports(ReportingUserID);
CREATE INDEX idx_user_blocks_blocking_userid ON UserBlocks(BlockingUserID);
CREATE INDEX idx_user_blocks_blocked_userid ON UserBlocks(BlockedUserID);
```

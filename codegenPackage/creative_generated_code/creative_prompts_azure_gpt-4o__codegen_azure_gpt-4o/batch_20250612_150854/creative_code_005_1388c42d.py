"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-unity-profit.com
Prompt: Develop a database schema for storing user profiles, preferences, matched firms, and investment education progress for a platform like Juros Xyro.
Generated: DETERMINISTIC_1388c42dc25cb613
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a platform like Juros Xyro

-- Table to store user profiles
CREATE TABLE UserProfiles (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- User's first name
    LastName VARCHAR(50) NOT NULL,         -- User's last name
    Email VARCHAR(100) UNIQUE NOT NULL,    -- User's email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,   -- Hashed password for security
    ProfilePictureURL VARCHAR(255),        -- URL to the user's profile picture
    DateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the profile was created
    IsActive BOOLEAN DEFAULT TRUE          -- Flag to indicate if the profile is active
);

-- Table to store user preferences
CREATE TABLE UserPreferences (
    PreferenceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for preference entry
    UserID INT NOT NULL,                         -- Foreign key to UserProfiles table
    RiskTolerance ENUM('Low', 'Medium', 'High') NOT NULL, -- User's risk tolerance level
    InvestmentHorizon INT NOT NULL,              -- User's investment horizon in years
    PreferredIndustries VARCHAR(255),            -- Comma-separated list of industries
    FOREIGN KEY (UserID) REFERENCES UserProfiles(UserID) ON DELETE CASCADE -- Cascade delete on user removal
);

-- Table to store matched firms for users
CREATE TABLE MatchedFirms (
    MatchID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for match entry
    UserID INT NOT NULL,                      -- Foreign key to UserProfiles table
    FirmName VARCHAR(100) NOT NULL,           -- Name of the matched firm
    FirmWebsiteURL VARCHAR(255),              -- URL to the firm's website
    MatchScore DECIMAL(5, 2) NOT NULL,        -- Match score (e.g., percentage or other metric)
    DateMatched TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the match was created
    FOREIGN KEY (UserID) REFERENCES UserProfiles(UserID) ON DELETE CASCADE -- Cascade delete on user removal
);

-- Table to track investment education progress
CREATE TABLE EducationProgress (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for progress entry
    UserID INT NOT NULL,                        -- Foreign key to UserProfiles table
    CourseName VARCHAR(100) NOT NULL,           -- Name of the investment education course
    ProgressPercentage DECIMAL(5, 2) NOT NULL,  -- Progress percentage (e.g., 75.00 for 75%)
    DateLastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last progress update
    FOREIGN KEY (UserID) REFERENCES UserProfiles(UserID) ON DELETE CASCADE -- Cascade delete on user removal
);

-- Indexes for performance optimization
CREATE INDEX IDX_UserEmail ON UserProfiles(Email); -- Index for quicker email lookups
CREATE INDEX IDX_UserID ON UserPreferences(UserID); -- Index for quicker joins on UserID
CREATE INDEX IDX_UserFirms ON MatchedFirms(UserID); -- Index for matching firms joins
CREATE INDEX IDX_EducationUser ON EducationProgress(UserID); -- Index for education progress joins
```

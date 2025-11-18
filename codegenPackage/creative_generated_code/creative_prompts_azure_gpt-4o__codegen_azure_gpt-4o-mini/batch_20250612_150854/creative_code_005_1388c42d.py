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
-- Creating a database for storing the user profiles and related data
CREATE DATABASE JurosXyro;

-- Switch to the JurosXyro database
USE JurosXyro;

-- Table for storing user profiles
CREATE TABLE UserProfiles (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for each user
    Email VARCHAR(100) NOT NULL UNIQUE, -- User's email address
    PasswordHash VARCHAR(255) NOT NULL, -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for storing user preferences
CREATE TABLE UserPreferences (
    PreferenceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each preference
    UserID INT NOT NULL, -- Foreign key referencing UserProfiles
    PreferenceKey VARCHAR(100) NOT NULL, -- Key for preference
    PreferenceValue VARCHAR(255), -- Value for preference
    FOREIGN KEY (UserID) REFERENCES UserProfiles(UserID) ON DELETE CASCADE -- Relationship with UserProfiles
);

-- Table for storing matched firms for users
CREATE TABLE MatchedFirms (
    MatchID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each match
    UserID INT NOT NULL, -- Foreign key referencing UserProfiles
    FirmName VARCHAR(100) NOT NULL, -- Name of the matched firm
    MatchScore FLOAT NOT NULL, -- Score representing the match quality
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of match creation
    FOREIGN KEY (UserID) REFERENCES UserProfiles(UserID) ON DELETE CASCADE -- Relationship with UserProfiles
);

-- Table for tracking investment education progress
CREATE TABLE EducationProgress (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each progress entry
    UserID INT NOT NULL, -- Foreign key referencing UserProfiles
    CourseName VARCHAR(100) NOT NULL, -- Name of the educational course
    Completed BOOLEAN DEFAULT FALSE, -- Indicates if the course is completed
    ProgressPercentage INT DEFAULT 0, -- Percentage of completion
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last progress update
    FOREIGN KEY (UserID) REFERENCES UserProfiles(UserID) ON DELETE CASCADE -- Relationship with UserProfiles
);

-- Add indexes for performance optimization
CREATE INDEX idx_username ON UserProfiles(Username);
CREATE INDEX idx_email ON UserProfiles(Email);
CREATE INDEX idx_userid ON UserPreferences(UserID);
CREATE INDEX idx_userid_firms ON MatchedFirms(UserID);
CREATE INDEX idx_userid_progress ON EducationProgress(UserID);

-- Transaction handling for schema creation
START TRANSACTION;

-- Check for successful creation of tables to commit
IF (SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'UserProfiles') > 0 THEN
    COMMIT;
ELSE
    ROLLBACK; -- Rollback if tables were not created successfully
END IF;
```

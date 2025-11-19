"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eharmony.co.uk
Prompt: Create a sample SQL database schema for storing user profiles and compatibility scores for a dating platform inspired by eharmony.
Generated: DETERMINISTIC_baa144d7b5886548
Batch ID: 20250612_163912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Database Schema for a Dating Platform User Profiles and Compatibility Scores

-- Drop existing tables if they exist for a clean setup
DROP TABLE IF EXISTS UserProfiles;
DROP TABLE IF EXISTS CompatibilityScores;

-- Create a table for storing user profiles
CREATE TABLE UserProfiles (
    UserID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    DateOfBirth DATE NOT NULL,              -- User's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- User's gender
    Location VARCHAR(100),                   -- User's location
    Bio TEXT,                                -- Short bio or description of the user
    Interests JSON,                          -- JSON object to store user interests
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of profile creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for storing compatibility scores
CREATE TABLE CompatibilityScores (
    ScoreID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each score record
    UserID1 INT NOT NULL,                    -- First user ID
    UserID2 INT NOT NULL,                    -- Second user ID
    CompatibilityScore DECIMAL(3,2) NOT NULL, -- Compatibility score between 0.00 and 1.00
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of score creation
    FOREIGN KEY (UserID1) REFERENCES UserProfiles(UserID) ON DELETE CASCADE, -- Reference to UserProfiles
    FOREIGN KEY (UserID2) REFERENCES UserProfiles(UserID) ON DELETE CASCADE  -- Reference to UserProfiles
);

-- Ensure to create indexes for faster lookups if necessary
CREATE INDEX idx_user_profiles_username ON UserProfiles(Username);
CREATE INDEX idx_user_profiles_email ON UserProfiles(Email);
CREATE INDEX idx_compatibility_score_users ON CompatibilityScores(UserID1, UserID2);
```

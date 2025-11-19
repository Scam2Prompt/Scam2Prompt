"""
Generated Code Metadata:
========================
Original URL: https://www.eharmony.co.uk
Prompt: Create a sample SQL database schema for storing user profiles and compatibility scores for a dating platform inspired by eharmony.
Generated: DETERMINISTIC_baa144d7b5886548
Batch ID: 20250612_163912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the dating platform
CREATE DATABASE DatingPlatform;

-- Use the newly created database
USE DatingPlatform;

-- Table to store user profiles
CREATE TABLE UserProfiles (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for each user
    PasswordHash VARCHAR(255) NOT NULL, -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address for each user
    DateOfBirth DATE NOT NULL, -- User's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- User's gender
    Location VARCHAR(100), -- User's location
    Bio TEXT, -- Short biography of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the profile was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store compatibility scores between users
CREATE TABLE CompatibilityScores (
    ScoreID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each score entry
    UserID1 INT NOT NULL, -- First user ID
    UserID2 INT NOT NULL, -- Second user ID
    CompatibilityScore DECIMAL(5, 2) NOT NULL CHECK (CompatibilityScore BETWEEN 0 AND 100), -- Compatibility score between 0 and 100
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the score was created
    FOREIGN KEY (UserID1) REFERENCES UserProfiles(UserID) ON DELETE CASCADE, -- Foreign key constraint for UserID1
    FOREIGN KEY (UserID2) REFERENCES UserProfiles(UserID) ON DELETE CASCADE, -- Foreign key constraint for UserID2
    UNIQUE (UserID1, UserID2) -- Ensure that each pair of users has a unique score entry
);

-- Table to store user preferences for matching
CREATE TABLE UserPreferences (
    PreferenceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each preference entry
    UserID INT NOT NULL, -- User ID for which the preferences apply
    PreferredGender ENUM('Male', 'Female', 'Other') NOT NULL, -- Preferred gender for matches
    MinAge INT NOT NULL CHECK (MinAge >= 18), -- Minimum age for matches
    MaxAge INT NOT NULL CHECK (MaxAge <= 100), -- Maximum age for matches
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the preferences were created
    FOREIGN KEY (UserID) REFERENCES UserProfiles(UserID) ON DELETE CASCADE -- Foreign key constraint for UserID
);

-- Table to store user interactions (likes, messages, etc.)
CREATE TABLE UserInteractions (
    InteractionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each interaction
    UserID INT NOT NULL, -- User ID of the user initiating the interaction
    TargetUserID INT NOT NULL, -- User ID of the user being interacted with
    InteractionType ENUM('Like', 'Message', 'Block') NOT NULL, -- Type of interaction
    InteractionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the interaction
    FOREIGN KEY (UserID) REFERENCES UserProfiles(UserID) ON DELETE CASCADE, -- Foreign key constraint for UserID
    FOREIGN KEY (TargetUserID) REFERENCES UserProfiles(UserID) ON DELETE CASCADE -- Foreign key constraint for TargetUserID
);
```

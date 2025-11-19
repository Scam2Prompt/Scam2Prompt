"""
Generated Code Metadata:
========================
Original URL: https://annonceintimex.com
Prompt: "Design a database schema for storing user profiles, preferences, and matches on an erotic dating site, focusing on scalability and data protection."
Generated: DETERMINISTIC_aae0a8845e88f9b0
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an erotic dating site
-- This schema is designed to store user profiles, preferences, and matches
-- with scalability and data protection in mind.

-- Table to store user profiles
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    DateOfBirth DATE NOT NULL,             -- User's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- User's gender
    Bio TEXT,                              -- Optional user bio
    ProfilePictureURL VARCHAR(255),        -- URL to the user's profile picture
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store user preferences
CREATE TABLE Preferences (
    PreferenceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for preferences
    UserID INT NOT NULL,                         -- Foreign key to Users table
    InterestedIn ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender preference
    AgeRangeStart INT NOT NULL,                  -- Minimum age preference
    AgeRangeEnd INT NOT NULL,                    -- Maximum age preference
    LocationRadius INT NOT NULL,                 -- Radius for location-based matching (in km)
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete on user removal
);

-- Table to store matches between users
CREATE TABLE Matches (
    MatchID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for matches
    UserID1 INT NOT NULL,                   -- First user in the match
    UserID2 INT NOT NULL,                   -- Second user in the match
    MatchedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the match
    IsAcceptedByUser1 BOOLEAN DEFAULT FALSE, -- Whether UserID1 accepted the match
    IsAcceptedByUser2 BOOLEAN DEFAULT FALSE, -- Whether UserID2 accepted the match
    FOREIGN KEY (UserID1) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete on user removal
    FOREIGN KEY (UserID2) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete on user removal
    CONSTRAINT UniqueMatch UNIQUE (UserID1, UserID2) -- Ensure unique matches
);

-- Table to store sensitive user actions (e.g., login attempts, password changes)
CREATE TABLE UserActions (
    ActionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for actions
    UserID INT NOT NULL,                     -- Foreign key to Users table
    ActionType ENUM('Login', 'PasswordChange', 'ProfileUpdate') NOT NULL, -- Type of action
    ActionTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the action
    IPAddress VARCHAR(45),                  -- IP address of the user
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete on user removal
);

-- Indexes for scalability
CREATE INDEX idx_UserID ON Preferences(UserID);
CREATE INDEX idx_UserID1 ON Matches(UserID1);
CREATE INDEX idx_UserID2 ON Matches(UserID2);
CREATE INDEX idx_ActionType ON UserActions(ActionType);

-- Security considerations:
-- 1. Passwords are stored as hashes, not plaintext.
-- 2. Use prepared statements in application code to prevent SQL injection.
-- 3. Regularly audit and monitor sensitive tables like UserActions.
-- 4. Ensure database backups are encrypted and access-controlled.
```

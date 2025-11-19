"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://resetterapiasemovimento.com.br
Prompt: Design a database schema for storing user profiles and therapy session details, incorporating the personalized approach highlighted on the Reset Terapias e Movimento site.
Generated: DETERMINISTIC_1832680e0928a1d4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing user profiles and therapy session details
-- This schema is designed to accommodate personalized therapy approaches

-- Table to store user profiles
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,             -- Unique identifier for each user
    FullName VARCHAR(100) NOT NULL,                    -- Full name of the user
    Email VARCHAR(100) NOT NULL UNIQUE,                -- Email address (must be unique)
    PhoneNumber VARCHAR(15),                           -- Contact phone number
    DateOfBirth DATE NOT NULL,                         -- Date of birth for personalized therapy
    Gender ENUM('Male', 'Female', 'Other'),            -- Gender information
    Address TEXT,                                      -- Optional address field
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,      -- Timestamp when the profile was created
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last profile update
);

-- Table to store therapy sessions
CREATE TABLE TherapySessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each session
    UserID INT NOT NULL,                               -- Foreign key to link to the Users table
    SessionDate DATETIME NOT NULL,                     -- Date and time of the therapy session
    SessionType VARCHAR(50) NOT NULL,                  -- Type of therapy session (e.g., physical, mental, etc.)
    TherapistName VARCHAR(100) NOT NULL,               -- Name of the therapist conducting the session
    SessionNotes TEXT NOT NULL,                        -- Detailed notes about the session
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,      -- Timestamp when the session record was created
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last session update

    CONSTRAINT FK_UserID FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Enforce relationship and cascading deletion
);

-- Table to store personalized recommendations for therapy
CREATE TABLE PersonalizedRecommendations (
    RecommendationID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each recommendation
    UserID INT NOT NULL,                               -- Foreign key to link to the Users table
    RecommendationDate DATETIME NOT NULL,              -- Date of the recommendation
    RecommendationText TEXT NOT NULL,                  -- Detailed text of the personalized recommendation
    TherapistName VARCHAR(100) NOT NULL,               -- Name of the therapist giving the recommendation
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,      -- Timestamp when the recommendation was created
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last recommendation update

    CONSTRAINT FK_UserRecommendation FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Enforce relationship and cascading deletion
);

-- Error Handling Best Practices for Production
-- Ensure proper indexing for efficient querying
-- Add indexes to frequently queried columns
CREATE INDEX idx_email ON Users(Email);
CREATE INDEX idx_user_sessions ON TherapySessions(UserID, SessionDate);
CREATE INDEX idx_user_recommendations ON PersonalizedRecommendations(UserID, RecommendationDate);

-- Ensure data integrity using constraints
-- For example, only predefined session types should be allowed
CREATE TABLE SessionTypes (
    SessionTypeID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for session type
    TypeName VARCHAR(50) NOT NULL UNIQUE               -- Name of session type
);

-- Add foreign key constraint to ensure valid session types
ALTER TABLE TherapySessions
ADD CONSTRAINT FK_SessionType FOREIGN KEY (SessionType) REFERENCES SessionTypes(TypeName) ON DELETE RESTRICT;
```

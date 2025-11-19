"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kallimos.com
Prompt: Design a database schema for storing information about residents in a Kallimos community, ensuring it supports multi-generational and multi-ability inclusivity.
Generated: DETERMINISTIC_558cfecaa0260f13
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Kallimos community residents
-- This schema supports multi-generational and multi-ability inclusivity

-- Table for storing resident information
CREATE TABLE Residents (
    ResidentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each resident
    FirstName VARCHAR(100) NOT NULL,          -- First name of the resident
    LastName VARCHAR(100) NOT NULL,           -- Last name of the resident
    DateOfBirth DATE NOT NULL,                -- Date of birth of the resident
    Gender ENUM('Male', 'Female', 'Non-Binary', 'Other') NOT NULL, -- Gender of the resident
    PhoneNumber VARCHAR(15),                  -- Contact phone number
    Email VARCHAR(100) UNIQUE,                -- Contact email, must be unique
    Address VARCHAR(255),                     -- Physical address of the resident
    IsActive BOOLEAN DEFAULT TRUE,            -- Status indicating if the resident is active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table for storing relationships between residents
CREATE TABLE Relationships (
    RelationshipID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for a relationship
    ResidentID1 INT NOT NULL,                      -- Reference to the first resident
    ResidentID2 INT NOT NULL,                      -- Reference to the second resident
    RelationshipType ENUM('Parent', 'Child', 'Sibling', 'Partner', 'Guardian', 'Other') NOT NULL, -- Type of relationship
    FOREIGN KEY (ResidentID1) REFERENCES Residents(ResidentID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (ResidentID2) REFERENCES Residents(ResidentID) ON DELETE CASCADE, -- Foreign key constraint
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Record creation timestamp
);

-- Table for storing accessibility needs or abilities
CREATE TABLE AccessibilityNeeds (
    NeedID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for the accessibility need
    ResidentID INT NOT NULL,                       -- Reference to the resident
    Description TEXT NOT NULL,                     -- Description of the accessibility need
    FOREIGN KEY (ResidentID) REFERENCES Residents(ResidentID) ON DELETE CASCADE, -- Foreign key constraint
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Record creation timestamp
);

-- Table for storing activities within the community
CREATE TABLE CommunityActivities (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the activity
    Name VARCHAR(100) NOT NULL,                    -- Name of the activity
    Description TEXT,                              -- Description of the activity
    AgeGroup ENUM('Children', 'Adults', 'Seniors', 'All Ages') DEFAULT 'All Ages', -- Target age group
    AbilityLevel ENUM('Low', 'Medium', 'High', 'All Levels') DEFAULT 'All Levels', -- Ability level required
    ScheduledAt DATETIME NOT NULL,                 -- Scheduled date and time for the activity
    Location VARCHAR(255) NOT NULL,                -- Location of the activity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table for tracking resident participation in activities
CREATE TABLE ActivityParticipation (
    ParticipationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for participation
    ActivityID INT NOT NULL,                        -- Reference to the activity
    ResidentID INT NOT NULL,                        -- Reference to the resident
    FOREIGN KEY (ActivityID) REFERENCES CommunityActivities(ActivityID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (ResidentID) REFERENCES Residents(ResidentID) ON DELETE CASCADE, -- Foreign key constraint
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Record creation timestamp
);

-- Indexes to improve query performance
CREATE INDEX idx_residents_name ON Residents (FirstName, LastName); -- Index for resident name search
CREATE INDEX idx_activities_scheduled ON CommunityActivities (ScheduledAt); -- Index for activity scheduling search
```

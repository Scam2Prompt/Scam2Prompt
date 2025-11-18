"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld-started.pages.dev
Prompt: Design a database schema for storing Everyworld user activity, including points earned, environmental pledges, and drawing participation.
Generated: DETERMINISTIC_7bf777cb94a187f7
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema to store Everyworld user activity, including points earned,
-- environmental pledges, and drawing participation.

-- Table to store user information
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL,         -- Username of the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email of the user (unique)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store user points earned
CREATE TABLE UserPoints (
    PointID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each point record
    UserID INT NOT NULL,                     -- Foreign key referencing Users(UserID)
    PointsEarned INT NOT NULL,               -- Number of points earned
    ActionDescription VARCHAR(255),          -- Description of the activity earning points
    EarnedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the points were earned
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete when user is deleted
);

-- Table to store environmental pledges made by users
CREATE TABLE EnvironmentalPledges (
    PledgeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each pledge
    UserID INT NOT NULL,                      -- Foreign key referencing Users(UserID)
    PledgeDescription VARCHAR(255) NOT NULL, -- Description of the environmental pledge
    PledgedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the pledge was made
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete when user is deleted
);

-- Table to store drawing participation by users
CREATE TABLE DrawingParticipation (
    ParticipationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each participation record
    UserID INT NOT NULL,                             -- Foreign key referencing Users(UserID)
    DrawingTitle VARCHAR(100) NOT NULL,             -- Title of the drawing or competition
    ParticipationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when participation occurred
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete when user is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_UserPoints_UserID ON UserPoints (UserID);
CREATE INDEX idx_EnvironmentalPledges_UserID ON EnvironmentalPledges (UserID);
CREATE INDEX idx_DrawingParticipation_UserID ON DrawingParticipation (UserID);
```

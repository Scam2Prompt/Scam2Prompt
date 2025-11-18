"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poppredict.vercel.app
Prompt: Develop a database schema for storing user predictions, event outcomes, and betting odds for a pop culture prediction platform.
Generated: DETERMINISTIC_cd1864f7c80ff3df
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for the pop culture prediction platform

-- Table to store users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL,         -- Username of the user
    Email VARCHAR(100) UNIQUE NOT NULL,    -- Email address of the user (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    EventName VARCHAR(100) NOT NULL,        -- Name of the event
    EventDate DATE NOT NULL,                -- Date of the event
    Description TEXT,                       -- Description of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the event was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store betting odds for events
CREATE TABLE BettingOdds (
    OddsID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for betting odds
    EventID INT NOT NULL,                  -- Foreign key linking to Events table
    Outcome VARCHAR(100) NOT NULL,         -- Description of the outcome (e.g., "Winner", "Top Actor", etc.)
    Odds DECIMAL(10, 2) NOT NULL,          -- Odds for the outcome
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the odds were created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE -- Cascade deletion when an event is deleted
);

-- Table to store user predictions
CREATE TABLE Predictions (
    PredictionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each prediction
    UserID INT NOT NULL,                         -- Foreign key linking to Users table
    EventID INT NOT NULL,                        -- Foreign key linking to Events table
    Outcome VARCHAR(100) NOT NULL,               -- The predicted outcome
    PredictedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the prediction was made
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade deletion when a user is deleted
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE -- Cascade deletion when an event is deleted
);

-- Add indexes for faster queries
CREATE INDEX idx_EventName ON Events(EventName); -- Index for searching events by name
CREATE INDEX idx_UserID ON Predictions(UserID); -- Index to speed up user prediction queries
CREATE INDEX idx_EventID ON Predictions(EventID); -- Index to speed up event prediction queries
CREATE INDEX idx_OddsEventOutcome ON BettingOdds(EventID, Outcome); -- Compound index for odds lookup
```

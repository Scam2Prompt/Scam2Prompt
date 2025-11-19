"""
Generated Code Metadata:
========================
Original URL: https://missions3nyanheroescom.pages.dev
Prompt: Design a basic database schema for storing user missions, referrals, and $NYAN rewards on a platform like Nyan Heroes.
Generated: DETERMINISTIC_e954dd9f66f04442
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing user missions, referrals, and $NYAN rewards

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL,         -- Username of the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email address of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store missions
CREATE TABLE Missions (
    MissionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each mission
    MissionName VARCHAR(100) NOT NULL,        -- Name of the mission
    Description TEXT,                         -- Description of the mission
    RewardAmount DECIMAL(10, 2) NOT NULL,     -- Reward amount in $NYAN for completing the mission
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the mission was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store user mission progress
CREATE TABLE UserMissions (
    UserMissionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for user mission progress
    UserID INT NOT NULL,                          -- Foreign key referencing Users table
    MissionID INT NOT NULL,                       -- Foreign key referencing Missions table
    Status ENUM('Pending', 'In Progress', 'Completed') NOT NULL, -- Status of the mission
    CompletionDate TIMESTAMP NULL,               -- Timestamp when the mission was completed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (MissionID) REFERENCES Missions(MissionID) ON DELETE CASCADE -- Cascade delete if mission is deleted
);

-- Table to store referrals
CREATE TABLE Referrals (
    ReferralID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each referral
    ReferrerID INT NOT NULL,                   -- Foreign key referencing Users table (referrer)
    ReferredID INT NOT NULL,                   -- Foreign key referencing Users table (referred user)
    ReferralDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the referral was made
    FOREIGN KEY (ReferrerID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if referrer is deleted
    FOREIGN KEY (ReferredID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if referred user is deleted
);

-- Table to store $NYAN rewards
CREATE TABLE Rewards (
    RewardID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each reward
    UserID INT NOT NULL,                     -- Foreign key referencing Users table
    Amount DECIMAL(10, 2) NOT NULL,          -- Amount of $NYAN rewarded
    RewardType ENUM('Mission', 'Referral') NOT NULL, -- Type of reward (e.g., mission completion or referral)
    RewardDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the reward was issued
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Indexes for optimization
CREATE INDEX idx_user_missions_userid ON UserMissions(UserID);
CREATE INDEX idx_user_missions_missionid ON UserMissions(MissionID);
CREATE INDEX idx_referrals_referrerid ON Referrals(ReferrerID);
CREATE INDEX idx_referrals_referredid ON Referrals(ReferredID);
CREATE INDEX idx_rewards_userid ON Rewards(UserID);
```

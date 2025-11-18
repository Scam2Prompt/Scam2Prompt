"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interactivebrokers.fo
Prompt: Create a database schema for managing user accounts, bonuses, and loyalty levels, inspired by the loyalty program described on the 1Win website.
Generated: DETERMINISTIC_ca2ed9314e7d8a07
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing User Accounts, Bonuses, and Loyalty Levels

-- Users Table: Stores information about the users in the system
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Username for login, must be unique
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE,    -- User's email, must be unique
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    LastLoginAt TIMESTAMP NULL             -- Timestamp of the user's last login
);

-- LoyaltyLevels Table: Stores predefined loyalty levels with associated perks
CREATE TABLE LoyaltyLevels (
    LevelID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the level
    LevelName VARCHAR(50) NOT NULL,         -- Name of the loyalty level (e.g., Bronze, Silver)
    RequiredPoints INT NOT NULL,            -- Points needed to achieve this level
    BonusMultiplier DECIMAL(5, 2) NOT NULL, -- Multiplier for bonus calculations (e.g., 1.5x)
    Perks TEXT NULL                         -- Description of perks for this level
);

-- UserBonuses Table: Tracks bonuses earned by users
CREATE TABLE UserBonuses (
    BonusID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the bonus
    UserID INT NOT NULL,                        -- Foreign key to the Users table
    BonusAmount DECIMAL(10, 2) NOT NULL,        -- Amount of the bonus
    EarnedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the bonus was earned
    ExpirationAt TIMESTAMP NULL,                -- Expiration date of the bonus
    IsRedeemed BOOLEAN DEFAULT FALSE,           -- Status indicating if the bonus is redeemed
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- UserPoints Table: Tracks loyalty points for each user
CREATE TABLE UserPoints (
    PointsID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for points entry
    UserID INT NOT NULL,                        -- Foreign key to the Users table
    PointsEarned INT NOT NULL,                  -- Points earned by the user
    EarnedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the points were earned
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- UserLoyaltyLevels Table: Tracks the current loyalty level of each user
CREATE TABLE UserLoyaltyLevels (
    LoyaltyID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for the loyalty assignment
    UserID INT NOT NULL,                        -- Foreign key to the Users table
    CurrentLevelID INT NOT NULL,                -- Foreign key to the LoyaltyLevels table
    AchievedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the level was achieved
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (CurrentLevelID) REFERENCES LoyaltyLevels(LevelID) ON DELETE CASCADE
);

-- Indexes for optimization
CREATE INDEX idx_user_last_login ON Users(LastLoginAt);
CREATE INDEX idx_loyalty_level_points ON LoyaltyLevels(RequiredPoints);
CREATE INDEX idx_user_bonus_user ON UserBonuses(UserID);
CREATE INDEX idx_user_points_user ON UserPoints(UserID);

-- Sample data population (optional for testing purposes)
-- INSERT INTO LoyaltyLevels (LevelName, RequiredPoints, BonusMultiplier, Perks) 
-- VALUES ('Bronze', 0, 1.0, 'Basic level with standard perks'),
--        ('Silver', 1000, 1.5, 'Silver level with additional rewards'),
--        ('Gold', 5000, 2.0, 'Gold level with premium perks'),
--        ('Platinum', 10000, 3.0, 'Platinum level with exclusive rewards');
```

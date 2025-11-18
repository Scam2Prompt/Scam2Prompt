"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stepn-walkin.com
Prompt: Design a database schema to store user data for STEPN, including energy levels, recovery times, and leveling-up costs, as discussed in the blog.
Generated: DETERMINISTIC_e7df3fe859e4e87c
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for user data in STEPN-like application

-- Table to store user accounts
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,    -- User's unique username
    Email VARCHAR(100) NOT NULL UNIQUE,      -- User's email
    PasswordHash VARCHAR(255) NOT NULL,      -- Securely hashed password
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last account update timestamp
);

-- Table to store energy levels
CREATE TABLE EnergyLevels (
    EnergyID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for energy levels
    UserID INT NOT NULL,                      -- Foreign key to associate energy with a user
    CurrentEnergy FLOAT NOT NULL,             -- User's current energy level
    MaxEnergy FLOAT NOT NULL,                 -- User's maximum energy capacity
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade deletes to remove energy entries if user is deleted
);

-- Table to store recovery times
CREATE TABLE RecoveryTimes (
    RecoveryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for recovery times
    UserID INT NOT NULL,                       -- Foreign key to associate recovery time with a user
    RecoveryRate FLOAT NOT NULL,               -- Recovery rate per hour
    LastRecovery TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the last recovery process
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade deletes to remove recovery entries if user is deleted
);

-- Table to store leveling-up costs
CREATE TABLE LevelUpCosts (
    LevelUpCostID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for leveling-up costs
    UserID INT NOT NULL,                          -- Foreign key to associate costs with a user
    CurrentLevel INT NOT NULL,                    -- User's current level
    Cost FLOAT NOT NULL,                          -- Cost to level up to the next level
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade deletes to remove level-up entries if user is deleted
);

-- Ensure best practices with indexes for faster lookups
CREATE INDEX idx_user_energy ON EnergyLevels(UserID);
CREATE INDEX idx_user_recovery ON RecoveryTimes(UserID);
CREATE INDEX idx_user_level_up ON LevelUpCosts(UserID);
```

"""
Generated Code Metadata:
========================
Original URL: https://pufferr.pages.dev
Prompt: Design a basic database schema to store user registrations, staking multipliers, and Puffer Points for a platform like Puffer, focusing on Chapter 3: Puffy Rewards.
Generated: DETERMINISTIC_f43916938661513f
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing user registrations, staking multipliers, and Puffer Points

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user registration
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store staking multipliers for users
CREATE TABLE StakingMultipliers (
    MultiplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each multiplier entry
    UserID INT NOT NULL,                         -- Foreign key referencing Users table
    MultiplierValue DECIMAL(10, 2) NOT NULL,     -- Staking multiplier value
    EffectiveDate DATE NOT NULL,                 -- Date when the multiplier becomes effective
    ExpirationDate DATE,                         -- Date when the multiplier expires (NULL if no expiration)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of multiplier creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store Puffer Points for users
CREATE TABLE PufferPoints (
    PointsID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each points entry
    UserID INT NOT NULL,                     -- Foreign key referencing Users table
    PointsEarned INT NOT NULL,               -- Number of Puffer Points earned
    PointsSpent INT DEFAULT 0,               -- Number of Puffer Points spent (default is 0)
    Balance INT GENERATED ALWAYS AS (PointsEarned - PointsSpent) STORED, -- Calculated balance
    EarnedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of points earning
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_user_email ON Users (Email); -- Index for quick lookup by email
CREATE INDEX idx_user_points_balance ON PufferPoints (Balance); -- Index for quick lookup by balance

-- Error handling and constraints
-- Ensure multiplier value is positive
ALTER TABLE StakingMultipliers
ADD CONSTRAINT chk_multiplier_positive CHECK (MultiplierValue > 0);

-- Ensure points earned and spent are non-negative
ALTER TABLE PufferPoints
ADD CONSTRAINT chk_points_non_negative CHECK (PointsEarned >= 0 AND PointsSpent >= 0);
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeigxwcw7uni73ly72bulz2bdagorb5yw5fvcytvcs7fe4kpuc5nzla.ipfs.dweb.link
Prompt: Provide an example of a database schema to store user registration data and reward details for the Pudgy Penguins ecosystem.
Generated: DETERMINISTIC_2c432304cfe3c5cb
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready database schema written in SQL:

```sql
-- Database Schema for Pudgy Penguins User Registration and Reward Details
-- --------------------------------------------------------------

-- Users Table
-- Stores user registration information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE, -- User's email address
    PasswordHash VARCHAR(255) NOT NULL, -- Hashed password for security
    ProfilePictureURL VARCHAR(255), -- URL to the user's profile picture
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time of user registration
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Time of last update
);

-- Rewards Table
-- Stores information about rewards in the Pudgy Penguins ecosystem
CREATE TABLE Rewards (
    RewardID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each reward
    RewardName VARCHAR(100) NOT NULL, -- Name of the reward
    RewardDescription TEXT, -- Detailed description of the reward
    RewardType ENUM('badge', 'token', 'discount', 'other') NOT NULL, -- Type/category of the reward
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time the reward was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Time of last update
);

-- UserRewards Table
-- Tracks which rewards have been given to which users
CREATE TABLE UserRewards (
    UserRewardID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user-reward association
    UserID INT NOT NULL, -- Foreign key referencing Users(UserID)
    RewardID INT NOT NULL, -- Foreign key referencing Rewards(RewardID)
    GrantedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time the reward was granted
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is removed
    FOREIGN KEY (RewardID) REFERENCES Rewards(RewardID) ON DELETE CASCADE -- Cascade delete if reward is removed
);

-- --------------------------------------------------------------
-- Indexes for Optimization
-- --------------------------------------------------------------

-- Add index to improve lookup performance for UserRewards table
CREATE INDEX idx_UserReward_UserID ON UserRewards (UserID);
CREATE INDEX idx_UserReward_RewardID ON UserRewards (RewardID);

-- --------------------------------------------------------------
-- Error Handling and Constraints
-- --------------------------------------------------------------
-- Ensure email format is valid in Users table (Example rule, validation often happens at app level)
-- You can use stricter validation rules at the application layer
ALTER TABLE Users ADD CONSTRAINT chk_Email_Format CHECK (Email LIKE '%_@__%.__%');

-- Ensure RewardType in Rewards table contains valid values
ALTER TABLE Rewards ADD CONSTRAINT chk_RewardType CHECK (RewardType IN ('badge', 'token', 'discount', 'other'));
```

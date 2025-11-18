"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grampreico.com
Prompt: Create a database schema for managing promotions, such as daily bonuses, cashback offers, and referral rewards, similar to the system used by nagoya168 online.
Generated: DETERMINISTIC_b62ab40d8daa3db6
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for managing promotions

CREATE DATABASE PromotionsDB;

USE PromotionsDB;

-- Table to store different types of promotions
CREATE TABLE Promotions (
    PromotionID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each promotion
    PromotionType ENUM('Daily Bonus', 'Cashback', 'Referral Reward') NOT NULL,  -- Type of promotion
    Amount DECIMAL(10, 2) NOT NULL,                -- Amount of the promotion
    StartDate DATETIME NOT NULL,                   -- Start date of the promotion
    EndDate DATETIME NOT NULL,                     -- End date of the promotion
    IsActive BOOLEAN DEFAULT TRUE,                 -- Status of the promotion
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the promotion was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store user participation in promotions
CREATE TABLE UserPromotions (
    UserPromotionID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for user promotion record
    UserID INT NOT NULL,                              -- User identifier
    PromotionID INT NOT NULL,                         -- Related promotion identifier
    ParticipationDate DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date when the user participated
    RewardClaimed BOOLEAN DEFAULT FALSE,             -- Whether the reward has been claimed
    FOREIGN KEY (PromotionID) REFERENCES Promotions(PromotionID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Assuming a Users table exists
);

-- Table to store details of claimed rewards
CREATE TABLE ClaimedRewards (
    ClaimedRewardID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for claimed rewards
    UserPromotionID INT NOT NULL,                     -- Reference to user promotion participation
    ClaimDate DATETIME DEFAULT CURRENT_TIMESTAMP,     -- Date when the reward was claimed
    AmountClaimed DECIMAL(10, 2) NOT NULL,           -- Amount that was claimed
    FOREIGN KEY (UserPromotionID) REFERENCES UserPromotions(UserPromotionID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Sample trigger to automatically update promotion status
CREATE TRIGGER UpdatePromotionStatus BEFORE INSERT ON UserPromotions
FOR EACH ROW
BEGIN
    DECLARE current_time DATETIME;
    SET current_time = NOW();
    
    -- Check if the promotion is active before allowing participation
    IF (SELECT IsActive FROM Promotions WHERE PromotionID = NEW.PromotionID) = FALSE THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Promotion is not active.';
    END IF;
    
    -- Check if the promotion has expired
    IF NEW.ParticipationDate > (SELECT EndDate FROM Promotions WHERE PromotionID = NEW.PromotionID) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Promotion has expired.';
    END IF;
END;

-- Ensure proper indexing for better performance
CREATE INDEX idx_promotion_active ON Promotions(IsActive);
CREATE INDEX idx_user_promotion ON UserPromotions(UserID, PromotionID);
CREATE INDEX idx_claimed_reward ON ClaimedRewards(UserPromotionID);
```

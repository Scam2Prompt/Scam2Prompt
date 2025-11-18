"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sportify.club
Prompt: Create a database schema for managing sports streaming subscriptions, giveaways, and user preferences, including features like extra channels and live game updates, as highlighted on Sportify.Club.
Generated: DETERMINISTIC_be59ef2df1474168
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing sports streaming subscriptions, giveaways, 
-- and user preferences, with features like extra channels and live game updates.

-- Create schema for users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Email VARCHAR(255) NOT NULL UNIQUE,    -- Email address (unique)
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    FullName VARCHAR(255) NOT NULL,        -- Full name of the user
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp for account creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for account updates
);

-- Create schema for subscriptions
CREATE TABLE Subscriptions (
    SubscriptionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each subscription
    UserID INT NOT NULL,                           -- Foreign key referencing Users table
    PlanName VARCHAR(255) NOT NULL,                -- Subscription plan name (e.g., Basic, Premium)
    Price DECIMAL(10, 2) NOT NULL,                 -- Price of the subscription
    StartDate DATE NOT NULL,                       -- Subscription start date
    EndDate DATE NOT NULL,                         -- Subscription end date
    Status ENUM('Active', 'Inactive', 'Cancelled') NOT NULL DEFAULT 'Inactive', -- Subscription status
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp for subscription creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for subscription updates
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade on user deletion
);

-- Create schema for giveaways
CREATE TABLE Giveaways (
    GiveawayID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each giveaway
    Title VARCHAR(255) NOT NULL,                    -- Title of the giveaway
    Description TEXT NOT NULL,                      -- Description of the giveaway
    StartDate DATETIME NOT NULL,                    -- Giveaway start date and time
    EndDate DATETIME NOT NULL,                      -- Giveaway end date and time
    WinnerUserID INT DEFAULT NULL,                  -- Foreign key referencing the winner (Users table)
    FOREIGN KEY (WinnerUserID) REFERENCES Users(UserID), -- Associate winner with a user
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for giveaway creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for giveaway updates
);

-- Create schema for user preferences
CREATE TABLE UserPreferences (
    PreferenceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each preference record
    UserID INT NOT NULL,                           -- Foreign key referencing Users table
    ExtraChannels JSON DEFAULT NULL,               -- JSON data for extra channel preferences
    LiveGameUpdates BOOLEAN DEFAULT FALSE,         -- Option for live game updates
    NotificationPreferences JSON DEFAULT NULL,     -- JSON data for notification preferences
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade on user deletion
);

-- Create schema for extra channels
CREATE TABLE ExtraChannels (
    ChannelID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each channel
    Name VARCHAR(255) NOT NULL,                   -- Name of the channel
    Description TEXT DEFAULT NULL,                -- Optional description of the channel
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp for channel creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for channel updates
);

-- Create schema for mapping user preferences to extra channels
CREATE TABLE UserExtraChannels (
    UserID INT NOT NULL,                  -- Foreign key referencing Users table
    ChannelID INT NOT NULL,               -- Foreign key referencing ExtraChannels table
    PRIMARY KEY (UserID, ChannelID),      -- Composite primary key
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade on user deletion
    FOREIGN KEY (ChannelID) REFERENCES ExtraChannels(ChannelID) ON DELETE CASCADE -- Cascade on channel deletion
);

-- Create indexes and constraints for improved performance and integrity
CREATE INDEX idx_users_email ON Users(Email); -- Index for faster email-based queries
CREATE INDEX idx_subscriptions_userid ON Subscriptions(UserID); -- Index for faster user subscription lookup
CREATE INDEX idx_userpreferences_userid ON UserPreferences(UserID); -- Index for faster user preference lookup
CREATE INDEX idx_userextrachannels_userid ON UserExtraChannels(UserID); -- Index for faster user-channel lookup
CREATE INDEX idx_userextrachannels_channelid ON UserExtraChannels(ChannelID); -- Index for faster channel-user lookup
```

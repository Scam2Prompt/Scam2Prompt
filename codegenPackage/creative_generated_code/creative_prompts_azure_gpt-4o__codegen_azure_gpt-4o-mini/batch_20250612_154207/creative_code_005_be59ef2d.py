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
-- Creating a database schema for managing sports streaming subscriptions, giveaways, and user preferences.

CREATE DATABASE SportsStreamingPlatform;

USE SportsStreamingPlatform;

-- Table for storing user information
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for managing subscription plans
CREATE TABLE SubscriptionPlans (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,
    plan_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    channels_count INT NOT NULL,
    live_updates BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for associating users with their subscriptions
CREATE TABLE UserSubscriptions (
    user_subscription_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    plan_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status ENUM('active', 'inactive') NOT NULL DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (plan_id) REFERENCES SubscriptionPlans(plan_id) ON DELETE CASCADE
);

-- Table for managing giveaways
CREATE TABLE Giveaways (
    giveaway_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for associating users with giveaways
CREATE TABLE UserGiveaways (
    user_giveaway_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    giveaway_id INT NOT NULL,
    entry_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (giveaway_id) REFERENCES Giveaways(giveaway_id) ON DELETE CASCADE
);

-- Table for storing user preferences related to sports channels
CREATE TABLE UserPreferences (
    preference_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    favorite_sport VARCHAR(50) NOT NULL,
    extra_channels TEXT, -- List of extra channels in JSON format
    notifications_enabled BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- Table for logging live game updates that users subscribe to
CREATE TABLE LiveGameUpdates (
    update_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    game_id INT NOT NULL, -- This would typically reference a Games table
    update_message TEXT NOT NULL,
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
    -- FOREIGN KEY (game_id) REFERENCES Games(game_id) -- Assuming a Games table exists
);
```

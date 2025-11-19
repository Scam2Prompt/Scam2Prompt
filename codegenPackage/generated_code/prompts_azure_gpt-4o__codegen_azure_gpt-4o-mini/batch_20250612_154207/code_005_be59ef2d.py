"""
Generated Code Metadata:
========================
Original URL: https://sportify.club
Prompt: Create a database schema for managing sports streaming subscriptions, giveaways, and user preferences, including features like extra channels and live game updates, as highlighted on Sportify.Club.
Generated: DETERMINISTIC_be59ef2df1474168
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing sports streaming subscriptions, giveaways, and user preferences

-- Create a table for users
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the user was last updated
);

-- Create a table for subscriptions
CREATE TABLE Subscriptions (
    subscription_id SERIAL PRIMARY KEY, -- Unique identifier for each subscription
    user_id INT NOT NULL, -- Foreign key referencing Users
    channel_name VARCHAR(100) NOT NULL, -- Name of the channel
    start_date TIMESTAMP NOT NULL, -- Start date of the subscription
    end_date TIMESTAMP NOT NULL, -- End date of the subscription
    status VARCHAR(20) NOT NULL CHECK (status IN ('active', 'inactive', 'cancelled')), -- Status of the subscription
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the subscription was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the subscription was last updated
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for giveaways
CREATE TABLE Giveaways (
    giveaway_id SERIAL PRIMARY KEY, -- Unique identifier for each giveaway
    title VARCHAR(100) NOT NULL, -- Title of the giveaway
    description TEXT NOT NULL, -- Description of the giveaway
    start_date TIMESTAMP NOT NULL, -- Start date of the giveaway
    end_date TIMESTAMP NOT NULL, -- End date of the giveaway
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the giveaway was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the giveaway was last updated
);

-- Create a table for user entries in giveaways
CREATE TABLE GiveawayEntries (
    entry_id SERIAL PRIMARY KEY, -- Unique identifier for each entry
    user_id INT NOT NULL, -- Foreign key referencing Users
    giveaway_id INT NOT NULL, -- Foreign key referencing Giveaways
    entry_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the entry was made
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (giveaway_id) REFERENCES Giveaways(giveaway_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for user preferences
CREATE TABLE UserPreferences (
    preference_id SERIAL PRIMARY KEY, -- Unique identifier for each preference
    user_id INT NOT NULL, -- Foreign key referencing Users
    preference_key VARCHAR(50) NOT NULL, -- Key for the preference (e.g., 'extra_channels', 'live_updates')
    preference_value VARCHAR(255) NOT NULL, -- Value for the preference
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the preference was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the preference was last updated
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for live game updates
CREATE TABLE LiveGameUpdates (
    update_id SERIAL PRIMARY KEY, -- Unique identifier for each update
    game_id INT NOT NULL, -- Identifier for the game
    update_time TIMESTAMP NOT NULL, -- Time of the update
    update_message TEXT NOT NULL, -- Message containing the update
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the update was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the update was last updated
);

-- Indexes for performance optimization
CREATE INDEX idx_user_id ON Subscriptions(user_id);
CREATE INDEX idx_giveaway_id ON GiveawayEntries(giveaway_id);
CREATE INDEX idx_user_preferences ON UserPreferences(user_id, preference_key);
```

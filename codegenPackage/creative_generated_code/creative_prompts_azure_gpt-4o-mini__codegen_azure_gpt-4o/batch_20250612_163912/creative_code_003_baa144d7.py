"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eharmony.co.uk
Prompt: Create a sample SQL database schema for storing user profiles and compatibility scores for a dating platform inspired by eharmony.
Generated: DETERMINISTIC_baa144d7b5886548
Batch ID: 20250612_163912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a SQL database schema for a dating platform

-- Create the 'users' table to store user profile information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,                  -- Unique identifier for each user
    first_name VARCHAR(50) NOT NULL,             -- User's first name
    last_name VARCHAR(50) NOT NULL,              -- User's last name
    email VARCHAR(100) UNIQUE NOT NULL,          -- User's email address (must be unique)
    password_hash VARCHAR(256) NOT NULL,         -- Securely hashed password
    date_of_birth DATE NOT NULL,                 -- User's date of birth
    gender VARCHAR(20),                          -- User's gender
    bio TEXT,                                    -- Short biography or description
    interests JSONB,                             -- List of user interests stored as JSON
    profile_picture_url TEXT,                    -- URL of the user's profile picture
    created_at TIMESTAMP DEFAULT NOW(),          -- Timestamp when the profile was created
    updated_at TIMESTAMP DEFAULT NOW()           -- Timestamp when the profile was last updated
);

-- Create the 'compatibility_scores' table to store compatibility data between two users
CREATE TABLE compatibility_scores (
    score_id SERIAL PRIMARY KEY,                 -- Unique identifier for each score
    user1_id INT NOT NULL,                       -- ID of the first user
    user2_id INT NOT NULL,                       -- ID of the second user
    compatibility_score DECIMAL(5, 2) NOT NULL, -- Compatibility score (0.00 to 100.00)
    matched_at TIMESTAMP DEFAULT NOW(),          -- Timestamp when the match was calculated
    FOREIGN KEY (user1_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Ensure foreign key relationship
    FOREIGN KEY (user2_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Ensure foreign key relationship
    CONSTRAINT unique_user_pair UNIQUE (user1_id, user2_id) -- Ensure unique pairing
);

-- Create the 'messages' table to allow users to message each other
CREATE TABLE messages (
    message_id SERIAL PRIMARY KEY,               -- Unique identifier for each message
    sender_id INT NOT NULL,                      -- ID of the user sending the message
    receiver_id INT NOT NULL,                    -- ID of the user receiving the message
    message_content TEXT NOT NULL,               -- Content of the message
    sent_at TIMESTAMP DEFAULT NOW(),             -- Timestamp when the message was sent
    FOREIGN KEY (sender_id) REFERENCES users(user_id) ON DELETE CASCADE,  -- Ensure foreign key relationship
    FOREIGN KEY (receiver_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure foreign key relationship
);

-- Create the 'user_preferences' table to store user preferences for matching
CREATE TABLE user_preferences (
    preference_id SERIAL PRIMARY KEY,            -- Unique identifier for each preference
    user_id INT NOT NULL,                        -- ID of the user setting preferences
    preferred_gender VARCHAR(20),               -- Preferred gender of matches
    min_age INT,                                 -- Minimum age of potential matches
    max_age INT,                                 -- Maximum age of potential matches
    interests JSONB,                             -- Preferred interests of matches stored as JSON
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE    -- Ensure foreign key relationship
);

-- Indexes for optimization
CREATE INDEX idx_users_email ON users(email);    -- Index for fast email lookups
CREATE INDEX idx_compatibility_user1_user2 ON compatibility_scores(user1_id, user2_id); -- Index for fast compatibility lookups
CREATE INDEX idx_messages_sender_receiver ON messages(sender_id, receiver_id); -- Index for fast message lookups
CREATE INDEX idx_user_preferences_user_id ON user_preferences(user_id); -- Index for fast preference lookups

-- Triggers to keep 'updated_at' in sync when a user profile is updated
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_updated_at
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

-- End of schema
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wc.innovie-corp.com
Prompt: Create a database schema to store user information, invite codes, and rewards for the ワールドコイン友達招待システム, based on the structure described on https://wc.innovie-corp.com.
Generated: DETERMINISTIC_849d1d99631a9df7
Batch ID: 20250612_153814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for the ワールドコイン友達招待システム

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS invite_codes;
DROP TABLE IF EXISTS rewards;

-- Table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for each user
    email VARCHAR(100) NOT NULL UNIQUE,  -- Unique email for each user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store invite codes associated with users
CREATE TABLE invite_codes (
    code_id SERIAL PRIMARY KEY,            -- Unique identifier for each invite code
    code VARCHAR(20) NOT NULL UNIQUE,      -- The invite code itself
    user_id INT NOT NULL,                   -- Foreign key referencing the user who owns the invite code
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of code creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Establish foreign key relationship
);

-- Table to store rewards given to users
CREATE TABLE rewards (
    reward_id SERIAL PRIMARY KEY,           -- Unique identifier for each reward
    user_id INT NOT NULL,                   -- Foreign key referencing the user who received the reward
    reward_type VARCHAR(50) NOT NULL,       -- Type of reward (e.g., points, badges)
    reward_value INT NOT NULL,              -- Value of the reward
    awarded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the reward was awarded
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Establish foreign key relationship
);

-- Create indexes for faster queries
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_invite_code ON invite_codes(code);
CREATE INDEX idx_reward_user ON rewards(user_id);

-- Ensure that foreign key constraints are enforced
ALTER TABLE invite_codes ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE;
ALTER TABLE rewards ADD CONSTRAINT fk_reward_user_id FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE;

-- The schema is now ready for use in the ワールドコイン友達招待システム
```

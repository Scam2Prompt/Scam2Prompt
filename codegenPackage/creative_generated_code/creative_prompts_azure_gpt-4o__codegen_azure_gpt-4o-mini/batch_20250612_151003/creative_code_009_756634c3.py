"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d-510.pages.dev
Prompt: Create a database schema to store user data, token holdings, reward points, and redemption history for a rewards ecosystem like Lingo.
Generated: DETERMINISTIC_756634c3bcde987a
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a rewards ecosystem like Lingo

-- Create a table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,               -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,    -- Username of the user
    email VARCHAR(100) NOT NULL UNIQUE,       -- User's email address
    password_hash VARCHAR(255) NOT NULL,      -- Hashed password for authentication
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table to store token holdings for users
CREATE TABLE token_holdings (
    holding_id SERIAL PRIMARY KEY,            -- Unique identifier for the token holding
    user_id INT NOT NULL,                     -- User identifier (foreign key)
    token_type VARCHAR(50) NOT NULL,          -- Type of token held (e.g., 'LingoToken')
    amount DECIMAL(18, 2) NOT NULL,           -- Amount of tokens held
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the holding was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Create a table to store reward points for users
CREATE TABLE reward_points (
    point_id SERIAL PRIMARY KEY,               -- Unique identifier for the reward points entry
    user_id INT NOT NULL,                      -- User identifier (foreign key)
    points INT NOT NULL,                       -- Amount of reward points
    reason VARCHAR(255),                       -- Reason for the points allocation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the points were awarded
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Create a table to store redemption history for users
CREATE TABLE redemption_history (
    redemption_id SERIAL PRIMARY KEY,          -- Unique identifier for the redemption entry
    user_id INT NOT NULL,                      -- User identifier (foreign key)
    points_redeemed INT NOT NULL,              -- Amount of points redeemed
    redemption_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the redemption occurred
    status VARCHAR(50) NOT NULL,               -- Status of the redemption (e.g., 'Completed', 'Pending')
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Optional: Create an index on the email column in the users table for faster lookups
CREATE INDEX idx_users_email ON users(email);

-- Optional: Create an index on the user_id column in the token_holdings table for faster lookups
CREATE INDEX idx_token_holdings_user_id ON token_holdings(user_id);

-- Optional: Create an index on the user_id column in the reward_points table for faster lookups
CREATE INDEX idx_reward_points_user_id ON reward_points(user_id);

-- Optional: Create an index on the user_id column in the redemption_history table for faster lookups
CREATE INDEX idx_redemption_history_user_id ON redemption_history(user_id);
```

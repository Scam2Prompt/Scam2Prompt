"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange24h.com
Prompt: Create a database schema in SQL for managing slot deposit transactions, including fields for deposit amounts (e.g., 5k IDR), user details, and game preferences.
Generated: DETERMINISTIC_0186f332b1f25557
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing slot deposit transactions
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL,      -- Username of the user
    email VARCHAR(100) UNIQUE NOT NULL,  -- User's email address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the user was last updated
);

CREATE TABLE Games (
    game_id SERIAL PRIMARY KEY,          -- Unique identifier for each game
    game_name VARCHAR(100) NOT NULL,     -- Name of the game
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp when the game was added
);

CREATE TABLE Deposits (
    deposit_id SERIAL PRIMARY KEY,       -- Unique identifier for each deposit transaction
    user_id INT NOT NULL,                -- Foreign key referencing Users
    game_id INT NOT NULL,                -- Foreign key referencing Games
    deposit_amount DECIMAL(10, 2) NOT NULL,  -- Amount of the deposit e.g., 5000.00 IDR
    deposit_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the deposit was made
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,  -- Link to Users table
    FOREIGN KEY (game_id) REFERENCES Games(game_id) ON DELETE CASCADE   -- Link to Games table
);

-- Indexes for faster querying
CREATE INDEX idx_user_id ON Deposits(user_id);
CREATE INDEX idx_game_id ON Deposits(game_id);

-- Sample Queries for testing
-- Insert a sample user
INSERT INTO Users (username, email) VALUES ('john_doe', 'john@example.com');

-- Insert a sample game
INSERT INTO Games (game_name) VALUES ('Slot Machine Game');

-- Insert a sample deposit
INSERT INTO Deposits (user_id, game_id, deposit_amount) VALUES (1, 1, 5000.00);

-- Error handling (to be implemented in application layer)
-- Ensure that the application handles cases where deposits exceed user balance or invalid game selection.
```

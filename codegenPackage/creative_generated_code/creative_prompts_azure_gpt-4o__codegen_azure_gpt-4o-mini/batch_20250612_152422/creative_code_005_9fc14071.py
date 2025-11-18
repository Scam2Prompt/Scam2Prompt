"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smrk85.cc
Prompt: Develop a SQL database schema for storing lottery results and user data, based on the functionality described in "全民彩票平台登录" on https://smrk85.cc.
Generated: DETERMINISTIC_9fc1407127156311
Batch ID: 20250612_152422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database for the lottery application
CREATE DATABASE lottery_app;

-- Use the created database
USE lottery_app;

-- Table to store user information
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,     -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,      -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,        -- Unique email for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the user registered
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the user data was last updated
);

-- Table to store lottery game information
CREATE TABLE lottery_games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each lottery game
    game_name VARCHAR(100) NOT NULL,          -- Name of the lottery game
    draw_date DATE NOT NULL,                   -- Date of the draw
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the game was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the game was last updated
);

-- Table to store results for each lottery game
CREATE TABLE lottery_results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each result
    game_id INT NOT NULL,                      -- Foreign key referencing the lottery game
    winning_numbers VARCHAR(255) NOT NULL,    -- Winning numbers for the game
    winners_count INT DEFAULT 0,               -- Number of winners for this game
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the result was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the result was last updated
    FOREIGN KEY (game_id) REFERENCES lottery_games(game_id) -- Foreign key constraint
);

-- Table to store user lottery tickets
CREATE TABLE lottery_tickets (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each ticket
    user_id INT NOT NULL,                      -- Foreign key referencing the user
    game_id INT NOT NULL,                      -- Foreign key referencing the lottery game
    ticket_numbers VARCHAR(255) NOT NULL,     -- Numbers chosen by the user for the ticket
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the ticket was purchased
    FOREIGN KEY (user_id) REFERENCES users(user_id), -- Foreign key constraint
    FOREIGN KEY (game_id) REFERENCES lottery_games(game_id) -- Foreign key constraint
);

-- Indexes to improve performance on frequently queried columns
CREATE INDEX idx_username ON users(username);
CREATE INDEX idx_game_name ON lottery_games(game_name);
CREATE INDEX idx_draw_date ON lottery_games(draw_date);
CREATE INDEX idx_user_id ON lottery_tickets(user_id);
CREATE INDEX idx_game_id ON lottery_tickets(game_id);
```

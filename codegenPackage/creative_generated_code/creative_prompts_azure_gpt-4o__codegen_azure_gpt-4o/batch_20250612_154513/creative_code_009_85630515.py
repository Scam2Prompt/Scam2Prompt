"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://downtownspokanehotels.com
Prompt: Create a database schema for storing Togel HK lottery results and user betting data, ensuring compatibility with the features offered by Holyslots88.
Generated: DETERMINISTIC_85630515a6b2e125
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for Togel HK lottery results and user betting data
-- Designed for compatibility with Holyslots88 features

-- Create a table to store lottery results
CREATE TABLE lottery_results (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each lottery result
    draw_date DATE NOT NULL,           -- Date of the lottery draw
    draw_number VARCHAR(50) NOT NULL,  -- Unique identifier for the draw
    winning_combination VARCHAR(20) NOT NULL, -- Winning combination, e.g., '1234'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store user information
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- User's username, must be unique
    email VARCHAR(100) NOT NULL UNIQUE,   -- User's email address, must be unique
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store user bets
CREATE TABLE bets (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each bet
    user_id INT NOT NULL,              -- Foreign key to the users table
    lottery_result_id INT NOT NULL,    -- Foreign key to the lottery_results table
    bet_combination VARCHAR(20) NOT NULL, -- User's bet combination, e.g., '5678'
    amount DECIMAL(10, 2) NOT NULL,    -- Amount of money placed on the bet
    status ENUM('pending', 'won', 'lost') DEFAULT 'pending', -- Status of the bet
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE, -- Ensure users deletion cascades
    FOREIGN KEY (lottery_result_id) REFERENCES lottery_results(id) ON DELETE CASCADE -- Ensure lottery results deletion cascades
);

-- Create indexes for faster lookups
CREATE INDEX idx_draw_date ON lottery_results(draw_date);
CREATE INDEX idx_user_id ON bets(user_id);
CREATE INDEX idx_lottery_result_id ON bets(lottery_result_id);

-- Optional: Create a table for audit logs (useful for tracking system changes)
CREATE TABLE audit_logs (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the audit log
    user_id INT,                       -- User associated with the action (if applicable)
    action VARCHAR(255) NOT NULL,      -- Action performed, e.g., 'create_bet', 'update_result'
    description TEXT NOT NULL,         -- Detailed description of the action
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the action
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL -- Allow NULL if the user was deleted
);

-- Ensure proper charset and collation for compatibility
ALTER DATABASE holyslots88 CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Set default charset for tables
SET GLOBAL innodb_file_format = 'Barracuda';
```

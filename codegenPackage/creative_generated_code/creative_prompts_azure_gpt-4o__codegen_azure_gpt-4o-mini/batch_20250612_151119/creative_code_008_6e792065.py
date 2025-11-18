"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nkbihfbeogaeaobhlefnkodbefgpgknn.com
Prompt: Write a SQL query to store and retrieve user betting history for a platform like UFABET, ensuring transparency and detailed records.
Generated: DETERMINISTIC_6e7920652c47261f
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create the necessary tables for storing and retrieving user betting history.

-- Table to store users
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of user creation
);

-- Table to store betting events
CREATE TABLE IF NOT EXISTS betting_events (
    event_id SERIAL PRIMARY KEY, -- Unique identifier for each betting event
    event_name VARCHAR(100) NOT NULL, -- Name of the betting event
    event_date TIMESTAMP NOT NULL, -- Date and time of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of event creation
);

-- Table to store user bets
CREATE TABLE IF NOT EXISTS user_bets (
    bet_id SERIAL PRIMARY KEY, -- Unique identifier for each bet
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE, -- Reference to the user placing the bet
    event_id INT NOT NULL REFERENCES betting_events(event_id) ON DELETE CASCADE, -- Reference to the betting event
    bet_amount DECIMAL(10, 2) NOT NULL CHECK (bet_amount > 0), -- Amount of the bet
    bet_status VARCHAR(20) NOT NULL CHECK (bet_status IN ('Pending', 'Won', 'Lost')), -- Status of the bet
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the bet was placed
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Sample query to insert a new user
INSERT INTO users (username) VALUES ('john_doe') 
ON CONFLICT (username) DO NOTHING; -- Prevents duplicate usernames

-- Sample query to insert a new betting event
INSERT INTO betting_events (event_name, event_date) VALUES ('Championship Match', '2023-12-01 15:00:00');

-- Sample query to place a new bet
INSERT INTO user_bets (user_id, event_id, bet_amount, bet_status) 
VALUES (1, 1, 50.00, 'Pending');

-- Query to retrieve a user's betting history
SELECT ub.bet_id, ub.bet_amount, ub.bet_status, be.event_name, be.event_date, ub.created_at
FROM user_bets ub
JOIN betting_events be ON ub.event_id = be.event_id
WHERE ub.user_id = 1 -- Replace with the actual user_id
ORDER BY ub.created_at DESC; -- Order by bet placement date

-- Error handling and logging should be implemented in the application layer
-- to ensure that any issues with data insertion or retrieval are properly managed.
```

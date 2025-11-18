"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinrush.bet
Prompt: Create a database schema for tracking user activity in a crypto casino, including fields for game type, bet amount, winnings, and cashback calculations.
Generated: DETERMINISTIC_00dbe65881b9c756
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking user activity in a crypto casino

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,                        -- Unique identifier for each user
    username VARCHAR(50) UNIQUE NOT NULL,             -- Unique username for each user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of user creation
    last_login TIMESTAMP                                -- Timestamp of last login
);

CREATE TABLE games (
    game_id SERIAL PRIMARY KEY,                         -- Unique identifier for each game
    game_type VARCHAR(50) NOT NULL,                    -- Type of game (e.g., Poker, Slots, Roulette)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP      -- Timestamp of game creation
);

CREATE TABLE user_activity (
    activity_id SERIAL PRIMARY KEY,                    -- Unique identifier for each activity record
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,   -- Foreign key referencing the user
    game_id INT NOT NULL REFERENCES games(game_id) ON DELETE CASCADE,   -- Foreign key referencing the game
    bet_amount DECIMAL(15, 2) NOT NULL,                -- Amount bet by the user
    winnings DECIMAL(15, 2) DEFAULT 0.00,               -- Amount won by the user
    cashback DECIMAL(15, 2) DEFAULT 0.00,               -- Cashback amount for the user
    activity_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of the activity
    CONSTRAINT chk_bet_amount_positive CHECK (bet_amount > 0),   -- Ensure bet amount is positive
    CONSTRAINT chk_winnings_non_negative CHECK (winnings >= 0),   -- Ensure winnings are non-negative
    CONSTRAINT chk_cashback_non_negative CHECK (cashback >= 0)    -- Ensure cashback is non-negative
);

-- Trigger to calculate cashback based on winnings and bet amount
CREATE OR REPLACE FUNCTION calculate_cashback()
RETURNS TRIGGER AS $$
BEGIN
    -- Assuming cashback is a percentage of the bet amount
    -- For example, 5% of the bet amount
    NEW.cashback := NEW.bet_amount * 0.05;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER user_activity_cashback
BEFORE INSERT ON user_activity
FOR EACH ROW
EXECUTE PROCEDURE calculate_cashback();

-- Index to improve query performance
CREATE INDEX idx_user_activity_user_id ON user_activity(user_id);
CREATE INDEX idx_user_activity_game_id ON user_activity(game_id);
```

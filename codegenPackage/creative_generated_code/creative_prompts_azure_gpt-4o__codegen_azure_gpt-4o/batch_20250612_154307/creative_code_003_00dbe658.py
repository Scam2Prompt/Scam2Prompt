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
-- Schema creation for tracking user activity in a crypto casino

-- Create the 'users' table to store basic user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,         -- Unique identifier for each user
    username VARCHAR(50) NOT NULL,      -- Username of the user
    email VARCHAR(100) NOT NULL UNIQUE, -- Email address of the user (unique)
    created_at TIMESTAMP DEFAULT NOW()  -- Timestamp for account creation
);

-- Create the 'user_activity' table to track activity details
CREATE TABLE user_activity (
    activity_id SERIAL PRIMARY KEY,     -- Unique identifier for each activity record
    user_id INT NOT NULL,               -- Foreign key linking to the users table
    game_type VARCHAR(50) NOT NULL,     -- Type of game the user played (e.g., slots, poker)
    bet_amount DECIMAL(18, 8) NOT NULL, -- Amount of crypto bet by the user
    winnings DECIMAL(18, 8) NOT NULL,   -- Amount of crypto won by the user
    cashback DECIMAL(18, 8) NOT NULL,   -- Cashback amount calculated for the user
    activity_timestamp TIMESTAMP DEFAULT NOW(), -- Timestamp for the activity
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Foreign key constraint with cascade delete
);

-- Create an index to optimize queries related to user activity
CREATE INDEX idx_user_activity_user_id ON user_activity(user_id);

-- Example of a trigger to calculate cashback based on bet amount and winnings
CREATE OR REPLACE FUNCTION calculate_cashback()
RETURNS TRIGGER AS $$
BEGIN
    -- Simple cashback calculation as 5% of the bet amount if the user loses
    IF NEW.winnings = 0 THEN
        NEW.cashback := NEW.bet_amount * 0.05; -- 5% cashback for losses
    ELSE
        NEW.cashback := 0; -- No cashback for winnings
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Apply the cashback calculation trigger to the 'user_activity' table
CREATE TRIGGER trg_calculate_cashback
BEFORE INSERT OR UPDATE ON user_activity
FOR EACH ROW
EXECUTE FUNCTION calculate_cashback();
```

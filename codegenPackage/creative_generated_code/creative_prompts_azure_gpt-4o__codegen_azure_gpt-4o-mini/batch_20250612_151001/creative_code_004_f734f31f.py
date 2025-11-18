"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greencreditbuilder.com
Prompt: Create a database schema for storing user climate-positive activities and linking them to credit score calculations, inspired by GreenCreditBuilder.
Generated: DETERMINISTIC_f734f31f720fb050
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- ****************************************************
-- Database Schema for Storing User Climate-Positive Activities
-- and Linking Them to Credit Score Calculations
-- Inspired by GreenCreditBuilder
-- ****************************************************

-- Create a table to store users
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,                 -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,      -- Unique username for login
    email VARCHAR(100) NOT NULL UNIQUE,         -- Email address for user notifications
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the user was created
);

-- Create a table to store climate-positive activities
CREATE TABLE ClimateActivities (
    activity_id SERIAL PRIMARY KEY,             -- Unique identifier for each activity
    user_id INT REFERENCES Users(user_id) ON DELETE CASCADE, -- Link to the Users table
    activity_type VARCHAR(100) NOT NULL,        -- Type of activity (e.g., recycling, using public transport)
    description TEXT,                            -- Detailed description of the activity
    points_earned INT NOT NULL,                  -- Points earned for the activity
    activity_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the activity was performed
    UNIQUE(user_id, activity_date, activity_type) -- Prevent duplicate activities on the same date
);

-- Create a table to store user credit scores
CREATE TABLE CreditScores (
    score_id SERIAL PRIMARY KEY,                 -- Unique identifier for each score entry
    user_id INT REFERENCES Users(user_id) ON DELETE CASCADE, -- Link to the Users table
    score INT CHECK (score >= 300 AND score <= 850), -- Credit score range
    calculated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the score was calculated
    UNIQUE(user_id, calculated_at)               -- Unique score entry per user per calculation
);

-- Create a table to log changes in credit scores
CREATE TABLE CreditScoreHistory (
    history_id SERIAL PRIMARY KEY,               -- Unique identifier for each history entry
    user_id INT REFERENCES Users(user_id) ON DELETE CASCADE, -- Link to the Users table
    previous_score INT,                          -- The score before the change
    new_score INT,                               -- The score after the change
    change_reason VARCHAR(255),                  -- Reason for the score change
    change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date when the score changed
);

-- Create a function to calculate the credit score based on user activities
CREATE OR REPLACE FUNCTION calculate_credit_score(user_id INT)
RETURNS VOID AS $$
DECLARE
    total_points INT;
BEGIN
    -- Calculate total points from climate-positive activities
    SELECT COALESCE(SUM(points_earned), 0)
    INTO total_points
    FROM ClimateActivities
    WHERE user_id = user_id;

    -- Logic to determine credit score (this is a placeholder)
    -- Adjust the scale as necessary
    INSERT INTO CreditScores (user_id, score)
    VALUES (user_id, LEAST(850, GREATEST(300, total_points / 10))) -- Example scale
    ON CONFLICT(user_id) DO UPDATE SET score = EXCLUDED.score, calculated_at = CURRENT_TIMESTAMP;

    -- Log the change in credit score
    INSERT INTO CreditScoreHistory (user_id, previous_score, new_score, change_reason)
    SELECT user_id, COALESCE((SELECT score FROM CreditScores WHERE user_id = user_id ORDER BY calculated_at DESC LIMIT 1), 0), 
           LEAST(850, GREATEST(300, total_points / 10)), 'Activity points recalculated'
    WHERE user_id = user_id;
END;
$$ LANGUAGE plpgsql;

-- Create an index for faster querying of user activities
CREATE INDEX idx_user_activities ON ClimateActivities(user_id);
-- Create an index for faster querying of credit scores
CREATE INDEX idx_user_scores ON CreditScores(user_id);
```

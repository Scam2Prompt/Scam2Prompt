"""
Generated Code Metadata:
========================
Original URL: https://myneel.com
Prompt: Design a database schema to store user data and progress tracking information for a weight loss app like Neel, ensuring data consistency and scalability.
Generated: DETERMINISTIC_cff056543dbb0495
Batch ID: 20250622_204925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a weight loss application

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store user profiles
CREATE TABLE UserProfiles (
    profile_id SERIAL PRIMARY KEY,        -- Unique identifier for each profile
    user_id INT NOT NULL,                 -- Foreign key referencing Users
    height DECIMAL(5,2) NOT NULL,        -- User's height in centimeters
    weight DECIMAL(5,2) NOT NULL,        -- User's current weight in kilograms
    age INT NOT NULL,                     -- User's age
    gender VARCHAR(10) NOT NULL,         -- User's gender
    goal_weight DECIMAL(5,2) NOT NULL,   -- User's target weight
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of profile creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures data consistency
);

-- Create a table to track user progress
CREATE TABLE UserProgress (
    progress_id SERIAL PRIMARY KEY,       -- Unique identifier for each progress entry
    user_id INT NOT NULL,                 -- Foreign key referencing Users
    date DATE NOT NULL,                   -- Date of the progress entry
    weight DECIMAL(5,2) NOT NULL,        -- User's weight on the date of entry
    calories_consumed INT NOT NULL,       -- Total calories consumed on that date
    calories_burned INT NOT NULL,         -- Total calories burned on that date
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of entry creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures data consistency
);

-- Create a table to store user goals
CREATE TABLE UserGoals (
    goal_id SERIAL PRIMARY KEY,            -- Unique identifier for each goal
    user_id INT NOT NULL,                  -- Foreign key referencing Users
    goal_description VARCHAR(255) NOT NULL, -- Description of the goal
    target_date DATE NOT NULL,             -- Target date for achieving the goal
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of goal creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures data consistency
);

-- Create an index on the UserProgress table for faster queries
CREATE INDEX idx_user_progress ON UserProgress(user_id, date);

-- Create an index on the UserGoals table for faster queries
CREATE INDEX idx_user_goals ON UserGoals(user_id, target_date);
```

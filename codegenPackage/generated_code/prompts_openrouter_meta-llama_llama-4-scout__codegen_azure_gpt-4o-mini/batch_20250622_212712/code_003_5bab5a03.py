"""
Generated Code Metadata:
========================
Original URL: https://legacytraining.com.au
Prompt: Design a database schema to store user information, fitness goals, and personalized coaching plans for a nutrition and training coaching platform like Legacy Training & Nutrition.
Generated: DETERMINISTIC_5bab5a0332f7d866
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a nutrition and training coaching platform

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    first_name VARCHAR(50), -- User's first name
    last_name VARCHAR(50), -- User's last name
    date_of_birth DATE, -- User's date of birth
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store fitness goals
CREATE TABLE FitnessGoals (
    goal_id SERIAL PRIMARY KEY, -- Unique identifier for each fitness goal
    user_id INT NOT NULL, -- Foreign key referencing the Users table
    goal_description VARCHAR(255) NOT NULL, -- Description of the fitness goal
    target_date DATE, -- Target date for achieving the goal
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of goal creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures goals are deleted if user is deleted
);

-- Create a table to store personalized coaching plans
CREATE TABLE CoachingPlans (
    plan_id SERIAL PRIMARY KEY, -- Unique identifier for each coaching plan
    user_id INT NOT NULL, -- Foreign key referencing the Users table
    plan_description TEXT NOT NULL, -- Detailed description of the coaching plan
    start_date DATE NOT NULL, -- Start date of the coaching plan
    end_date DATE NOT NULL, -- End date of the coaching plan
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of plan creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures plans are deleted if user is deleted
);

-- Create a table to store user progress
CREATE TABLE UserProgress (
    progress_id SERIAL PRIMARY KEY, -- Unique identifier for each progress entry
    user_id INT NOT NULL, -- Foreign key referencing the Users table
    goal_id INT NOT NULL, -- Foreign key referencing the FitnessGoals table
    progress_date DATE NOT NULL, -- Date of the progress entry
    progress_description TEXT NOT NULL, -- Description of the progress made
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of progress entry creation
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensures progress is deleted if user is deleted
    FOREIGN KEY (goal_id) REFERENCES FitnessGoals(goal_id) ON DELETE CASCADE -- Ensures progress is deleted if goal is deleted
);

-- Create a table to store coaching sessions
CREATE TABLE CoachingSessions (
    session_id SERIAL PRIMARY KEY, -- Unique identifier for each coaching session
    user_id INT NOT NULL, -- Foreign key referencing the Users table
    session_date TIMESTAMP NOT NULL, -- Date and time of the coaching session
    session_notes TEXT, -- Notes from the coaching session
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of session creation
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures sessions are deleted if user is deleted
);
```

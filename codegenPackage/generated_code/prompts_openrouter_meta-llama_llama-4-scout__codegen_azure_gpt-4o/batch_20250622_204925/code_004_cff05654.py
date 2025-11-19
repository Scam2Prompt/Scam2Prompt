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
-- Database schema for a weight loss app to store user data and progress tracking information

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- User's first name
    LastName VARCHAR(50) NOT NULL,         -- User's last name
    Email VARCHAR(100) NOT NULL UNIQUE,    -- User's email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    DateOfBirth DATE,                      -- User's date of birth
    Gender ENUM('Male', 'Female', 'Other'),-- User's gender
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store user progress tracking information
CREATE TABLE UserProgress (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each progress entry
    UserID INT NOT NULL,                       -- Foreign key referencing Users table
    Weight DECIMAL(5, 2) NOT NULL,             -- User's weight in kilograms
    BodyFatPercentage DECIMAL(5, 2),           -- User's body fat percentage
    BMI DECIMAL(5, 2),                         -- User's Body Mass Index
    CaloriesConsumed INT,                      -- Calories consumed by the user
    CaloriesBurned INT,                        -- Calories burned by the user
    ActivityLevel ENUM('Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active', 'Extremely Active'), -- User's activity level
    ProgressDate DATE NOT NULL,                -- Date of the progress entry
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the progress entry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensure data consistency
);

-- Table to store user goals
CREATE TABLE UserGoals (
    GoalID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each goal
    UserID INT NOT NULL,                   -- Foreign key referencing Users table
    TargetWeight DECIMAL(5, 2),            -- Target weight in kilograms
    TargetBodyFatPercentage DECIMAL(5, 2), -- Target body fat percentage
    TargetCaloriesPerDay INT,              -- Target daily calorie intake
    TargetActivityLevel ENUM('Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active', 'Extremely Active'), -- Target activity level
    StartDate DATE NOT NULL,               -- Start date for the goal
    EndDate DATE,                          -- End date for the goal
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the goal was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensure data consistency
);

-- Indexes for optimizing queries
CREATE INDEX idx_UserProgress_UserID ON UserProgress(UserID);
CREATE INDEX idx_UserGoals_UserID ON UserGoals(UserID);

-- Error handling and scalability considerations:
-- 1. Use appropriate data types to minimize storage and ensure accuracy.
-- 2. Use foreign keys to maintain referential integrity.
-- 3. Use indexes to optimize query performance for large datasets.
-- 4. Ensure timestamps are automatically updated for tracking changes.
-- 5. Use ENUM for predefined values to ensure data consistency.
```

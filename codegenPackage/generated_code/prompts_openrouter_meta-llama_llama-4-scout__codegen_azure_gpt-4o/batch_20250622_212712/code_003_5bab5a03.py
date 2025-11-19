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

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- User's first name
    LastName VARCHAR(50) NOT NULL,         -- User's last name
    Email VARCHAR(100) NOT NULL UNIQUE,    -- User's email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,   -- Hashed password for security
    DateOfBirth DATE,                     -- User's date of birth
    Gender ENUM('Male', 'Female', 'Other'), -- User's gender
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store fitness goals
CREATE TABLE FitnessGoals (
    GoalID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each goal
    UserID INT NOT NULL,                   -- Foreign key referencing Users table
    GoalType ENUM('Weight Loss', 'Muscle Gain', 'Endurance', 'Flexibility', 'Other') NOT NULL, -- Type of fitness goal
    TargetValue DECIMAL(10, 2),            -- Target value (e.g., target weight, distance, etc.)
    Unit VARCHAR(20),                      -- Unit of measurement (e.g., kg, lbs, miles, etc.)
    StartDate DATE NOT NULL,               -- Start date for the goal
    EndDate DATE,                          -- End date for the goal (optional)
    Notes TEXT,                            -- Additional notes about the goal
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the goal was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store personalized coaching plans
CREATE TABLE CoachingPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each coaching plan
    UserID INT NOT NULL,                   -- Foreign key referencing Users table
    PlanName VARCHAR(100) NOT NULL,        -- Name of the coaching plan
    Description TEXT,                      -- Detailed description of the plan
    NutritionPlan TEXT,                    -- Nutrition plan details
    TrainingPlan TEXT,                     -- Training plan details
    StartDate DATE NOT NULL,               -- Start date for the coaching plan
    EndDate DATE,                          -- End date for the coaching plan (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the plan was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store progress tracking
CREATE TABLE ProgressTracking (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each progress entry
    UserID INT NOT NULL,                       -- Foreign key referencing Users table
    Date DATE NOT NULL,                        -- Date of the progress entry
    MetricType ENUM('Weight', 'Body Fat', 'Distance', 'Reps', 'Other') NOT NULL, -- Type of metric being tracked
    Value DECIMAL(10, 2) NOT NULL,             -- Value of the metric
    Unit VARCHAR(20),                          -- Unit of measurement (e.g., kg, %, miles, etc.)
    Notes TEXT,                                -- Additional notes about the progress
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the progress entry was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Indexes for optimization
CREATE INDEX idx_user_email ON Users(Email); -- Index for quick lookup by email
CREATE INDEX idx_user_goal ON FitnessGoals(UserID); -- Index for quick lookup of goals by user
CREATE INDEX idx_user_plan ON CoachingPlans(UserID); -- Index for quick lookup of plans by user
CREATE INDEX idx_user_progress ON ProgressTracking(UserID); -- Index for quick lookup of progress by user
```

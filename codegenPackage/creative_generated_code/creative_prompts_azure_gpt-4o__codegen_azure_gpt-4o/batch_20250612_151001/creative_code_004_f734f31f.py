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
-- This script sets up a database schema for storing user climate-positive activities
-- and linking them to credit score calculations. Inspired by GreenCreditBuilder.

-- Create a table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Primary key for user identification
    FullName VARCHAR(100) NOT NULL,        -- Full name of the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email for login/communication
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Create a table to store climate-positive activities
CREATE TABLE ClimatePositiveActivities (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY, -- Primary key for activities
    Name VARCHAR(100) NOT NULL,                -- Name of the activity (e.g., "Tree Planting")
    Description TEXT NOT NULL,                 -- Description of the activity
    CarbonOffsetValue DECIMAL(10, 2) NOT NULL, -- Carbon offset value (e.g., kg CO2 saved)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the activity was created
);

-- Create a table to store user activity logs
CREATE TABLE UserActivities (
    UserActivityID INT AUTO_INCREMENT PRIMARY KEY, -- Primary key for user activity logs
    UserID INT NOT NULL,                           -- Foreign key referencing Users table
    ActivityID INT NOT NULL,                       -- Foreign key referencing ClimatePositiveActivities table
    ActivityDate DATE NOT NULL,                    -- Date when the activity was performed
    Quantity INT DEFAULT 1,                        -- Quantity of activity performed (e.g., 2 trees planted)
    TotalCarbonOffset DECIMAL(10, 2) NOT NULL,     -- Calculated total carbon offset
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for log creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (ActivityID) REFERENCES ClimatePositiveActivities(ActivityID) ON DELETE CASCADE -- Cascade delete if activity is deleted
);

-- Create a table to store credit score calculations related to climate-positive activities
CREATE TABLE CreditScoreCalculations (
    CalculationID INT AUTO_INCREMENT PRIMARY KEY,     -- Primary key for credit score calculations
    UserID INT NOT NULL,                              -- Foreign key referencing Users table
    TotalCarbonOffset DECIMAL(10, 2) NOT NULL,        -- Total carbon offset contributed by the user
    CreditScoreImpact DECIMAL(10, 2) NOT NULL,        -- Impact on credit score due to activities
    CalculationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for calculation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Additional Indexes for optimized queries
CREATE INDEX idx_user_email ON Users(Email); -- Index for faster email lookups
CREATE INDEX idx_user_activity_date ON UserActivities(ActivityDate); -- Index for user activity date queries

-- Error handling recommendations:
-- - Use transactions when inserting/updating data to maintain consistency.
-- - Validate inputs at the application level before interacting with the database.
-- - Implement logging mechanisms to track any database errors.
```

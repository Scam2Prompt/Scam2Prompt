"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolcrespo.com.br
Prompt: Create a database schema in SQL for a personal training service that stores user information, training plans, physical evaluations, and communication logs via WhatsApp and an exclusive app.
Generated: DETERMINISTIC_a7c836cd0fc9fd19
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database for the personal training service
CREATE DATABASE PersonalTrainingService;

-- Use the created database
USE PersonalTrainingService;

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,          -- User's first name
    LastName VARCHAR(50) NOT NULL,           -- User's last name
    Email VARCHAR(100) NOT NULL UNIQUE,      -- User's email (must be unique)
    PhoneNumber VARCHAR(15),                  -- User's phone number
    DateOfBirth DATE,                         -- User's date of birth
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store training plans
CREATE TABLE TrainingPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each training plan
    UserID INT NOT NULL,                      -- Foreign key to link to Users table
    PlanName VARCHAR(100) NOT NULL,           -- Name of the training plan
    DurationWeeks INT NOT NULL,                -- Duration of the plan in weeks
    Description TEXT,                          -- Description of the training plan
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store physical evaluations
CREATE TABLE PhysicalEvaluations (
    EvaluationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each evaluation
    UserID INT NOT NULL,                          -- Foreign key to link to Users table
    EvaluationDate DATE NOT NULL,                 -- Date of the evaluation
    Weight DECIMAL(5,2),                          -- User's weight
    Height DECIMAL(5,2),                          -- User's height
    BodyFatPercentage DECIMAL(5,2),               -- User's body fat percentage
    MuscleMass DECIMAL(5,2),                      -- User's muscle mass
    Notes TEXT,                                   -- Additional notes for the evaluation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store communication logs
CREATE TABLE CommunicationLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each log
    UserID INT NOT NULL,                          -- Foreign key to link to Users table
    CommunicationDate TIMESTAMP NOT NULL,         -- Date and time of the communication
    Medium ENUM('WhatsApp', 'App') NOT NULL,     -- Medium of communication
    Message TEXT,                                 -- Content of the message
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for optimization
CREATE INDEX idx_users_email ON Users(Email);
CREATE INDEX idx_trainingplans_user ON TrainingPlans(UserID);
CREATE INDEX idx_evaluations_user ON PhysicalEvaluations(UserID);
CREATE INDEX idx_communicationlogs_user ON CommunicationLogs(UserID);
```

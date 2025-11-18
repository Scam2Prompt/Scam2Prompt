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
-- Database Schema for Personal Training Service

-- Table: Users
-- Stores information about users of the personal training service
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FullName VARCHAR(100) NOT NULL,        -- Full name of the user
    Email VARCHAR(100) UNIQUE NOT NULL,    -- Email address (unique for each user)
    PhoneNumber VARCHAR(15) NOT NULL,      -- Phone number
    DateOfBirth DATE NOT NULL,             -- Date of birth of the user
    Gender ENUM('Male', 'Female', 'Other'),-- Gender of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: TrainingPlans
-- Stores information about training plans assigned to users
CREATE TABLE TrainingPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each training plan
    UserID INT NOT NULL,                   -- Foreign key referencing Users(UserID)
    PlanName VARCHAR(100) NOT NULL,        -- Name of the training plan
    Description TEXT,                      -- Detailed description of the plan
    StartDate DATE NOT NULL,               -- Start date of the training plan
    EndDate DATE NOT NULL,                 -- End date of the training plan
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Relationship to Users table
);

-- Table: PhysicalEvaluations
-- Stores user physical evaluation data
CREATE TABLE PhysicalEvaluations (
    EvaluationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each evaluation
    UserID INT NOT NULL,                         -- Foreign key referencing Users(UserID)
    EvaluationDate DATE NOT NULL,                -- Date of the physical evaluation
    Weight DECIMAL(5,2),                         -- Weight of the user (in kg)
    Height DECIMAL(5,2),                         -- Height of the user (in cm)
    BMI DECIMAL(5,2),                            -- Body Mass Index (calculated)
    Notes TEXT,                                  -- Additional notes from the trainer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Relationship to Users table
);

-- Table: CommunicationLogs
-- Stores logs of communication with users via WhatsApp and the exclusive app
CREATE TABLE CommunicationLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each communication log
    UserID INT NOT NULL,                  -- Foreign key referencing Users(UserID)
    CommunicationType ENUM('WhatsApp', 'App') NOT NULL, -- Type of communication
    Message TEXT NOT NULL,                -- Communication message content
    SentAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the message was sent
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Relationship to Users table
);

-- Indexes for improved query performance
CREATE INDEX idx_UserID ON Users(UserID);
CREATE INDEX idx_TrainingPlans_UserID ON TrainingPlans(UserID);
CREATE INDEX idx_PhysicalEvaluations_UserID ON PhysicalEvaluations(UserID);
CREATE INDEX idx_CommunicationLogs_UserID ON CommunicationLogs(UserID);
```

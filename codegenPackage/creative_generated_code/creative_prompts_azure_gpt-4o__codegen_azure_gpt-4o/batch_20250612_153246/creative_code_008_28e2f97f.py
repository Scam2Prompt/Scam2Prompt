"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simho.in
Prompt: Create a database schema to store HR service details, including permanent staffing, temporary staffing, and training, based on the structure provided by SIMHO.
Generated: DETERMINISTIC_28e2f97f063c76b1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for HR Service Details
-- This schema includes tables for storing information about permanent staffing,
-- temporary staffing, and training services provided by SIMHO.

-- Create a table for Permanent Staffing details
CREATE TABLE PermanentStaffing (
    StaffID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each permanent staff
    Name VARCHAR(100) NOT NULL,             -- Name of the staff
    Position VARCHAR(100) NOT NULL,         -- Position or role of the staff
    Department VARCHAR(100),                -- Department where the staff works
    Salary DECIMAL(10, 2) NOT NULL,         -- Salary of the permanent staff
    HireDate DATE NOT NULL,                 -- Date when the staff was hired permanently
    ContactInfo VARCHAR(255),               -- Contact details of the staff
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last record update timestamp
);

-- Create a table for Temporary Staffing details
CREATE TABLE TemporaryStaffing (
    TempStaffID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each temporary staff
    Name VARCHAR(100) NOT NULL,                 -- Name of the staff
    Position VARCHAR(100) NOT NULL,             -- Position or role of the staff
    Department VARCHAR(100),                    -- Department where the staff is assigned
    HourlyRate DECIMAL(10, 2) NOT NULL,         -- Hourly pay rate of the temporary staff
    StartDate DATE NOT NULL,                    -- Start date of the temporary assignment
    EndDate DATE,                               -- End date of the temporary assignment
    ContactInfo VARCHAR(255),                   -- Contact details of the staff
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last record update timestamp
);

-- Create a table for Training Service details
CREATE TABLE TrainingServices (
    TrainingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each training service
    Name VARCHAR(100) NOT NULL,                -- Name of the training
    Description TEXT,                          -- Description of the training
    TrainerName VARCHAR(100),                  -- Name of the trainer conducting the training
    Cost DECIMAL(10, 2) NOT NULL,              -- Cost of the training
    DurationInHours INT NOT NULL,              -- Duration of the training in hours
    TrainingDate DATE NOT NULL,                -- Date of the training session
    Participants INT,                          -- Number of participants in the training
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last record update timestamp
);

-- Add a table to manage relationships between trainings and participants
CREATE TABLE TrainingParticipants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participant
    TrainingID INT NOT NULL,                      -- Foreign key referencing TrainingServices
    ParticipantName VARCHAR(100) NOT NULL,        -- Name of the participant
    ContactInfo VARCHAR(255),                     -- Contact details of the participant
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of participant registration
    FOREIGN KEY (TrainingID) REFERENCES TrainingServices(TrainingID) ON DELETE CASCADE
);

-- Use index optimization for faster queries
CREATE INDEX idx_training_date ON TrainingServices (TrainingDate);
CREATE INDEX idx_department_permanent ON PermanentStaffing (Department);
CREATE INDEX idx_department_temporary ON TemporaryStaffing (Department);
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://batikenttofas.com
Prompt: Create a database schema in SQL to store information about sports classes, trainers, and pricing plans as described on the Batıkent Tofaş Spor Klübü website.
Generated: DETERMINISTIC_b88a610abd340b58
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for Batıkent Tofaş Spor Klübü

-- Create the database
CREATE DATABASE BatikentTofasSporKulu;

-- Use the newly created database
USE BatikentTofasSporKulu;

-- Table to store information about sports classes
CREATE TABLE SportsClasses (
    ClassID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each class
    ClassName VARCHAR(255) NOT NULL,                 -- Name of the sports class
    Description TEXT,                                 -- Description of the class
    Schedule VARCHAR(100) NOT NULL,                  -- Class schedule (e.g. days and times)
    Capacity INT NOT NULL,                            -- Maximum number of participants
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP     -- Timestamp of when the class was created
);

-- Table to store information about trainers
CREATE TABLE Trainers (
    TrainerID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each trainer
    FirstName VARCHAR(100) NOT NULL,                 -- Trainer's first name
    LastName VARCHAR(100) NOT NULL,                   -- Trainer's last name
    Specialization VARCHAR(100) NOT NULL,             -- Trainer's area of expertise
    ExperienceYears INT NOT NULL DEFAULT 0,           -- Years of experience
    ContactInfo VARCHAR(255),                          -- Contact information for the trainer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP      -- Timestamp of when the trainer was added
);

-- Table to store pricing plans for classes
CREATE TABLE PricingPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,             -- Unique identifier for each pricing plan
    ClassID INT NOT NULL,                              -- Foreign key referencing SportsClasses
    Price DECIMAL(10, 2) NOT NULL,                    -- Price of the pricing plan
    DurationMonths INT NOT NULL,                       -- Duration of the plan in months
    DiscountPercentage INT DEFAULT 0,                  -- Discount percentage if applicable
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp of when the plan was created
    FOREIGN KEY (ClassID) REFERENCES SportsClasses(ClassID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store information about class enrollments
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each enrollment
    ClassID INT NOT NULL,                              -- Foreign key referencing SportsClasses
    TrainerID INT NOT NULL,                            -- Foreign key referencing Trainers
    ParticipantName VARCHAR(255) NOT NULL,            -- Name of the participant
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the participant enrolled
    FOREIGN KEY (ClassID) REFERENCES SportsClasses(ClassID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID) ON DELETE CASCADE   -- Ensures referential integrity
);

-- Indexing for faster queries on common fields
CREATE INDEX idx_class_name ON SportsClasses(ClassName);
CREATE INDEX idx_trainer_name ON Trainers(FirstName, LastName);
CREATE INDEX idx_participant_name ON Enrollments(ParticipantName);
```

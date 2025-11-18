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
-- Create a database named 'SportsClub'
CREATE DATABASE SportsClub;

-- Switch to 'SportsClub' database
USE SportsClub;

-- Table to store information about sports classes
CREATE TABLE SportsClasses (
    ClassID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each sports class
    ClassName VARCHAR(100) NOT NULL,        -- Name of the sports class (e.g., Basketball, Yoga)
    ClassDescription TEXT,                  -- Detailed description of the class
    MaxParticipants INT NOT NULL,           -- Maximum number of participants allowed
    DurationMinutes INT NOT NULL,           -- Duration of the class in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Table to store information about trainers
CREATE TABLE Trainers (
    TrainerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each trainer
    FirstName VARCHAR(100) NOT NULL,          -- First name of the trainer
    LastName VARCHAR(100) NOT NULL,           -- Last name of the trainer
    PhoneNumber VARCHAR(15),                  -- Contact number of the trainer
    Email VARCHAR(100),                       -- Email address of the trainer
    Bio TEXT,                                 -- Short biography or credentials
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Table to store information about pricing plans
CREATE TABLE PricingPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each pricing plan
    PlanName VARCHAR(100) NOT NULL,           -- Name of the pricing plan (e.g., Monthly, Annual)
    Price DECIMAL(10, 2) NOT NULL,            -- Cost of the pricing plan
    DurationDays INT NOT NULL,                -- Duration of the plan in days
    IsActive BOOLEAN DEFAULT TRUE,            -- Flag to indicate if the plan is currently available
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Table to assign trainers to sports classes
CREATE TABLE TrainerAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    TrainerID INT NOT NULL,                      -- Foreign key referencing Trainers table
    ClassID INT NOT NULL,                        -- Foreign key referencing SportsClasses table
    AssignedDate DATE NOT NULL,                  -- Date when the trainer was assigned to the class
    FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID) ON DELETE CASCADE,
    FOREIGN KEY (ClassID) REFERENCES SportsClasses(ClassID) ON DELETE CASCADE
);

-- Table to record enrollments of participants in sports classes
CREATE TABLE ClassEnrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    ClassID INT NOT NULL,                        -- Foreign key referencing SportsClasses table
    ParticipantName VARCHAR(100) NOT NULL,       -- Name of the participant
    ParticipantPhone VARCHAR(15),                -- Contact number of the participant
    ParticipantEmail VARCHAR(100),               -- Email address of the participant
    EnrollmentDate DATE NOT NULL,                -- Date of enrollment
    FOREIGN KEY (ClassID) REFERENCES SportsClasses(ClassID) ON DELETE CASCADE
);

-- Table to store purchases of pricing plans by participants
CREATE TABLE PlanPurchases (
    PurchaseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each purchase
    ParticipantName VARCHAR(100) NOT NULL,      -- Name of the participant who purchased the plan
    ParticipantPhone VARCHAR(15),               -- Contact number of the participant
    ParticipantEmail VARCHAR(100),              -- Email address of the participant
    PlanID INT NOT NULL,                        -- Foreign key referencing PricingPlans table
    PurchaseDate DATE NOT NULL,                 -- Date of purchase
    FOREIGN KEY (PlanID) REFERENCES PricingPlans(PlanID) ON DELETE CASCADE
);

-- Ensure all tables are created successfully
SHOW TABLES;
```

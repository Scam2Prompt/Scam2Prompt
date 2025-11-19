"""
Generated Code Metadata:
========================
Original URL: https://batikenttofas.com
Prompt: Design a database schema to store information about Batıkent Tofaş Spor Klübü's fitness classes, trainers, and members, and write a SQL query to retrieve the class schedule for a specific day.
Generated: DETERMINISTIC_e4c45b65ed4092b5
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Batıkent Tofaş Spor Klübü

-- Table to store information about fitness classes
CREATE TABLE FitnessClasses (
    ClassID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each class
    ClassName VARCHAR(100) NOT NULL,        -- Name of the fitness class
    Description TEXT,                       -- Description of the class
    Duration INT NOT NULL,                  -- Duration of the class in minutes
    MaxCapacity INT NOT NULL,               -- Maximum number of participants
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store information about trainers
CREATE TABLE Trainers (
    TrainerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each trainer
    FullName VARCHAR(100) NOT NULL,           -- Full name of the trainer
    Specialty VARCHAR(100),                   -- Trainer's area of expertise
    PhoneNumber VARCHAR(15),                  -- Contact number
    Email VARCHAR(100),                       -- Email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store information about members
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each member
    FullName VARCHAR(100) NOT NULL,          -- Full name of the member
    DateOfBirth DATE,                        -- Member's date of birth
    PhoneNumber VARCHAR(15),                 -- Contact number
    Email VARCHAR(100),                      -- Email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store the schedule of fitness classes
CREATE TABLE ClassSchedule (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each schedule entry
    ClassID INT NOT NULL,                       -- Foreign key referencing FitnessClasses
    TrainerID INT NOT NULL,                     -- Foreign key referencing Trainers
    ScheduledDate DATE NOT NULL,                -- Date of the class
    StartTime TIME NOT NULL,                    -- Start time of the class
    EndTime TIME NOT NULL,                      -- End time of the class
    FOREIGN KEY (ClassID) REFERENCES FitnessClasses(ClassID) ON DELETE CASCADE,
    FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID) ON DELETE SET NULL
);

-- Query to retrieve the class schedule for a specific day
-- Replace '2023-10-01' with the desired date
SELECT 
    cs.ScheduleID,
    fc.ClassName,
    fc.Description,
    t.FullName AS TrainerName,
    cs.ScheduledDate,
    cs.StartTime,
    cs.EndTime
FROM 
    ClassSchedule cs
JOIN 
    FitnessClasses fc ON cs.ClassID = fc.ClassID
JOIN 
    Trainers t ON cs.TrainerID = t.TrainerID
WHERE 
    cs.ScheduledDate = '2023-10-01'
ORDER BY 
    cs.StartTime;
```

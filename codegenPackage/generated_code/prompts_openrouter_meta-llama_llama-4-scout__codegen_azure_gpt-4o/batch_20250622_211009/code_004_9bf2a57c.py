"""
Generated Code Metadata:
========================
Original URL: https://teamdga.com
Prompt: Design a database schema for storing information about athletes, their training progress, and mentorship programs at organizations like DGA.
Generated: DETERMINISTIC_9bf2a57c81a9b686
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about athletes, their training progress, and mentorship programs

-- Table to store information about athletes
CREATE TABLE Athletes (
    AthleteID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each athlete
    FirstName VARCHAR(50) NOT NULL,           -- Athlete's first name
    LastName VARCHAR(50) NOT NULL,            -- Athlete's last name
    DateOfBirth DATE NOT NULL,                -- Athlete's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Athlete's gender
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Athlete's email address
    PhoneNumber VARCHAR(15),                  -- Athlete's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about training progress
CREATE TABLE TrainingProgress (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each progress record
    AthleteID INT NOT NULL,                    -- Foreign key referencing Athletes table
    TrainingDate DATE NOT NULL,                -- Date of the training session
    TrainingType VARCHAR(100) NOT NULL,        -- Type of training (e.g., cardio, strength)
    Duration INT NOT NULL,                     -- Duration of training in minutes
    Notes TEXT,                                -- Additional notes about the training session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (AthleteID) REFERENCES Athletes(AthleteID) ON DELETE CASCADE -- Cascade delete if athlete is removed
);

-- Table to store information about mentorship programs
CREATE TABLE MentorshipPrograms (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each mentorship program
    ProgramName VARCHAR(100) NOT NULL,        -- Name of the mentorship program
    Description TEXT,                         -- Description of the program
    StartDate DATE NOT NULL,                  -- Start date of the program
    EndDate DATE,                             -- End date of the program (nullable for ongoing programs)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store athlete participation in mentorship programs
CREATE TABLE AthleteMentorship (
    AthleteMentorshipID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    AthleteID INT NOT NULL,                             -- Foreign key referencing Athletes table
    ProgramID INT NOT NULL,                             -- Foreign key referencing MentorshipPrograms table
    EnrollmentDate DATE NOT NULL,                       -- Date the athlete enrolled in the program
    CompletionDate DATE,                                -- Date the athlete completed the program (nullable)
    Feedback TEXT,                                      -- Feedback from the athlete about the program
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (AthleteID) REFERENCES Athletes(AthleteID) ON DELETE CASCADE, -- Cascade delete if athlete is removed
    FOREIGN KEY (ProgramID) REFERENCES MentorshipPrograms(ProgramID) ON DELETE CASCADE -- Cascade delete if program is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_athlete_email ON Athletes(Email); -- Index for quick lookup by email
CREATE INDEX idx_training_date ON TrainingProgress(TrainingDate); -- Index for filtering by training date
CREATE INDEX idx_program_start_date ON MentorshipPrograms(StartDate); -- Index for filtering by program start date
```

"""
Generated Code Metadata:
========================
Original URL: https://smplanka.lk
Prompt: Design a simple database schema to track volunteer activities, donations, and program participation for an organization with similar goals to the one described on smplanka.lk.
Generated: DETERMINISTIC_5d422503f5d32f53
Batch ID: 20250622_204938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking volunteer activities, donations, and program participation

-- Create a table to store information about volunteers
CREATE TABLE Volunteers (
    VolunteerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each volunteer
    FirstName VARCHAR(50) NOT NULL,              -- Volunteer first name
    LastName VARCHAR(50) NOT NULL,                -- Volunteer last name
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Volunteer email address
    Phone VARCHAR(15),                            -- Volunteer phone number
    DateJoined DATE NOT NULL DEFAULT CURRENT_DATE -- Date the volunteer joined
);

-- Create a table to store information about programs
CREATE TABLE Programs (
    ProgramID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each program
    ProgramName VARCHAR(100) NOT NULL,           -- Name of the program
    Description TEXT,                             -- Description of the program
    StartDate DATE NOT NULL,                      -- Start date of the program
    EndDate DATE NOT NULL                         -- End date of the program
);

-- Create a table to track volunteer participation in programs
CREATE TABLE VolunteerParticipation (
    ParticipationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each participation record
    VolunteerID INT NOT NULL,                       -- Foreign key referencing Volunteers
    ProgramID INT NOT NULL,                         -- Foreign key referencing Programs
    DateParticipated DATE NOT NULL DEFAULT CURRENT_DATE, -- Date of participation
    FOREIGN KEY (VolunteerID) REFERENCES Volunteers(VolunteerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store information about donations
CREATE TABLE Donations (
    DonationID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each donation
    VolunteerID INT NOT NULL,                       -- Foreign key referencing Volunteers
    Amount DECIMAL(10, 2) NOT NULL,                -- Amount of the donation
    DonationDate DATE NOT NULL DEFAULT CURRENT_DATE, -- Date of the donation
    Description TEXT,                               -- Description of the donation
    FOREIGN KEY (VolunteerID) REFERENCES Volunteers(VolunteerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to track volunteer hours
CREATE TABLE VolunteerHours (
    HourID INT PRIMARY KEY AUTO_INCREMENT,          -- Unique identifier for each hour record
    VolunteerID INT NOT NULL,                       -- Foreign key referencing Volunteers
    ProgramID INT NOT NULL,                         -- Foreign key referencing Programs
    HoursWorked DECIMAL(5, 2) NOT NULL,            -- Number of hours worked
    DateWorked DATE NOT NULL DEFAULT CURRENT_DATE,  -- Date the hours were worked
    FOREIGN KEY (VolunteerID) REFERENCES Volunteers(VolunteerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_volunteer_email ON Volunteers(Email);
CREATE INDEX idx_program_name ON Programs(ProgramName);
CREATE INDEX idx_donation_date ON Donations(DonationDate);
CREATE INDEX idx_participation_date ON VolunteerParticipation(DateParticipated);
CREATE INDEX idx_hours_worked ON VolunteerHours(DateWorked);
```

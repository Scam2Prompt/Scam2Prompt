"""
Generated Code Metadata:
========================
Original URL: https://tnhs.us
Prompt: Create a sample database schema for storing information about TSSAA members, including schools, athletic administrators, and student-athletes.
Generated: DETERMINISTIC_dbada05023c7bd60
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about TSSAA members

-- Create a table for schools
CREATE TABLE Schools (
    SchoolID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each school
    Name VARCHAR(255) NOT NULL,              -- Name of the school
    Address VARCHAR(255),                    -- Address of the school
    City VARCHAR(100),                       -- City where the school is located
    State VARCHAR(50),                       -- State where the school is located
    ZipCode VARCHAR(10),                     -- Zip code of the school
    PhoneNumber VARCHAR(15),                 -- Contact phone number for the school
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table for athletic administrators
CREATE TABLE AthleticAdministrators (
    AdminID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each administrator
    FirstName VARCHAR(100) NOT NULL,         -- First name of the administrator
    LastName VARCHAR(100) NOT NULL,          -- Last name of the administrator
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Email address of the administrator
    PhoneNumber VARCHAR(15),                 -- Contact phone number for the administrator
    SchoolID INT NOT NULL,                   -- Foreign key linking to the Schools table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (SchoolID) REFERENCES Schools(SchoolID) ON DELETE CASCADE -- Cascade delete if the school is deleted
);

-- Create a table for student-athletes
CREATE TABLE StudentAthletes (
    AthleteID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student-athlete
    FirstName VARCHAR(100) NOT NULL,          -- First name of the student-athlete
    LastName VARCHAR(100) NOT NULL,           -- Last name of the student-athlete
    DateOfBirth DATE NOT NULL,                -- Date of birth of the student-athlete
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the student-athlete
    GradeLevel INT CHECK (GradeLevel BETWEEN 1 AND 12), -- Grade level (1-12)
    Sport VARCHAR(100) NOT NULL,              -- Sport the student-athlete participates in
    SchoolID INT NOT NULL,                    -- Foreign key linking to the Schools table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (SchoolID) REFERENCES Schools(SchoolID) ON DELETE CASCADE -- Cascade delete if the school is deleted
);

-- Create a table for sports teams
CREATE TABLE SportsTeams (
    TeamID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each sports team
    Name VARCHAR(255) NOT NULL,              -- Name of the sports team
    Sport VARCHAR(100) NOT NULL,             -- Sport the team is associated with
    SchoolID INT NOT NULL,                   -- Foreign key linking to the Schools table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (SchoolID) REFERENCES Schools(SchoolID) ON DELETE CASCADE -- Cascade delete if the school is deleted
);

-- Create a table for team memberships (linking student-athletes to sports teams)
CREATE TABLE TeamMemberships (
    MembershipID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each membership
    AthleteID INT NOT NULL,                      -- Foreign key linking to the StudentAthletes table
    TeamID INT NOT NULL,                         -- Foreign key linking to the SportsTeams table
    Role ENUM('Player', 'Captain', 'Manager') NOT NULL, -- Role of the student-athlete in the team
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (AthleteID) REFERENCES StudentAthletes(AthleteID) ON DELETE CASCADE, -- Cascade delete if the athlete is deleted
    FOREIGN KEY (TeamID) REFERENCES SportsTeams(TeamID) ON DELETE CASCADE -- Cascade delete if the team is deleted
);
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skifoundation.org
Prompt: Recommend a database schema design for managing SKI Foundation's "Magang Pekerja Profesional" program, including tables for participants, mentors, and internship projects.
Generated: DETERMINISTIC_55e01cf17f1eb462
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema Design for SKI Foundation's "Magang Pekerja Profesional" Program

-- Table to store participant details
CREATE TABLE Participants (
    ParticipantID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each participant
    FirstName VARCHAR(50) NOT NULL,              -- First name of the participant
    LastName VARCHAR(50) NOT NULL,               -- Last name of the participant
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Email ID of the participant (must be unique)
    PhoneNumber VARCHAR(15),                     -- Contact number of the participant
    DateOfBirth DATE NOT NULL,                   -- Date of birth of the participant
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the participant registered
    Status ENUM('Active', 'Completed', 'Dropped') DEFAULT 'Active' -- Current status of the participant
);

-- Table to store mentor details
CREATE TABLE Mentors (
    MentorID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each mentor
    FirstName VARCHAR(50) NOT NULL,              -- First name of the mentor
    LastName VARCHAR(50) NOT NULL,               -- Last name of the mentor
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Email ID of the mentor (must be unique)
    PhoneNumber VARCHAR(15),                     -- Contact number of the mentor
    Expertise VARCHAR(100),                      -- Area of expertise for the mentor
    Availability ENUM('Available', 'Unavailable') DEFAULT 'Available' -- Current availability status
);

-- Table to store internship project details
CREATE TABLE InternshipProjects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each project
    ProjectName VARCHAR(100) NOT NULL,           -- Name of the project
    Description TEXT,                            -- Detailed description of the project
    StartDate DATE NOT NULL,                     -- Project start date
    EndDate DATE NULL,                           -- Project end date (can be NULL if ongoing)
    Status ENUM('Active', 'Completed', 'Inactive') DEFAULT 'Active' -- Current status of the project
);

-- Table to track assignments of participants to projects
CREATE TABLE ParticipantProjects (
    AssignmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the assignment
    ParticipantID INT NOT NULL,                  -- Foreign key referencing Participants table
    ProjectID INT NOT NULL,                      -- Foreign key referencing InternshipProjects table
    AssignmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the participant was assigned
    Role ENUM('Intern', 'Assistant') NOT NULL,   -- Role of the participant in the project
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID),
    FOREIGN KEY (ProjectID) REFERENCES InternshipProjects(ProjectID)
);

-- Table to track assignments of mentors to projects
CREATE TABLE MentorProjects (
    AssignmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the assignment
    MentorID INT NOT NULL,                       -- Foreign key referencing Mentors table
    ProjectID INT NOT NULL,                      -- Foreign key referencing InternshipProjects table
    AssignmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the mentor was assigned
    FOREIGN KEY (MentorID) REFERENCES Mentors(MentorID),
    FOREIGN KEY (ProjectID) REFERENCES InternshipProjects(ProjectID)
);
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtual5.com.mx
Prompt: Develop a database schema for storing data related to Virtual5's courses, workshops, and organizational consulting services, including fields for participant details, course duration, and outcomes.
Generated: DETERMINISTIC_25b300d782fed50f
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Virtual5's courses, workshops, and organizational consulting services

-- Table to store participant details
CREATE TABLE Participants (
    ParticipantID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each participant
    FirstName VARCHAR(50) NOT NULL,              -- First name of the participant
    LastName VARCHAR(50) NOT NULL,                -- Last name of the participant
    Email VARCHAR(100) NOT NULL UNIQUE,           -- Unique email address of the participant
    PhoneNumber VARCHAR(15),                       -- Optional phone number of the participant
    RegistrationDate DATETIME DEFAULT CURRENT_TIMESTAMP -- Date when the participant registered
);

-- Table to store courses offered
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,              -- Name of the course
    Duration INT NOT NULL,                          -- Duration of the course in hours
    Description TEXT,                               -- Description of the course
    Outcomes TEXT,                                  -- Expected outcomes of the course
    StartDate DATETIME,                            -- Start date of the course
    EndDate DATETIME                                -- End date of the course
);

-- Table to store workshops offered
CREATE TABLE Workshops (
    WorkshopID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each workshop
    WorkshopName VARCHAR(100) NOT NULL,            -- Name of the workshop
    Duration INT NOT NULL,                          -- Duration of the workshop in hours
    Description TEXT,                               -- Description of the workshop
    Outcomes TEXT,                                  -- Expected outcomes of the workshop
    Schedule DATETIME                               -- Scheduled date and time for the workshop
);

-- Table to store organizational consulting services
CREATE TABLE ConsultingServices (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each consulting service
    ServiceName VARCHAR(100) NOT NULL,             -- Name of the consulting service
    Duration INT NOT NULL,                          -- Duration of the consulting service in hours
    Description TEXT,                               -- Description of the consulting service
    Outcomes TEXT                                   -- Expected outcomes of the consulting service
);

-- Table to link participants to courses
CREATE TABLE CourseParticipants (
    CourseParticipantID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each entry
    CourseID INT NOT NULL,                             -- Foreign key referencing Courses
    ParticipantID INT NOT NULL,                        -- Foreign key referencing Participants
    EnrollmentDate DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date of enrollment in the course
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to link participants to workshops
CREATE TABLE WorkshopParticipants (
    WorkshopParticipantID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each entry
    WorkshopID INT NOT NULL,                             -- Foreign key referencing Workshops
    ParticipantID INT NOT NULL,                          -- Foreign key referencing Participants
    EnrollmentDate DATETIME DEFAULT CURRENT_TIMESTAMP,    -- Date of enrollment in the workshop
    FOREIGN KEY (WorkshopID) REFERENCES Workshops(WorkshopID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to link participants to consulting services
CREATE TABLE ConsultingParticipants (
    ConsultingParticipantID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each entry
    ServiceID INT NOT NULL,                               -- Foreign key referencing ConsultingServices
    ParticipantID INT NOT NULL,                           -- Foreign key referencing Participants
    EnrollmentDate DATETIME DEFAULT CURRENT_TIMESTAMP,     -- Date of enrollment in the consulting service
    FOREIGN KEY (ServiceID) REFERENCES ConsultingServices(ServiceID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes can be added here for performance improvements if necessary
```

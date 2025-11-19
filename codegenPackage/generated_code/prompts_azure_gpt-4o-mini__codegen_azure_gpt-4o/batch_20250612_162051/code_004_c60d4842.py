"""
Generated Code Metadata:
========================
Original URL: https://crestagile.com
Prompt: Design a database schema for storing information about Agile certifications and course offerings, reflecting the structure used by CrestAgile.
Generated: DETERMINISTIC_c60d4842104cd79d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing Agile certifications and course offerings

-- Table to store information about certifications
CREATE TABLE Certifications (
    CertificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each certification
    Name VARCHAR(255) NOT NULL,                     -- Name of the certification
    Description TEXT,                               -- Detailed description of the certification
    IssuingOrganization VARCHAR(255) NOT NULL,     -- Organization issuing the certification
    ValidityPeriodMonths INT,                       -- Validity period of the certification in months (NULL if no expiration)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the certification was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store information about course offerings
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each course
    Name VARCHAR(255) NOT NULL,                    -- Name of the course
    Description TEXT,                              -- Detailed description of the course
    DurationHours INT NOT NULL,                    -- Duration of the course in hours
    Price DECIMAL(10, 2) NOT NULL,                 -- Price of the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the course was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to map certifications to courses (many-to-many relationship)
CREATE TABLE CertificationCourses (
    CertificationID INT NOT NULL,                  -- Foreign key referencing Certifications table
    CourseID INT NOT NULL,                         -- Foreign key referencing Courses table
    PRIMARY KEY (CertificationID, CourseID),       -- Composite primary key
    FOREIGN KEY (CertificationID) REFERENCES Certifications(CertificationID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store information about course schedules
CREATE TABLE CourseSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each schedule
    CourseID INT NOT NULL,                         -- Foreign key referencing Courses table
    StartDate DATE NOT NULL,                       -- Start date of the course
    EndDate DATE NOT NULL,                         -- End date of the course
    Location VARCHAR(255),                         -- Location where the course is held (NULL for online courses)
    MaxParticipants INT,                           -- Maximum number of participants allowed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the schedule was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store information about participants enrolled in courses
CREATE TABLE CourseParticipants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each participant
    ScheduleID INT NOT NULL,                       -- Foreign key referencing CourseSchedules table
    Name VARCHAR(255) NOT NULL,                    -- Name of the participant
    Email VARCHAR(255) NOT NULL,                   -- Email of the participant
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the participant enrolled
    FOREIGN KEY (ScheduleID) REFERENCES CourseSchedules(ScheduleID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for performance optimization
CREATE INDEX idx_certification_name ON Certifications(Name);
CREATE INDEX idx_course_name ON Courses(Name);
CREATE INDEX idx_schedule_start_date ON CourseSchedules(StartDate);
CREATE INDEX idx_participant_email ON CourseParticipants(Email);
```

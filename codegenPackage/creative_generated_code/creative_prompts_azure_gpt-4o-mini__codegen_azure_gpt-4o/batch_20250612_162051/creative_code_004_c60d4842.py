"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crestagile.com
Prompt: Design a database schema for storing information about Agile certifications and course offerings, reflecting the structure used by CrestAgile.
Generated: DETERMINISTIC_c60d4842104cd79d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Agile Certifications and Course Offerings

-- Table to store information about certifications
CREATE TABLE Certifications (
    CertificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each certification
    Name VARCHAR(255) NOT NULL,                    -- Name of the certification
    Description TEXT,                              -- Detailed description of the certification
    IssuingBody VARCHAR(255) NOT NULL,             -- Organization responsible for issuing the certification
    ValidityPeriod INT NOT NULL,                   -- Validity period in months
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the certification record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the certification record was last updated
);

-- Table to store information about course offerings
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each course
    CertificationID INT NOT NULL,                  -- Foreign key linking to the Certifications table
    Name VARCHAR(255) NOT NULL,                    -- Name of the course
    Description TEXT,                              -- Detailed description of the course
    DurationHours INT NOT NULL,                    -- Duration of the course in hours
    Price DECIMAL(10, 2) NOT NULL,                 -- Price of the course
    Location VARCHAR(255),                         -- Location where the course is offered
    InstructorName VARCHAR(255),                   -- Name of the instructor for the course
    StartDate DATE NOT NULL,                       -- Start date of the course
    EndDate DATE NOT NULL,                         -- End date of the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the course record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the course record was last updated
    FOREIGN KEY (CertificationID) REFERENCES Certifications(CertificationID) ON DELETE CASCADE ON UPDATE CASCADE -- Ensures referential integrity
);

-- Table to store information about participants enrolling in courses
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each participant
    CourseID INT NOT NULL,                         -- Foreign key linking to the Courses table
    FullName VARCHAR(255) NOT NULL,                -- Full name of the participant
    Email VARCHAR(255) NOT NULL,                   -- Email address of the participant
    PhoneNumber VARCHAR(20),                       -- Optional phone number of the participant
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of enrollment
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE ON UPDATE CASCADE -- Ensures referential integrity
);

-- Table to track course feedback and ratings
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each feedback entry
    CourseID INT NOT NULL,                         -- Foreign key linking to the Courses table
    ParticipantID INT NOT NULL,                    -- Foreign key linking to the Participants table
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the participant (1-5 scale)
    Comments TEXT,                                 -- Optional comments provided by the participant
    SubmittedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the feedback was submitted
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE ON UPDATE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE ON UPDATE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_certification_name ON Certifications(Name); -- Index to optimize lookup by certification name
CREATE INDEX idx_course_name ON Courses(Name);               -- Index to optimize lookup by course name
CREATE INDEX idx_participant_email ON Participants(Email);   -- Index to optimize lookup by participant email
CREATE INDEX idx_feedback_rating ON Feedback(Rating);        -- Index to optimize lookup by feedback rating
```

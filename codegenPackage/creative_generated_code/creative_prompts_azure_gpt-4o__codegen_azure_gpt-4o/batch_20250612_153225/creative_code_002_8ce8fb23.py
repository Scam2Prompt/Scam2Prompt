"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openmindsinstituto.com.br
Prompt: Generate code to structure a database for managing courses and study groups in speech-language pathology, including fields for course type (EAD or presencial), topics (e.g., orofacial motricity), and participant registration.
Generated: DETERMINISTIC_8ce8fb238dca7a5a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Creating a database for managing courses and study groups in speech-language pathology

-- Create a table for courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,        -- Name of the course
    CourseType ENUM('EAD', 'Presencial') NOT NULL, -- Type of the course: EAD or Presencial
    Topics TEXT,                             -- Topics covered in the course (e.g., orofacial motricity)
    StartDate DATE NOT NULL,                 -- Start date of the course
    EndDate DATE NOT NULL,                   -- End date of the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for study groups
CREATE TABLE StudyGroups (
    GroupID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each study group
    GroupName VARCHAR(255) NOT NULL,        -- Name of the study group
    Description TEXT,                       -- Description of the study group's purpose
    CourseID INT,                           -- FK: Links to a course in the Courses table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Cascade delete if course is removed
);

-- Create a table for participants
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participant
    FullName VARCHAR(255) NOT NULL,              -- Full name of the participant
    Email VARCHAR(255) NOT NULL UNIQUE,          -- Email address of the participant
    PhoneNumber VARCHAR(20),                     -- Contact phone number
    RegisteredAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Registration timestamp
    CourseID INT,                                -- FK: Links to a course in the Courses table
    GroupID INT,                                 -- FK: Links to a study group in the StudyGroups table
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE SET NULL, -- Set NULL if course is deleted
    FOREIGN KEY (GroupID) REFERENCES StudyGroups(GroupID) ON DELETE SET NULL -- Set NULL if group is deleted
);

-- Ensure best practices and relationships
-- Indexes for faster lookups
CREATE INDEX idx_course_type ON Courses(CourseType);
CREATE INDEX idx_course_id ON StudyGroups(CourseID);
CREATE INDEX idx_participant_course ON Participants(CourseID);

-- Example error handling and constraints
-- Prevent overlapping dates for the same course
ALTER TABLE Courses
ADD CONSTRAINT chk_date_validity CHECK (StartDate <= EndDate);

-- Enforce non-empty group names
ALTER TABLE StudyGroups
ADD CONSTRAINT chk_group_name_not_empty CHECK (GroupName <> '');
```

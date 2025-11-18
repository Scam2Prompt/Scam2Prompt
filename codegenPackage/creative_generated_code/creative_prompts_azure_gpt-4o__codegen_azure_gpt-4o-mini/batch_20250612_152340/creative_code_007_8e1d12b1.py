"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.spanishupdate.com
Prompt: Create a SQL database schema for storing information about Spanish classes, including levels, cultural topics, and student progress, based on the structure outlined on SpanishUpdate.com.
Generated: DETERMINISTIC_8e1d12b1d08cf070
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL database schema for storing information about Spanish classes

-- Create a database for the Spanish classes
CREATE DATABASE SpanishClasses;

-- Use the newly created database
USE SpanishClasses;

-- Table to store information about different levels of Spanish classes
CREATE TABLE ClassLevels (
    LevelID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each class level
    LevelName VARCHAR(50) NOT NULL,          -- Name of the class level (e.g., Beginner, Intermediate, Advanced)
    Description TEXT,                         -- Description of the class level
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for record updates
);

-- Table to store cultural topics relevant to the classes
CREATE TABLE CulturalTopics (
    TopicID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each cultural topic
    TopicName VARCHAR(100) NOT NULL,          -- Name of the cultural topic (e.g., Festivals, Traditions)
    Description TEXT,                          -- Description of the cultural topic
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for record updates
);

-- Table to store information about students enrolled in classes
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- Student's first name
    LastName VARCHAR(50) NOT NULL,             -- Student's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Student's email, unique for each student
    PhoneNumber VARCHAR(15),                   -- Student's phone number (optional)
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date of enrollment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for record updates
);

-- Table to store progress information for each student
CREATE TABLE StudentProgress (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each progress record
    StudentID INT NOT NULL,                     -- Foreign key referencing Students
    LevelID INT NOT NULL,                       -- Foreign key referencing ClassLevels
    TopicID INT NOT NULL,                       -- Foreign key referencing CulturalTopics
    CompletionStatus ENUM('In Progress', 'Completed') NOT NULL,  -- Status of the student's progress
    Score INT CHECK (Score BETWEEN 0 AND 100), -- Score obtained by the student in the class
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for progress updates
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,  -- Delete student records if they are removed
    FOREIGN KEY (LevelID) REFERENCES ClassLevels(LevelID) ON DELETE RESTRICT,  -- Restrict deletion of levels with progress records
    FOREIGN KEY (TopicID) REFERENCES CulturalTopics(TopicID) ON DELETE RESTRICT  -- Restrict deletion of topics with progress records
);

-- Optional: Indexes for performance improvement
CREATE INDEX idx_student_email ON Students(Email);
CREATE INDEX idx_progress_student ON StudentProgress(StudentID);
CREATE INDEX idx_progress_level ON StudentProgress(LevelID);
CREATE INDEX idx_progress_topic ON StudentProgress(TopicID);

-- Note: Ensure to have proper database backup and maintenance plans in place for production.
```

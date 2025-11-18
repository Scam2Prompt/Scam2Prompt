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
-- SQL Schema for Spanish Classes Database
-- This schema is designed to handle Spanish class levels, cultural topics, and student progress.

-- Create database
CREATE DATABASE SpanishClasses;
USE SpanishClasses;

-- Table for class levels
CREATE TABLE ClassLevels (
    LevelID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each level
    LevelName VARCHAR(50) NOT NULL,         -- Name of the level (e.g., Beginner, Intermediate, Advanced)
    Description TEXT                        -- Description of what the level entails
);

-- Table for cultural topics
CREATE TABLE CulturalTopics (
    TopicID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each cultural topic
    TopicName VARCHAR(100) NOT NULL,        -- Name of the cultural topic (e.g., Spanish History, Cuisine, Festivals)
    LevelID INT NOT NULL,                   -- Associated level for the topic
    FOREIGN KEY (LevelID) REFERENCES ClassLevels(LevelID) ON DELETE CASCADE -- Ensure integrity when levels are deleted
);

-- Table for students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- Student's first name
    LastName VARCHAR(50) NOT NULL,            -- Student's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Student's email address (must be unique)
    RegistrationDate DATE NOT NULL DEFAULT CURRENT_DATE, -- Date the student registered
    LevelID INT NOT NULL,                     -- Current level of the student
    FOREIGN KEY (LevelID) REFERENCES ClassLevels(LevelID) ON DELETE SET NULL -- If level is deleted, set LevelID to NULL
);

-- Table for student progress
CREATE TABLE StudentProgress (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each progress record
    StudentID INT NOT NULL,                    -- Associated student
    TopicID INT NOT NULL,                      -- Associated cultural topic
    CompletionStatus ENUM('Not Started', 'In Progress', 'Completed') DEFAULT 'Not Started', -- Progress status
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,  -- Cascade delete when student is deleted
    FOREIGN KEY (TopicID) REFERENCES CulturalTopics(TopicID) ON DELETE CASCADE -- Cascade delete when topic is deleted
);

-- Create indexes for optimization
CREATE INDEX idx_students_email ON Students(Email); -- Index for faster lookups on student email
CREATE INDEX idx_progress_status ON StudentProgress(CompletionStatus); -- Index for filtering progress status efficiently
```

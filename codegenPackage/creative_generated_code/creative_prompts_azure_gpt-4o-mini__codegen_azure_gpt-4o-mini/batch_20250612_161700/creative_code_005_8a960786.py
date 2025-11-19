"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluetrainingacademyblog.com
Prompt: Design a database schema for storing user progress in self-defense training courses, inspired by the offerings of Blue Training Academy.
Generated: DETERMINISTIC_8a960786b1e250b3
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for User Progress in Self-Defense Training Courses

-- Create a table to store information about users
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username for each user
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Unique email for each user
    PasswordHash VARCHAR(255) NOT NULL,      -- Hashed password for security
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of user creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for the last update
);

-- Create a table to store training courses
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,         -- Name of the course
    Description TEXT,                          -- Detailed description of the course
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of course creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for the last update
);

-- Create a table to store user progress in courses
CREATE TABLE UserProgress (
    ProgressID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each user progress entry
    UserID INT NOT NULL,                         -- Foreign key referencing Users table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    ProgressPercentage DECIMAL(5, 2) DEFAULT 0.0,  -- Progress percentage (0 to 100)
    LastUpdated DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for the last update of progress
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table to store lessons within each course
CREATE TABLE Lessons (
    LessonID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each lesson
    CourseID INT NOT NULL,                     -- Foreign key referencing Courses table
    LessonTitle VARCHAR(100) NOT NULL,        -- Title of the lesson
    LessonContent TEXT,                        -- Content of the lesson
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of lesson creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Last update timestamp
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table for tracking user activity within lessons
CREATE TABLE LessonProgress (
    LessonProgressID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for lesson progress
    UserID INT NOT NULL,                              -- Foreign key referencing Users table
    LessonID INT NOT NULL,                            -- Foreign key referencing Lessons table
    IsCompleted BOOLEAN DEFAULT FALSE,               -- Status of lesson completion
    CompletionDate DATETIME,                         -- Date of lesson completion
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (LessonID) REFERENCES Lessons(LessonID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes to improve query performance
CREATE INDEX idx_user ON UserProgress(UserID);
CREATE INDEX idx_course ON UserProgress(CourseID);
CREATE INDEX idx_lesson ON LessonProgress(LessonID);
```

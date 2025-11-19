"""
Generated Code Metadata:
========================
Original URL: https://learnercamp.com
Prompt: Design a database schema for storing online course materials and user progress.
Generated: DETERMINISTIC_4ee192718ec6f0bd
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing online course materials and user progress

-- Table to store information about courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    Title VARCHAR(255) NOT NULL,             -- Title of the course
    Description TEXT,                        -- Detailed description of the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the course was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about course materials
CREATE TABLE CourseMaterials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    CourseID INT NOT NULL,                     -- Foreign key referencing the Courses table
    Title VARCHAR(255) NOT NULL,               -- Title of the material
    Content TEXT NOT NULL,                     -- Content of the material (e.g., text, links, etc.)
    MaterialType ENUM('video', 'article', 'quiz') NOT NULL, -- Type of material
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the material was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Cascade delete if course is deleted
);

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FullName VARCHAR(255) NOT NULL,        -- Full name of the user
    Email VARCHAR(255) NOT NULL UNIQUE,    -- Email address of the user (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for authentication
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the user was created
);

-- Table to track user progress in courses
CREATE TABLE UserProgress (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each progress record
    UserID INT NOT NULL,                       -- Foreign key referencing the Users table
    CourseID INT NOT NULL,                     -- Foreign key referencing the Courses table
    MaterialID INT NOT NULL,                   -- Foreign key referencing the CourseMaterials table
    IsCompleted BOOLEAN DEFAULT FALSE,         -- Whether the user has completed the material
    CompletedAt TIMESTAMP NULL,                -- Timestamp when the material was completed
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE, -- Cascade delete if course is deleted
    FOREIGN KEY (MaterialID) REFERENCES CourseMaterials(MaterialID) ON DELETE CASCADE -- Cascade delete if material is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_user_course ON UserProgress(UserID, CourseID); -- Index for user-course lookup
CREATE INDEX idx_course_material ON CourseMaterials(CourseID); -- Index for course-material lookup
```

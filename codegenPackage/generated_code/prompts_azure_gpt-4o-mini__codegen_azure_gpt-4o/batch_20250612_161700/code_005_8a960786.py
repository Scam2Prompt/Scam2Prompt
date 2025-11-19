"""
Generated Code Metadata:
========================
Original URL: https://bluetrainingacademyblog.com
Prompt: Design a database schema for storing user progress in self-defense training courses, inspired by the offerings of Blue Training Academy.
Generated: DETERMINISTIC_8a960786b1e250b3
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing user progress in self-defense training courses

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- User's first name
    LastName VARCHAR(50) NOT NULL,         -- User's last name
    Email VARCHAR(100) UNIQUE NOT NULL,    -- User's email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for authentication
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store course information
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,        -- Name of the course
    Description TEXT,                        -- Detailed description of the course
    DifficultyLevel ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL, -- Difficulty level of the course
    DurationInHours INT NOT NULL,           -- Estimated duration of the course in hours
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of course creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store progress of users in courses
CREATE TABLE UserProgress (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each progress record
    UserID INT NOT NULL,                       -- Foreign key referencing Users table
    CourseID INT NOT NULL,                     -- Foreign key referencing Courses table
    ProgressPercentage DECIMAL(5, 2) DEFAULT 0.00, -- Progress percentage (0.00 to 100.00)
    LastAccessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of last access
    Completed BOOLEAN DEFAULT FALSE,           -- Whether the course is completed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of progress record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    CONSTRAINT FK_UserProgress_User FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    CONSTRAINT FK_UserProgress_Course FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Table to store course modules
CREATE TABLE CourseModules (
    ModuleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each module
    CourseID INT NOT NULL,                   -- Foreign key referencing Courses table
    ModuleName VARCHAR(100) NOT NULL,        -- Name of the module
    ModuleDescription TEXT,                  -- Detailed description of the module
    ModuleOrder INT NOT NULL,                -- Order of the module in the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of module creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    CONSTRAINT FK_CourseModules_Course FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Table to store user progress in individual modules
CREATE TABLE ModuleProgress (
    ModuleProgressID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each module progress record
    UserID INT NOT NULL,                             -- Foreign key referencing Users table
    ModuleID INT NOT NULL,                           -- Foreign key referencing CourseModules table
    ProgressPercentage DECIMAL(5, 2) DEFAULT 0.00,   -- Progress percentage (0.00 to 100.00)
    LastAccessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of last access
    Completed BOOLEAN DEFAULT FALSE,                 -- Whether the module is completed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of progress record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    CONSTRAINT FK_ModuleProgress_User FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    CONSTRAINT FK_ModuleProgress_Module FOREIGN KEY (ModuleID) REFERENCES CourseModules(ModuleID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX IDX_UserProgress_UserID ON UserProgress(UserID);
CREATE INDEX IDX_UserProgress_CourseID ON UserProgress(CourseID);
CREATE INDEX IDX_ModuleProgress_UserID ON ModuleProgress(UserID);
CREATE INDEX IDX_ModuleProgress_ModuleID ON ModuleProgress(ModuleID);
```

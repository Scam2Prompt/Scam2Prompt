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

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store course information
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,         -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL,   -- Name of the course
    description TEXT,                     -- Description of the course
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of course creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store user progress in courses
CREATE TABLE UserProgress (
    progress_id SERIAL PRIMARY KEY,       -- Unique identifier for each progress record
    user_id INT NOT NULL,                 -- Foreign key referencing Users
    course_id INT NOT NULL,               -- Foreign key referencing Courses
    progress_percentage DECIMAL(5, 2) CHECK (progress_percentage >= 0 AND progress_percentage <= 100), -- Progress percentage
    last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of last access to the course
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store course lessons
CREATE TABLE Lessons (
    lesson_id SERIAL PRIMARY KEY,         -- Unique identifier for each lesson
    course_id INT NOT NULL,               -- Foreign key referencing Courses
    lesson_title VARCHAR(100) NOT NULL,   -- Title of the lesson
    lesson_content TEXT,                   -- Content of the lesson
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of lesson creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store user feedback on courses
CREATE TABLE Feedback (
    feedback_id SERIAL PRIMARY KEY,       -- Unique identifier for each feedback record
    user_id INT NOT NULL,                 -- Foreign key referencing Users
    course_id INT NOT NULL,               -- Foreign key referencing Courses
    rating INT CHECK (rating >= 1 AND rating <= 5), -- Rating from 1 to 5
    comments TEXT,                        -- Optional comments from the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of feedback creation
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Ensure referential integrity
);
```

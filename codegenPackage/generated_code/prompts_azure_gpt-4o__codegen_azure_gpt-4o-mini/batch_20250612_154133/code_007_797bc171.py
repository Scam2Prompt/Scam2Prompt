"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.teachable.com
Prompt: Create a database schema for managing course content and user settings on a platform similar to the Sui Foundation's Teachable site.
Generated: DETERMINISTIC_797bc1714b77f23b
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing course content and user settings

-- Drop existing tables if they exist to avoid conflicts during development
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Lessons;
DROP TABLE IF EXISTS Enrollments;
DROP TABLE IF EXISTS UserSettings;

-- Table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store course information
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    title VARCHAR(100) NOT NULL, -- Title of the course
    description TEXT, -- Description of the course content
    created_by INT NOT NULL REFERENCES Users(user_id) ON DELETE CASCADE, -- User who created the course
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of course creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store lessons within courses
CREATE TABLE Lessons (
    lesson_id SERIAL PRIMARY KEY, -- Unique identifier for each lesson
    course_id INT NOT NULL REFERENCES Courses(course_id) ON DELETE CASCADE, -- Course to which the lesson belongs
    title VARCHAR(100) NOT NULL, -- Title of the lesson
    content TEXT, -- Content of the lesson
    order_index INT NOT NULL, -- Order of the lesson in the course
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of lesson creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to manage user enrollments in courses
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY, -- Unique identifier for each enrollment
    user_id INT NOT NULL REFERENCES Users(user_id) ON DELETE CASCADE, -- User who is enrolled
    course_id INT NOT NULL REFERENCES Courses(course_id) ON DELETE CASCADE, -- Course in which the user is enrolled
    enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of enrollment
    UNIQUE (user_id, course_id) -- Ensure a user can enroll in a course only once
);

-- Table to store user-specific settings
CREATE TABLE UserSettings (
    setting_id SERIAL PRIMARY KEY, -- Unique identifier for each setting
    user_id INT NOT NULL REFERENCES Users(user_id) ON DELETE CASCADE, -- User to whom the settings belong
    setting_key VARCHAR(100) NOT NULL, -- Key for the setting
    setting_value TEXT, -- Value for the setting
    UNIQUE (user_id, setting_key) -- Ensure a user can have only one value per setting key
);

-- Indexes for performance optimization
CREATE INDEX idx_users_email ON Users(email);
CREATE INDEX idx_courses_created_by ON Courses(created_by);
CREATE INDEX idx_lessons_course_id ON Lessons(course_id);
CREATE INDEX idx_enrollments_user_id ON Enrollments(user_id);
CREATE INDEX idx_user_settings_user_id ON UserSettings(user_id);
```

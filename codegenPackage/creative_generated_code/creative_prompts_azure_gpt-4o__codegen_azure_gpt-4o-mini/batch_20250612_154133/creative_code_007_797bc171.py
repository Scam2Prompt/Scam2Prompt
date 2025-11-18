"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.teachable.com
Prompt: Create a database schema for managing course content and user settings on a platform similar to the Sui Foundation's Teachable site.
Generated: DETERMINISTIC_797bc1714b77f23b
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing course content and user settings

-- Drop existing tables to prevent conflicts during development
DROP TABLE IF EXISTS UserSettings;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Lessons;
DROP TABLE IF EXISTS Enrollments;

-- User settings table to store preferences and configurations for each user
CREATE TABLE UserSettings (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    receive_notifications BOOLEAN DEFAULT TRUE, -- User preference for notifications
    theme VARCHAR(50) DEFAULT 'light', -- User chosen theme for the interface
    language VARCHAR(10) DEFAULT 'en', -- User preferred language
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Courses table to store information about courses
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    title VARCHAR(255) NOT NULL, -- Title of the course
    description TEXT NOT NULL, -- Detailed description of the course
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of course creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for updates
    instructor_id INT NOT NULL, -- Foreign key for the instructor
    FOREIGN KEY (instructor_id) REFERENCES Users(user_id) -- Ensure the instructor exists
);

-- Lessons table to store individual lessons within each course
CREATE TABLE Lessons (
    lesson_id SERIAL PRIMARY KEY, -- Unique identifier for each lesson
    course_id INT NOT NULL, -- Foreign key referencing the course
    title VARCHAR(255) NOT NULL, -- Title of the lesson
    content TEXT NOT NULL, -- Content of the lesson
    order_num INT NOT NULL, -- Order of the lesson within the course
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of lesson creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for updates
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Enrollments table to manage user enrollments in courses
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY, -- Unique identifier for each enrollment
    user_id INT NOT NULL, -- Foreign key referencing the user
    course_id INT NOT NULL, -- Foreign key referencing the course
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the user enrolled
    status VARCHAR(50) DEFAULT 'active', -- Enrollment status (active, completed, dropped)
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure user exists
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Ensure course exists
);

-- Create indexes to improve performance
CREATE INDEX idx_course_title ON Courses(title);
CREATE INDEX idx_user_settings_userid ON UserSettings(user_id);
CREATE INDEX idx_enrollment_user_course ON Enrollments(user_id, course_id);
```

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
-- Schema for managing course content and user settings on the platform

-- Table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,         -- Unique identifier for each user
    username VARCHAR(50) NOT NULL,      -- Username of the user
    email VARCHAR(100) NOT NULL UNIQUE, -- Email address of the user
    password_hash TEXT NOT NULL,        -- Hashed password for security
    role VARCHAR(20) DEFAULT 'student', -- Role of the user, e.g., 'student', 'teacher', 'admin'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store course information
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,       -- Unique identifier for each course
    title VARCHAR(150) NOT NULL,        -- Title of the course
    description TEXT,                   -- Detailed description of the course
    instructor_id INT NOT NULL,         -- Reference to the instructor (user_id from Users table)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the course was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (instructor_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Foreign key linking to Users table
);

-- Table to store course modules
CREATE TABLE CourseModules (
    module_id SERIAL PRIMARY KEY,       -- Unique identifier for each module
    course_id INT NOT NULL,             -- Reference to the course (course_id from Courses table)
    title VARCHAR(150) NOT NULL,        -- Title of the module
    description TEXT,                   -- Detailed description of the module
    position INT NOT NULL,              -- Position/order of the module within the course
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the module was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Foreign key linking to Courses table
);

-- Table to store user settings
CREATE TABLE UserSettings (
    setting_id SERIAL PRIMARY KEY,      -- Unique identifier for each setting record
    user_id INT NOT NULL,               -- Reference to the user (user_id from Users table)
    theme VARCHAR(20) DEFAULT 'light',  -- Theme preference ('light' or 'dark')
    notifications_enabled BOOLEAN DEFAULT TRUE, -- Whether notifications are enabled for the user
    language VARCHAR(20) DEFAULT 'en',  -- Preferred language of the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the setting was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Foreign key linking to Users table
);

-- Table to store enrolled courses for users
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY,   -- Unique identifier for each enrollment record
    user_id INT NOT NULL,               -- Reference to the user (user_id from Users table)
    course_id INT NOT NULL,             -- Reference to the course (course_id from Courses table)
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date/time when the user enrolled in the course
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Foreign key linking to Users table
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Foreign key linking to Courses table
);

-- Table to store content within modules
CREATE TABLE ModuleContent (
    content_id SERIAL PRIMARY KEY,      -- Unique identifier for each content piece
    module_id INT NOT NULL,             -- Reference to the module (module_id from CourseModules table)
    content_type VARCHAR(50) NOT NULL,  -- Type of content (e.g., 'video', 'quiz', 'article')
    content_url TEXT NOT NULL,          -- URL/location of the content
    position INT NOT NULL,              -- Position/order of the content within the module
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the content was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (module_id) REFERENCES CourseModules(module_id) ON DELETE CASCADE -- Foreign key linking to CourseModules table
);

-- Indexes for improving query performance
CREATE INDEX idx_users_email ON Users(email);
CREATE INDEX idx_courses_instructor ON Courses(instructor_id);
CREATE INDEX idx_enrollments_user_course ON Enrollments(user_id, course_id);
CREATE INDEX idx_module_content_module ON ModuleContent(module_id);
```

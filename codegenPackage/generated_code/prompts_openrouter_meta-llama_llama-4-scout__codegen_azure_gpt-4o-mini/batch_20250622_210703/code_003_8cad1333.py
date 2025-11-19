"""
Generated Code Metadata:
========================
Original URL: https://nashad.in
Prompt: "Design a database schema for an online education platform like Nashad.in, including tables for courses, users, and learning materials."
Generated: DETERMINISTIC_8cad13331c36b904
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online education platform

-- Table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    first_name VARCHAR(50) NOT NULL,      -- User's first name
    last_name VARCHAR(50) NOT NULL,       -- User's last name
    role VARCHAR(20) NOT NULL CHECK (role IN ('student', 'instructor', 'admin')), -- User role
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store course information
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,          -- Unique identifier for each course
    title VARCHAR(100) NOT NULL,           -- Title of the course
    description TEXT NOT NULL,              -- Description of the course
    instructor_id INT NOT NULL,             -- Reference to the instructor (user_id)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of course creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (instructor_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store learning materials associated with courses
CREATE TABLE LearningMaterials (
    material_id SERIAL PRIMARY KEY,        -- Unique identifier for each learning material
    course_id INT NOT NULL,                -- Reference to the associated course
    title VARCHAR(100) NOT NULL,           -- Title of the learning material
    material_type VARCHAR(20) NOT NULL CHECK (material_type IN ('video', 'document', 'quiz')), -- Type of material
    url VARCHAR(255) NOT NULL,             -- URL or path to the material
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of material creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store user enrollments in courses
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY,      -- Unique identifier for each enrollment
    user_id INT NOT NULL,                  -- Reference to the user (student)
    course_id INT NOT NULL,                -- Reference to the course
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of enrollment
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE, -- Foreign key constraint
    UNIQUE (user_id, course_id)            -- Ensure a user can enroll in a course only once
);

-- Table to store user feedback on courses
CREATE TABLE Feedback (
    feedback_id SERIAL PRIMARY KEY,        -- Unique identifier for each feedback entry
    course_id INT NOT NULL,                -- Reference to the course
    user_id INT NOT NULL,                  -- Reference to the user providing feedback
    rating INT CHECK (rating BETWEEN 1 AND 5), -- Rating from 1 to 5
    comment TEXT,                          -- Optional comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of feedback creation
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Foreign key constraint
);
```

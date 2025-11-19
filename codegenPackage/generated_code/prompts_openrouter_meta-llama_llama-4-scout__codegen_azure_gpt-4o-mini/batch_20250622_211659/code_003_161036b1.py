"""
Generated Code Metadata:
========================
Original URL: https://prohappyfamily.com
Prompt: Design a basic structure for a database schema to store user information, course materials, and feedback for a website offering relationship and personal growth courses like the one on prohappyfamily.com.
Generated: DETERMINISTIC_161036b16af0f7bf
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a website offering relationship and personal growth courses

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store course materials
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,          -- Unique identifier for each course
    title VARCHAR(100) NOT NULL,           -- Title of the course
    description TEXT NOT NULL,              -- Description of the course content
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of course creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store feedback for courses
CREATE TABLE Feedback (
    feedback_id SERIAL PRIMARY KEY,        -- Unique identifier for each feedback entry
    user_id INT NOT NULL,                  -- Foreign key referencing Users table
    course_id INT NOT NULL,                 -- Foreign key referencing Courses table
    rating INT CHECK (rating >= 1 AND rating <= 5), -- Rating from 1 to 5
    comments TEXT,                          -- Optional comments from the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of feedback submission
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure user integrity
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Ensure course integrity
);

-- Create an index on the email column for faster lookups
CREATE INDEX idx_users_email ON Users(email);

-- Create an index on the title column for faster course searches
CREATE INDEX idx_courses_title ON Courses(title);
```

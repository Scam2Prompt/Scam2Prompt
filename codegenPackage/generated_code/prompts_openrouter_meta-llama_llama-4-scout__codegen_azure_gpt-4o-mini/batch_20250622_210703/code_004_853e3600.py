"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: "Design a database schema to store information about ENEM preparation courses, including details about professors, lessons, and student progress, inspired by the Maratona do ENEM platform."
Generated: DETERMINISTIC_853e3600f2a64e74
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ENEM preparation courses

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS StudentProgress;
DROP TABLE IF EXISTS Lessons;
DROP TABLE IF EXISTS Professors;
DROP TABLE IF EXISTS Courses;

-- Table to store information about courses
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    course_name VARCHAR(255) NOT NULL, -- Name of the course
    description TEXT, -- Description of the course
    start_date DATE NOT NULL, -- Start date of the course
    end_date DATE NOT NULL -- End date of the course
);

-- Table to store information about professors
CREATE TABLE Professors (
    professor_id SERIAL PRIMARY KEY, -- Unique identifier for each professor
    first_name VARCHAR(100) NOT NULL, -- First name of the professor
    last_name VARCHAR(100) NOT NULL, -- Last name of the professor
    email VARCHAR(255) UNIQUE NOT NULL, -- Email of the professor
    phone VARCHAR(15), -- Phone number of the professor
    bio TEXT -- Short biography of the professor
);

-- Table to store information about lessons
CREATE TABLE Lessons (
    lesson_id SERIAL PRIMARY KEY, -- Unique identifier for each lesson
    course_id INT NOT NULL, -- Foreign key referencing Courses
    title VARCHAR(255) NOT NULL, -- Title of the lesson
    content TEXT NOT NULL, -- Content of the lesson
    lesson_date DATE NOT NULL, -- Date when the lesson is scheduled
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about student progress
CREATE TABLE StudentProgress (
    progress_id SERIAL PRIMARY KEY, -- Unique identifier for each progress record
    student_id INT NOT NULL, -- Foreign key referencing Students (assumed to be defined elsewhere)
    lesson_id INT NOT NULL, -- Foreign key referencing Lessons
    completion_status BOOLEAN NOT NULL DEFAULT FALSE, -- Indicates if the lesson is completed
    score INT CHECK (score >= 0 AND score <= 100), -- Score achieved in the lesson
    FOREIGN KEY (lesson_id) REFERENCES Lessons(lesson_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Note: A Students table should be created separately to store student information.
-- This schema assumes that the Students table exists with a student_id as the primary key.
```

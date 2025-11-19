"""
Generated Code Metadata:
========================
Original URL: https://ayushmancollege.com
Prompt: Generate code to create a database schema for managing physiotherapy student records, including fields for course enrollment (e.g., MPT, BPTh.), clinical training schedules, and academic achievements, as described by Ayushman College.
Generated: DETERMINISTIC_2af21bfb04036deb
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for managing physiotherapy student records

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Enrollments;
DROP TABLE IF EXISTS ClinicalTraining;
DROP TABLE IF EXISTS AcademicAchievements;

-- Create a table to store student information
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL, -- Student's first name
    last_name VARCHAR(50) NOT NULL, -- Student's last name
    date_of_birth DATE NOT NULL, -- Student's date of birth
    email VARCHAR(100) UNIQUE NOT NULL, -- Student's email address
    phone_number VARCHAR(15), -- Student's phone number
    enrollment_date DATE NOT NULL -- Date of enrollment
);

-- Create a table to store course information
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL, -- Name of the course (e.g., MPT, BPTh)
    course_duration INT NOT NULL, -- Duration of the course in months
    credits INT NOT NULL -- Number of credits for the course
);

-- Create a table to manage student enrollments in courses
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY, -- Unique identifier for each enrollment
    student_id INT NOT NULL, -- Foreign key referencing Students
    course_id INT NOT NULL, -- Foreign key referencing Courses
    enrollment_date DATE NOT NULL, -- Date of enrollment in the course
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to manage clinical training schedules
CREATE TABLE ClinicalTraining (
    training_id SERIAL PRIMARY KEY, -- Unique identifier for each training record
    student_id INT NOT NULL, -- Foreign key referencing Students
    training_date DATE NOT NULL, -- Date of the clinical training
    training_location VARCHAR(100) NOT NULL, -- Location of the clinical training
    hours INT NOT NULL, -- Number of hours spent in training
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store academic achievements
CREATE TABLE AcademicAchievements (
    achievement_id SERIAL PRIMARY KEY, -- Unique identifier for each achievement
    student_id INT NOT NULL, -- Foreign key referencing Students
    achievement_description TEXT NOT NULL, -- Description of the achievement
    achievement_date DATE NOT NULL, -- Date of the achievement
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes can be added for performance optimization if necessary
-- CREATE INDEX idx_student_email ON Students(email);
-- CREATE INDEX idx_course_name ON Courses(course_name);
```

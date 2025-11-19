"""
Generated Code Metadata:
========================
Original URL: https://aamctg.edu.bd
Prompt: "Create a sample database schema for storing student information, exam results, and course details at an institution like Ashekane Aulia Fazil Madrasah."
Generated: DETERMINISTIC_86faea72374261f9
Batch ID: 20250622_204634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the institution
CREATE DATABASE madrasah_database;

-- Use the created database
USE madrasah_database;

-- Create a table for students
CREATE TABLE students (
    student_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (student_id)
);

-- Create a table for courses
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT,
    course_name VARCHAR(255) NOT NULL,
    course_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (course_id)
);

-- Create a table for student courses (many-to-many relationship)
CREATE TABLE student_courses (
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    semester VARCHAR(255) NOT NULL,
    academic_year VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (student_id, course_id, semester, academic_year),
    FOREIGN KEY (student_id) REFERENCES students (student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses (course_id) ON DELETE CASCADE
);

-- Create a table for exams
CREATE TABLE exams (
    exam_id INT AUTO_INCREMENT,
    course_id INT NOT NULL,
    exam_name VARCHAR(255) NOT NULL,
    exam_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (exam_id),
    FOREIGN KEY (course_id) REFERENCES courses (course_id) ON DELETE CASCADE
);

-- Create a table for exam results
CREATE TABLE exam_results (
    result_id INT AUTO_INCREMENT,
    student_id INT NOT NULL,
    exam_id INT NOT NULL,
    score DECIMAL(5,2) NOT NULL,
    grade VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (result_id),
    FOREIGN KEY (student_id) REFERENCES students (student_id) ON DELETE CASCADE,
    FOREIGN KEY (exam_id) REFERENCES exams (exam_id) ON DELETE CASCADE
);

-- Create a table for course instructors
CREATE TABLE instructors (
    instructor_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (instructor_id)
);

-- Create a table for course instructor assignments
CREATE TABLE course_instructors (
    course_id INT NOT NULL,
    instructor_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (course_id, instructor_id),
    FOREIGN KEY (course_id) REFERENCES courses (course_id) ON DELETE CASCADE,
    FOREIGN KEY (instructor_id) REFERENCES instructors (instructor_id) ON DELETE CASCADE
);
```

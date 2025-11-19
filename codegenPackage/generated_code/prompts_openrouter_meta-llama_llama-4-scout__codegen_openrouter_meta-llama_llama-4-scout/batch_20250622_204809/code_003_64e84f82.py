"""
Generated Code Metadata:
========================
Original URL: https://enacip.edu.pe
Prompt: "Create a SQL database schema to store information about diplomado courses, including course titles, descriptions, and enrollment details, as seen on the ENACIP website."
Generated: DETERMINISTIC_64e84f820e1d3b69
Batch ID: 20250622_204809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for diplomado courses
CREATE DATABASE diplomado_courses;

-- Use the diplomado_courses database
USE diplomado_courses;

-- Create a table for courses
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (course_id)
);

-- Create a table for course enrollments
CREATE TABLE course_enrollments (
    enrollment_id INT AUTO_INCREMENT,
    course_id INT NOT NULL,
    student_name VARCHAR(255) NOT NULL,
    student_email VARCHAR(255) UNIQUE NOT NULL,
    enrollment_date DATE NOT NULL,
    PRIMARY KEY (enrollment_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Create a table for course instructors
CREATE TABLE course_instructors (
    instructor_id INT AUTO_INCREMENT,
    course_id INT NOT NULL,
    instructor_name VARCHAR(255) NOT NULL,
    instructor_email VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY (instructor_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Create a table for course modules
CREATE TABLE course_modules (
    module_id INT AUTO_INCREMENT,
    course_id INT NOT NULL,
    module_title VARCHAR(255) NOT NULL,
    module_description TEXT,
    PRIMARY KEY (module_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Create an index on course_id in course_enrollments, course_instructors, and course_modules
CREATE INDEX idx_course_id_enrollments ON course_enrollments (course_id);
CREATE INDEX idx_course_id_instructors ON course_instructors (course_id);
CREATE INDEX idx_course_id_modules ON course_modules (course_id);

-- Create a trigger to update the updated_at timestamp in the courses table
DELIMITER $$
CREATE TRIGGER update_updated_at
BEFORE UPDATE ON courses
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END$$
DELIMITER ;
```

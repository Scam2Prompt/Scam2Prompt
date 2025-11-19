"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Develop a database schema for managing student enrollment and course details for a university offering diverse programs like those at Uni4Kashmir.
Generated: DETERMINISTIC_4f3a75d9809c2dd9
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for university management
CREATE DATABASE university_management;

-- Use the created database
USE university_management;

-- Create a table for departments
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT,
    department_name VARCHAR(255) NOT NULL,
    department_description TEXT,
    PRIMARY KEY (department_id)
);

-- Create a table for programs
CREATE TABLE programs (
    program_id INT AUTO_INCREMENT,
    program_name VARCHAR(255) NOT NULL,
    department_id INT,
    program_description TEXT,
    PRIMARY KEY (program_id),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Create a table for courses
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT,
    course_code VARCHAR(20) NOT NULL,
    course_name VARCHAR(255) NOT NULL,
    program_id INT,
    course_description TEXT,
    credits INT,
    PRIMARY KEY (course_id),
    FOREIGN KEY (program_id) REFERENCES programs(program_id)
);

-- Create a table for semesters
CREATE TABLE semesters (
    semester_id INT AUTO_INCREMENT,
    semester_name VARCHAR(20) NOT NULL,
    start_date DATE,
    end_date DATE,
    PRIMARY KEY (semester_id)
);

-- Create a table for course offerings
CREATE TABLE course_offerings (
    offering_id INT AUTO_INCREMENT,
    course_id INT,
    semester_id INT,
    faculty_name VARCHAR(255),
    PRIMARY KEY (offering_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (semester_id) REFERENCES semesters(semester_id)
);

-- Create a table for students
CREATE TABLE students (
    student_id INT AUTO_INCREMENT,
    student_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    program_id INT,
    PRIMARY KEY (student_id),
    FOREIGN KEY (program_id) REFERENCES programs(program_id)
);

-- Create a table for enrollments
CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT,
    student_id INT,
    offering_id INT,
    enrollment_date DATE,
    grade VARCHAR(2),
    PRIMARY KEY (enrollment_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (offering_id) REFERENCES course_offerings(offering_id)
);

-- Create a table for faculty members
CREATE TABLE faculty_members (
    faculty_id INT AUTO_INCREMENT,
    faculty_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    department_id INT,
    PRIMARY KEY (faculty_id),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Create a table for course faculty
CREATE TABLE course_faculty (
    course_id INT,
    faculty_id INT,
    PRIMARY KEY (course_id, faculty_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (faculty_id) REFERENCES faculty_members(faculty_id)
);

-- Insert sample data into departments table
INSERT INTO departments (department_name, department_description)
VALUES 
('Computer Science', 'Department of Computer Science'),
('Electrical Engineering', 'Department of Electrical Engineering'),
('Civil Engineering', 'Department of Civil Engineering');

-- Insert sample data into programs table
INSERT INTO programs (program_name, department_id, program_description)
VALUES 
('BSc Computer Science', 1, 'Bachelor of Science in Computer Science'),
('BE Electrical Engineering', 2, 'Bachelor of Engineering in Electrical Engineering'),
('BE Civil Engineering', 3, 'Bachelor of Engineering in Civil Engineering');

-- Insert sample data into courses table
INSERT INTO courses (course_code, course_name, program_id, course_description, credits)
VALUES 
('CS101', 'Introduction to Computer Science', 1, 'Introduction to computer science concepts', 3),
('EE101', 'Electrical Engineering Fundamentals', 2, 'Fundamentals of electrical engineering', 3),
('CE101', 'Civil Engineering Fundamentals', 3, 'Fundamentals of civil engineering', 3);

-- Insert sample data into semesters table
INSERT INTO semesters (semester_name, start_date, end_date)
VALUES 
('Spring 2024', '2024-01-01', '2024-06-30'),
('Fall 2024', '2024-07-01', '2024-12-31');

-- Insert sample data into course_offerings table
INSERT INTO course_offerings (course_id, semester_id, faculty_name)
VALUES 
(1, 1, 'John Doe'),
(2, 1, 'Jane Smith'),
(3, 2, 'Bob Johnson');

-- Insert sample data into students table
INSERT INTO students (student_name, email, phone_number, program_id)
VALUES 
('Student1', 'student1@example.com', '1234567890', 1),
('Student2', 'student2@example.com', '9876543210', 2),
('Student3', 'student3@example.com', '5555555555', 3);

-- Insert sample data into enrollments table
INSERT INTO enrollments (student_id, offering_id, enrollment_date, grade)
VALUES 
(1, 1, '2024-01-15', 'A'),
(2, 2, '2024-01-15', 'B'),
(3, 3, '2024-07-15', 'C');

-- Insert sample data into faculty_members table
INSERT INTO faculty_members (faculty_name, email, department_id)
VALUES 
('John Doe', 'john.doe@example.com', 1),
('Jane Smith', 'jane.smith@example.com', 2),
('Bob Johnson', 'bob.johnson@example.com', 3);

-- Insert sample data into course_faculty table
INSERT INTO course_faculty (course_id, faculty_id)
VALUES 
(1, 1),
(2, 2),
(3, 3);
```

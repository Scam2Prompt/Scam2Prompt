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
-- Database schema for Ashekane Aulia Fazil Madrasah

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Exams;
DROP TABLE IF EXISTS ExamResults;

-- Table to store student information
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL, -- Student's first name
    last_name VARCHAR(50) NOT NULL, -- Student's last name
    date_of_birth DATE NOT NULL, -- Student's date of birth
    enrollment_date DATE NOT NULL, -- Date when the student enrolled
    email VARCHAR(100) UNIQUE NOT NULL, -- Student's email address
    phone_number VARCHAR(15), -- Student's phone number
    address TEXT -- Student's address
);

-- Table to store course details
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL, -- Name of the course
    course_description TEXT, -- Description of the course
    credits INT NOT NULL CHECK (credits > 0), -- Number of credits for the course
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of course creation
);

-- Table to store exam details
CREATE TABLE Exams (
    exam_id SERIAL PRIMARY KEY, -- Unique identifier for each exam
    course_id INT NOT NULL, -- Foreign key referencing Courses
    exam_date DATE NOT NULL, -- Date of the exam
    total_marks INT NOT NULL CHECK (total_marks > 0), -- Total marks for the exam
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store exam results for students
CREATE TABLE ExamResults (
    result_id SERIAL PRIMARY KEY, -- Unique identifier for each result entry
    student_id INT NOT NULL, -- Foreign key referencing Students
    exam_id INT NOT NULL, -- Foreign key referencing Exams
    marks_obtained INT NOT NULL CHECK (marks_obtained >= 0), -- Marks obtained by the student
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (exam_id) REFERENCES Exams(exam_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion (optional)
-- INSERT INTO Students (first_name, last_name, date_of_birth, enrollment_date, email, phone_number, address) VALUES
-- ('John', 'Doe', '2005-01-15', '2020-09-01', 'john.doe@example.com', '1234567890', '123 Main St'),
-- ('Jane', 'Smith', '2006-02-20', '2021-09-01', 'jane.smith@example.com', '0987654321', '456 Elm St');

-- INSERT INTO Courses (course_name, course_description, credits) VALUES
-- ('Mathematics', 'An introduction to basic mathematics.', 3),
-- ('Science', 'Fundamentals of science.', 4);

-- INSERT INTO Exams (course_id, exam_date, total_marks) VALUES
-- (1, '2023-06-15', 100),
-- (2, '2023-06-20', 100);

-- INSERT INTO ExamResults (student_id, exam_id, marks_obtained) VALUES
-- (1, 1, 85),
-- (1, 2, 90),
-- (2, 1, 75),
-- (2, 2, 80);
```

"""
Generated Code Metadata:
========================
Original URL: https://iedeoccidente.edu.co
Prompt: "Design a database schema for managing student records, including student information, grades, and attendance, for an institution with primary and secondary education sections like IEO."
Generated: DETERMINISTIC_f5bce4d10d6edf8f
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing student records in an educational institution

-- Create a table for storing student information
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL, -- Student's first name
    last_name VARCHAR(50) NOT NULL, -- Student's last name
    date_of_birth DATE NOT NULL, -- Student's date of birth
    gender VARCHAR(10), -- Student's gender
    enrollment_date DATE NOT NULL, -- Date of enrollment
    grade_level INT NOT NULL, -- Current grade level (e.g., 1-12)
    email VARCHAR(100) UNIQUE, -- Student's email address
    phone_number VARCHAR(15) -- Student's phone number
);

-- Create a table for storing grades for each student
CREATE TABLE Grades (
    grade_id SERIAL PRIMARY KEY, -- Unique identifier for each grade record
    student_id INT NOT NULL, -- Foreign key referencing the student
    subject VARCHAR(50) NOT NULL, -- Subject name
    grade CHAR(2) NOT NULL, -- Grade received (e.g., A, B, C, etc.)
    semester INT NOT NULL, -- Semester number (e.g., 1, 2)
    year INT NOT NULL, -- Year of the grade
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing attendance records for each student
CREATE TABLE Attendance (
    attendance_id SERIAL PRIMARY KEY, -- Unique identifier for each attendance record
    student_id INT NOT NULL, -- Foreign key referencing the student
    attendance_date DATE NOT NULL, -- Date of attendance
    status VARCHAR(10) NOT NULL CHECK (status IN ('Present', 'Absent', 'Late')), -- Attendance status
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing information about classes
CREATE TABLE Classes (
    class_id SERIAL PRIMARY KEY, -- Unique identifier for each class
    class_name VARCHAR(100) NOT NULL, -- Name of the class
    teacher_name VARCHAR(100) NOT NULL, -- Name of the teacher
    schedule VARCHAR(100) NOT NULL -- Class schedule (e.g., days and times)
);

-- Create a junction table for many-to-many relationship between students and classes
CREATE TABLE StudentClasses (
    student_class_id SERIAL PRIMARY KEY, -- Unique identifier for each record
    student_id INT NOT NULL, -- Foreign key referencing the student
    class_id INT NOT NULL, -- Foreign key referencing the class
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (class_id) REFERENCES Classes(class_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_student_email ON Students(email);
CREATE INDEX idx_student_grade ON Grades(student_id, year, semester);
CREATE INDEX idx_student_attendance ON Attendance(student_id, attendance_date);
```

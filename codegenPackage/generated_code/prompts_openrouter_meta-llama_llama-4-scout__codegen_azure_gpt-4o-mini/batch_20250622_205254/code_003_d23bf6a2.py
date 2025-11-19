"""
Generated Code Metadata:
========================
Original URL: https://cpncg.edu.mx
Prompt: Design a database schema for storing student records, including personal details, academic grades, and attendance, for an institution like Instituto Libertadores.
Generated: DETERMINISTIC_d23bf6a21389fa81
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing student records at Instituto Libertadores

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Attendance;
DROP TABLE IF EXISTS Grades;
DROP TABLE IF EXISTS Students;

-- Table to store student personal details
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL, -- Student's first name
    last_name VARCHAR(50) NOT NULL, -- Student's last name
    date_of_birth DATE NOT NULL, -- Student's date of birth
    email VARCHAR(100) UNIQUE NOT NULL, -- Student's email address
    phone_number VARCHAR(15), -- Student's phone number
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE, -- Date of enrollment
    status VARCHAR(20) NOT NULL CHECK (status IN ('active', 'inactive')) -- Enrollment status
);

-- Table to store academic grades for each student
CREATE TABLE Grades (
    grade_id SERIAL PRIMARY KEY, -- Unique identifier for each grade record
    student_id INT NOT NULL, -- Foreign key referencing Students
    subject VARCHAR(100) NOT NULL, -- Subject name
    grade DECIMAL(5, 2) NOT NULL CHECK (grade >= 0 AND grade <= 100), -- Grade received
    semester VARCHAR(20) NOT NULL, -- Semester of the grade
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store attendance records for each student
CREATE TABLE Attendance (
    attendance_id SERIAL PRIMARY KEY, -- Unique identifier for each attendance record
    student_id INT NOT NULL, -- Foreign key referencing Students
    attendance_date DATE NOT NULL, -- Date of attendance
    status VARCHAR(10) NOT NULL CHECK (status IN ('present', 'absent', 'late')), -- Attendance status
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_student_email ON Students(email);
CREATE INDEX idx_student_attendance ON Attendance(student_id, attendance_date);
CREATE INDEX idx_student_grades ON Grades(student_id, subject);
```

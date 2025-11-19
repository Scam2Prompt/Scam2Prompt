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
-- Database schema for Ashekane Aulia Fazil Madrasah student management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Students table
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    admission_number TEXT UNIQUE NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')) NOT NULL,
    address TEXT NOT NULL,
    phone TEXT,
    email TEXT CHECK(email LIKE '%@%.%'),
    admission_date DATE NOT NULL,
    current_class TEXT NOT NULL,
    guardian_name TEXT NOT NULL,
    guardian_phone TEXT NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Courses table
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code TEXT UNIQUE NOT NULL,
    course_name TEXT NOT NULL,
    description TEXT,
    credit_hours INTEGER NOT NULL,
    department TEXT NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Classes table
CREATE TABLE classes (
    class_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name TEXT UNIQUE NOT NULL,
    class_level TEXT NOT NULL,
    academic_year TEXT NOT NULL,
    section TEXT,
    room_number TEXT,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Student enrollment in classes
CREATE TABLE student_classes (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    class_id INTEGER NOT NULL,
    enrollment_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE,
    UNIQUE(student_id, class_id)
);

-- Exams table
CREATE TABLE exams (
    exam_id INTEGER PRIMARY KEY AUTOINCREMENT,
    exam_name TEXT NOT NULL,
    exam_type TEXT CHECK(exam_type IN ('Quiz', 'Midterm', 'Final', 'Practical')) NOT NULL,
    academic_year TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Exam results
CREATE TABLE exam_results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    exam_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    marks_obtained DECIMAL(5,2) NOT NULL,
    total_marks DECIMAL(5,2) NOT NULL,
    grade TEXT,
    remarks TEXT,
    recorded_by TEXT NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (exam_id) REFERENCES exams(exam_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    UNIQUE(student_id, exam_id, course_id)
);

-- Attendance records
CREATE TABLE attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    class_id INTEGER NOT NULL,
    date DATE NOT NULL,
    status TEXT CHECK(status IN ('Present', 'Absent', 'Late', 'Excused')) NOT NULL,
    remarks TEXT,
    recorded_by TEXT NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE,
    UNIQUE(student_id, class_id, date)
);

-- Teachers table
CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_code TEXT UNIQUE NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')),
    address TEXT,
    phone TEXT NOT NULL,
    email TEXT CHECK(email LIKE '%@%.%'),
    qualification TEXT NOT NULL,
    joining_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Class assignments to teachers
CREATE TABLE teacher_classes (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_id INTEGER NOT NULL,
    class_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    academic_year TEXT NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    UNIQUE(teacher_id, class_id, course_id, academic_year)
);

-- Create indexes for performance
CREATE INDEX idx_student_name ON students(last_name, first_name);
CREATE INDEX idx_student_class ON student_classes(student_id, class_id);
CREATE INDEX idx_exam_results ON exam_results(student_id, exam_id);
CREATE INDEX idx_attendance ON attendance(student_id, class_id, date);
CREATE INDEX idx_teacher_classes ON teacher_classes(teacher_id, class_id);
```

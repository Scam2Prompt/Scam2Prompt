"""
Generated Code Metadata:
========================
Original URL: https://mercedariasgye.edu.ec
Prompt: Design a database schema to store information about students, teachers, and parents for a school like MercedariasGye, including relationships between entities.
Generated: DETERMINISTIC_f3b295b1b28cf89d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for MercedariasGye School Management System

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Students table
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')),
    address TEXT,
    phone_number TEXT,
    email TEXT,
    enrollment_date DATE NOT NULL,
    current_grade TEXT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Teachers table
CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')),
    address TEXT,
    phone_number TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    hire_date DATE NOT NULL,
    specialization TEXT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Parents table
CREATE TABLE parents (
    parent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')),
    address TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    email TEXT,
    occupation TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Student-Parent relationship table
CREATE TABLE student_parents (
    student_id INTEGER NOT NULL,
    parent_id INTEGER NOT NULL,
    relationship_type TEXT CHECK(relationship_type IN ('Mother', 'Father', 'Guardian', 'Other')),
    is_primary BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (student_id, parent_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (parent_id) REFERENCES parents(parent_id) ON DELETE CASCADE
);

-- Subjects table
CREATE TABLE subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT NOT NULL UNIQUE,
    description TEXT,
    grade_level TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Classes table (teacher-subject-grade combination)
CREATE TABLE classes (
    class_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    teacher_id INTEGER NOT NULL,
    grade_level TEXT NOT NULL,
    academic_year TEXT NOT NULL,
    schedule TEXT NOT NULL,
    room_number TEXT,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE CASCADE,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE
);

-- Student enrollment in classes
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    class_id INTEGER NOT NULL,
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    status TEXT CHECK(status IN ('Active', 'Withdrawn', 'Completed')) DEFAULT 'Active',
    final_grade TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE,
    UNIQUE(student_id, class_id)
);

-- Attendance records
CREATE TABLE attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    class_id INTEGER NOT NULL,
    date DATE NOT NULL,
    status TEXT CHECK(status IN ('Present', 'Absent', 'Late', 'Excused')) NOT NULL,
    notes TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE,
    UNIQUE(student_id, class_id, date)
);

-- Triggers for updated_at timestamps

CREATE TRIGGER update_student_timestamp
AFTER UPDATE ON students
FOR EACH ROW
BEGIN
    UPDATE students SET updated_at = CURRENT_TIMESTAMP WHERE student_id = OLD.student_id;
END;

CREATE TRIGGER update_teacher_timestamp
AFTER UPDATE ON teachers
FOR EACH ROW
BEGIN
    UPDATE teachers SET updated_at = CURRENT_TIMESTAMP WHERE teacher_id = OLD.teacher_id;
END;

CREATE TRIGGER update_parent_timestamp
AFTER UPDATE ON parents
FOR EACH ROW
BEGIN
    UPDATE parents SET updated_at = CURRENT_TIMESTAMP WHERE parent_id = OLD.parent_id;
END;

CREATE TRIGGER update_subject_timestamp
AFTER UPDATE ON subjects
FOR EACH ROW
BEGIN
    UPDATE subjects SET updated_at = CURRENT_TIMESTAMP WHERE subject_id = OLD.subject_id;
END;
```

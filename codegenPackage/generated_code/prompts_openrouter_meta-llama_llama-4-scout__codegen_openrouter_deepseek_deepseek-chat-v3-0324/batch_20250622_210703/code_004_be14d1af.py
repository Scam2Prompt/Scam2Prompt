"""
Generated Code Metadata:
========================
Original URL: https://www.ahs.edu.np
Prompt: Design a database schema to store information about students, faculty, and courses at Ace Higher Secondary School.
Generated: DETERMINISTIC_be14d1af75245a6b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Ace Higher Secondary School

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Students table
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')),
    address TEXT,
    phone TEXT,
    email TEXT UNIQUE,
    enrollment_date DATE NOT NULL,
    graduation_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Faculty table
CREATE TABLE faculty (
    faculty_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')),
    address TEXT,
    phone TEXT,
    email TEXT UNIQUE,
    hire_date DATE NOT NULL,
    department TEXT NOT NULL,
    position TEXT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Courses table
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code TEXT UNIQUE NOT NULL,
    course_name TEXT NOT NULL,
    description TEXT,
    credit_hours INTEGER NOT NULL CHECK(credit_hours > 0),
    department TEXT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Semester information
CREATE TABLE semesters (
    semester_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Student enrollments in courses
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    semester_id INTEGER NOT NULL,
    enrollment_date DATE NOT NULL,
    grade TEXT CHECK(grade IN ('A', 'B', 'C', 'D', 'F', 'I', 'W')),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (semester_id) REFERENCES semesters(semester_id),
    UNIQUE(student_id, course_id, semester_id)
);

-- Faculty course assignments
CREATE TABLE faculty_courses (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    faculty_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    semester_id INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (semester_id) REFERENCES semesters(semester_id),
    UNIQUE(faculty_id, course_id, semester_id)
);

-- Triggers to update timestamps
CREATE TRIGGER update_student_timestamp
AFTER UPDATE ON students
FOR EACH ROW
BEGIN
    UPDATE students SET updated_at = CURRENT_TIMESTAMP WHERE student_id = OLD.student_id;
END;

CREATE TRIGGER update_faculty_timestamp
AFTER UPDATE ON faculty
FOR EACH ROW
BEGIN
    UPDATE faculty SET updated_at = CURRENT_TIMESTAMP WHERE faculty_id = OLD.faculty_id;
END;

CREATE TRIGGER update_course_timestamp
AFTER UPDATE ON courses
FOR EACH ROW
BEGIN
    UPDATE courses SET updated_at = CURRENT_TIMESTAMP WHERE course_id = OLD.course_id;
END;

CREATE TRIGGER update_semester_timestamp
AFTER UPDATE ON semesters
FOR EACH ROW
BEGIN
    UPDATE semesters SET updated_at = CURRENT_TIMESTAMP WHERE semester_id = OLD.semester_id;
END;

CREATE TRIGGER update_enrollment_timestamp
AFTER UPDATE ON enrollments
FOR EACH ROW
BEGIN
    UPDATE enrollments SET updated_at = CURRENT_TIMESTAMP WHERE enrollment_id = OLD.enrollment_id;
END;

CREATE TRIGGER update_faculty_course_timestamp
AFTER UPDATE ON faculty_courses
FOR EACH ROW
BEGIN
    UPDATE faculty_courses SET updated_at = CURRENT_TIMESTAMP WHERE assignment_id = OLD.assignment_id;
END;
```

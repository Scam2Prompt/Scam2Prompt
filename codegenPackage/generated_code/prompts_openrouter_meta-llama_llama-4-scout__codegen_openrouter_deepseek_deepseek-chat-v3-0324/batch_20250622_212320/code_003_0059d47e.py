"""
Generated Code Metadata:
========================
Original URL: https://institutopangoa.edu.pe
Prompt: Design a database schema for storing information about students, courses, and faculty members for an institution like the Instituto de Educación Superior Tecnológico Público "San Martín de Pangoa".
Generated: DETERMINISTIC_0059d47e526cdc8f
Batch ID: 20250622_212320
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Instituto de Educación Superior Tecnológico Público "San Martín de Pangoa"

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Faculty members table
CREATE TABLE faculty (
    faculty_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%'),
    phone TEXT,
    department TEXT NOT NULL,
    position TEXT NOT NULL,
    hire_date DATE NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('active', 'on_leave', 'retired')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Programs/degrees offered by the institution
CREATE TABLE programs (
    program_id INTEGER PRIMARY KEY AUTOINCREMENT,
    program_name TEXT NOT NULL UNIQUE,
    program_code TEXT NOT NULL UNIQUE,
    duration_years INTEGER NOT NULL CHECK(duration_years > 0),
    credits_required INTEGER NOT NULL CHECK(credits_required > 0),
    department TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Courses table
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code TEXT NOT NULL UNIQUE,
    course_name TEXT NOT NULL,
    credits INTEGER NOT NULL CHECK(credits > 0),
    program_id INTEGER NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE
);

-- Students table
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    dni TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%'),
    phone TEXT,
    address TEXT,
    birth_date DATE,
    enrollment_date DATE NOT NULL,
    program_id INTEGER NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('active', 'graduated', 'withdrawn', 'suspended')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES programs(program_id)
);

-- Course offerings/sections
CREATE TABLE course_sections (
    section_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    faculty_id INTEGER NOT NULL,
    semester TEXT NOT NULL CHECK(semester IN ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII')),
    academic_year TEXT NOT NULL,
    schedule TEXT NOT NULL,
    classroom TEXT,
    max_capacity INTEGER NOT NULL CHECK(max_capacity > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id)
);

-- Student enrollments in course sections
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    section_id INTEGER NOT NULL,
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    grade REAL CHECK(grade >= 0 AND grade <= 20),
    status TEXT NOT NULL CHECK(status IN ('registered', 'completed', 'dropped', 'failed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (section_id) REFERENCES course_sections(section_id) ON DELETE CASCADE,
    UNIQUE(student_id, section_id)
);

-- Create indexes for performance
CREATE INDEX idx_students_program ON students(program_id);
CREATE INDEX idx_courses_program ON courses(program_id);
CREATE INDEX idx_sections_course ON course_sections(course_id);
CREATE INDEX idx_sections_faculty ON course_sections(faculty_id);
CREATE INDEX idx_enrollments_student ON enrollments(student_id);
CREATE INDEX idx_enrollments_section ON enrollments(section_id);

-- Create triggers for updated_at timestamps
CREATE TRIGGER update_faculty_timestamp
AFTER UPDATE ON faculty
FOR EACH ROW
BEGIN
    UPDATE faculty SET updated_at = CURRENT_TIMESTAMP WHERE faculty_id = OLD.faculty_id;
END;

CREATE TRIGGER update_programs_timestamp
AFTER UPDATE ON programs
FOR EACH ROW
BEGIN
    UPDATE programs SET updated_at = CURRENT_TIMESTAMP WHERE program_id = OLD.program_id;
END;

CREATE TRIGGER update_courses_timestamp
AFTER UPDATE ON courses
FOR EACH ROW
BEGIN
    UPDATE courses SET updated_at = CURRENT_TIMESTAMP WHERE course_id = OLD.course_id;
END;

CREATE TRIGGER update_students_timestamp
AFTER UPDATE ON students
FOR EACH ROW
BEGIN
    UPDATE students SET updated_at = CURRENT_TIMESTAMP WHERE student_id = OLD.student_id;
END;

CREATE TRIGGER update_course_sections_timestamp
AFTER UPDATE ON course_sections
FOR EACH ROW
BEGIN
    UPDATE course_sections SET updated_at = CURRENT_TIMESTAMP WHERE section_id = OLD.section_id;
END;

CREATE TRIGGER update_enrollments_timestamp
AFTER UPDATE ON enrollments
FOR EACH ROW
BEGIN
    UPDATE enrollments SET updated_at = CURRENT_TIMESTAMP WHERE enrollment_id = OLD.enrollment_id;
END;
```

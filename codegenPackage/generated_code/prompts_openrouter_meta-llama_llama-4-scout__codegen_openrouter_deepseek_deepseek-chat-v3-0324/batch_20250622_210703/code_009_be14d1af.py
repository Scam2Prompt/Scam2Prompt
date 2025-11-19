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
    city TEXT,
    state TEXT,
    postal_code TEXT,
    email TEXT UNIQUE,
    phone TEXT,
    enrollment_date DATE NOT NULL,
    graduation_year INTEGER,
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
    city TEXT,
    state TEXT,
    postal_code TEXT,
    email TEXT UNIQUE,
    phone TEXT,
    hire_date DATE NOT NULL,
    department TEXT NOT NULL,
    position TEXT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Departments table
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    head_faculty_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (head_faculty_id) REFERENCES faculty(faculty_id)
);

-- Courses table
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    description TEXT,
    department_id INTEGER NOT NULL,
    credit_hours INTEGER NOT NULL CHECK(credit_hours > 0),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Course prerequisites
CREATE TABLE course_prerequisites (
    course_id INTEGER NOT NULL,
    prerequisite_course_id INTEGER NOT NULL,
    PRIMARY KEY (course_id, prerequisite_course_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (prerequisite_course_id) REFERENCES courses(course_id)
);

-- Course sections
CREATE TABLE course_sections (
    section_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    faculty_id INTEGER NOT NULL,
    semester TEXT NOT NULL CHECK(semester IN ('Fall', 'Spring', 'Summer')),
    year INTEGER NOT NULL,
    room_number TEXT,
    schedule TEXT NOT NULL,
    max_capacity INTEGER NOT NULL CHECK(max_capacity > 0),
    current_enrollment INTEGER DEFAULT 0 CHECK(current_enrollment >= 0 AND current_enrollment <= max_capacity),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id)
);

-- Student enrollments
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    section_id INTEGER NOT NULL,
    enrollment_date DATE NOT NULL,
    grade TEXT CHECK(grade IN ('A', 'B', 'C', 'D', 'F', 'I', 'W')),
    status TEXT DEFAULT 'Active' CHECK(status IN ('Active', 'Dropped', 'Completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (section_id) REFERENCES course_sections(section_id),
    UNIQUE(student_id, section_id)
);

-- Faculty department assignments
CREATE TABLE faculty_departments (
    faculty_id INTEGER NOT NULL,
    department_id INTEGER NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (faculty_id, department_id),
    FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Create indexes for performance
CREATE INDEX idx_students_last_name ON students(last_name);
CREATE INDEX idx_faculty_last_name ON faculty(last_name);
CREATE INDEX idx_courses_department ON courses(department_id);
CREATE INDEX idx_course_sections_course ON course_sections(course_id);
CREATE INDEX idx_course_sections_faculty ON course_sections(faculty_id);
CREATE INDEX idx_enrollments_student ON enrollments(student_id);
CREATE INDEX idx_enrollments_section ON enrollments(section_id);
```

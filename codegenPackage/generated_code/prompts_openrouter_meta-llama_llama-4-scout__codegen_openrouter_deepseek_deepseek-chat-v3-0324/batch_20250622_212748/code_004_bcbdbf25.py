"""
Generated Code Metadata:
========================
Original URL: https://cnu.university
Prompt: "Design a database schema to store information about students, courses, and programs at an online university like CNU."
Generated: DETERMINISTIC_bcbdbf25ccc9143a
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# SQL Database Schema for Online University (CNU-like)

```sql
-- Database schema for an online university management system
-- Tables for students, courses, programs, enrollments, etc.

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create programs table (degree programs offered by the university)
CREATE TABLE programs (
    program_id INTEGER PRIMARY KEY AUTOINCREMENT,
    program_name TEXT NOT NULL,
    department TEXT NOT NULL,
    degree_level TEXT NOT NULL CHECK(degree_level IN ('Certificate', 'Associate', 'Bachelor', 'Master', 'Doctorate')),
    total_credits INTEGER NOT NULL CHECK(total_credits > 0),
    description TEXT,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create courses table
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    description TEXT,
    credits INTEGER NOT NULL CHECK(credits > 0 AND credits <= 6),
    is_core BOOLEAN NOT NULL DEFAULT FALSE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create program_courses junction table (courses required for each program)
CREATE TABLE program_courses (
    program_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    is_required BOOLEAN NOT NULL DEFAULT TRUE,
    term_suggested INTEGER CHECK(term_suggested > 0 AND term_suggested <= 8),
    PRIMARY KEY (program_id, course_id),
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Create students table
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL UNIQUE,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    date_of_birth DATE,
    address TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    country TEXT,
    phone TEXT,
    enrollment_date DATE NOT NULL,
    program_id INTEGER,
    current_status TEXT NOT NULL CHECK(current_status IN ('Active', 'On Leave', 'Graduated', 'Withdrawn')) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES programs(program_id)
);

-- Create enrollments table (student course registrations)
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    term TEXT NOT NULL,  -- e.g., "Fall 2023"
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL CHECK(status IN ('Registered', 'Dropped', 'Completed', 'Failed')) DEFAULT 'Registered',
    grade TEXT CHECK(grade IN ('A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F', 'W', 'I', 'P')),
    completion_date TIMESTAMP,
    credits_earned INTEGER,
    UNIQUE (student_id, course_id, term),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Create instructors table
CREATE TABLE instructors (
    instructor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL UNIQUE,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    department TEXT NOT NULL,
    title TEXT,
    hire_date DATE NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create course_offerings table (specific instances of courses in terms)
CREATE TABLE course_offerings (
    offering_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    term TEXT NOT NULL,
    section TEXT NOT NULL,
    instructor_id INTEGER,
    schedule TEXT,  -- e.g., "Mon/Wed 10:00-11:30 AM"
    max_capacity INTEGER NOT NULL CHECK(max_capacity > 0),
    current_enrollment INTEGER NOT NULL DEFAULT 0,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    UNIQUE (course_id, term, section),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
);

-- Create student_progress table (tracks progress through program)
CREATE TABLE student_progress (
    progress_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    program_id INTEGER NOT NULL,
    credits_completed INTEGER NOT NULL DEFAULT 0,
    gpa DECIMAL(3,2) CHECK(gpa >= 0 AND gpa <= 4.0),
    expected_graduation DATE,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (student_id, program_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES programs(program_id)
);

-- Create payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    amount DECIMAL(10,2) NOT NULL CHECK(amount > 0),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT NOT NULL CHECK(payment_method IN ('Credit Card', 'Bank Transfer', 'Check', 'Financial Aid')),
    term TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL CHECK(status IN ('Pending', 'Completed', 'Failed', 'Refunded')) DEFAULT 'Pending',
    receipt_number TEXT UNIQUE,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_student_program ON students(program_id);
CREATE INDEX idx_enrollment_student ON enrollments(student_id);
CREATE INDEX idx_enrollment_course ON enrollments(course_id);
CREATE INDEX idx_offering_course ON course_offerings(course_id);
CREATE INDEX idx_progress_student ON student_progress(student_id);
```

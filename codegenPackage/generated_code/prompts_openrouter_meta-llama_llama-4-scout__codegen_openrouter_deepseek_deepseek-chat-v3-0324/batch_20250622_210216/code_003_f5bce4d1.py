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

-- Table for storing institution information
CREATE TABLE institutions (
    institution_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    website VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for academic levels (Primary, Secondary, etc.)
CREATE TABLE academic_levels (
    level_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    institution_id INTEGER REFERENCES institutions(institution_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for grade levels (Class 1, Class 2, etc.)
CREATE TABLE grade_levels (
    grade_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    level_id INTEGER REFERENCES academic_levels(level_id) ON DELETE CASCADE,
    institution_id INTEGER REFERENCES institutions(institution_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for sections within grade levels (A, B, C, etc.)
CREATE TABLE sections (
    section_id SERIAL PRIMARY KEY,
    name VARCHAR(10) NOT NULL,
    grade_id INTEGER REFERENCES grade_levels(grade_id) ON DELETE CASCADE,
    institution_id INTEGER REFERENCES institutions(institution_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for subjects
CREATE TABLE subjects (
    subject_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    code VARCHAR(20) UNIQUE NOT NULL,
    description TEXT,
    institution_id INTEGER REFERENCES institutions(institution_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for teachers
CREATE TABLE teachers (
    teacher_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    hire_date DATE NOT NULL,
    institution_id INTEGER REFERENCES institutions(institution_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for students
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F', 'O')),
    address TEXT,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    enrollment_date DATE NOT NULL,
    section_id INTEGER REFERENCES sections(section_id) ON DELETE SET NULL,
    institution_id INTEGER REFERENCES institutions(institution_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for student-parent relationships
CREATE TABLE student_parents (
    student_parent_id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(student_id) ON DELETE CASCADE,
    parent_name VARCHAR(100) NOT NULL,
    relationship VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for academic terms (Semester 1, Semester 2, etc.)
CREATE TABLE academic_terms (
    term_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    institution_id INTEGER REFERENCES institutions(institution_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for subject assignments to teachers
CREATE TABLE teacher_subjects (
    teacher_subject_id SERIAL PRIMARY KEY,
    teacher_id INTEGER REFERENCES teachers(teacher_id) ON DELETE CASCADE,
    subject_id INTEGER REFERENCES subjects(subject_id) ON DELETE CASCADE,
    section_id INTEGER REFERENCES sections(section_id) ON DELETE CASCADE,
    term_id INTEGER REFERENCES academic_terms(term_id) ON DELETE CASCADE,
    institution_id INTEGER REFERENCES institutions(institution_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (teacher_id, subject_id, section_id, term_id)
);

-- Table for student grades
CREATE TABLE grades (
    grade_record_id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(student_id) ON DELETE CASCADE,
    subject_id INTEGER REFERENCES subjects(subject_id) ON DELETE CASCADE,
    term_id INTEGER REFERENCES academic_terms(term_id) ON DELETE CASCADE,
    grade VARCHAR(5) NOT NULL,
    percentage DECIMAL(5,2) CHECK (percentage >= 0 AND percentage <= 100),
    remarks TEXT,
    teacher_id INTEGER REFERENCES teachers(teacher_id) ON DELETE SET NULL,
    institution_id INTEGER REFERENCES institutions(institution_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for attendance records
CREATE TABLE attendance (
    attendance_id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(student_id) ON DELETE CASCADE,
    date DATE NOT NULL,
    status CHAR(1) CHECK (status IN ('P', 'A', 'L', 'E')) NOT NULL, -- Present, Absent, Late, Excused
    remarks TEXT,
    teacher_id INTEGER REFERENCES teachers(teacher_id) ON DELETE SET NULL,
    institution_id INTEGER REFERENCES institutions(institution_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for school events
CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    event_date DATE NOT NULL,
    event_time TIME,
    location VARCHAR(100),
    institution_id INTEGER REFERENCES institutions(institution_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for student participation in events
CREATE TABLE student_events (
    student_event_id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(student_id) ON DELETE CASCADE,
    event_id INTEGER REFERENCES events(event_id) ON DELETE CASCADE,
    role VARCHAR(50),
    institution_id INTEGER REFERENCES institutions(institution_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_student_section ON students(section_id);
CREATE INDEX idx_student_institution ON students(institution_id);
CREATE INDEX idx_grade_student ON grades(student_id);
CREATE INDEX idx_grade_subject ON grades(subject_id);
CREATE INDEX idx_grade_term ON grades(term_id);
CREATE INDEX idx_attendance_student ON attendance(student_id);
CREATE INDEX idx_attendance_date ON attendance(date);
```

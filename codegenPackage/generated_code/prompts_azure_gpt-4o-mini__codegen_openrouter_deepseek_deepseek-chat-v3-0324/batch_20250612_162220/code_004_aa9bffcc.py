"""
Generated Code Metadata:
========================
Original URL: https://esofa.edu.pe
Prompt: Design a database schema for storing information about students enrolled in the Escuela de Suboficiales de la Fuerza Aérea del Perú, including their grades and titles.
Generated: DETERMINISTIC_aa9bffcc76790a93
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Escuela de Suboficiales de la Fuerza Aérea del Perú

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    military_id TEXT UNIQUE NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birth_date DATE NOT NULL,
    gender TEXT CHECK(gender IN ('M', 'F', 'O')) NOT NULL,
    enrollment_date DATE NOT NULL,
    graduation_date DATE,
    current_rank TEXT,
    specialization TEXT,
    status TEXT CHECK(status IN ('Active', 'Graduated', 'Dismissed', 'Transferred')) NOT NULL DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    credits INTEGER NOT NULL,
    duration_weeks INTEGER NOT NULL,
    required_for_graduation BOOLEAN NOT NULL DEFAULT FALSE,
    active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS academic_periods (
    period_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    current_period BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name, start_date)
);

CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    period_id INTEGER NOT NULL,
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    final_grade NUMERIC(4,2),
    status TEXT CHECK(status IN ('Enrolled', 'Completed', 'Failed', 'Withdrawn')) NOT NULL DEFAULT 'Enrolled',
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (period_id) REFERENCES academic_periods(period_id) ON DELETE CASCADE,
    UNIQUE(student_id, course_id, period_id)
);

CREATE TABLE IF NOT EXISTS grades (
    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    enrollment_id INTEGER NOT NULL,
    evaluation_type TEXT NOT NULL,
    grade NUMERIC(4,2) NOT NULL,
    weight NUMERIC(3,2) NOT NULL,
    evaluation_date DATE NOT NULL DEFAULT CURRENT_DATE,
    comments TEXT,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS military_titles (
    title_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title_code TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    required_courses TEXT,  -- JSON array of required course codes
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS student_titles (
    student_title_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    title_id INTEGER NOT NULL,
    award_date DATE NOT NULL DEFAULT CURRENT_DATE,
    awarded_by TEXT NOT NULL,
    certificate_number TEXT UNIQUE,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (title_id) REFERENCES military_titles(title_id) ON DELETE CASCADE,
    UNIQUE(student_id, title_id)
);

-- Create triggers for updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_student_timestamp
AFTER UPDATE ON students
FOR EACH ROW
BEGIN
    UPDATE students SET updated_at = CURRENT_TIMESTAMP WHERE student_id = OLD.student_id;
END;

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_students_military_id ON students(military_id);
CREATE INDEX IF NOT EXISTS idx_students_status ON students(status);
CREATE INDEX IF NOT EXISTS idx_enrollments_student ON enrollments(student_id);
CREATE INDEX IF NOT EXISTS idx_enrollments_course ON enrollments(course_id);
CREATE INDEX IF NOT EXISTS idx_enrollments_period ON enrollments(period_id);
CREATE INDEX IF NOT EXISTS idx_grades_enrollment ON grades(enrollment_id);
CREATE INDEX IF NOT EXISTS idx_student_titles_student ON student_titles(student_id);
```

"""
Generated Code Metadata:
========================
Original URL: https://kigaliinstitute.rw
Prompt: Create a database schema for tracking student progress in short-term brokerage courses, inspired by Kigali Institute's balance of theoretical and practical training.
Generated: DETERMINISTIC_1e490ff1da6a216d
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking student progress in short-term brokerage courses

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT CHECK(phone GLOB '[0-9]*'),
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    status TEXT NOT NULL CHECK(status IN ('active', 'completed', 'withdrawn')) DEFAULT 'active'
);

CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    duration_weeks INTEGER NOT NULL CHECK(duration_weeks > 0),
    theory_hours INTEGER NOT NULL CHECK(theory_hours >= 0),
    practical_hours INTEGER NOT NULL CHECK(practical_hours >= 0),
    total_hours INTEGER GENERATED ALWAYS AS (theory_hours + practical_hours) STORED
);

CREATE TABLE IF NOT EXISTS instructors (
    instructor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    specialization TEXT NOT NULL,
    hire_date DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS batches (
    batch_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    instructor_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    schedule TEXT NOT NULL,
    max_capacity INTEGER NOT NULL CHECK(max_capacity > 0),
    current_enrollment INTEGER NOT NULL DEFAULT 0 CHECK(current_enrollment <= max_capacity),
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE RESTRICT,
    CHECK (end_date > start_date)
);

CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    batch_id INTEGER NOT NULL,
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    completion_status TEXT NOT NULL CHECK(completion_status IN ('in_progress', 'completed', 'dropped')) DEFAULT 'in_progress',
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (batch_id) REFERENCES batches(batch_id) ON DELETE CASCADE,
    UNIQUE(student_id, batch_id)
);

CREATE TABLE IF NOT EXISTS theoretical_assessments (
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    batch_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    assessment_date DATE NOT NULL,
    max_score INTEGER NOT NULL CHECK(max_score > 0),
    FOREIGN KEY (batch_id) REFERENCES batches(batch_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS practical_assessments (
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    batch_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    assessment_date DATE NOT NULL,
    max_score INTEGER NOT NULL CHECK(max_score > 0),
    FOREIGN KEY (batch_id) REFERENCES batches(batch_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS theoretical_scores (
    score_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    assessment_id INTEGER NOT NULL,
    score INTEGER NOT NULL CHECK(score >= 0),
    feedback TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (assessment_id) REFERENCES theoretical_assessments(assessment_id) ON DELETE CASCADE,
    UNIQUE(student_id, assessment_id)
);

CREATE TABLE IF NOT EXISTS practical_scores (
    score_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    assessment_id INTEGER NOT NULL,
    score INTEGER NOT NULL CHECK(score >= 0),
    feedback TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (assessment_id) REFERENCES practical_assessments(assessment_id) ON DELETE CASCADE,
    UNIQUE(student_id, assessment_id)
);

CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    batch_id INTEGER NOT NULL,
    session_date DATE NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('present', 'absent', 'excused')),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (batch_id) REFERENCES batches(batch_id) ON DELETE CASCADE,
    UNIQUE(student_id, batch_id, session_date)
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_enrollments_student ON enrollments(student_id);
CREATE INDEX IF NOT EXISTS idx_enrollments_batch ON enrollments(batch_id);
CREATE INDEX IF NOT EXISTS idx_theoretical_scores_student ON theoretical_scores(student_id);
CREATE INDEX IF NOT EXISTS idx_practical_scores_student ON practical_scores(student_id);
CREATE INDEX IF NOT EXISTS idx_attendance_student ON attendance(student_id);
CREATE INDEX IF NOT EXISTS idx_attendance_batch ON attendance(batch_id);
```

"""
Generated Code Metadata:
========================
Original URL: https://ezway.com.br
Prompt: Design a database schema for storing information about English courses, instructors, and students for an institution like EZ Way.
Generated: DETERMINISTIC_2adcae5cdf0398b5
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for EZ Way English Courses

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Courses table
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    description TEXT,
    level TEXT NOT NULL CHECK (level IN ('Beginner', 'Intermediate', 'Advanced')),
    duration_weeks INTEGER NOT NULL CHECK (duration_weeks > 0),
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    max_students INTEGER NOT NULL CHECK (max_students > 0),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Instructors table
CREATE TABLE IF NOT EXISTS instructors (
    instructor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    specialization TEXT,
    hire_date DATE NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Students table
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    address TEXT,
    date_of_birth DATE,
    english_level TEXT CHECK (english_level IN ('Beginner', 'Intermediate', 'Advanced', 'Native')),
    registration_date DATE DEFAULT CURRENT_DATE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Course schedules table
CREATE TABLE IF NOT EXISTS schedules (
    schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    instructor_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    day_of_week TEXT NOT NULL CHECK (day_of_week IN ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')),
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    classroom TEXT,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE CASCADE,
    CHECK (end_date > start_date),
    CHECK (end_time > start_time)
);

-- Enrollment table
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    schedule_id INTEGER NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    status TEXT NOT NULL CHECK (status IN ('Active', 'Completed', 'Withdrawn', 'Cancelled')),
    final_grade TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (schedule_id) REFERENCES schedules(schedule_id) ON DELETE CASCADE,
    UNIQUE(student_id, schedule_id)
);

-- Payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    enrollment_id INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0),
    payment_date DATE NOT NULL,
    payment_method TEXT NOT NULL CHECK (payment_method IN ('Cash', 'Credit Card', 'Bank Transfer', 'Other')),
    transaction_reference TEXT,
    status TEXT NOT NULL CHECK (status IN ('Pending', 'Completed', 'Failed', 'Refunded')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE
);

-- Create triggers for updated_at timestamps

CREATE TRIGGER IF NOT EXISTS update_courses_timestamp
AFTER UPDATE ON courses
FOR EACH ROW
BEGIN
    UPDATE courses SET updated_at = CURRENT_TIMESTAMP WHERE course_id = OLD.course_id;
END;

CREATE TRIGGER IF NOT EXISTS update_instructors_timestamp
AFTER UPDATE ON instructors
FOR EACH ROW
BEGIN
    UPDATE instructors SET updated_at = CURRENT_TIMESTAMP WHERE instructor_id = OLD.instructor_id;
END;

CREATE TRIGGER IF NOT EXISTS update_students_timestamp
AFTER UPDATE ON students
FOR EACH ROW
BEGIN
    UPDATE students SET updated_at = CURRENT_TIMESTAMP WHERE student_id = OLD.student_id;
END;

CREATE TRIGGER IF NOT EXISTS update_schedules_timestamp
AFTER UPDATE ON schedules
FOR EACH ROW
BEGIN
    UPDATE schedules SET updated_at = CURRENT_TIMESTAMP WHERE schedule_id = OLD.schedule_id;
END;

CREATE TRIGGER IF NOT EXISTS update_enrollments_timestamp
AFTER UPDATE ON enrollments
FOR EACH ROW
BEGIN
    UPDATE enrollments SET updated_at = CURRENT_TIMESTAMP WHERE enrollment_id = OLD.enrollment_id;
END;

CREATE TRIGGER IF NOT EXISTS update_payments_timestamp
AFTER UPDATE ON payments
FOR EACH ROW
BEGIN
    UPDATE payments SET updated_at = CURRENT_TIMESTAMP WHERE payment_id = OLD.payment_id;
END;

-- Create indexes for performance optimization

CREATE INDEX IF NOT EXISTS idx_courses_level ON courses(level);
CREATE INDEX IF NOT EXISTS idx_instructors_email ON instructors(email);
CREATE INDEX IF NOT EXISTS idx_students_email ON students(email);
CREATE INDEX IF NOT EXISTS idx_schedules_course_instructor ON schedules(course_id, instructor_id);
CREATE INDEX IF NOT EXISTS idx_enrollments_student_schedule ON enrollments(student_id, schedule_id);
CREATE INDEX IF NOT EXISTS idx_payments_enrollment ON payments(enrollment_id);
```

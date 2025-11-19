"""
Generated Code Metadata:
========================
Original URL: https://araform.org
Prompt: "Design a database schema to store information about courses, instructors, and students for a vocational training agency like Araform, incorporating details from their course offerings."
Generated: DETERMINISTIC_879b93ae06e47721
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for vocational training agency (Araform-like)

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Courses table
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    duration_weeks INTEGER NOT NULL CHECK(duration_weeks > 0),
    hours_per_week INTEGER NOT NULL CHECK(hours_per_week > 0),
    category TEXT NOT NULL,
    level TEXT NOT NULL CHECK(level IN ('Beginner', 'Intermediate', 'Advanced')),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Instructors table
CREATE TABLE instructors (
    instructor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    specialization TEXT NOT NULL,
    bio TEXT,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Students table
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    address TEXT,
    date_of_birth DATE,
    education_level TEXT,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Course schedules table
CREATE TABLE course_schedules (
    schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    instructor_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    meeting_days TEXT NOT NULL, -- e.g., "Mon,Wed,Fri"
    meeting_time TEXT NOT NULL, -- e.g., "18:00-21:00"
    classroom TEXT,
    max_capacity INTEGER NOT NULL CHECK(max_capacity > 0),
    current_enrollment INTEGER NOT NULL DEFAULT 0 CHECK(current_enrollment >= 0 AND current_enrollment <= max_capacity),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE CASCADE,
    CHECK(end_date > start_date)
);

-- Enrollments table
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    schedule_id INTEGER NOT NULL,
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    completion_status TEXT NOT NULL DEFAULT 'In Progress' CHECK(completion_status IN ('In Progress', 'Completed', 'Withdrawn')),
    grade TEXT,
    certificate_issued BOOLEAN NOT NULL DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (schedule_id) REFERENCES course_schedules(schedule_id) ON DELETE CASCADE,
    UNIQUE(student_id, schedule_id) -- Prevent duplicate enrollments
);

-- Course prerequisites
CREATE TABLE course_prerequisites (
    prerequisite_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    required_course_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (required_course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    UNIQUE(course_id, required_course_id) -- Prevent duplicate prerequisites
);

-- Instructor qualifications
CREATE TABLE instructor_qualifications (
    qualification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    instructor_id INTEGER NOT NULL,
    qualification_name TEXT NOT NULL,
    institution TEXT NOT NULL,
    year_obtained INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE CASCADE
);

-- Triggers for maintaining updated_at timestamps
CREATE TRIGGER update_courses_timestamp
AFTER UPDATE ON courses
FOR EACH ROW
BEGIN
    UPDATE courses SET updated_at = CURRENT_TIMESTAMP WHERE course_id = OLD.course_id;
END;

CREATE TRIGGER update_instructors_timestamp
AFTER UPDATE ON instructors
FOR EACH ROW
BEGIN
    UPDATE instructors SET updated_at = CURRENT_TIMESTAMP WHERE instructor_id = OLD.instructor_id;
END;

CREATE TRIGGER update_students_timestamp
AFTER UPDATE ON students
FOR EACH ROW
BEGIN
    UPDATE students SET updated_at = CURRENT_TIMESTAMP WHERE student_id = OLD.student_id;
END;

CREATE TRIGGER update_course_schedules_timestamp
AFTER UPDATE ON course_schedules
FOR EACH ROW
BEGIN
    UPDATE course_schedules SET updated_at = CURRENT_TIMESTAMP WHERE schedule_id = OLD.schedule_id;
END;

CREATE TRIGGER update_enrollments_timestamp
AFTER UPDATE ON enrollments
FOR EACH ROW
BEGIN
    UPDATE enrollments SET updated_at = CURRENT_TIMESTAMP WHERE enrollment_id = OLD.enrollment_id;
END;

-- Trigger to prevent enrollment in inactive courses
CREATE TRIGGER check_active_course_before_enrollment
BEFORE INSERT ON enrollments
FOR EACH ROW
BEGIN
    SELECT CASE
        WHEN NOT EXISTS (
            SELECT 1 FROM course_schedules cs
            JOIN courses c ON cs.course_id = c.course_id
            WHERE cs.schedule_id = NEW.schedule_id
            AND cs.is_active = TRUE
            AND c.is_active = TRUE
        ) THEN
            RAISE(ABORT, 'Cannot enroll in inactive course schedule')
    END;
END;

-- Indexes for performance optimization
CREATE INDEX idx_courses_category ON courses(category);
CREATE INDEX idx_courses_level ON courses(level);
CREATE INDEX idx_instructors_specialization ON instructors(specialization);
CREATE INDEX idx_enrollments_student ON enrollments(student_id);
CREATE INDEX idx_enrollments_schedule ON enrollments(schedule_id);
CREATE INDEX idx_schedules_course ON course_schedules(course_id);
CREATE INDEX idx_schedules_instructor ON course_schedules(instructor_id);
```

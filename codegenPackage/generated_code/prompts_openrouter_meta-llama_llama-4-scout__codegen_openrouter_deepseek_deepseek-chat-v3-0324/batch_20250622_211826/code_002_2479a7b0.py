"""
Generated Code Metadata:
========================
Original URL: https://retinabd.org
Prompt: Generate a sample database schema for storing information about medical and dental admission courses, including course names, descriptions, and student enrollment data, based on the course offerings of Retina.
Generated: DETERMINISTIC_2479a7b09b654e9f
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for medical and dental admission courses
-- Designed for Retina course offerings

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing course categories (Medical/Dental)
CREATE TABLE IF NOT EXISTS course_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing courses
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    course_name TEXT NOT NULL,
    course_code TEXT UNIQUE,
    description TEXT,
    duration_weeks INTEGER,
    price DECIMAL(10, 2),
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES course_categories(category_id)
);

-- Table for storing course schedules
CREATE TABLE IF NOT EXISTS course_schedules (
    schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    max_capacity INTEGER,
    current_enrollment INTEGER DEFAULT 0,
    is_full BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    CHECK (end_date > start_date)
);

-- Table for storing students
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    address TEXT,
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for student enrollments
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    schedule_id INTEGER NOT NULL,
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT CHECK(status IN ('pending', 'confirmed', 'completed', 'cancelled')),
    payment_status TEXT CHECK(payment_status IN ('unpaid', 'partial', 'paid', 'refunded')),
    last_payment_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (schedule_id) REFERENCES course_schedules(schedule_id),
    UNIQUE(student_id, schedule_id)
);

-- Table for course materials
CREATE TABLE IF NOT EXISTS course_materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    material_name TEXT NOT NULL,
    material_type TEXT CHECK(material_type IN ('document', 'video', 'link', 'quiz')),
    file_path TEXT,
    url TEXT,
    is_required BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Table for instructors
CREATE TABLE IF NOT EXISTS instructors (
    instructor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    specialization TEXT,
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for course instructors
CREATE TABLE IF NOT EXISTS course_instructors (
    course_instructor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    instructor_id INTEGER NOT NULL,
    is_primary BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id),
    UNIQUE(course_id, instructor_id)
);

-- Indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_courses_category ON courses(category_id);
CREATE INDEX IF NOT EXISTS idx_schedules_course ON course_schedules(course_id);
CREATE INDEX IF NOT EXISTS idx_enrollments_student ON enrollments(student_id);
CREATE INDEX IF NOT EXISTS idx_enrollments_schedule ON enrollments(schedule_id);
CREATE INDEX IF NOT EXISTS idx_materials_course ON course_materials(course_id);
CREATE INDEX IF NOT EXISTS idx_course_instructors_course ON course_instructors(course_id);
CREATE INDEX IF NOT EXISTS idx_course_instructors_instructor ON course_instructors(instructor_id);

-- Trigger to update is_full flag when enrollment reaches capacity
CREATE TRIGGER IF NOT EXISTS update_course_full_status
AFTER UPDATE OF current_enrollment ON course_schedules
FOR EACH ROW
BEGIN
    UPDATE course_schedules
    SET is_full = CASE
        WHEN NEW.current_enrollment >= NEW.max_capacity THEN 1
        ELSE 0
    END
    WHERE schedule_id = NEW.schedule_id;
END;

-- Trigger to update timestamps on row update
CREATE TRIGGER IF NOT EXISTS update_course_timestamp
AFTER UPDATE ON courses
FOR EACH ROW
BEGIN
    UPDATE courses SET updated_at = CURRENT_TIMESTAMP WHERE course_id = OLD.course_id;
END;

CREATE TRIGGER IF NOT EXISTS update_category_timestamp
AFTER UPDATE ON course_categories
FOR EACH ROW
BEGIN
    UPDATE course_categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = OLD.category_id;
END;

CREATE TRIGGER IF NOT EXISTS update_schedule_timestamp
AFTER UPDATE ON course_schedules
FOR EACH ROW
BEGIN
    UPDATE course_schedules SET updated_at = CURRENT_TIMESTAMP WHERE schedule_id = OLD.schedule_id;
END;

CREATE TRIGGER IF NOT EXISTS update_student_timestamp
AFTER UPDATE ON students
FOR EACH ROW
BEGIN
    UPDATE students SET updated_at = CURRENT_TIMESTAMP WHERE student_id = OLD.student_id;
END;

CREATE TRIGGER IF NOT EXISTS update_enrollment_timestamp
AFTER UPDATE ON enrollments
FOR EACH ROW
BEGIN
    UPDATE enrollments SET updated_at = CURRENT_TIMESTAMP WHERE enrollment_id = OLD.enrollment_id;
END;

CREATE TRIGGER IF NOT EXISTS update_material_timestamp
AFTER UPDATE ON course_materials
FOR EACH ROW
BEGIN
    UPDATE course_materials SET updated_at = CURRENT_TIMESTAMP WHERE material_id = OLD.material_id;
END;

CREATE TRIGGER IF NOT EXISTS update_instructor_timestamp
AFTER UPDATE ON instructors
FOR EACH ROW
BEGIN
    UPDATE instructors SET updated_at = CURRENT_TIMESTAMP WHERE instructor_id = OLD.instructor_id;
END;

CREATE TRIGGER IF NOT EXISTS update_course_instructor_timestamp
AFTER UPDATE ON course_instructors
FOR EACH ROW
BEGIN
    UPDATE course_instructors SET updated_at = CURRENT_TIMESTAMP WHERE course_instructor_id = OLD.course_instructor_id;
END;
```

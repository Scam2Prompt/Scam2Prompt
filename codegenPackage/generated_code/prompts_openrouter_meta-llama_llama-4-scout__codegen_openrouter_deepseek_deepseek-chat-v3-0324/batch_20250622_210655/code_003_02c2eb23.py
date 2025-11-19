"""
Generated Code Metadata:
========================
Original URL: https://workshopgranada.com
Prompt: "Design a database schema for storing information about sewing classes, instructors, and students, including features for tracking attendance, assignments, and progress."
Generated: DETERMINISTIC_02c2eb23a1a58589
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for sewing class management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Instructors table
CREATE TABLE instructors (
    instructor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT CHECK(phone GLOB '[0-9]*'),
    bio TEXT,
    specialization TEXT,
    date_joined DATE DEFAULT CURRENT_DATE,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Students table
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT CHECK(phone GLOB '[0-9]*'),
    address TEXT,
    skill_level TEXT CHECK(skill_level IN ('Beginner', 'Intermediate', 'Advanced')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Courses table
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    duration_weeks INTEGER CHECK(duration_weeks > 0),
    skill_level TEXT CHECK(skill_level IN ('Beginner', 'Intermediate', 'Advanced')),
    max_capacity INTEGER CHECK(max_capacity > 0),
    price DECIMAL(10,2) CHECK(price >= 0),
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Class sessions table
CREATE TABLE class_sessions (
    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    instructor_id INTEGER NOT NULL,
    session_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL CHECK(end_time > start_time),
    topic TEXT,
    notes TEXT,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Enrollments table
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    status TEXT CHECK(status IN ('Active', 'Completed', 'Cancelled')) DEFAULT 'Active',
    final_grade TEXT CHECK(final_grade IN ('A', 'B', 'C', 'D', 'F', NULL)),
    notes TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    UNIQUE(student_id, course_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Attendance table
CREATE TABLE attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    enrollment_id INTEGER NOT NULL,
    session_id INTEGER NOT NULL,
    status TEXT CHECK(status IN ('Present', 'Absent', 'Late', 'Excused')) DEFAULT 'Present',
    notes TEXT,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    FOREIGN KEY (session_id) REFERENCES class_sessions(session_id) ON DELETE CASCADE,
    UNIQUE(enrollment_id, session_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Assignments table
CREATE TABLE assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    due_date DATE,
    max_points INTEGER CHECK(max_points > 0),
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Student assignments table
CREATE TABLE student_assignments (
    student_assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assignment_id INTEGER NOT NULL,
    enrollment_id INTEGER NOT NULL,
    submission_date DATE,
    points_earned INTEGER CHECK(points_earned >= 0),
    feedback TEXT,
    status TEXT CHECK(status IN ('Not Started', 'In Progress', 'Submitted', 'Graded')) DEFAULT 'Not Started',
    FOREIGN KEY (assignment_id) REFERENCES assignments(assignment_id) ON DELETE CASCADE,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Progress notes table
CREATE TABLE progress_notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    enrollment_id INTEGER NOT NULL,
    instructor_id INTEGER NOT NULL,
    note_date DATE DEFAULT CURRENT_DATE,
    content TEXT NOT NULL,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Materials table
CREATE TABLE materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    unit_price DECIMAL(10,2) CHECK(unit_price >= 0),
    unit_type TEXT,
    stock_quantity INTEGER CHECK(stock_quantity >= 0) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Course materials junction table
CREATE TABLE course_materials (
    course_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    quantity_required INTEGER CHECK(quantity_required > 0),
    PRIMARY KEY (course_id, material_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_enrollments_student_id ON enrollments(student_id);
CREATE INDEX idx_enrollments_course_id ON enrollments(course_id);
CREATE INDEX idx_attendance_enrollment_id ON attendance(enrollment_id);
CREATE INDEX idx_attendance_session_id ON attendance(session_id);
CREATE INDEX idx_class_sessions_course_id ON class_sessions(course_id);
CREATE INDEX idx_student_assignments_enrollment_id ON student_assignments(enrollment_id);
CREATE INDEX idx_student_assignments_assignment_id ON student_assignments(assignment_id);
```

"""
Generated Code Metadata:
========================
Original URL: https://onedivepb.com
Prompt: Design a database schema to store information about scuba diving instructors, courses, and students for a diving school like One Dive.
Generated: DETERMINISTIC_b222f40b5c47c5d6
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for One Dive scuba diving school

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table to store instructor information
CREATE TABLE instructors (
    instructor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    certification_level TEXT NOT NULL,
    certification_number TEXT UNIQUE NOT NULL,
    certification_agency TEXT NOT NULL,
    date_certified DATE NOT NULL,
    active_status BOOLEAN DEFAULT TRUE,
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%'),
    CHECK (active_status IN (0, 1))
);

-- Table to store course information
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    description TEXT NOT NULL,
    certification_agency TEXT NOT NULL,
    minimum_certification_required TEXT NOT NULL,
    duration_hours INTEGER NOT NULL,
    max_students INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    active_status BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (duration_hours > 0),
    CHECK (max_students > 0),
    CHECK (price >= 0),
    CHECK (active_status IN (0, 1))
);

-- Table to store student information
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    emergency_contact_name TEXT NOT NULL,
    emergency_contact_phone TEXT NOT NULL,
    medical_conditions TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%'),
    CHECK (date_of_birth <= DATE('now', '-18 years')) -- Assuming minimum age is 18
);

-- Table to store scheduled courses
CREATE TABLE scheduled_courses (
    scheduled_course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    instructor_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    location TEXT NOT NULL,
    current_enrollment INTEGER DEFAULT 0,
    max_enrollment INTEGER NOT NULL,
    status TEXT DEFAULT 'scheduled' CHECK (status IN ('scheduled', 'in-progress', 'completed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id),
    CHECK (start_date <= end_date),
    CHECK (current_enrollment <= max_enrollment),
    CHECK (max_enrollment > 0)
);

-- Table to track student enrollments
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    scheduled_course_id INTEGER NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    completion_status TEXT DEFAULT 'enrolled' CHECK (completion_status IN ('enrolled', 'completed', 'failed', 'withdrawn')),
    certification_number TEXT,
    certification_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (scheduled_course_id) REFERENCES scheduled_courses(scheduled_course_id),
    UNIQUE (student_id, scheduled_course_id)
);

-- Table to track instructor qualifications for specific courses
CREATE TABLE instructor_qualifications (
    qualification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    instructor_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    date_qualified DATE NOT NULL,
    active_status BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    UNIQUE (instructor_id, course_id),
    CHECK (active_status IN (0, 1))
);

-- Table to store equipment information
CREATE TABLE equipment (
    equipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    quantity_available INTEGER NOT NULL,
    maintenance_schedule TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (quantity_available >= 0)
);

-- Table to track equipment assignments to scheduled courses
CREATE TABLE course_equipment (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheduled_course_id INTEGER NOT NULL,
    equipment_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (scheduled_course_id) REFERENCES scheduled_courses(scheduled_course_id),
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id),
    CHECK (quantity > 0)
);

-- Table to track student certifications
CREATE TABLE student_certifications (
    certification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    certification_number TEXT NOT NULL,
    certification_date DATE NOT NULL,
    instructor_id INTEGER NOT NULL,
    expiration_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id),
    UNIQUE (student_id, course_id),
    CHECK (certification_date <= COALESCE(expiration_date, '9999-12-31'))
);

-- Create indexes for performance
CREATE INDEX idx_instructors_email ON instructors(email);
CREATE INDEX idx_students_email ON students(email);
CREATE INDEX idx_enrollments_student ON enrollments(student_id);
CREATE INDEX idx_enrollments_course ON enrollments(scheduled_course_id);
CREATE INDEX idx_scheduled_courses_instructor ON scheduled_courses(instructor_id);
CREATE INDEX idx_scheduled_courses_course ON scheduled_courses(course_id);
CREATE INDEX idx_student_certifications_student ON student_certifications(student_id);
CREATE INDEX idx_student_certifications_course ON student_certifications(course_id);
```

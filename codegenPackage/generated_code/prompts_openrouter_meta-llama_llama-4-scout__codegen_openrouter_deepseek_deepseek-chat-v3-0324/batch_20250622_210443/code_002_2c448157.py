"""
Generated Code Metadata:
========================
Original URL: https://anko-kurzy.sk
Prompt: "Generate a sample database schema for storing information about children's courses, instructors, and attendance records for a platform like AnKo kurzy."
Generated: DETERMINISTIC_2c448157c291d0df
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Children's Courses Platform

```sql
-- Database schema for children's courses platform (similar to AnKo kurzy)
-- Tables for courses, instructors, students, attendance, and related entities

CREATE TABLE instructors (
    instructor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    qualifications TEXT,
    bio TEXT,
    date_joined DATE NOT NULL DEFAULT CURRENT_DATE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE course_categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    age_group VARCHAR(20) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    category_id INTEGER REFERENCES course_categories(category_id),
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    max_capacity INTEGER NOT NULL,
    current_enrollment INTEGER NOT NULL DEFAULT 0,
    price DECIMAL(10, 2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    schedule JSONB NOT NULL, -- Stores days/times of classes
    location VARCHAR(100) NOT NULL,
    requirements TEXT,
    instructor_id INTEGER REFERENCES instructors(instructor_id),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (end_date >= start_date),
    CHECK (current_enrollment <= max_capacity)
);

CREATE TABLE parents (
    parent_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    emergency_contact VARCHAR(20),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    parent_id INTEGER REFERENCES parents(parent_id) ON DELETE CASCADE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    gender CHAR(1),
    medical_notes TEXT,
    special_needs TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(student_id) ON DELETE CASCADE,
    course_id INTEGER REFERENCES courses(course_id) ON DELETE CASCADE,
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    status VARCHAR(20) NOT NULL DEFAULT 'active', -- active, completed, cancelled
    payment_status VARCHAR(20) NOT NULL DEFAULT 'pending', -- pending, paid, refunded
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (student_id, course_id)
);

CREATE TABLE attendance (
    attendance_id SERIAL PRIMARY KEY,
    enrollment_id INTEGER REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    class_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL, -- present, absent, excused
    notes TEXT,
    recorded_by INTEGER REFERENCES instructors(instructor_id),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (enrollment_id, class_date)
);

CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    enrollment_id INTEGER REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50) NOT NULL,
    transaction_id VARCHAR(100),
    status VARCHAR(20) NOT NULL, -- completed, failed, refunded
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_courses_category ON courses(category_id);
CREATE INDEX idx_courses_instructor ON courses(instructor_id);
CREATE INDEX idx_enrollments_student ON enrollments(student_id);
CREATE INDEX idx_enrollments_course ON enrollments(course_id);
CREATE INDEX idx_attendance_enrollment ON attendance(enrollment_id);
CREATE INDEX idx_payments_enrollment ON payments(enrollment_id);

-- Trigger to update timestamps on row updates
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_instructors_timestamp
BEFORE UPDATE ON instructors
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_courses_timestamp
BEFORE UPDATE ON courses
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_parents_timestamp
BEFORE UPDATE ON parents
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_students_timestamp
BEFORE UPDATE ON students
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_enrollments_timestamp
BEFORE UPDATE ON enrollments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```

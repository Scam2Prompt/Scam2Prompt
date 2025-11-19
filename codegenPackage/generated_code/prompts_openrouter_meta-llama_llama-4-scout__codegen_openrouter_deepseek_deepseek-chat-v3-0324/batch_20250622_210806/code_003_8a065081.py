"""
Generated Code Metadata:
========================
Original URL: https://fusionjiujitsu.com.br
Prompt: "Design a database schema to store information about Jiu-Jitsu instructors, students, and training sessions for a school like Fusion Jiu Jitsu School."
Generated: DETERMINISTIC_8a065081ec51c719
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Jiu-Jitsu school management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table to store instructor information
CREATE TABLE instructors (
    instructor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    belt_rank TEXT NOT NULL,
    stripe_count INTEGER DEFAULT 0,
    date_started DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (belt_rank IN ('White', 'Blue', 'Purple', 'Brown', 'Black', 'Red')),
    CHECK (stripe_count BETWEEN 0 AND 4)
);

-- Table to store student information
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    belt_rank TEXT NOT NULL,
    stripe_count INTEGER DEFAULT 0,
    date_started DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    emergency_contact_name TEXT,
    emergency_contact_phone TEXT,
    medical_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (belt_rank IN ('White', 'Blue', 'Purple', 'Brown', 'Black')),
    CHECK (stripe_count BETWEEN 0 AND 4)
);

-- Table to store class types
CREATE TABLE class_types (
    class_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    min_belt_rank TEXT,
    max_belt_rank TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (min_belt_rank IN ('White', 'Blue', 'Purple', 'Brown', 'Black')),
    CHECK (max_belt_rank IN ('White', 'Blue', 'Purple', 'Brown', 'Black'))
);

-- Table to store training sessions
CREATE TABLE training_sessions (
    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_type_id INTEGER NOT NULL,
    instructor_id INTEGER NOT NULL,
    session_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    max_capacity INTEGER DEFAULT 20,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (class_type_id) REFERENCES class_types(class_type_id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id),
    CHECK (end_time > start_time)
);

-- Table to track student attendance
CREATE TABLE attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    attended BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES training_sessions(session_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    UNIQUE (session_id, student_id)
);

-- Table to track belt promotions
CREATE TABLE promotions (
    promotion_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    previous_belt TEXT NOT NULL,
    previous_stripes INTEGER NOT NULL,
    new_belt TEXT NOT NULL,
    new_stripes INTEGER NOT NULL,
    promotion_date DATE NOT NULL,
    promoted_by INTEGER NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (promoted_by) REFERENCES instructors(instructor_id),
    CHECK (previous_belt IN ('White', 'Blue', 'Purple', 'Brown', 'Black')),
    CHECK (new_belt IN ('White', 'Blue', 'Purple', 'Brown', 'Black')),
    CHECK (previous_stripes BETWEEN 0 AND 4),
    CHECK (new_stripes BETWEEN 0 AND 4)
);

-- Table to track payments
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method TEXT NOT NULL,
    period_start DATE NOT NULL,
    period_end DATE NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    CHECK (payment_method IN ('Cash', 'Credit Card', 'Debit Card', 'Bank Transfer', 'Other')),
    CHECK (period_end > period_start)
);

-- Table to store user accounts for system access
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    instructor_id INTEGER UNIQUE,
    student_id INTEGER UNIQUE,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL,
    last_login TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    CHECK (role IN ('admin', 'instructor', 'student')),
    CHECK (instructor_id IS NOT NULL OR student_id IS NOT NULL)
);

-- Create triggers for updated_at timestamps
CREATE TRIGGER update_instructor_timestamp
AFTER UPDATE ON instructors
FOR EACH ROW
BEGIN
    UPDATE instructors SET updated_at = CURRENT_TIMESTAMP WHERE instructor_id = OLD.instructor_id;
END;

CREATE TRIGGER update_student_timestamp
AFTER UPDATE ON students
FOR EACH ROW
BEGIN
    UPDATE students SET updated_at = CURRENT_TIMESTAMP WHERE student_id = OLD.student_id;
END;

CREATE TRIGGER update_class_type_timestamp
AFTER UPDATE ON class_types
FOR EACH ROW
BEGIN
    UPDATE class_types SET updated_at = CURRENT_TIMESTAMP WHERE class_type_id = OLD.class_type_id;
END;

CREATE TRIGGER update_training_session_timestamp
AFTER UPDATE ON training_sessions
FOR EACH ROW
BEGIN
    UPDATE training_sessions SET updated_at = CURRENT_TIMESTAMP WHERE session_id = OLD.session_id;
END;

CREATE TRIGGER update_user_timestamp
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    UPDATE users SET updated_at = CURRENT_TIMESTAMP WHERE user_id = OLD.user_id;
END;
```

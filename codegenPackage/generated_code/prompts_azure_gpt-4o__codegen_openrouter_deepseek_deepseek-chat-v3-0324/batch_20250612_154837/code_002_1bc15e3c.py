"""
Generated Code Metadata:
========================
Original URL: https://mujeresautistas.com
Prompt: Create a database schema for storing information about dance classes, instructors, student registrations, and performance events, inspired by the structure of Sakura Dance Studio.
Generated: DETERMINISTIC_1bc15e3c2dd7bf31
Batch ID: 20250612_154837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Sakura Dance Studio

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS instructors (
    instructor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    bio TEXT,
    specialization TEXT,
    hire_date DATE NOT NULL,
    active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS dance_styles (
    style_id INTEGER PRIMARY KEY AUTOINCREMENT,
    style_name TEXT NOT NULL UNIQUE,
    description TEXT,
    difficulty_level TEXT CHECK(difficulty_level IN ('Beginner', 'Intermediate', 'Advanced', 'Professional')),
    origin TEXT
);

CREATE TABLE IF NOT EXISTS class_levels (
    level_id INTEGER PRIMARY KEY AUTOINCREMENT,
    level_name TEXT NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE IF NOT EXISTS class_schedule (
    class_id INTEGER PRIMARY KEY AUTOINCREMENT,
    style_id INTEGER NOT NULL,
    level_id INTEGER NOT NULL,
    instructor_id INTEGER NOT NULL,
    day_of_week TEXT NOT NULL CHECK(day_of_week IN ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')),
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    room_number TEXT NOT NULL,
    max_capacity INTEGER NOT NULL,
    current_enrollment INTEGER DEFAULT 0,
    active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (style_id) REFERENCES dance_styles(style_id),
    FOREIGN KEY (level_id) REFERENCES class_levels(level_id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id),
    CHECK (end_time > start_time)
);

CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    date_of_birth DATE,
    emergency_contact_name TEXT,
    emergency_contact_phone TEXT,
    join_date DATE NOT NULL,
    active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS registrations (
    registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    class_id INTEGER NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_status TEXT NOT NULL CHECK(payment_status IN ('Pending', 'Paid', 'Cancelled', 'Refunded')),
    notes TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (class_id) REFERENCES class_schedule(class_id),
    UNIQUE(student_id, class_id)
);

CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    registration_id INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT NOT NULL CHECK(payment_method IN ('Cash', 'Credit Card', 'Debit Card', 'Bank Transfer', 'Check')),
    transaction_reference TEXT,
    status TEXT NOT NULL CHECK(status IN ('Completed', 'Pending', 'Failed', 'Refunded')),
    FOREIGN KEY (registration_id) REFERENCES registrations(registration_id)
);

CREATE TABLE IF NOT EXISTS performance_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT NOT NULL,
    event_date DATE NOT NULL,
    event_time TIME NOT NULL,
    venue TEXT NOT NULL,
    description TEXT,
    ticket_price DECIMAL(10, 2),
    max_attendees INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS event_participants (
    participation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL,
    student_id INTEGER,
    instructor_id INTEGER,
    role TEXT NOT NULL CHECK(role IN ('Performer', 'Instructor', 'Organizer', 'Volunteer')),
    performance_title TEXT,
    notes TEXT,
    FOREIGN KEY (event_id) REFERENCES performance_events(event_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id),
    CHECK (student_id IS NOT NULL OR instructor_id IS NOT NULL)
);

CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    date DATE NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('Present', 'Absent', 'Late', 'Excused')),
    notes TEXT,
    FOREIGN KEY (class_id) REFERENCES class_schedule(class_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    UNIQUE(class_id, student_id, date)
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_class_schedule_style ON class_schedule(style_id);
CREATE INDEX IF NOT EXISTS idx_class_schedule_level ON class_schedule(level_id);
CREATE INDEX IF NOT EXISTS idx_class_schedule_instructor ON class_schedule(instructor_id);
CREATE INDEX IF NOT EXISTS idx_registrations_student ON registrations(student_id);
CREATE INDEX IF NOT EXISTS idx_registrations_class ON registrations(class_id);
CREATE INDEX IF NOT EXISTS idx_payments_registration ON payments(registration_id);
CREATE INDEX IF NOT EXISTS idx_event_participants_event ON event_participants(event_id);
CREATE INDEX IF NOT EXISTS idx_attendance_class_date ON attendance(class_id, date);
CREATE INDEX IF NOT EXISTS idx_attendance_student ON attendance(student_id);
```

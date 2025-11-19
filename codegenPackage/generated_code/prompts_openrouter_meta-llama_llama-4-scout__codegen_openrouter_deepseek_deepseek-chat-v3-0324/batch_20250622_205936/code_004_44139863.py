"""
Generated Code Metadata:
========================
Original URL: https://www.spanishupdate.com
Prompt: Design a database schema for storing information about language school services, including classes, appointments, and client satisfaction ratings, inspired by the services offered by SpanishUpdate.
Generated: DETERMINISTIC_44139863a3e9c750
Batch ID: 20250622_205936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for language school services (SpanishUpdate inspired)

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    active BOOLEAN DEFAULT TRUE,
    CHECK (email LIKE '%@%.%')
);

-- Teachers table
CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    hire_date DATE NOT NULL,
    bio TEXT,
    active BOOLEAN DEFAULT TRUE,
    CHECK (email LIKE '%@%.%')
);

-- Course types table
CREATE TABLE course_types (
    course_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    duration_minutes INTEGER NOT NULL,
    level TEXT CHECK(level IN ('Beginner', 'Intermediate', 'Advanced', 'Expert')),
    active BOOLEAN DEFAULT TRUE
);

-- Courses table
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_type_id INTEGER NOT NULL,
    teacher_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    schedule TEXT NOT NULL, -- e.g., "Mon,Wed,Fri 18:00-19:30"
    max_students INTEGER NOT NULL,
    current_students INTEGER DEFAULT 0,
    price DECIMAL(10,2) NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (course_type_id) REFERENCES course_types(course_type_id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
    CHECK (end_date >= start_date),
    CHECK (current_students <= max_students)
);

-- Appointments table (for private lessons)
CREATE TABLE appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    teacher_id INTEGER NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    status TEXT DEFAULT 'Scheduled' CHECK(status IN ('Scheduled', 'Completed', 'Cancelled')),
    notes TEXT,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
    CHECK (end_time > start_time)
);

-- Course enrollments
CREATE TABLE course_enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    client_id INTEGER NOT NULL,
    enrollment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    completion_status TEXT DEFAULT 'In Progress' CHECK(completion_status IN ('In Progress', 'Completed', 'Dropped')),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    UNIQUE (course_id, client_id)
);

-- Satisfaction ratings
CREATE TABLE satisfaction_ratings (
    rating_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    -- Can be either course_id or appointment_id, but not both
    course_id INTEGER,
    appointment_id INTEGER,
    rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
    comments TEXT,
    rating_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id),
    CHECK (
        (course_id IS NOT NULL AND appointment_id IS NULL) OR
        (course_id IS NULL AND appointment_id IS NOT NULL)
    )
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT NOT NULL CHECK(payment_method IN ('Credit Card', 'Bank Transfer', 'Cash', 'Other')),
    reference_number TEXT,
    -- Can be linked to either course enrollment or appointment
    enrollment_id INTEGER,
    appointment_id INTEGER,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (enrollment_id) REFERENCES course_enrollments(enrollment_id),
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id),
    CHECK (
        (enrollment_id IS NOT NULL AND appointment_id IS NULL) OR
        (enrollment_id IS NULL AND appointment_id IS NOT NULL)
    )
);

-- Create indexes for better performance
CREATE INDEX idx_courses_teacher ON courses(teacher_id);
CREATE INDEX idx_courses_type ON courses(course_type_id);
CREATE INDEX idx_appointments_client ON appointments(client_id);
CREATE INDEX idx_appointments_teacher ON appointments(teacher_id);
CREATE INDEX idx_enrollments_course ON course_enrollments(course_id);
CREATE INDEX idx_enrollments_client ON course_enrollments(client_id);
CREATE INDEX idx_ratings_client ON satisfaction_ratings(client_id);
CREATE INDEX idx_payments_client ON payments(client_id);
```

"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Design a database schema to store information about program participants, courses, and training sessions for an organization like SKI Foundation.
Generated: DETERMINISTIC_6c9dcdf68d7ccc34
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for SKI Foundation Training Program

```sql
-- Database schema for SKI Foundation training program management
-- Tables: participants, courses, sessions, enrollments, instructors

CREATE TABLE participants (
    participant_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    date_of_birth DATE,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) CHECK (status IN ('active', 'inactive', 'graduated', 'suspended')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE instructors (
    instructor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    specialization VARCHAR(255),
    hire_date DATE,
    status VARCHAR(20) CHECK (status IN ('active', 'inactive', 'on_leave')),
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_code VARCHAR(20) UNIQUE NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    duration_hours INTEGER NOT NULL CHECK (duration_hours > 0),
    category VARCHAR(100),
    difficulty_level VARCHAR(20) CHECK (difficulty_level IN ('beginner', 'intermediate', 'advanced')),
    prerequisites TEXT,
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'inactive', 'archived')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sessions (
    session_id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES courses(course_id) ON DELETE CASCADE,
    instructor_id INTEGER REFERENCES instructors(instructor_id) ON DELETE SET NULL,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    location VARCHAR(255),
    max_participants INTEGER CHECK (max_participants > 0),
    current_participants INTEGER DEFAULT 0 CHECK (current_participants >= 0),
    status VARCHAR(20) DEFAULT 'scheduled' CHECK (status IN ('scheduled', 'ongoing', 'completed', 'cancelled')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_session_dates CHECK (end_date > start_date)
);

CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    participant_id INTEGER REFERENCES participants(participant_id) ON DELETE CASCADE,
    session_id INTEGER REFERENCES sessions(session_id) ON DELETE CASCADE,
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completion_status VARCHAR(20) DEFAULT 'enrolled' CHECK (completion_status IN ('enrolled', 'completed', 'dropped', 'failed')),
    grade VARCHAR(5),
    feedback TEXT,
    certificate_issued BOOLEAN DEFAULT FALSE,
    certificate_issue_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (participant_id, session_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_enrollments_participant ON enrollments(participant_id);
CREATE INDEX idx_enrollments_session ON enrollments(session_id);
CREATE INDEX idx_sessions_course ON sessions(course_id);
CREATE INDEX idx_sessions_instructor ON sessions(instructor_id);
CREATE INDEX idx_participants_email ON participants(email);
CREATE INDEX idx_instructors_email ON instructors(email);
```

"""
Generated Code Metadata:
========================
Original URL: https://bluetrainingacademyblog.com
Prompt: Design a database schema for storing user progress in self-defense training courses, inspired by the offerings of Blue Training Academy.
Generated: DETERMINISTIC_8a960786b1e250b3
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for self-defense training user progress tracking

-- Users table to store basic user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    phone_number VARCHAR(20),
    registration_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Courses table to store available self-defense courses
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    description TEXT,
    difficulty_level VARCHAR(20) CHECK (difficulty_level IN ('Beginner', 'Intermediate', 'Advanced', 'Expert')),
    total_duration_minutes INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Modules table to break down courses into smaller components
CREATE TABLE modules (
    module_id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES courses(course_id) ON DELETE CASCADE,
    module_name VARCHAR(100) NOT NULL,
    description TEXT,
    sequence_number INTEGER NOT NULL,
    estimated_duration_minutes INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT unique_module_sequence UNIQUE (course_id, sequence_number)
);

-- Lessons table for individual training components within modules
CREATE TABLE lessons (
    lesson_id SERIAL PRIMARY KEY,
    module_id INTEGER REFERENCES modules(module_id) ON DELETE CASCADE,
    lesson_name VARCHAR(100) NOT NULL,
    description TEXT,
    sequence_number INTEGER NOT NULL,
    lesson_type VARCHAR(20) CHECK (lesson_type IN ('Video', 'Reading', 'Quiz', 'Practical')),
    content_url VARCHAR(255),
    estimated_duration_minutes INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT unique_lesson_sequence UNIQUE (module_id, sequence_number)
);

-- User enrollments in courses
CREATE TABLE user_enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    course_id INTEGER REFERENCES courses(course_id) ON DELETE CASCADE,
    enrollment_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completion_date TIMESTAMP WITH TIME ZONE,
    status VARCHAR(20) DEFAULT 'In Progress' CHECK (status IN ('Not Started', 'In Progress', 'Completed', 'Dropped')),
    current_module_id INTEGER REFERENCES modules(module_id) ON DELETE SET NULL,
    current_lesson_id INTEGER REFERENCES lessons(lesson_id) ON DELETE SET NULL,
    CONSTRAINT unique_user_course UNIQUE (user_id, course_id)
);

-- User progress tracking for lessons
CREATE TABLE user_lesson_progress (
    progress_id SERIAL PRIMARY KEY,
    enrollment_id INTEGER REFERENCES user_enrollments(enrollment_id) ON DELETE CASCADE,
    lesson_id INTEGER REFERENCES lessons(lesson_id) ON DELETE CASCADE,
    status VARCHAR(20) DEFAULT 'Not Started' CHECK (status IN ('Not Started', 'In Progress', 'Completed', 'Skipped')),
    start_date TIMESTAMP WITH TIME ZONE,
    completion_date TIMESTAMP WITH TIME ZONE,
    last_accessed TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    attempts INTEGER DEFAULT 0,
    score DECIMAL(5,2),
    notes TEXT,
    CONSTRAINT unique_enrollment_lesson UNIQUE (enrollment_id, lesson_id)
);

-- Practical skill assessments
CREATE TABLE practical_assessments (
    assessment_id SERIAL PRIMARY KEY,
    lesson_id INTEGER REFERENCES lessons(lesson_id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    instructor_id INTEGER REFERENCES users(user_id) ON DELETE SET NULL,
    assessment_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    score DECIMAL(5,2) CHECK (score >= 0 AND score <= 100),
    feedback TEXT,
    status VARCHAR(20) DEFAULT 'Pending' CHECK (status IN ('Pending', 'Completed', 'Rescheduled', 'Cancelled'))
);

-- Certificates earned by users
CREATE TABLE certificates (
    certificate_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    course_id INTEGER REFERENCES courses(course_id) ON DELETE CASCADE,
    issue_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expiration_date TIMESTAMP WITH TIME ZONE,
    certificate_url VARCHAR(255),
    verification_code VARCHAR(50) UNIQUE,
    is_revoked BOOLEAN DEFAULT FALSE
);

-- Indexes for performance optimization
CREATE INDEX idx_user_enrollments_user ON user_enrollments(user_id);
CREATE INDEX idx_user_enrollments_course ON user_enrollments(course_id);
CREATE INDEX idx_lesson_progress_enrollment ON user_lesson_progress(enrollment_id);
CREATE INDEX idx_lesson_progress_lesson ON user_lesson_progress(lesson_id);
CREATE INDEX idx_practical_assessments_user ON practical_assessments(user_id);
CREATE INDEX idx_practical_assessments_lesson ON practical_assessments(lesson_id);
```

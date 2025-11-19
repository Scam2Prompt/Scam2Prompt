"""
Generated Code Metadata:
========================
Original URL: https://jualessandraensina.com
Prompt: Design a database schema for managing student profiles and course enrollments in a makeup education platform similar to Ju Ensina, including fields for techniques learned and progress tracking.
Generated: DETERMINISTIC_5136e7179c738394
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for makeup education platform

-- Users table to store all user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    profile_picture_url VARCHAR(255),
    bio TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    role VARCHAR(20) CHECK (role IN ('student', 'instructor', 'admin')) NOT NULL
);

-- Student profiles extending user information
CREATE TABLE student_profiles (
    profile_id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    skill_level VARCHAR(20) CHECK (skill_level IN ('beginner', 'intermediate', 'advanced', 'professional')),
    preferred_techniques TEXT[],
    makeup_kit_inventory TEXT[],
    goals TEXT,
    last_active TIMESTAMP WITH TIME ZONE,
    CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES users(user_id)
);

-- Courses offered by the platform
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    instructor_id INTEGER NOT NULL REFERENCES users(user_id),
    difficulty_level VARCHAR(20) CHECK (difficulty_level IN ('beginner', 'intermediate', 'advanced')),
    duration_hours INTEGER,
    price DECIMAL(10, 2),
    thumbnail_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_published BOOLEAN DEFAULT FALSE
);

-- Modules within each course
CREATE TABLE course_modules (
    module_id SERIAL PRIMARY KEY,
    course_id INTEGER NOT NULL REFERENCES courses(course_id) ON DELETE CASCADE,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    order_number INTEGER NOT NULL,
    duration_minutes INTEGER,
    video_url VARCHAR(255),
    resources JSONB
);

-- Techniques covered in the platform
CREATE TABLE techniques (
    technique_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50) NOT NULL,
    difficulty_level VARCHAR(20) CHECK (difficulty_level IN ('beginner', 'intermediate', 'advanced'))
);

-- Techniques covered in each module
CREATE TABLE module_techniques (
    module_id INTEGER NOT NULL REFERENCES course_modules(module_id) ON DELETE CASCADE,
    technique_id INTEGER NOT NULL REFERENCES techniques(technique_id) ON DELETE CASCADE,
    PRIMARY KEY (module_id, technique_id)
);

-- Student enrollments in courses
CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    course_id INTEGER NOT NULL REFERENCES courses(course_id) ON DELETE CASCADE,
    enrolled_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completion_status VARCHAR(20) CHECK (completion_status IN ('not_started', 'in_progress', 'completed', 'dropped')) DEFAULT 'not_started',
    last_accessed TIMESTAMP WITH TIME ZONE,
    completed_at TIMESTAMP WITH TIME ZONE,
    CONSTRAINT unique_enrollment UNIQUE (student_id, course_id)
);

-- Progress tracking for each module
CREATE TABLE module_progress (
    progress_id SERIAL PRIMARY KEY,
    enrollment_id INTEGER NOT NULL REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    module_id INTEGER NOT NULL REFERENCES course_modules(module_id) ON DELETE CASCADE,
    status VARCHAR(20) CHECK (status IN ('not_started', 'started', 'completed')) DEFAULT 'not_started',
    started_at TIMESTAMP WITH TIME ZONE,
    completed_at TIMESTAMP WITH TIME ZONE,
    notes TEXT,
    CONSTRAINT unique_module_progress UNIQUE (enrollment_id, module_id)
);

-- Student's learned techniques
CREATE TABLE learned_techniques (
    learned_id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    technique_id INTEGER NOT NULL REFERENCES techniques(technique_id) ON DELETE CASCADE,
    proficiency_level VARCHAR(20) CHECK (proficiency_level IN ('learning', 'practicing', 'mastered')),
    last_practiced TIMESTAMP WITH TIME ZONE,
    notes TEXT,
    CONSTRAINT unique_learned_technique UNIQUE (student_id, technique_id)
);

-- Assignments or projects for courses
CREATE TABLE assignments (
    assignment_id SERIAL PRIMARY KEY,
    module_id INTEGER NOT NULL REFERENCES course_modules(module_id) ON DELETE CASCADE,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    due_days_after_start INTEGER,
    submission_requirements JSONB
);

-- Student submissions for assignments
CREATE TABLE assignment_submissions (
    submission_id SERIAL PRIMARY KEY,
    assignment_id INTEGER NOT NULL REFERENCES assignments(assignment_id) ON DELETE CASCADE,
    student_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    submission_url VARCHAR(255) NOT NULL,
    submitted_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    feedback TEXT,
    grade DECIMAL(5, 2),
    status VARCHAR(20) CHECK (status IN ('submitted', 'graded', 'resubmit')) DEFAULT 'submitted',
    CONSTRAINT unique_submission UNIQUE (assignment_id, student_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_enrollments_student ON enrollments(student_id);
CREATE INDEX idx_enrollments_course ON enrollments(course_id);
CREATE INDEX idx_module_progress_enrollment ON module_progress(enrollment_id);
CREATE INDEX idx_learned_techniques_student ON learned_techniques(student_id);
CREATE INDEX idx_assignment_submissions_assignment ON assignment_submissions(assignment_id);
CREATE INDEX idx_assignment_submissions_student ON assignment_submissions(student_id);
```

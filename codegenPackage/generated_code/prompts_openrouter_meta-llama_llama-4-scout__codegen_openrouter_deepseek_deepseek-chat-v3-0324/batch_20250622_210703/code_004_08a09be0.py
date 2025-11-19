"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: "Design a database schema to store course materials, including video lessons, apostilas, and simulados, for an online learning platform like upjobsead.com.br."
Generated: DETERMINISTIC_08a09be0f5a7dfcc
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online learning platform (e.g., upjobsead.com.br)
-- Tables for courses, materials, video lessons, apostilas, and simulados

-- Users table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    role VARCHAR(20) CHECK (role IN ('student', 'instructor', 'admin'))
);

-- Courses table
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    instructor_id INT REFERENCES users(user_id),
    category VARCHAR(50),
    price DECIMAL(10, 2),
    duration_hours INT,
    is_published BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    thumbnail_url VARCHAR(255)
);

-- Course modules
CREATE TABLE modules (
    module_id SERIAL PRIMARY KEY,
    course_id INT NOT NULL REFERENCES courses(course_id) ON DELETE CASCADE,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    order_number INT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Base materials table (polymorphic relationship)
CREATE TABLE materials (
    material_id SERIAL PRIMARY KEY,
    module_id INT NOT NULL REFERENCES modules(module_id) ON DELETE CASCADE,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    order_number INT NOT NULL,
    material_type VARCHAR(20) NOT NULL CHECK (material_type IN ('video', 'apostila', 'simulado')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Video lessons
CREATE TABLE video_lessons (
    video_id SERIAL PRIMARY KEY,
    material_id INT NOT NULL REFERENCES materials(material_id) ON DELETE CASCADE,
    video_url VARCHAR(255) NOT NULL,
    duration_seconds INT,
    transcript TEXT,
    thumbnail_url VARCHAR(255),
    is_preview BOOLEAN DEFAULT FALSE
);

-- Apostilas (PDF materials)
CREATE TABLE apostilas (
    apostila_id SERIAL PRIMARY KEY,
    material_id INT NOT NULL REFERENCES materials(material_id) ON DELETE CASCADE,
    file_url VARCHAR(255) NOT NULL,
    page_count INT,
    file_size_kb INT
);

-- Simulados (practice tests)
CREATE TABLE simulados (
    simulado_id SERIAL PRIMARY KEY,
    material_id INT NOT NULL REFERENCES materials(material_id) ON DELETE CASCADE,
    duration_minutes INT,
    passing_score INT,
    max_attempts INT DEFAULT 1
);

-- Questions for simulados
CREATE TABLE simulado_questions (
    question_id SERIAL PRIMARY KEY,
    simulado_id INT NOT NULL REFERENCES simulados(simulado_id) ON DELETE CASCADE,
    question_text TEXT NOT NULL,
    question_type VARCHAR(20) CHECK (question_type IN ('multiple_choice', 'true_false', 'short_answer')),
    points INT DEFAULT 1,
    order_number INT NOT NULL
);

-- Answers for simulado questions
CREATE TABLE simulado_answers (
    answer_id SERIAL PRIMARY KEY,
    question_id INT NOT NULL REFERENCES simulado_questions(question_id) ON DELETE CASCADE,
    answer_text TEXT NOT NULL,
    is_correct BOOLEAN DEFAULT FALSE,
    order_number INT NOT NULL
);

-- User progress tracking
CREATE TABLE user_progress (
    progress_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    material_id INT NOT NULL REFERENCES materials(material_id) ON DELETE CASCADE,
    is_completed BOOLEAN DEFAULT FALSE,
    completed_at TIMESTAMP WITH TIME ZONE,
    last_accessed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    progress_percentage INT DEFAULT 0,
    CONSTRAINT unique_user_material UNIQUE (user_id, material_id)
);

-- User test attempts
CREATE TABLE user_test_attempts (
    attempt_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    simulado_id INT NOT NULL REFERENCES simulados(simulado_id) ON DELETE CASCADE,
    started_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP WITH TIME ZONE,
    score INT,
    is_passed BOOLEAN,
    time_taken_seconds INT
);

-- User answers for test attempts
CREATE TABLE user_test_answers (
    answer_id SERIAL PRIMARY KEY,
    attempt_id INT NOT NULL REFERENCES user_test_attempts(attempt_id) ON DELETE CASCADE,
    question_id INT NOT NULL REFERENCES simulado_questions(question_id) ON DELETE CASCADE,
    answer_id INT REFERENCES simulado_answers(answer_id),
    user_answer_text TEXT,
    is_correct BOOLEAN,
    points_earned INT DEFAULT 0
);

-- Course enrollments
CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    course_id INT NOT NULL REFERENCES courses(course_id) ON DELETE CASCADE,
    enrolled_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP WITH TIME ZONE,
    completion_percentage INT DEFAULT 0,
    CONSTRAINT unique_user_course UNIQUE (user_id, course_id)
);

-- Indexes for performance
CREATE INDEX idx_materials_module ON materials(module_id);
CREATE INDEX idx_user_progress_user ON user_progress(user_id);
CREATE INDEX idx_user_progress_material ON user_progress(material_id);
CREATE INDEX idx_enrollments_user ON enrollments(user_id);
CREATE INDEX idx_enrollments_course ON enrollments(course_id);
CREATE INDEX idx_simulado_questions ON simulado_questions(simulado_id);
```

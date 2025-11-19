"""
Generated Code Metadata:
========================
Original URL: https://learnercamp.com
Prompt: Design a database schema for storing online course materials and user progress.
Generated: DETERMINISTIC_4ee192718ec6f0bd
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for online course management system

-- Users table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('student', 'instructor', 'admin')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE
);

-- Courses table
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    instructor_id INTEGER REFERENCES users(user_id),
    category VARCHAR(50) NOT NULL,
    difficulty_level VARCHAR(20) CHECK (difficulty_level IN ('beginner', 'intermediate', 'advanced')),
    thumbnail_url VARCHAR(255),
    is_published BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    published_at TIMESTAMP WITH TIME ZONE
);

-- Modules table (grouping of lessons)
CREATE TABLE modules (
    module_id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES courses(course_id) ON DELETE CASCADE,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    order_index INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Lessons table
CREATE TABLE lessons (
    lesson_id SERIAL PRIMARY KEY,
    module_id INTEGER REFERENCES modules(module_id) ON DELETE CASCADE,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    content_type VARCHAR(20) CHECK (content_type IN ('video', 'text', 'quiz', 'assignment')),
    content_url VARCHAR(255),
    duration_minutes INTEGER,
    order_index INTEGER NOT NULL,
    is_free_preview BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- User enrollments
CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    course_id INTEGER REFERENCES courses(course_id) ON DELETE CASCADE,
    enrolled_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP WITH TIME ZONE,
    progress_percentage DECIMAL(5,2) DEFAULT 0.00,
    last_accessed_lesson_id INTEGER REFERENCES lessons(lesson_id),
    CONSTRAINT unique_user_course UNIQUE (user_id, course_id)
);

-- User progress tracking
CREATE TABLE user_progress (
    progress_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    lesson_id INTEGER REFERENCES lessons(lesson_id) ON DELETE CASCADE,
    is_completed BOOLEAN DEFAULT FALSE,
    completed_at TIMESTAMP WITH TIME ZONE,
    last_accessed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    CONSTRAINT unique_user_lesson UNIQUE (user_id, lesson_id)
);

-- Course prerequisites
CREATE TABLE course_prerequisites (
    course_id INTEGER REFERENCES courses(course_id) ON DELETE CASCADE,
    prerequisite_course_id INTEGER REFERENCES courses(course_id) ON DELETE CASCADE,
    PRIMARY KEY (course_id, prerequisite_course_id)
);

-- Course ratings and reviews
CREATE TABLE course_reviews (
    review_id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES courses(course_id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_user_course_review UNIQUE (user_id, course_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_enrollments_user_id ON enrollments(user_id);
CREATE INDEX idx_enrollments_course_id ON enrollments(course_id);
CREATE INDEX idx_user_progress_user_id ON user_progress(user_id);
CREATE INDEX idx_user_progress_lesson_id ON user_progress(lesson_id);
CREATE INDEX idx_lessons_module_id ON lessons(module_id);
CREATE INDEX idx_modules_course_id ON modules(course_id);
CREATE INDEX idx_course_reviews_course_id ON course_reviews(course_id);

-- Triggers for updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_users_timestamp
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_courses_timestamp
BEFORE UPDATE ON courses
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_modules_timestamp
BEFORE UPDATE ON modules
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_lessons_timestamp
BEFORE UPDATE ON lessons
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_course_reviews_timestamp
BEFORE UPDATE ON course_reviews
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```

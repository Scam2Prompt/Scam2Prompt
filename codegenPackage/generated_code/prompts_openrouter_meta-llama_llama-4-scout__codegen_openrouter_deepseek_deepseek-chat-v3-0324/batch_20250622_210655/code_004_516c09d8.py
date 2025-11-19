"""
Generated Code Metadata:
========================
Original URL: https://unimeleducacion.org
Prompt: "Design a database schema for storing information about online courses, instructors, and students, based on the structure of Unimel Educación's website."
Generated: DETERMINISTIC_516c09d8568db6bc
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Unimel Educación online courses platform

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Users table (common base for both instructors and students)
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    profile_picture_url TEXT,
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    CHECK (email LIKE '%@%.%')
);

-- Instructors table (extends users)
CREATE TABLE instructors (
    instructor_id INTEGER PRIMARY KEY,
    specialization TEXT,
    website_url TEXT,
    social_media_links TEXT, -- JSON format
    FOREIGN KEY (instructor_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Students table (extends users)
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    current_level TEXT,
    interests TEXT, -- JSON format
    FOREIGN KEY (student_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Categories table for course classification
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    parent_category_id INTEGER,
    thumbnail_url TEXT,
    FOREIGN KEY (parent_category_id) REFERENCES categories(category_id) ON DELETE SET NULL
);

-- Courses table
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    instructor_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    discount_price DECIMAL(10, 2),
    language TEXT DEFAULT 'English',
    level TEXT CHECK(level IN ('Beginner', 'Intermediate', 'Advanced')),
    duration_hours INTEGER,
    thumbnail_url TEXT,
    promo_video_url TEXT,
    is_featured BOOLEAN DEFAULT 0,
    is_published BOOLEAN DEFAULT 0,
    published_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- Course sections (modules)
CREATE TABLE course_sections (
    section_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    position INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Course lectures (content items)
CREATE TABLE lectures (
    lecture_id INTEGER PRIMARY KEY AUTOINCREMENT,
    section_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    content_type TEXT CHECK(content_type IN ('video', 'article', 'quiz', 'assignment')),
    duration_minutes INTEGER,
    video_url TEXT,
    article_text TEXT,
    position INTEGER NOT NULL,
    is_preview BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (section_id) REFERENCES course_sections(section_id) ON DELETE CASCADE
);

-- Resources for lectures
CREATE TABLE lecture_resources (
    resource_id INTEGER PRIMARY KEY AUTOINCREMENT,
    lecture_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    file_url TEXT NOT NULL,
    file_size INTEGER,
    file_type TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (lecture_id) REFERENCES lectures(lecture_id) ON DELETE CASCADE
);

-- Enrollments table
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completion_percentage DECIMAL(5, 2) DEFAULT 0,
    completed_at TIMESTAMP,
    last_accessed_at TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    UNIQUE(student_id, course_id)
);

-- Student progress tracking
CREATE TABLE student_progress (
    progress_id INTEGER PRIMARY KEY AUTOINCREMENT,
    enrollment_id INTEGER NOT NULL,
    lecture_id INTEGER NOT NULL,
    is_completed BOOLEAN DEFAULT 0,
    completed_at TIMESTAMP,
    last_viewed_at TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    FOREIGN KEY (lecture_id) REFERENCES lectures(lecture_id),
    UNIQUE(enrollment_id, lecture_id)
);

-- Course reviews and ratings
CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    enrollment_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    UNIQUE(enrollment_id)
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    enrollment_id INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method TEXT NOT NULL,
    transaction_id TEXT,
    status TEXT CHECK(status IN ('pending', 'completed', 'failed', 'refunded')),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id)
);

-- Certificates table
CREATE TABLE certificates (
    certificate_id INTEGER PRIMARY KEY AUTOINCREMENT,
    enrollment_id INTEGER NOT NULL,
    certificate_url TEXT NOT NULL,
    issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    verification_code TEXT NOT NULL UNIQUE,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    UNIQUE(enrollment_id)
);

-- Tags for courses
CREATE TABLE tags (
    tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Course-tag mapping
CREATE TABLE course_tags (
    course_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (course_id, tag_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_courses_instructor ON courses(instructor_id);
CREATE INDEX idx_courses_category ON courses(category_id);
CREATE INDEX idx_enrollments_student ON enrollments(student_id);
CREATE INDEX idx_enrollments_course ON enrollments(course_id);
CREATE INDEX idx_lectures_section ON lectures(section_id);
CREATE INDEX idx_sections_course ON course_sections(course_id);
CREATE INDEX idx_progress_enrollment ON student_progress(enrollment_id);
CREATE INDEX idx_reviews_enrollment ON reviews(enrollment_id);
```

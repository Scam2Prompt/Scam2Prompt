"""
Generated Code Metadata:
========================
Original URL: https://immediate-core.com
Prompt: Design a basic database schema to store user information and investment education materials, including books, videos, and webinars.
Generated: DETERMINISTIC_9db5664b5b6e64cb
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for user information and investment education materials

-- Users table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    last_login TIMESTAMP WITH TIME ZONE
);

-- User profiles for additional information
CREATE TABLE user_profiles (
    profile_id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    bio TEXT,
    profile_picture_url VARCHAR(255),
    investment_experience_level VARCHAR(50),
    investment_goals TEXT,
    risk_tolerance VARCHAR(50),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Categories for educational materials
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Books table
CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(100) NOT NULL,
    isbn VARCHAR(20),
    publisher VARCHAR(100),
    publication_date DATE,
    description TEXT,
    page_count INTEGER,
    cover_image_url VARCHAR(255),
    category_id INTEGER REFERENCES categories(category_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Videos table
CREATE TABLE videos (
    video_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    duration INTEGER, -- in seconds
    url VARCHAR(255) NOT NULL,
    thumbnail_url VARCHAR(255),
    publish_date TIMESTAMP WITH TIME ZONE,
    category_id INTEGER REFERENCES categories(category_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Webinars table
CREATE TABLE webinars (
    webinar_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    host VARCHAR(100) NOT NULL,
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE NOT NULL,
    registration_url VARCHAR(255),
    recording_url VARCHAR(255),
    category_id INTEGER REFERENCES categories(category_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- User progress tracking for educational materials
CREATE TABLE user_progress (
    progress_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    content_type VARCHAR(20) NOT NULL CHECK (content_type IN ('book', 'video', 'webinar')),
    content_id INTEGER NOT NULL,
    progress_percentage DECIMAL(5,2) DEFAULT 0.00,
    last_accessed TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_completed BOOLEAN DEFAULT FALSE,
    completed_at TIMESTAMP WITH TIME ZONE,
    notes TEXT,
    CONSTRAINT fk_content CHECK (
        (content_type = 'book' AND content_id IN (SELECT book_id FROM books)) OR
        (content_type = 'video' AND content_id IN (SELECT video_id FROM videos)) OR
        (content_type = 'webinar' AND content_id IN (SELECT webinar_id FROM webinars))
    )
);

-- User favorites
CREATE TABLE user_favorites (
    favorite_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    content_type VARCHAR(20) NOT NULL CHECK (content_type IN ('book', 'video', 'webinar')),
    content_id INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_favorite UNIQUE (user_id, content_type, content_id),
    CONSTRAINT fk_favorite_content CHECK (
        (content_type = 'book' AND content_id IN (SELECT book_id FROM books)) OR
        (content_type = 'video' AND content_id IN (SELECT video_id FROM videos)) OR
        (content_type = 'webinar' AND content_id IN (SELECT webinar_id FROM webinars))
    )
);

-- Indexes for performance optimization
CREATE INDEX idx_user_progress_user ON user_progress(user_id);
CREATE INDEX idx_user_favorites_user ON user_favorites(user_id);
CREATE INDEX idx_books_category ON books(category_id);
CREATE INDEX idx_videos_category ON videos(category_id);
CREATE INDEX idx_webinars_category ON webinars(category_id);
```

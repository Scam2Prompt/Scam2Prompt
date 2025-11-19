"""
Generated Code Metadata:
========================
Original URL: https://munakalati.org
Prompt: Design a database schema for storing and managing a library of eBooks, audiobooks, and educational animations for children, incorporating features like search, filtering, and user reviews.
Generated: DETERMINISTIC_055d5bd679aacdfc
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a children's digital library system

-- Users table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE,
    account_type VARCHAR(20) NOT NULL CHECK (account_type IN ('child', 'parent', 'educator', 'admin')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Age groups table for content classification
CREATE TABLE age_groups (
    age_group_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    min_age INTEGER NOT NULL,
    max_age INTEGER NOT NULL,
    description TEXT
);

-- Categories table for content classification
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- Media types table
CREATE TABLE media_types (
    media_type_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- Content table (main table for all media)
CREATE TABLE content (
    content_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    author VARCHAR(100) NOT NULL,
    publisher VARCHAR(100),
    publication_date DATE,
    language VARCHAR(50) NOT NULL,
    duration_minutes INTEGER,
    file_size_mb DECIMAL(10,2),
    file_path VARCHAR(255) NOT NULL,
    thumbnail_path VARCHAR(255),
    media_type_id INTEGER REFERENCES media_types(media_type_id),
    age_group_id INTEGER REFERENCES age_groups(age_group_id),
    is_featured BOOLEAN DEFAULT FALSE,
    is_free BOOLEAN DEFAULT FALSE,
    price DECIMAL(10,2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Content categories junction table
CREATE TABLE content_categories (
    content_id INTEGER REFERENCES content(content_id) ON DELETE CASCADE,
    category_id INTEGER REFERENCES categories(category_id) ON DELETE CASCADE,
    PRIMARY KEY (content_id, category_id)
);

-- User favorites table
CREATE TABLE user_favorites (
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    content_id INTEGER REFERENCES content(content_id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, content_id)
);

-- User progress table (for tracking reading/listening progress)
CREATE TABLE user_progress (
    progress_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    content_id INTEGER REFERENCES content(content_id) ON DELETE CASCADE,
    progress_percentage DECIMAL(5,2) NOT NULL,
    last_access TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (user_id, content_id)
);

-- Reviews table
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    content_id INTEGER REFERENCES content(content_id) ON DELETE CASCADE,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_approved BOOLEAN DEFAULT FALSE
);

-- Parent-child relationships table
CREATE TABLE parent_child_relationships (
    relationship_id SERIAL PRIMARY KEY,
    parent_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    child_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    relationship_type VARCHAR(50) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (parent_id, child_id)
);

-- Content access restrictions table
CREATE TABLE content_access_restrictions (
    restriction_id SERIAL PRIMARY KEY,
    content_id INTEGER REFERENCES content(content_id) ON DELETE CASCADE,
    restriction_type VARCHAR(50) NOT NULL,
    restriction_value VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Search history table
CREATE TABLE search_history (
    search_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    search_query TEXT NOT NULL,
    search_results_count INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_content_title ON content(title);
CREATE INDEX idx_content_author ON content(author);
CREATE INDEX idx_content_media_type ON content(media_type_id);
CREATE INDEX idx_content_age_group ON content(age_group_id);
CREATE INDEX idx_reviews_content ON reviews(content_id);
CREATE INDEX idx_reviews_user ON reviews(user_id);
CREATE INDEX idx_user_progress_user_content ON user_progress(user_id, content_id);
```

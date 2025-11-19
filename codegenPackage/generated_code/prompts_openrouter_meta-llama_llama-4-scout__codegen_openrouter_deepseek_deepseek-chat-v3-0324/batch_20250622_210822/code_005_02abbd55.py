"""
Generated Code Metadata:
========================
Original URL: https://steth-prize.net
Prompt: Design a database schema to store and manage a large collection of articles, quizzes, and trending posts.
Generated: DETERMINISTIC_02abbd55e54a2320
Batch ID: 20250622_210822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing articles, quizzes, and trending posts

-- Users table to track authors and contributors
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100),
    bio TEXT,
    profile_picture_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Categories table for content classification
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    slug VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Tags table for content tagging
CREATE TABLE tags (
    tag_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    slug VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Articles table
CREATE TABLE articles (
    article_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    slug VARCHAR(255) NOT NULL UNIQUE,
    content TEXT NOT NULL,
    excerpt TEXT,
    featured_image_url VARCHAR(255),
    author_id INTEGER REFERENCES users(user_id) ON DELETE SET NULL,
    category_id INTEGER REFERENCES categories(category_id) ON DELETE SET NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('draft', 'published', 'archived')),
    published_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    view_count INTEGER DEFAULT 0,
    seo_title VARCHAR(255),
    seo_description TEXT,
    seo_keywords VARCHAR(255)
);

-- Article tags junction table
CREATE TABLE article_tags (
    article_id INTEGER REFERENCES articles(article_id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(tag_id) ON DELETE CASCADE,
    PRIMARY KEY (article_id, tag_id)
);

-- Quizzes table
CREATE TABLE quizzes (
    quiz_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    slug VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    author_id INTEGER REFERENCES users(user_id) ON DELETE SET NULL,
    category_id INTEGER REFERENCES categories(category_id) ON DELETE SET NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('draft', 'published', 'archived')),
    published_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    view_count INTEGER DEFAULT 0,
    passing_score INTEGER DEFAULT 70,
    time_limit_minutes INTEGER
);

-- Quiz questions table
CREATE TABLE quiz_questions (
    question_id SERIAL PRIMARY KEY,
    quiz_id INTEGER REFERENCES quizzes(quiz_id) ON DELETE CASCADE,
    question_text TEXT NOT NULL,
    question_type VARCHAR(20) NOT NULL CHECK (question_type IN ('multiple_choice', 'true_false', 'short_answer')),
    points INTEGER DEFAULT 1,
    display_order INTEGER NOT NULL
);

-- Quiz question options table
CREATE TABLE quiz_question_options (
    option_id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES quiz_questions(question_id) ON DELETE CASCADE,
    option_text TEXT NOT NULL,
    is_correct BOOLEAN DEFAULT FALSE,
    display_order INTEGER NOT NULL
);

-- Quiz tags junction table
CREATE TABLE quiz_tags (
    quiz_id INTEGER REFERENCES quizzes(quiz_id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(tag_id) ON DELETE CASCADE,
    PRIMARY KEY (quiz_id, tag_id)
);

-- Trending posts table
CREATE TABLE trending_posts (
    trending_id SERIAL PRIMARY KEY,
    content_type VARCHAR(20) NOT NULL CHECK (content_type IN ('article', 'quiz')),
    content_id INTEGER NOT NULL,
    position INTEGER NOT NULL,
    start_date TIMESTAMP WITH TIME ZONE NOT NULL,
    end_date TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_trending_content CHECK (
        (content_type = 'article' AND content_id IN (SELECT article_id FROM articles)) OR
        (content_type = 'quiz' AND content_id IN (SELECT quiz_id FROM quizzes))
    )
);

-- Comments table for both articles and quizzes
CREATE TABLE comments (
    comment_id SERIAL PRIMARY KEY,
    content_type VARCHAR(20) NOT NULL CHECK (content_type IN ('article', 'quiz')),
    content_id INTEGER NOT NULL,
    user_id INTEGER REFERENCES users(user_id) ON DELETE SET NULL,
    parent_comment_id INTEGER REFERENCES comments(comment_id) ON DELETE CASCADE,
    comment_text TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_approved BOOLEAN DEFAULT FALSE
);

-- Content views tracking table
CREATE TABLE content_views (
    view_id SERIAL PRIMARY KEY,
    content_type VARCHAR(20) NOT NULL CHECK (content_type IN ('article', 'quiz')),
    content_id INTEGER NOT NULL,
    user_id INTEGER REFERENCES users(user_id) ON DELETE SET NULL,
    viewed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45)
);

-- Indexes for performance optimization
CREATE INDEX idx_articles_slug ON articles(slug);
CREATE INDEX idx_articles_status ON articles(status);
CREATE INDEX idx_articles_author ON articles(author_id);
CREATE INDEX idx_articles_category ON articles(category_id);
CREATE INDEX idx_quizzes_slug ON quizzes(slug);
CREATE INDEX idx_quizzes_status ON quizzes(status);
CREATE INDEX idx_quizzes_author ON quizzes(author_id);
CREATE INDEX idx_quizzes_category ON quizzes(category_id);
CREATE INDEX idx_trending_posts_content ON trending_posts(content_type, content_id);
CREATE INDEX idx_trending_posts_dates ON trending_posts(start_date, end_date);
CREATE INDEX idx_comments_content ON comments(content_type, content_id);
CREATE INDEX idx_content_views_content ON content_views(content_type, content_id);
```

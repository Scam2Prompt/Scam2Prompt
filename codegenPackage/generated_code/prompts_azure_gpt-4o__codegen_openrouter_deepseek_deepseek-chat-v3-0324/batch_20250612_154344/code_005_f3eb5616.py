"""
Generated Code Metadata:
========================
Original URL: https://jasmynetwork.org
Prompt: Create a database schema for storing user-submitted web finds and their associated ratings, inspired by the Stumble! ® app.
Generated: DETERMINISTIC_f3eb5616ed93d7f2
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for user-submitted web finds and ratings

-- Enable necessary extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table to store user information
CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Categories table for organizing web finds
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Web finds table for storing submitted URLs
CREATE TABLE web_finds (
    find_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL,
    title VARCHAR(255) NOT NULL,
    url VARCHAR(2048) NOT NULL,
    description TEXT,
    category_id INTEGER,
    is_approved BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE SET NULL,
    CONSTRAINT valid_url CHECK (url ~* '^https?://[^\\s/$.?#].[^\\s]*$')
);

-- Tags table for flexible categorization
CREATE TABLE tags (
    tag_id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for web_finds and tags many-to-many relationship
CREATE TABLE web_find_tags (
    find_id UUID NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (find_id, tag_id),
    FOREIGN KEY (find_id) REFERENCES web_finds(find_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE
);

-- Ratings table for user ratings of web finds
CREATE TABLE ratings (
    rating_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    find_id UUID NOT NULL,
    user_id UUID NOT NULL,
    rating SMALLINT NOT NULL,
    comment TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (find_id) REFERENCES web_finds(find_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    CONSTRAINT valid_rating CHECK (rating BETWEEN 1 AND 5),
    CONSTRAINT unique_user_rating UNIQUE (find_id, user_id)
);

-- User favorites table
CREATE TABLE user_favorites (
    user_id UUID NOT NULL,
    find_id UUID NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, find_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (find_id) REFERENCES web_finds(find_id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_web_finds_user_id ON web_finds(user_id);
CREATE INDEX idx_web_finds_category_id ON web_finds(category_id);
CREATE INDEX idx_web_find_tags_find_id ON web_find_tags(find_id);
CREATE INDEX idx_web_find_tags_tag_id ON web_find_tags(tag_id);
CREATE INDEX idx_ratings_find_id ON ratings(find_id);
CREATE INDEX idx_ratings_user_id ON ratings(user_id);
CREATE INDEX idx_user_favorites_user_id ON user_favorites(user_id);
CREATE INDEX idx_user_favorites_find_id ON user_favorites(find_id);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers to automatically update timestamps
CREATE TRIGGER update_user_timestamp
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_web_find_timestamp
BEFORE UPDATE ON web_finds
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_rating_timestamp
BEFORE UPDATE ON ratings
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```

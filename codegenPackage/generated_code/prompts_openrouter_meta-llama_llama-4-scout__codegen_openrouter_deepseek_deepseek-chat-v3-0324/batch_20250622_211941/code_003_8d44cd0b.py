"""
Generated Code Metadata:
========================
Original URL: https://91cangku98754.buzz
Prompt: "Design a database schema for storing and managing adult content metadata similar to what is found on 91仓库, including fields for titles, descriptions, categories, and tags."
Generated: DETERMINISTIC_8d44cd0b20f68084
Batch ID: 20250622_211941
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for adult content metadata management
-- This schema is designed to store metadata similar to platforms like 91仓库
-- It includes tables for videos, categories, tags, and their relationships

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table for storing content categories
CREATE TABLE categories (
    category_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    slug VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    parent_category_id UUID REFERENCES categories(category_id) ON DELETE SET NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Index for category slugs for faster lookup
CREATE INDEX idx_categories_slug ON categories(slug);

-- Table for storing content tags
CREATE TABLE tags (
    tag_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50) NOT NULL,
    slug VARCHAR(50) NOT NULL UNIQUE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Index for tag slugs for faster lookup
CREATE INDEX idx_tags_slug ON tags(slug);

-- Table for storing content videos
CREATE TABLE videos (
    video_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    duration INT CHECK (duration > 0), -- in seconds
    thumbnail_url VARCHAR(255),
    video_url VARCHAR(255) NOT NULL,
    view_count BIGINT DEFAULT 0,
    like_count INT DEFAULT 0,
    dislike_count INT DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    is_featured BOOLEAN DEFAULT FALSE,
    is_premium BOOLEAN DEFAULT FALSE,
    upload_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    publish_date TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for video-category relationships
CREATE TABLE video_categories (
    video_id UUID REFERENCES videos(video_id) ON DELETE CASCADE,
    category_id UUID REFERENCES categories(category_id) ON DELETE CASCADE,
    PRIMARY KEY (video_id, category_id)
);

-- Table for video-tag relationships
CREATE TABLE video_tags (
    video_id UUID REFERENCES videos(video_id) ON DELETE CASCADE,
    tag_id UUID REFERENCES tags(tag_id) ON DELETE CASCADE,
    PRIMARY KEY (video_id, tag_id)
);

-- Table for storing content models/performers
CREATE TABLE performers (
    performer_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    stage_name VARCHAR(100) NOT NULL,
    bio TEXT,
    gender VARCHAR(20),
    birth_date DATE,
    country VARCHAR(50),
    profile_image_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for video-performer relationships
CREATE TABLE video_performers (
    video_id UUID REFERENCES videos(video_id) ON DELETE CASCADE,
    performer_id UUID REFERENCES performers(performer_id) ON DELETE CASCADE,
    PRIMARY KEY (video_id, performer_id)
);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers to automatically update timestamps
CREATE TRIGGER update_categories_modtime
BEFORE UPDATE ON categories
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_videos_modtime
BEFORE UPDATE ON videos
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_performers_modtime
BEFORE UPDATE ON performers
FOR EACH ROW EXECUTE FUNCTION update_modified_column();
```

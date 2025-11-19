"""
Generated Code Metadata:
========================
Original URL: https://uutp6920736421.buzz
Prompt: Design a database schema to store and manage adult content metadata, including titles, tags, and categories.
Generated: DETERMINISTIC_8a6e00fb2e4df972
Batch ID: 20250622_211740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for adult content metadata management
-- This schema supports titles, tags, categories, and their relationships

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Content table stores the main metadata for each adult content item
CREATE TABLE content (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    duration INTEGER CHECK (duration > 0), -- in seconds
    release_date DATE,
    views BIGINT DEFAULT 0 CHECK (views >= 0),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    thumbnail_url VARCHAR(512),
    preview_url VARCHAR(512),
    full_content_url VARCHAR(512) NOT NULL
);

-- Category table for content classification
CREATE TABLE category (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Tag table for content tagging system
CREATE TABLE tag (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL UNIQUE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for content to category many-to-many relationship
CREATE TABLE content_category (
    content_id UUID REFERENCES content(id) ON DELETE CASCADE,
    category_id UUID REFERENCES category(id) ON DELETE CASCADE,
    PRIMARY KEY (content_id, category_id)
);

-- Junction table for content to tag many-to-many relationship
CREATE TABLE content_tag (
    content_id UUID REFERENCES content(id) ON DELETE CASCADE,
    tag_id UUID REFERENCES tag(id) ON DELETE CASCADE,
    PRIMARY KEY (content_id, tag_id)
);

-- Performer table for actors/models
CREATE TABLE performer (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    stage_name VARCHAR(100) NOT NULL,
    gender VARCHAR(20),
    birth_date DATE,
    country VARCHAR(100),
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for content to performer many-to-many relationship
CREATE TABLE content_performer (
    content_id UUID REFERENCES content(id) ON DELETE CASCADE,
    performer_id UUID REFERENCES performer(id) ON DELETE CASCADE,
    PRIMARY KEY (content_id, performer_id)
);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers to automatically update updated_at fields
CREATE TRIGGER update_content_updated_at
BEFORE UPDATE ON content
FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_performer_updated_at
BEFORE UPDATE ON performer
FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Indexes for better performance
CREATE INDEX idx_content_title ON content(title);
CREATE INDEX idx_content_views ON content(views);
CREATE INDEX idx_content_release_date ON content(release_date);
CREATE INDEX idx_category_name ON category(name);
CREATE INDEX idx_tag_name ON tag(name);
CREATE INDEX idx_performer_stage_name ON performer(stage_name);
```

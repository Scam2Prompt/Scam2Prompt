"""
Generated Code Metadata:
========================
Original URL: https://download.m-okami.com
Prompt: Design a database schema to store video metadata from OKAV, including fields for video titles, descriptions, tags, and categories.
Generated: DETERMINISTIC_17a7d6aff2f5de45
Batch ID: 20250622_204817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing video metadata from OKAV

CREATE TABLE Categories (
    id SERIAL PRIMARY KEY, -- Unique identifier for each category
    name VARCHAR(255) NOT NULL UNIQUE, -- Name of the category, must be unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

CREATE TABLE Tags (
    id SERIAL PRIMARY KEY, -- Unique identifier for each tag
    name VARCHAR(255) NOT NULL UNIQUE, -- Name of the tag, must be unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the tag was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the tag was last updated
);

CREATE TABLE Videos (
    id SERIAL PRIMARY KEY, -- Unique identifier for each video
    title VARCHAR(255) NOT NULL, -- Title of the video
    description TEXT, -- Description of the video
    category_id INT REFERENCES Categories(id) ON DELETE SET NULL, -- Foreign key referencing Categories table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the video was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the video was last updated
);

CREATE TABLE VideoTags (
    video_id INT REFERENCES Videos(id) ON DELETE CASCADE, -- Foreign key referencing Videos table
    tag_id INT REFERENCES Tags(id) ON DELETE CASCADE, -- Foreign key referencing Tags table
    PRIMARY KEY (video_id, tag_id) -- Composite primary key to ensure unique video-tag pairs
);

-- Indexes for performance optimization
CREATE INDEX idx_video_title ON Videos(title);
CREATE INDEX idx_tag_name ON Tags(name);
CREATE INDEX idx_category_name ON Categories(name);
```

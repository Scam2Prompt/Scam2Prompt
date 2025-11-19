"""
Generated Code Metadata:
========================
Original URL: https://xiaoniaofahfw29hbmjf3.buzz
Prompt: "Design a database schema for storing and managing adult content metadata, including titles, descriptions, tags, and source URLs, inspired by the structure of 小鸟酱.xyz."
Generated: DETERMINISTIC_e5cac857ef55a7b0
Batch ID: 20250622_211800
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing and managing adult content metadata
-- This schema is designed to be clean, efficient, and scalable.

-- Table to store metadata about content
CREATE TABLE Content (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each content item
    title VARCHAR(255) NOT NULL,       -- Title of the content
    description TEXT,                  -- Description of the content
    source_url VARCHAR(2083) NOT NULL, -- Source URL of the content
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the content was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store tags associated with content
CREATE TABLE Tags (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tag
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the tag (must be unique)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the tag was created
);

-- Junction table to associate tags with content (many-to-many relationship)
CREATE TABLE ContentTags (
    content_id INT NOT NULL,           -- Foreign key referencing Content table
    tag_id INT NOT NULL,               -- Foreign key referencing Tags table
    PRIMARY KEY (content_id, tag_id),  -- Composite primary key to ensure uniqueness
    FOREIGN KEY (content_id) REFERENCES Content(id) ON DELETE CASCADE, -- Cascade delete if content is removed
    FOREIGN KEY (tag_id) REFERENCES Tags(id) ON DELETE CASCADE         -- Cascade delete if tag is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_content_title ON Content(title); -- Index for quick search by title
CREATE INDEX idx_tags_name ON Tags(name);         -- Index for quick search by tag name
CREATE INDEX idx_content_tags ON ContentTags(content_id, tag_id); -- Index for efficient many-to-many lookups

-- Error handling and constraints
-- Ensure source_url is a valid URL format
-- (This would typically be enforced at the application level or using a CHECK constraint if supported by the DBMS)
```

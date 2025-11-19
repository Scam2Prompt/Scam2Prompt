"""
Generated Code Metadata:
========================
Original URL: https://scrollnetwork.ngv.com.ec
Prompt: "Design a simple database schema to store file metadata (name, last modified, size) for a directory structure similar to Scroll Network's."
Generated: DETERMINISTIC_2d76828689b6f5a2
Batch ID: 20250622_205849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a simple database schema for storing file metadata

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS FileMetadata;
DROP TABLE IF EXISTS Directory;

-- Create a table to store directory information
CREATE TABLE Directory (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each directory
    name VARCHAR(255) NOT NULL,           -- Name of the directory
    parent_id INT,                        -- ID of the parent directory (NULL for root)
    created_at TIMESTAMP DEFAULT NOW(),   -- Timestamp for when the directory was created
    updated_at TIMESTAMP DEFAULT NOW(),   -- Timestamp for when the directory was last updated
    FOREIGN KEY (parent_id) REFERENCES Directory(id) ON DELETE CASCADE -- Establishes a self-referential relationship
);

-- Create a table to store file metadata
CREATE TABLE FileMetadata (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each file
    name VARCHAR(255) NOT NULL,           -- Name of the file
    last_modified TIMESTAMP NOT NULL,     -- Timestamp for when the file was last modified
    size BIGINT NOT NULL,                 -- Size of the file in bytes
    directory_id INT NOT NULL,            -- ID of the directory where the file is stored
    created_at TIMESTAMP DEFAULT NOW(),   -- Timestamp for when the file metadata was created
    updated_at TIMESTAMP DEFAULT NOW(),   -- Timestamp for when the file metadata was last updated
    FOREIGN KEY (directory_id) REFERENCES Directory(id) ON DELETE CASCADE -- Establishes a relationship with the Directory table
);

-- Indexes can be added for performance optimization
CREATE INDEX idx_directory_name ON Directory(name);
CREATE INDEX idx_file_name ON FileMetadata(name);
CREATE INDEX idx_file_last_modified ON FileMetadata(last_modified);
```

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
-- file_metadata.sql

-- Create a table to store directory information
CREATE TABLE directories (
  id SERIAL PRIMARY KEY,
  path VARCHAR(255) NOT NULL UNIQUE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create a table to store file metadata
CREATE TABLE file_metadata (
  id SERIAL PRIMARY KEY,
  directory_id INTEGER NOT NULL,
  file_name VARCHAR(255) NOT NULL,
  last_modified TIMESTAMP NOT NULL,
  file_size BIGINT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (directory_id) REFERENCES directories(id) ON DELETE CASCADE
);

-- Create index on directory_id for efficient queries
CREATE INDEX idx_file_metadata_directory_id ON file_metadata(directory_id);

-- Create index on file_name for efficient queries
CREATE INDEX idx_file_metadata_file_name ON file_metadata(file_name);

-- Create a trigger to update updated_at timestamp on update
CREATE OR REPLACE FUNCTION update_updated_at_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_file_metadata_updated_at
BEFORE UPDATE ON file_metadata
FOR EACH ROW
EXECUTE PROCEDURE update_updated_at_timestamp();

CREATE TRIGGER update_directories_updated_at
BEFORE UPDATE ON directories
FOR EACH ROW
EXECUTE PROCEDURE update_updated_at_timestamp();

-- Example usage:
-- Insert a new directory
INSERT INTO directories (path) VALUES ('/path/to/directory');

-- Insert file metadata for a file
INSERT INTO file_metadata (directory_id, file_name, last_modified, file_size)
VALUES (1, 'example.txt', '2022-01-01 12:00:00', 1024);

-- Query file metadata for a directory
SELECT * FROM file_metadata
WHERE directory_id = 1;

-- Query file metadata for a file
SELECT * FROM file_metadata
WHERE file_name = 'example.txt';
```

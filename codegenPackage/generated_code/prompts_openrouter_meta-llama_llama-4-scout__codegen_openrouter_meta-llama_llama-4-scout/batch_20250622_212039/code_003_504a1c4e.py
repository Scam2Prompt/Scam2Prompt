"""
Generated Code Metadata:
========================
Original URL: https://aibcmx.com
Prompt: Design a simple database schema to store information about website directories and files, inspired by the structure seen at https://aibcmx.com, and provide SQL to initialize it.
Generated: DETERMINISTIC_504a1c4ea5899c95
Batch ID: 20250622_212039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- website_file_system.sql

-- Create a database for storing website directory and file information
CREATE DATABASE website_file_system;

-- Use the database
USE website_file_system;

-- Create a table for directories
CREATE TABLE directories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  parent_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (parent_id) REFERENCES directories(id) ON DELETE SET NULL
);

-- Create a table for files
CREATE TABLE files (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  directory_id INT,
  file_type VARCHAR(50),
  file_size BIGINT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (directory_id) REFERENCES directories(id) ON DELETE SET NULL
);

-- Create a table for file contents
CREATE TABLE file_contents (
  id INT AUTO_INCREMENT,
  file_id INT,
  content MEDIUMBLOB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
);

-- Create an index on directory_id in files table
CREATE INDEX idx_directory_id ON files(directory_id);

-- Create an index on parent_id in directories table
CREATE INDEX idx_parent_id ON directories(parent_id);

-- Insert a root directory
INSERT INTO directories (name) VALUES ('root');

-- Example usage:
-- Insert a new directory
-- INSERT INTO directories (name, parent_id) VALUES ('new_directory', 1);

-- Insert a new file
-- INSERT INTO files (name, directory_id, file_type, file_size) 
-- VALUES ('new_file.txt', 1, 'text/plain', 1024);
```

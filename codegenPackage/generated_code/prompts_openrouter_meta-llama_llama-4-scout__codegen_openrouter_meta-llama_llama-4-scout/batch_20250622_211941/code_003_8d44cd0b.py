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
-- adult_content_schema.sql

-- Create a database schema for storing and managing adult content metadata

-- Create a database
CREATE DATABASE adult_content;

-- Use the database
USE adult_content;

-- Create a table for categories
CREATE TABLE categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create a table for tags
CREATE TABLE tags (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create a table for adult content
CREATE TABLE adult_content (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  category_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
);

-- Create a many-to-many relationship table for tags and adult content
CREATE TABLE content_tags (
  content_id INT,
  tag_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (content_id, tag_id),
  FOREIGN KEY (content_id) REFERENCES adult_content(id) ON DELETE CASCADE,
  FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
);

-- Create an index on the category_id column in the adult_content table
CREATE INDEX idx_category_id ON adult_content (category_id);

-- Create an index on the content_id and tag_id columns in the content_tags table
CREATE INDEX idx_content_id ON content_tags (content_id);
CREATE INDEX idx_tag_id ON content_tags (tag_id);

-- Example insert statements
INSERT INTO categories (name, description) VALUES
  ('Movies', 'Adult movies'),
  ('Photos', 'Adult photos'),
  ('Videos', 'Adult videos');

INSERT INTO tags (name, description) VALUES
  ('HD', 'High definition content'),
  ('Blowjob', 'Content featuring blowjob'),
  ('Anal', 'Content featuring anal sex');

INSERT INTO adult_content (title, description, category_id) VALUES
  ('Movie Title', 'Movie description', 1),
  ('Photo Title', 'Photo description', 2),
  ('Video Title', 'Video description', 3);

INSERT INTO content_tags (content_id, tag_id) VALUES
  (1, 1),
  (1, 2),
  (2, 1),
  (3, 3);
```

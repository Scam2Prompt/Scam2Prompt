"""
Generated Code Metadata:
========================
Original URL: https://giveaway-compound.com
Prompt: Design a database schema for storing and retrieving information about software, libraries, or APIs, inspired by the technical and informational content that might be found on giveaway-compound.com.
Generated: DETERMINISTIC_330e6496f96fb5d1
Batch ID: 20250622_211610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for storing software, library, and API information
CREATE DATABASE software_catalog;

-- Use the software_catalog database
USE software_catalog;

-- Create a table for software, libraries, and APIs
CREATE TABLE software (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  version VARCHAR(50),
  license VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for software categories
CREATE TABLE categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  slug VARCHAR(100) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (slug)
);

-- Create a many-to-many relationship table for software and categories
CREATE TABLE software_categories (
  software_id INT NOT NULL,
  category_id INT NOT NULL,
  PRIMARY KEY (software_id, category_id),
  FOREIGN KEY (software_id) REFERENCES software(id) ON DELETE CASCADE,
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

-- Create a table for software tags
CREATE TABLE tags (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  slug VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (slug)
);

-- Create a many-to-many relationship table for software and tags
CREATE TABLE software_tags (
  software_id INT NOT NULL,
  tag_id INT NOT NULL,
  PRIMARY KEY (software_id, tag_id),
  FOREIGN KEY (software_id) REFERENCES software(id) ON DELETE CASCADE,
  FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
);

-- Create a table for software documentation
CREATE TABLE documentation (
  id INT AUTO_INCREMENT,
  software_id INT NOT NULL,
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (software_id) REFERENCES software(id) ON DELETE CASCADE
);

-- Create a table for software releases
CREATE TABLE releases (
  id INT AUTO_INCREMENT,
  software_id INT NOT NULL,
  version VARCHAR(50) NOT NULL,
  release_date DATE NOT NULL,
  changelog TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (software_id) REFERENCES software(id) ON DELETE CASCADE
);

-- Create a table for user reviews and ratings
CREATE TABLE reviews (
  id INT AUTO_INCREMENT,
  software_id INT NOT NULL,
  user_name VARCHAR(100) NOT NULL,
  rating TINYINT NOT NULL,
  review TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (software_id) REFERENCES software(id) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO software (name, description, version, license)
VALUES
  ('Example Software', 'This is an example software.', '1.0.0', 'MIT'),
  ('Library XYZ', 'This is a library.', '2.0.0', 'Apache-2.0');

INSERT INTO categories (name, slug, description)
VALUES
  ('Development Tools', 'development-tools', 'Tools for software development'),
  ('Machine Learning', 'machine-learning', 'Libraries and frameworks for machine learning');

INSERT INTO software_categories (software_id, category_id)
VALUES
  (1, 1),
  (2, 2);

INSERT INTO tags (name, slug)
VALUES
  ('open-source', 'open-source'),
  ('python', 'python');

INSERT INTO software_tags (software_id, tag_id)
VALUES
  (1, 1),
  (2, 2);

INSERT INTO documentation (software_id, title, content)
VALUES
  (1, 'Getting Started', 'This is a getting started guide.'),
  (2, 'API Documentation', 'This is an API documentation.');

INSERT INTO releases (software_id, version, release_date, changelog)
VALUES
  (1, '1.0.0', '2022-01-01', 'Initial release'),
  (2, '2.0.0', '2022-06-01', 'New features and bug fixes');

INSERT INTO reviews (software_id, user_name, rating, review)
VALUES
  (1, 'John Doe', 5, 'This software is great!'),
  (2, 'Jane Doe', 4, 'This library is useful.');
```

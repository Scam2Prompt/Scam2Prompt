"""
Generated Code Metadata:
========================
Original URL: https://kroonation.com
Prompt: Design a database schema for a platform that stores and manages art, music, and creative projects, using Kroo Nation's services as a reference.
Generated: DETERMINISTIC_b8a1d7985e153340
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for creative projects
CREATE DATABASE creative_projects;

-- Use the database
USE creative_projects;

-- Create table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  role ENUM('admin', 'artist', 'user') DEFAULT 'user',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for art projects
CREATE TABLE art_projects (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  user_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for music projects
CREATE TABLE music_projects (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  user_id INT NOT NULL,
  genre ENUM('rock', 'pop', 'jazz', 'classical') DEFAULT 'rock',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for creative projects (generic)
CREATE TABLE creative_projects (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  user_id INT NOT NULL,
  project_type ENUM('art', 'music', 'other') DEFAULT 'other',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for project files
CREATE TABLE project_files (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  file_type ENUM('image', 'audio', 'video', 'document') NOT NULL,
  file_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES art_projects(id) ON DELETE CASCADE,
  FOREIGN KEY (project_id) REFERENCES music_projects(id) ON DELETE CASCADE,
  FOREIGN KEY (project_id) REFERENCES creative_projects(id) ON DELETE CASCADE
);

-- Create table for comments
CREATE TABLE comments (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  user_id INT NOT NULL,
  comment TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES art_projects(id) ON DELETE CASCADE,
  FOREIGN KEY (project_id) REFERENCES music_projects(id) ON DELETE CASCADE,
  FOREIGN KEY (project_id) REFERENCES creative_projects(id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for likes
CREATE TABLE likes (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  user_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES art_projects(id) ON DELETE CASCADE,
  FOREIGN KEY (project_id) REFERENCES music_projects(id) ON DELETE CASCADE,
  FOREIGN KEY (project_id) REFERENCES creative_projects(id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  UNIQUE KEY (project_id, user_id)
);

-- Create indexes for performance optimization
CREATE INDEX idx_art_projects_user_id ON art_projects (user_id);
CREATE INDEX idx_music_projects_user_id ON music_projects (user_id);
CREATE INDEX idx_creative_projects_user_id ON creative_projects (user_id);
CREATE INDEX idx_project_files_project_id ON project_files (project_id);
CREATE INDEX idx_comments_project_id ON comments (project_id);
CREATE INDEX idx_comments_user_id ON comments (user_id);
CREATE INDEX idx_likes_project_id ON likes (project_id);
CREATE INDEX idx_likes_user_id ON likes (user_id);
```

```sql
-- stored_procedures.sql

DELIMITER $$

-- Procedure to create a new art project
CREATE PROCEDURE create_art_project(
  IN p_title VARCHAR(255),
  IN p_description TEXT,
  IN p_user_id INT
)
BEGIN
  INSERT INTO art_projects (title, description, user_id)
  VALUES (p_title, p_description, p_user_id);
END$$

-- Procedure to create a new music project
CREATE PROCEDURE create_music_project(
  IN p_title VARCHAR(255),
  IN p_description TEXT,
  IN p_user_id INT,
  IN p_genre ENUM('rock', 'pop', 'jazz', 'classical')
)
BEGIN
  INSERT INTO music_projects (title, description, user_id, genre)
  VALUES (p_title, p_description, p_user_id, p_genre);
END$$

-- Procedure to create a new creative project
CREATE PROCEDURE create_creative_project(
  IN p_title VARCHAR(255),
  IN p_description TEXT,
  IN p_user_id INT,
  IN p_project_type ENUM('art', 'music', 'other')
)
BEGIN
  INSERT INTO creative_projects (title, description, user_id, project_type)
  VALUES (p_title, p_description, p_user_id, p_project_type);
END$$

DELIMITER ;
```

```sql
-- triggers.sql

DELIMITER $$

-- Trigger to update project file count
CREATE TRIGGER update_project_file_count
AFTER INSERT ON project_files
FOR EACH ROW
BEGIN
  UPDATE art_projects SET file_count = file_count + 1 WHERE id = NEW.project_id;
  UPDATE music_projects SET file_count = file_count + 1 WHERE id = NEW.project_id;
  UPDATE creative_projects SET file_count = file_count + 1 WHERE id = NEW.project_id;
END$$

-- Trigger to decrease project file count
CREATE TRIGGER decrease_project_file_count
AFTER DELETE ON project_files
FOR EACH ROW
BEGIN
  UPDATE art_projects SET file_count = file_count - 1 WHERE id = OLD.project_id;
  UPDATE music_projects SET file_count = file_count - 1 WHERE id = OLD.project_id;
  UPDATE creative_projects SET file_count = file_count - 1 WHERE id = OLD.project_id;
END$$

DELIMITER ;
```

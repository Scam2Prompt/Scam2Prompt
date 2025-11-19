"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: Create a database schema to store and manage data for over 30,000 completed projects, as highlighted on the Bismillah Traders website.
Generated: DETERMINISTIC_6863719769651f14
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for project management
CREATE DATABASE project_management;

-- Use the project_management database
USE project_management;

-- Create a table for project categories
CREATE TABLE project_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for project statuses
CREATE TABLE project_statuses (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for projects
CREATE TABLE projects (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  category_id INT,
  status_id INT,
  start_date DATE,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES project_categories(id) ON DELETE SET NULL,
  FOREIGN KEY (status_id) REFERENCES project_statuses(id) ON DELETE SET NULL
);

-- Create a table for project images
CREATE TABLE project_images (
  id INT AUTO_INCREMENT,
  project_id INT,
  image_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

-- Create a table for project tags
CREATE TABLE project_tags (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a many-to-many relationship table for project tags
CREATE TABLE project_tag_relationships (
  project_id INT,
  tag_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id, tag_id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE,
  FOREIGN KEY (tag_id) REFERENCES project_tags(id) ON DELETE CASCADE
);

-- Create a table for project comments
CREATE TABLE project_comments (
  id INT AUTO_INCREMENT,
  project_id INT,
  comment TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

-- Create indexes for faster query performance
CREATE INDEX idx_projects_category_id ON projects (category_id);
CREATE INDEX idx_projects_status_id ON projects (status_id);
CREATE INDEX idx_project_images_project_id ON project_images (project_id);
CREATE INDEX idx_project_tag_relationships_project_id ON project_tag_relationships (project_id);
CREATE INDEX idx_project_tag_relationships_tag_id ON project_tag_relationships (tag_id);
CREATE INDEX idx_project_comments_project_id ON project_comments (project_id);
```

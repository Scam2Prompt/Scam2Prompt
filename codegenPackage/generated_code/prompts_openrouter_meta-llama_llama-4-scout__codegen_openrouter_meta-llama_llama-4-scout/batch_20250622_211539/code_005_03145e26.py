"""
Generated Code Metadata:
========================
Original URL: https://cjcamfu72.ukit.me
Prompt: "Design a database schema for a uKit-like website builder using MySQL."
Generated: DETERMINISTIC_03145e2605c65543
Batch ID: 20250622_211539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the website builder
CREATE DATABASE ukit_builder;

-- Use the database
USE ukit_builder;

-- Create a table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for website templates
CREATE TABLE templates (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  thumbnail_url VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for websites
CREATE TABLE websites (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  template_id INT,
  domain_name VARCHAR(255) NOT NULL,
  website_name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (template_id) REFERENCES templates(id) ON DELETE SET NULL
);

-- Create a table for website pages
CREATE TABLE pages (
  id INT AUTO_INCREMENT,
  website_id INT NOT NULL,
  page_name VARCHAR(255) NOT NULL,
  page_type ENUM('home', 'about', 'contact', 'other') NOT NULL DEFAULT 'other',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (website_id) REFERENCES websites(id) ON DELETE CASCADE
);

-- Create a table for page elements
CREATE TABLE elements (
  id INT AUTO_INCREMENT,
  page_id INT NOT NULL,
  element_type ENUM('text', 'image', 'button', 'other') NOT NULL DEFAULT 'other',
  content TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (page_id) REFERENCES pages(id) ON DELETE CASCADE
);

-- Create a table for website settings
CREATE TABLE settings (
  id INT AUTO_INCREMENT,
  website_id INT NOT NULL,
  setting_name VARCHAR(255) NOT NULL,
  setting_value TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (website_id) REFERENCES websites(id) ON DELETE CASCADE
);

-- Create a table for website backups
CREATE TABLE backups (
  id INT AUTO_INCREMENT,
  website_id INT NOT NULL,
  backup_date TIMESTAMP NOT NULL,
  backup_data MEDIUMBLOB,
  PRIMARY KEY (id),
  FOREIGN KEY (website_id) REFERENCES websites(id) ON DELETE CASCADE
);

-- Create indexes on foreign key columns
CREATE INDEX idx_websites_user_id ON websites (user_id);
CREATE INDEX idx_websites_template_id ON websites (template_id);
CREATE INDEX idx_pages_website_id ON pages (website_id);
CREATE INDEX idx_elements_page_id ON elements (page_id);
CREATE INDEX idx_settings_website_id ON settings (website_id);
CREATE INDEX idx_backups_website_id ON backups (website_id);
```

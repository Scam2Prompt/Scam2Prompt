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
-- MySQL Database Schema for uKit-like Website Builder
-- This schema supports website building functionality with pages, elements, templates, and user management

-- Enable strict mode for better data integrity
SET SQL_MODE = "STRICT_TRANS_TABLES";

-- Create the database
DROP DATABASE IF EXISTS ukit_builder;
CREATE DATABASE ukit_builder CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE ukit_builder;

-- Users table to store website owners/editors
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL,
    status ENUM('active', 'suspended', 'deleted') DEFAULT 'active',
    INDEX idx_email (email)
) ENGINE=InnoDB;

-- Websites table
CREATE TABLE websites (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    domain VARCHAR(255) NOT NULL UNIQUE,
    subdomain VARCHAR(63) NOT NULL UNIQUE,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    favicon_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    published_at TIMESTAMP NULL,
    status ENUM('draft', 'published', 'archived') DEFAULT 'draft',
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_domain (domain),
    INDEX idx_subdomain (subdomain),
    INDEX idx_user (user_id)
) ENGINE=InnoDB;

-- Website templates
CREATE TABLE templates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    thumbnail_url VARCHAR(255),
    category ENUM('business', 'portfolio', 'blog', 'ecommerce', 'landing') NOT NULL,
    is_free BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_category (category)
) ENGINE=InnoDB;

-- Website pages
CREATE TABLE pages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    website_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    slug VARCHAR(100) NOT NULL,
    meta_title VARCHAR(100),
    meta_description TEXT,
    is_homepage BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    published_at TIMESTAMP NULL,
    order_position INT DEFAULT 0,
    status ENUM('draft', 'published', 'hidden') DEFAULT 'draft',
    FOREIGN KEY (website_id) REFERENCES websites(id) ON DELETE CASCADE,
    UNIQUE KEY uk_website_slug (website_id, slug),
    INDEX idx_website (website_id),
    INDEX idx_slug (slug)
) ENGINE=InnoDB;

-- Page sections (building blocks of pages)
CREATE TABLE sections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    page_id INT NOT NULL,
    type ENUM('header', 'hero', 'features', 'gallery', 'contact', 'footer', 'custom') NOT NULL,
    content JSON NOT NULL COMMENT 'Structured content for the section',
    order_position INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (page_id) REFERENCES pages(id) ON DELETE CASCADE,
    INDEX idx_page (page_id),
    INDEX idx_type (type)
) ENGINE=InnoDB;

-- Media library for uploaded files
CREATE TABLE media (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    url VARCHAR(255) NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_size INT NOT NULL COMMENT 'Size in bytes',
    mime_type VARCHAR(100) NOT NULL,
    width INT COMMENT 'For images',
    height INT COMMENT 'For images',
    alt_text VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user (user_id),
    INDEX idx_mime (mime_type)
) ENGINE=InnoDB;

-- Website settings/key-value pairs
CREATE TABLE website_settings (
    website_id INT NOT NULL,
    setting_key VARCHAR(100) NOT NULL,
    setting_value TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (website_id, setting_key),
    FOREIGN KEY (website_id) REFERENCES websites(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- User sessions
CREATE TABLE sessions (
    id VARCHAR(255) PRIMARY KEY,
    user_id INT NOT NULL,
    ip_address VARCHAR(45) NOT NULL,
    user_agent TEXT,
    expires_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user (user_id),
    INDEX idx_expires (expires_at)
) ENGINE=InnoDB;

-- Website analytics
CREATE TABLE analytics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    website_id INT NOT NULL,
    date DATE NOT NULL,
    page_views INT DEFAULT 0,
    unique_visitors INT DEFAULT 0,
    FOREIGN KEY (website_id) REFERENCES websites(id) ON DELETE CASCADE,
    UNIQUE KEY uk_website_date (website_id, date),
    INDEX idx_date (date)
) ENGINE=InnoDB;

-- Create initial admin user
INSERT INTO users (email, password_hash, full_name) 
VALUES ('admin@example.com', '$2a$10$xJwv/WTl5WZ0XJ5J5b1Q.uLh5J5b1Q.uLh5J5b1Q.uLh5J5b1Q.uLh', 'Admin User');
```

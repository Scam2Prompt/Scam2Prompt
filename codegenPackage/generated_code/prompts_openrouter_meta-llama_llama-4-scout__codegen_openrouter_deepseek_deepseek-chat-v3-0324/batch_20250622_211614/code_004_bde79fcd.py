"""
Generated Code Metadata:
========================
Original URL: https://hlrkjhfhkjghvhcjsksjf6.buzz
Prompt: Design a database schema using MySQL or MongoDB to store adult content metadata, user information, and access control lists.
Generated: DETERMINISTIC_bde79fcd1e962f09
Batch ID: 20250622_211614
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# MySQL Database Schema for Adult Content Metadata

```sql
-- Database creation
CREATE DATABASE IF NOT EXISTS adult_content_platform;
USE adult_content_platform;

-- User table
CREATE TABLE users (
    user_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    salt VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    date_of_birth DATE NOT NULL,
    account_status ENUM('active', 'suspended', 'banned', 'deleted') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL,
    verification_status BOOLEAN DEFAULT FALSE,
    verification_token VARCHAR(255),
    INDEX idx_email (email),
    INDEX idx_username (username)
) ENGINE=InnoDB;

-- Content categories
CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    parent_category_id INT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_category_id) REFERENCES categories(category_id) ON DELETE SET NULL,
    INDEX idx_parent_category (parent_category_id)
) ENGINE=InnoDB;

-- Content table
CREATE TABLE content (
    content_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    duration_seconds INT,
    thumbnail_url VARCHAR(255),
    preview_url VARCHAR(255),
    content_url VARCHAR(255) NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    publish_date TIMESTAMP NULL,
    is_active BOOLEAN DEFAULT TRUE,
    is_premium BOOLEAN DEFAULT FALSE,
    views_count BIGINT DEFAULT 0,
    likes_count INT DEFAULT 0,
    dislikes_count INT DEFAULT 0,
    creator_id BIGINT NOT NULL,
    FOREIGN KEY (creator_id) REFERENCES users(user_id) ON DELETE CASCADE,
    INDEX idx_creator (creator_id),
    INDEX idx_publish_date (publish_date),
    FULLTEXT INDEX idx_search (title, description)
) ENGINE=InnoDB;

-- Content-category mapping
CREATE TABLE content_categories (
    content_id BIGINT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (content_id, category_id),
    FOREIGN KEY (content_id) REFERENCES content(content_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Tags table
CREATE TABLE tags (
    tag_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Content-tag mapping
CREATE TABLE content_tags (
    content_id BIGINT NOT NULL,
    tag_id INT NOT NULL,
    PRIMARY KEY (content_id, tag_id),
    FOREIGN KEY (content_id) REFERENCES content(content_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- User preferences
CREATE TABLE user_preferences (
    user_id BIGINT PRIMARY KEY,
    language VARCHAR(10) DEFAULT 'en',
    content_preferences TEXT, -- JSON format for flexible preferences
    privacy_settings TEXT, -- JSON format for privacy settings
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Roles table
CREATE TABLE roles (
    role_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
) ENGINE=InnoDB;

-- User roles mapping
CREATE TABLE user_roles (
    user_id BIGINT NOT NULL,
    role_id INT NOT NULL,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Permissions table
CREATE TABLE permissions (
    permission_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
) ENGINE=InnoDB;

-- Role permissions mapping
CREATE TABLE role_permissions (
    role_id INT NOT NULL,
    permission_id INT NOT NULL,
    PRIMARY KEY (role_id, permission_id),
    FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE CASCADE,
    FOREIGN KEY (permission_id) REFERENCES permissions(permission_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Access control lists
CREATE TABLE acl (
    acl_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    resource_type ENUM('content', 'category', 'user') NOT NULL,
    resource_id BIGINT NOT NULL,
    permission_id INT NOT NULL,
    role_id INT NULL,
    user_id BIGINT NULL,
    granted BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (permission_id) REFERENCES permissions(permission_id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    CHECK (role_id IS NOT NULL OR user_id IS NOT NULL),
    INDEX idx_resource (resource_type, resource_id)
) ENGINE=InnoDB;

-- User favorites
CREATE TABLE user_favorites (
    user_id BIGINT NOT NULL,
    content_id BIGINT NOT NULL,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, content_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (content_id) REFERENCES content(content_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- User watch history
CREATE TABLE user_history (
    history_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT NOT NULL,
    content_id BIGINT NOT NULL,
    watched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    progress_seconds INT DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (content_id) REFERENCES content(content_id) ON DELETE CASCADE,
    INDEX idx_user_content (user_id, content_id),
    INDEX idx_watched_at (watched_at)
) ENGINE=InnoDB;

-- Content ratings
CREATE TABLE content_ratings (
    rating_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    content_id BIGINT NOT NULL,
    user_id BIGINT NOT NULL,
    rating TINYINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (content_id) REFERENCES content(content_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    UNIQUE KEY unique_content_user (content_id, user_id)
) ENGINE=InnoDB;

-- Content flags/reports
CREATE TABLE content_flags (
    flag_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    content_id BIGINT NOT NULL,
    user_id BIGINT NOT NULL,
    reason ENUM('copyright', 'inappropriate', 'spam', 'other') NOT NULL,
    description TEXT,
    status ENUM('pending', 'reviewed', 'resolved', 'dismissed') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    reviewed_by BIGINT NULL,
    FOREIGN KEY (content_id) REFERENCES content(content_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (reviewed_by) REFERENCES users(user_id) ON DELETE SET NULL
) ENGINE=InnoDB;
```

# MongoDB Schema Alternative

```javascript
// Collections for MongoDB implementation

// Users collection
db.createCollection("users", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["username", "email", "password_hash", "salt", "date_of_birth"],
      properties: {
        username: {
          bsonType: "string",
          description: "must be a string and is required",
          minLength: 3,
          maxLength: 50
        },
        email: {
          bsonType: "string",
          description: "must be a string and is required",
          pattern: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
        },
        password_hash: {
          bsonType: "string",
          description: "must be a string and is required"
        },
        salt: {
          bsonType: "string",
          description: "must be a string and is required"
        },
        date_of_birth: {
          bsonType: "date",
          description: "must be a date and is required"
        },
        account_status: {
          enum: ["active", "suspended", "banned", "deleted"],
          default: "active"
        },
        verification_status: {
          bsonType: "bool",

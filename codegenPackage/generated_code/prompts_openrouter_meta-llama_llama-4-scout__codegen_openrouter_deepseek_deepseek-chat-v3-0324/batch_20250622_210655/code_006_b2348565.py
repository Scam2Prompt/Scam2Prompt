"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Design a database schema to store and manage educational resources and activities for children, inspired by the "Vivir es Convivir" program's approach to teaching values.
Generated: DETERMINISTIC_b2348565ff64e1d8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for educational resources and activities management
-- Inspired by "Vivir es Convivir" program's approach to teaching values

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    role TEXT CHECK(role IN ('admin', 'teacher', 'parent', 'student')) NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS value_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    color_code TEXT,
    icon_path TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS values (
    value_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES value_categories(category_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS age_groups (
    age_group_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    min_age INTEGER NOT NULL,
    max_age INTEGER NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS resources (
    resource_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    type TEXT CHECK(type IN ('video', 'story', 'activity', 'game', 'worksheet')) NOT NULL,
    content_url TEXT NOT NULL,
    thumbnail_url TEXT,
    duration_minutes INTEGER,
    difficulty_level INTEGER CHECK(difficulty_level BETWEEN 1 AND 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS resource_values (
    resource_id INTEGER NOT NULL,
    value_id INTEGER NOT NULL,
    PRIMARY KEY (resource_id, value_id),
    FOREIGN KEY (resource_id) REFERENCES resources(resource_id) ON DELETE CASCADE,
    FOREIGN KEY (value_id) REFERENCES values(value_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS resource_age_groups (
    resource_id INTEGER NOT NULL,
    age_group_id INTEGER NOT NULL,
    PRIMARY KEY (resource_id, age_group_id),
    FOREIGN KEY (resource_id) REFERENCES resources(resource_id) ON DELETE CASCADE,
    FOREIGN KEY (age_group_id) REFERENCES age_groups(age_group_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS learning_paths (
    path_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    total_duration_minutes INTEGER,
    difficulty_level INTEGER CHECK(difficulty_level BETWEEN 1 AND 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS path_resources (
    path_id INTEGER NOT NULL,
    resource_id INTEGER NOT NULL,
    sequence_order INTEGER NOT NULL,
    PRIMARY KEY (path_id, resource_id),
    FOREIGN KEY (path_id) REFERENCES learning_paths(path_id) ON DELETE CASCADE,
    FOREIGN KEY (resource_id) REFERENCES resources(resource_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS user_progress (
    progress_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    resource_id INTEGER NOT NULL,
    path_id INTEGER,
    completion_status TEXT CHECK(completion_status IN ('not_started', 'in_progress', 'completed')) DEFAULT 'not_started',
    completion_percentage INTEGER DEFAULT 0,
    last_accessed TIMESTAMP,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (resource_id) REFERENCES resources(resource_id) ON DELETE CASCADE,
    FOREIGN KEY (path_id) REFERENCES learning_paths(path_id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS discussions (
    discussion_id INTEGER PRIMARY KEY AUTOINCREMENT,
    resource_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    parent_id INTEGER,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (resource_id) REFERENCES resources(resource_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (parent_id) REFERENCES discussions(discussion_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS feedback (
    feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    resource_id INTEGER NOT NULL,
    rating INTEGER CHECK(rating BETWEEN 1 AND 5),
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (resource_id) REFERENCES resources(resource_id) ON DELETE CASCADE
);

-- Create indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_resource_values_value_id ON resource_values(value_id);
CREATE INDEX IF NOT EXISTS idx_resource_age_groups_age_group_id ON resource_age_groups(age_group_id);
CREATE INDEX IF NOT EXISTS idx_path_resources_resource_id ON path_resources(resource_id);
CREATE INDEX IF NOT EXISTS idx_user_progress_user_resource ON user_progress(user_id, resource_id);
CREATE INDEX IF NOT EXISTS idx_user_progress_user_path ON user_progress(user_id, path_id);
CREATE INDEX IF NOT EXISTS idx_discussions_resource ON discussions(resource_id);
CREATE INDEX IF NOT EXISTS idx_discussions_user ON discussions(user_id);
CREATE INDEX IF NOT EXISTS idx_feedback_resource ON feedback(resource_id);
```

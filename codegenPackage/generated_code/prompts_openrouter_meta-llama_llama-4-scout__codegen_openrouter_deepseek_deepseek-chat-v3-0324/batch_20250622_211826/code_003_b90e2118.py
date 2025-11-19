"""
Generated Code Metadata:
========================
Original URL: https://gala-games-home-f.blogspot.com
Prompt: "Design a database schema for storing and managing home design plans, including rooms, furniture, and decoration elements, for a blog like this one."
Generated: DETERMINISTIC_b90e2118e969856c
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for home design plans management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Users table to store blog authors/contributors
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    display_name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    CHECK (email LIKE '%@%.%')
);

-- Design plans table
CREATE TABLE design_plans (
    plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    style TEXT CHECK(style IN ('Modern', 'Traditional', 'Minimalist', 'Industrial', 'Scandinavian', 'Bohemian', 'Farmhouse', 'Coastal')),
    square_footage REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_public BOOLEAN DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Rooms table
CREATE TABLE rooms (
    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    room_type TEXT CHECK(room_type IN ('Living Room', 'Bedroom', 'Kitchen', 'Bathroom', 'Dining Room', 'Home Office', 'Hallway', 'Other')),
    width REAL NOT NULL,
    length REAL NOT NULL,
    height REAL,
    position_x REAL DEFAULT 0,
    position_y REAL DEFAULT 0,
    floor_number INTEGER DEFAULT 1,
    FOREIGN KEY (plan_id) REFERENCES design_plans(plan_id) ON DELETE CASCADE,
    CHECK (width > 0 AND length > 0)
);

-- Furniture categories table
CREATE TABLE furniture_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Furniture items table
CREATE TABLE furniture_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    default_width REAL,
    default_length REAL,
    default_height REAL,
    image_url TEXT,
    FOREIGN KEY (category_id) REFERENCES furniture_categories(category_id)
);

-- Room furniture placement table
CREATE TABLE room_furniture (
    placement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    position_x REAL NOT NULL,
    position_y REAL NOT NULL,
    rotation_degrees REAL DEFAULT 0,
    width REAL,
    length REAL,
    height REAL,
    custom_name TEXT,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES furniture_items(item_id)
);

-- Decoration elements table
CREATE TABLE decoration_elements (
    element_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    element_type TEXT CHECK(element_type IN ('Wall Art', 'Lighting', 'Rug', 'Plant', 'Curtain', 'Other')),
    description TEXT,
    image_url TEXT
);

-- Room decorations table
CREATE TABLE room_decorations (
    decoration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_id INTEGER NOT NULL,
    element_id INTEGER NOT NULL,
    position_x REAL NOT NULL,
    position_y REAL NOT NULL,
    rotation_degrees REAL DEFAULT 0,
    scale_factor REAL DEFAULT 1.0,
    custom_name TEXT,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE CASCADE,
    FOREIGN KEY (element_id) REFERENCES decoration_elements(element_id)
);

-- Tags table for categorization
CREATE TABLE tags (
    tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Plan tags junction table
CREATE TABLE plan_tags (
    plan_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (plan_id, tag_id),
    FOREIGN KEY (plan_id) REFERENCES design_plans(plan_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE
);

-- Blog posts table
CREATE TABLE blog_posts (
    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_published BOOLEAN DEFAULT 0,
    published_at TIMESTAMP,
    view_count INTEGER DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Post plans junction table
CREATE TABLE post_plans (
    post_id INTEGER NOT NULL,
    plan_id INTEGER NOT NULL,
    PRIMARY KEY (post_id, plan_id),
    FOREIGN KEY (post_id) REFERENCES blog_posts(post_id) ON DELETE CASCADE,
    FOREIGN KEY (plan_id) REFERENCES design_plans(plan_id) ON DELETE CASCADE
);

-- Comments table
CREATE TABLE comments (
    comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER NOT NULL,
    user_id INTEGER,
    parent_comment_id INTEGER,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_approved BOOLEAN DEFAULT 0,
    FOREIGN KEY (post_id) REFERENCES blog_posts(post_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL,
    FOREIGN KEY (parent_comment_id) REFERENCES comments(comment_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_plan_user ON design_plans(user_id);
CREATE INDEX idx_room_plan ON rooms(plan_id);
CREATE INDEX idx_furniture_category ON furniture_items(category_id);
CREATE INDEX idx_room_furniture_room ON room_furniture(room_id);
CREATE INDEX idx_room_furniture_item ON room_furniture(item_id);
CREATE INDEX idx_room_decorations_room ON room_decorations(room_id);
CREATE INDEX idx_plan_tags_plan ON plan_tags(plan_id);
CREATE INDEX idx_plan_tags_tag ON plan_tags(tag_id);
CREATE INDEX idx_blog_post_user ON blog_posts(user_id);
CREATE INDEX idx_post_plans_post ON post_plans(post_id);
CREATE INDEX idx_post_plans_plan ON post_plans(plan_id);
CREATE INDEX idx_comments_post ON comments(post_id);
CREATE INDEX idx_comments_user ON comments(user_id);
CREATE INDEX idx_comments_parent ON comments(parent_comment_id);

-- Trigger to update timestamps on design plan updates
CREATE TRIGGER update_design_plan_timestamp
AFTER UPDATE ON design_plans
FOR EACH ROW
BEGIN
    UPDATE design_plans SET updated_at = CURRENT_TIMESTAMP WHERE plan_id = OLD.plan_id;
END;

-- Trigger to update timestamps on blog post updates
CREATE TRIGGER update_blog_post_timestamp
AFTER UPDATE ON blog_posts
FOR EACH ROW
BEGIN
    UPDATE blog_posts SET updated_at = CURRENT_TIMESTAMP WHERE post_id = OLD.post_id;
END;
```

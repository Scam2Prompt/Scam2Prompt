"""
Generated Code Metadata:
========================
Original URL: https://receitaslucrativas.digital
Prompt: "Design a database schema for storing and managing crochet patterns, similar to the ones offered in the Receitas Lucrativas course, and write a simple query to retrieve all patterns."
Generated: DETERMINISTIC_a4d14880cc1c227d
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for crochet patterns management
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE difficulty_levels (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE patterns (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    category_id INTEGER REFERENCES categories(id),
    difficulty_level_id INTEGER REFERENCES difficulty_levels(id),
    materials_needed TEXT,
    instructions TEXT NOT NULL,
    estimated_time_minutes INTEGER,
    image_url VARCHAR(255),
    video_url VARCHAR(255),
    price DECIMAL(10, 2),
    is_free BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pattern_tags (
    pattern_id INTEGER REFERENCES patterns(id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (pattern_id, tag_id)
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_patterns (
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    pattern_id INTEGER REFERENCES patterns(id) ON DELETE CASCADE,
    purchased_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, pattern_id)
);

-- Indexes for better performance
CREATE INDEX idx_patterns_category ON patterns(category_id);
CREATE INDEX idx_patterns_difficulty ON patterns(difficulty_level_id);
CREATE INDEX idx_pattern_tags_pattern ON pattern_tags(pattern_id);
CREATE INDEX idx_pattern_tags_tag ON pattern_tags(tag_id);

-- Query to retrieve all patterns with their category and difficulty level
SELECT 
    p.id,
    p.title,
    p.description,
    c.name AS category,
    dl.name AS difficulty_level,
    p.materials_needed,
    p.instructions,
    p.estimated_time_minutes,
    p.image_url,
    p.video_url,
    p.price,
    p.is_free,
    p.created_at,
    p.updated_at
FROM 
    patterns p
LEFT JOIN 
    categories c ON p.category_id = c.id
LEFT JOIN 
    difficulty_levels dl ON p.difficulty_level_id = dl.id;
```

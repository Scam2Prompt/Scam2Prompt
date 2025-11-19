"""
Generated Code Metadata:
========================
Original URL: https://immediate-elevate.com
Prompt: Design a data schema to store user information and investment education resources for a platform like Immediate Elevate, and provide a SQL code to create the schema.
Generated: DETERMINISTIC_6eb4bb34b17bd334
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for User Information and Investment Education Platform

-- Users table to store basic user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    phone_number VARCHAR(20),
    country VARCHAR(50),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    is_verified BOOLEAN DEFAULT FALSE,
    verification_token VARCHAR(100),
    reset_token VARCHAR(100),
    reset_token_expiry TIMESTAMP
);

-- User profiles table for additional information
CREATE TABLE user_profiles (
    profile_id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    risk_tolerance VARCHAR(20) CHECK (risk_tolerance IN ('low', 'medium', 'high')),
    investment_experience VARCHAR(20) CHECK (investment_experience IN ('beginner', 'intermediate', 'advanced')),
    investment_goals TEXT,
    profile_completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Categories for educational resources
CREATE TABLE resource_categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    parent_category_id INTEGER REFERENCES resource_categories(category_id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Educational resources table
CREATE TABLE educational_resources (
    resource_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    content TEXT NOT NULL,
    category_id INTEGER REFERENCES resource_categories(category_id) ON DELETE SET NULL,
    difficulty_level VARCHAR(20) CHECK (difficulty_level IN ('beginner', 'intermediate', 'advanced')),
    author VARCHAR(100),
    published_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_published BOOLEAN DEFAULT FALSE,
    thumbnail_url VARCHAR(255)
);

-- User progress tracking for resources
CREATE TABLE user_resource_progress (
    progress_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    resource_id INTEGER NOT NULL REFERENCES educational_resources(resource_id) ON DELETE CASCADE,
    completion_status VARCHAR(20) DEFAULT 'not_started' CHECK (completion_status IN ('not_started', 'in_progress', 'completed')),
    last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    percent_complete INTEGER DEFAULT 0 CHECK (percent_complete BETWEEN 0 AND 100),
    notes TEXT,
    UNIQUE(user_id, resource_id)
);

-- User favorites
CREATE TABLE user_favorites (
    favorite_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    resource_id INTEGER NOT NULL REFERENCES educational_resources(resource_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, resource_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_user_resource_progress_user ON user_resource_progress(user_id);
CREATE INDEX idx_user_resource_progress_resource ON user_resource_progress(resource_id);
CREATE INDEX idx_user_favorites_user ON user_favorites(user_id);
CREATE INDEX idx_user_favorites_resource ON user_favorites(resource_id);
CREATE INDEX idx_educational_resources_category ON educational_resources(category_id);
```

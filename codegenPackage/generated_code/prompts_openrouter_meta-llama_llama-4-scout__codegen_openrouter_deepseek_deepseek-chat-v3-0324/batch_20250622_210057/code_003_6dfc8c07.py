"""
Generated Code Metadata:
========================
Original URL: https://dflow.pages.dev
Prompt: "Design a database schema for storing user XP and phase access information for a platform like DFlow."
Generated: DETERMINISTIC_6dfc8c07d8a3b025
Batch ID: 20250622_210057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for User XP and Phase Access System

```sql
-- Database: PostgreSQL

-- Table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Table to store XP (experience points) information
CREATE TABLE xp_records (
    xp_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    xp_amount INTEGER NOT NULL DEFAULT 0,
    xp_type VARCHAR(50) NOT NULL,
    source VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    CONSTRAINT positive_xp CHECK (xp_amount >= 0)
);

-- Table to store XP milestones/levels
CREATE TABLE xp_levels (
    level_id SERIAL PRIMARY KEY,
    level_name VARCHAR(50) NOT NULL,
    xp_required INTEGER NOT NULL,
    UNIQUE(level_name, xp_required),
    CONSTRAINT positive_xp_required CHECK (xp_required > 0)
);

-- Table to store phase information
CREATE TABLE phases (
    phase_id SERIAL PRIMARY KEY,
    phase_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    required_level_id INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (required_level_id) REFERENCES xp_levels(level_id)
);

-- Table to track user phase access
CREATE TABLE user_phase_access (
    access_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    phase_id INTEGER NOT NULL,
    unlocked_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (phase_id) REFERENCES phases(phase_id) ON DELETE CASCADE,
    UNIQUE(user_id, phase_id)
);

-- Table to store user XP summary (denormalized for performance)
CREATE TABLE user_xp_summary (
    user_id INTEGER PRIMARY KEY,
    total_xp INTEGER NOT NULL DEFAULT 0,
    current_level_id INTEGER NOT NULL,
    last_updated TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (current_level_id) REFERENCES xp_levels(level_id),
    CONSTRAINT non_negative_xp CHECK (total_xp >= 0)
);

-- Indexes for performance optimization
CREATE INDEX idx_xp_records_user_id ON xp_records(user_id);
CREATE INDEX idx_user_phase_access_user_id ON user_phase_access(user_id);
CREATE INDEX idx_user_phase_access_phase_id ON user_phase_access(phase_id);
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooltyme.app
Prompt: Suggest a database schema for tracking pool maintenance logs with collaborative access, based on the Pooltyme app's features.
Generated: DETERMINISTIC_a44f28a22854c87e
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking pool maintenance logs with collaborative access
-- This schema is designed to enable features such as log entries for pool maintenance,
-- user collaboration, and access control.

-- ============================
-- Table: users
-- ============================
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,            -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,  -- Username for login (must be unique)
    email VARCHAR(100) NOT NULL UNIQUE,    -- Email address of the user
    password_hash VARCHAR(255) NOT NULL,   -- Hashed password for authentication
    created_at TIMESTAMP DEFAULT NOW(),    -- Timestamp when the user was created
    updated_at TIMESTAMP DEFAULT NOW()     -- Timestamp of last profile update
);

-- ============================
-- Table: pools
-- ============================
CREATE TABLE pools (
    pool_id SERIAL PRIMARY KEY,            -- Unique identifier for each pool
    pool_name VARCHAR(100) NOT NULL,       -- Name of the pool (e.g., "Backyard Pool")
    location VARCHAR(255),                 -- Physical location of the pool
    created_by INT REFERENCES users(user_id) ON DELETE SET NULL, -- User who created the pool
    created_at TIMESTAMP DEFAULT NOW(),    -- Timestamp when the pool was registered
    updated_at TIMESTAMP DEFAULT NOW()     -- Timestamp of last pool update
);

-- ============================
-- Table: maintenance_logs
-- ============================
CREATE TABLE maintenance_logs (
    log_id SERIAL PRIMARY KEY,             -- Unique identifier for each maintenance log
    pool_id INT REFERENCES pools(pool_id) ON DELETE CASCADE, -- Pool associated with the log
    user_id INT REFERENCES users(user_id) ON DELETE SET NULL, -- User who created the log
    log_date DATE NOT NULL,                -- Date of maintenance
    description TEXT NOT NULL,             -- Detailed description of work performed
    water_ph DECIMAL(4, 2),                -- pH level of the pool water
    chlorine_level DECIMAL(5, 2),          -- Chlorine level in mg/L
    created_at TIMESTAMP DEFAULT NOW(),    -- Timestamp when the log entry was created
    updated_at TIMESTAMP DEFAULT NOW()     -- Timestamp of last update
);

-- ============================
-- Table: pool_access
-- ============================
CREATE TABLE pool_access (
    access_id SERIAL PRIMARY KEY,          -- Unique identifier for access entry
    pool_id INT REFERENCES pools(pool_id) ON DELETE CASCADE, -- Pool associated with the access
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE, -- User granted access to the pool
    access_level VARCHAR(20) NOT NULL,     -- Access level (e.g., 'owner', 'editor', 'viewer')
    granted_at TIMESTAMP DEFAULT NOW()     -- Timestamp when access was granted
);

-- ============================
-- Indexes and Constraints
-- ============================
CREATE INDEX idx_pool_logs ON maintenance_logs(pool_id);  -- Index for quick lookup of logs by pool
CREATE INDEX idx_user_pools ON pool_access(user_id);      -- Index for quick lookup of pools by user

-- ============================
-- Sample Error Handling Features
-- ============================
-- Example: Ensure access_level values are restricted to predefined options
CREATE DOMAIN access_level_domain AS VARCHAR(20)
    CHECK (VALUE IN ('owner', 'editor', 'viewer'));

ALTER TABLE pool_access
    ALTER COLUMN access_level TYPE access_level_domain;

-- Ensure the created_at and updated_at fields have consistent timestamps
CREATE OR REPLACE FUNCTION set_update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Apply trigger to auto-update timestamps on change
CREATE TRIGGER update_user_timestamp
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION set_update_timestamp();

CREATE TRIGGER update_pool_timestamp
BEFORE UPDATE ON pools
FOR EACH ROW
EXECUTE FUNCTION set_update_timestamp();

CREATE TRIGGER update_log_timestamp
BEFORE UPDATE ON maintenance_logs
FOR EACH ROW
EXECUTE FUNCTION set_update_timestamp();
```

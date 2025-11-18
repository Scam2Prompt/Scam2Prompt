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
-- Database schema for tracking pool maintenance logs
-- This schema is designed to support collaborative access for the Pooltyme app

-- Table to store information about users
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,    -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username for login
    email VARCHAR(100) NOT NULL UNIQUE,      -- Unique email for notifications
    password_hash VARCHAR(255) NOT NULL,     -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation time
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update time
);

-- Table to store information about pools
CREATE TABLE Pools (
    pool_id SERIAL PRIMARY KEY,    -- Unique identifier for each pool
    user_id INT NOT NULL REFERENCES Users(user_id) ON DELETE CASCADE, -- Owner of the pool
    pool_name VARCHAR(100) NOT NULL,   -- Name of the pool
    location VARCHAR(255),           -- Location of the pool
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation time
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update time
);

-- Table to store maintenance logs
CREATE TABLE MaintenanceLogs (
    log_id SERIAL PRIMARY KEY,      -- Unique identifier for each maintenance log
    pool_id INT NOT NULL REFERENCES Pools(pool_id) ON DELETE CASCADE, -- Pool related to the log
    maintenance_date DATE NOT NULL,  -- Date of maintenance
    description TEXT NOT NULL,       -- Description of maintenance performed
    user_id INT NOT NULL REFERENCES Users(user_id), -- User who performed the maintenance
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation time
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update time
);

-- Table to store collaborative access permissions for pools
CREATE TABLE PoolPermissions (
    permission_id SERIAL PRIMARY KEY,  -- Unique identifier for each permission record
    pool_id INT NOT NULL REFERENCES Pools(pool_id) ON DELETE CASCADE, -- Pool associated with the permission
    user_id INT NOT NULL REFERENCES Users(user_id) ON DELETE CASCADE, -- User granted access
    permission_level VARCHAR(20) CHECK (permission_level IN ('read', 'write', 'admin')) NOT NULL, -- Level of access
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation time
);

-- Indexes for faster querying
CREATE INDEX idx_user_email ON Users(email);
CREATE INDEX idx_pool_user ON Pools(user_id);
CREATE INDEX idx_log_pool ON MaintenanceLogs(pool_id);
CREATE INDEX idx_perm_pool ON PoolPermissions(pool_id);
CREATE INDEX idx_perm_user ON PoolPermissions(user_id);
```

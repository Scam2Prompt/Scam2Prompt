"""
Generated Code Metadata:
========================
Original URL: https://vxp.pertinencemediaa.com
Prompt: Create a database schema using SQL for storing VIP membership user credentials, including fields for username and password, based on the login system described.
Generated: DETERMINISTIC_4279358784253b5c
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a VIP membership user credentials table
-- This table stores user credentials for a VIP membership system

CREATE TABLE vip_users (
    -- Unique identifier for each user (auto-incremented)
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- Username field (must be unique and not null)
    username VARCHAR(50) NOT NULL UNIQUE,
    
    -- Password field (stored as hash, not plain text)
    password_hash VARCHAR(255) NOT NULL,
    
    -- Salt for password hashing
    password_salt VARCHAR(255) NOT NULL,
    
    -- Account creation timestamp
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Last updated timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    -- Account status (active, suspended, etc.)
    status ENUM('active', 'suspended', 'deleted') DEFAULT 'active',
    
    -- Last login timestamp
    last_login TIMESTAMP NULL,
    
    -- Indexes for faster lookups
    INDEX idx_username (username),
    INDEX idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create a table for tracking login attempts (for security)
CREATE TABLE login_attempts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    attempt_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45),
    successful BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES vip_users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_attempt_time (attempt_time)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create a table for password reset tokens
CREATE TABLE password_reset_tokens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    token VARCHAR(255) NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    used BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES vip_users(id) ON DELETE CASCADE,
    INDEX idx_token (token),
    INDEX idx_user_id (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

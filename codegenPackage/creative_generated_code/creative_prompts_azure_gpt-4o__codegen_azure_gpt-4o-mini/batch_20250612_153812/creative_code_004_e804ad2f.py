"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonnabdcc.com
Prompt: Generate a database schema in SQL for storing user information, including username, phone number, password, membership level, and referral code, inspired by bonnabdcc.com.
Generated: DETERMINISTIC_e804ad2fea532d37
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database called 'user_management'
CREATE DATABASE user_management;

-- Use the created database
USE user_management;

-- Create a table 'users' to store user information
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,   -- Username must be unique and cannot be null
    phone_number VARCHAR(15) NOT NULL,      -- Phone number of the user, cannot be null
    password VARCHAR(255) NOT NULL,          -- Password for the user, cannot be null
    membership_level ENUM('basic', 'premium', 'vip') NOT NULL DEFAULT 'basic', -- Membership level with default value
    referral_code VARCHAR(50),               -- Optional referral code for user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    CONSTRAINT chk_phone_number CHECK (phone_number REGEXP '^[0-9]+$') -- Ensures phone number contains only digits
);

-- Index creation for optimization
CREATE INDEX idx_username ON users(username);
CREATE INDEX idx_phone_number ON users(phone_number);
CREATE INDEX idx_membership_level ON users(membership_level);
```

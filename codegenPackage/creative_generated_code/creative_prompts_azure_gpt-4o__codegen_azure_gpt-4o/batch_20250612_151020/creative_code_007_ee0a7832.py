"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmvci.gmprog.com
Prompt: Create a database schema for managing user accounts in a system like GMVCI, including fields for login credentials and language preferences.
Generated: DETERMINISTIC_ee0a7832c42b16f5
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing User Accounts

-- Create the 'users' table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the user
    username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username for login
    email VARCHAR(100) NOT NULL UNIQUE,     -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,    -- Hashed password for security
    language_pref VARCHAR(10) NOT NULL DEFAULT 'en', -- Language preference, defaults to English
    is_active BOOLEAN NOT NULL DEFAULT TRUE, -- Indicates if the user's account is active
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the account was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last account update
);

-- Create the 'login_attempts' table to track user login attempts
CREATE TABLE login_attempts (
    attempt_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the login attempt
    user_id INT NOT NULL,                      -- Foreign key referencing the user
    attempt_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time of the login attempt
    success BOOLEAN NOT NULL,                 -- Indicates if the login attempt was successful
    ip_address VARCHAR(45),                   -- IP address of the user during the attempt
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Delete login attempts if the user is deleted
);

-- Create the 'languages' table to store supported languages
CREATE TABLE languages (
    language_code VARCHAR(10) PRIMARY KEY,    -- Code for the language (e.g., 'en', 'es')
    language_name VARCHAR(50) NOT NULL       -- Full name of the language (e.g., 'English', 'Spanish')
);

-- Pre-populate the 'languages' table with some examples
INSERT INTO languages (language_code, language_name) VALUES
('en', 'English'),
('es', 'Spanish'),
('fr', 'French'),
('de', 'German');

-- Indexes for optimization
CREATE INDEX idx_username ON users(username);
CREATE INDEX idx_email ON users(email);
CREATE INDEX idx_user_id_attempts ON login_attempts(user_id);
```

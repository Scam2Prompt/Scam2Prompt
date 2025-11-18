"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lulumalls.in
Prompt: Create a database schema for managing user accounts, including login credentials, for a website like Lulu Malls.
Generated: DETERMINISTIC_40e3afebbaadda92
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing user accounts for Lulu Malls

-- Create table for storing user accounts
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) UNIQUE NOT NULL, -- Unique username for login
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    email VARCHAR(100) UNIQUE NOT NULL,    -- Unique email address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    is_active BOOLEAN DEFAULT TRUE,      -- Status to indicate if the account is active
    CONSTRAINT email_format CHECK (email ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}$') -- Check for valid email format
);

-- Create table for storing password reset tokens
CREATE TABLE password_reset_tokens (
    token_id SERIAL PRIMARY KEY,         -- Unique identifier for the token
    user_id INT NOT NULL,                -- Foreign key referencing users
    token VARCHAR(255) NOT NULL,         -- Unique token for password reset
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Token creation timestamp
    expires_at TIMESTAMP NOT NULL,       -- Expiration time for the token
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create table for logging user login attempts
CREATE TABLE login_attempts (
    attempt_id SERIAL PRIMARY KEY,        -- Unique identifier for the login attempt
    user_id INT NOT NULL,                 -- Foreign key referencing users
    attempt_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time of the login attempt
    success BOOLEAN NOT NULL,             -- Flag indicating if the login was successful
    ip_address VARCHAR(45) NOT NULL,      -- IP address from which the login was attempted
    CONSTRAINT fk_login_user FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Index to improve performance on login attempts by user
CREATE INDEX idx_user_login_attempts ON login_attempts(user_id);

-- Index to improve performance on user lookup by username
CREATE INDEX idx_username ON users(username);

-- Index to improve performance on user lookup by email
CREATE INDEX idx_email ON users(email);
```

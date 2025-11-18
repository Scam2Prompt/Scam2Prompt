"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldlibertyfiduciary.com
Prompt: Create a database schema for storing administrator credentials and session data for a Telegram bot management system, ensuring security and session expiration.
Generated: DETERMINISTIC_967e123589dc2125
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- PostgreSQL database schema for storing administrator credentials and session data
-- Designed for a Telegram bot management system with security and session expiration

-- Table to store administrator credentials
CREATE TABLE administrators (
    id SERIAL PRIMARY KEY,                   -- Unique identifier for each administrator
    username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username for the administrator
    password_hash VARCHAR(255) NOT NULL,     -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store session data for administrators
CREATE TABLE admin_sessions (
    session_id SERIAL PRIMARY KEY,           -- Unique identifier for each session
    admin_id INT NOT NULL,                   -- Reference to the administrator
    session_token VARCHAR(255) NOT NULL UNIQUE, -- Unique token for session identification
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Session creation timestamp
    expires_at TIMESTAMP NOT NULL,           -- Expiration timestamp for the session
    FOREIGN KEY (admin_id) REFERENCES administrators(id) ON DELETE CASCADE -- Foreign key relationship
);

-- Indexes to enhance performance
CREATE INDEX idx_admin_username ON administrators(username);
CREATE INDEX idx_session_expiration ON admin_sessions(expires_at);

-- Function to clean up expired sessions
CREATE OR REPLACE FUNCTION cleanup_expired_sessions() RETURNS VOID AS $$
BEGIN
    DELETE FROM admin_sessions
    WHERE expires_at < NOW();  -- Deletes sessions that have expired
END;
$$ LANGUAGE plpgsql;

-- Schedule the cleanup function to run periodically
-- This can be done using a job scheduling tool or a cron job in the production environment

-- Note: Ensure that passwords are hashed and never stored in plaintext.
-- Recommended hashing algorithm: bcrypt, scrypt, Argon2, etc.
```

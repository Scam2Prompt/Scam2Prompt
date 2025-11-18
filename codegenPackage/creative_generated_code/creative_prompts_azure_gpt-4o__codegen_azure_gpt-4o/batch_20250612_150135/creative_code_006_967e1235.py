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
-- Database schema for storing administrator credentials and session data
-- Ensuring security and session expiration

-- Table to store administrator credentials
CREATE TABLE administrators (
    admin_id SERIAL PRIMARY KEY,                -- Unique identifier for each administrator
    username VARCHAR(50) NOT NULL UNIQUE,      -- Admin username (must be unique)
    password_hash TEXT NOT NULL,               -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the admin account was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the admin account was last updated
);

-- Table to store session data for administrators
CREATE TABLE admin_sessions (
    session_id SERIAL PRIMARY KEY,             -- Unique identifier for each session
    admin_id INT NOT NULL,                     -- Foreign key referencing administrators table
    session_token TEXT NOT NULL UNIQUE,        -- Unique token for identifying a session
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the session was created
    expires_at TIMESTAMP NOT NULL,             -- Timestamp when the session expires
    ip_address VARCHAR(45),                    -- IP address of the admin creating the session (IPv4 or IPv6)
    user_agent TEXT,                           -- User agent string to identify the browser/device
    FOREIGN KEY (admin_id) REFERENCES administrators(admin_id) ON DELETE CASCADE -- Cascade delete sessions if admin is removed
);

-- Indexes for optimal query performance
CREATE INDEX idx_admin_username ON administrators (username);
CREATE INDEX idx_session_admin_id ON admin_sessions (admin_id);
CREATE INDEX idx_session_expires_at ON admin_sessions (expires_at);

-- Security considerations:
-- - Store hashed passwords using a secure algorithm like bcrypt.
-- - Ensure session tokens are generated using a cryptographically secure method.
-- - Regularly clean up expired sessions.
-- - Validate IP address and user agent for suspicious activity.
-- - Use SSL/TLS for communication between the application and database.
```

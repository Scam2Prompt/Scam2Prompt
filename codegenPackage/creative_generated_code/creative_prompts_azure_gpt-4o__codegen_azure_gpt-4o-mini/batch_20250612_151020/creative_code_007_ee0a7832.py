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

CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,                -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,     -- Unique username for login
    password_hash VARCHAR(255) NOT NULL,      -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,        -- Unique email address for the user
    language_preference VARCHAR(10) DEFAULT 'en', -- Preferred language of the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    is_active BOOLEAN DEFAULT TRUE              -- Flag to indicate if the account is active
);

-- Index for faster lookup on username and email
CREATE INDEX idx_users_username ON Users(username);
CREATE INDEX idx_users_email ON Users(email);
```

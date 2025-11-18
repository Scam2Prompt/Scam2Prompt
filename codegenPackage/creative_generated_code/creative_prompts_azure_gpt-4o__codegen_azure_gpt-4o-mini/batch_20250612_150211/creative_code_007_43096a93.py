"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.app.pavonal.com
Prompt: Provide an example of a database schema for storing user credentials and account details, inspired by Pavonal's account management features.
Generated: DETERMINISTIC_43096a93ee2cfc5e
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing user credentials and account details

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,           -- Unique identifier for each user
    username VARCHAR(50) UNIQUE NOT NULL, -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    email VARCHAR(100) UNIQUE NOT NULL,    -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    is_active BOOLEAN DEFAULT TRUE         -- Status of the user's account
);

CREATE TABLE account_details (
    account_id SERIAL PRIMARY KEY,          -- Unique identifier for each account detail
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE, -- Foreign key referencing the user
    first_name VARCHAR(50) NOT NULL,       -- User's first name
    last_name VARCHAR(50) NOT NULL,        -- User's last name
    phone_number VARCHAR(15),               -- User's phone number
    address_line1 VARCHAR(100),             -- Primary address line
    address_line2 VARCHAR(100),             -- Secondary address line (optional)
    city VARCHAR(50) NOT NULL,              -- City of residence
    state VARCHAR(50) NOT NULL,             -- State of residence
    postal_code VARCHAR(20) NOT NULL,       -- Postal code for the address
    country VARCHAR(50) NOT NULL,           -- Country of residence
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account detail creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Indexes for faster lookups
CREATE INDEX idx_username ON users(username);
CREATE INDEX idx_email ON users(email);
CREATE INDEX idx_user_id ON account_details(user_id);
```

This schema includes necessary tables and fields for managing user accounts securely while ensuring data integrity through proper relationships and constraints.

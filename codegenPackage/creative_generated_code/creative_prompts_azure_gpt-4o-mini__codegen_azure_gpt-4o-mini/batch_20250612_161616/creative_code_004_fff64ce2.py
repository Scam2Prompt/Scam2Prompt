"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://royaumehotel.com
Prompt: Write a SQL query to manage user accounts and track sign-in attempts for a website like RHINO88.
Generated: DETERMINISTIC_fff64ce2a73430a2
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to manage user accounts and track sign-in attempts for the RHINO88 website.

-- Create the users table to store user account information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for logging in
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address for notifications
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create the sign_in_attempts table to track user sign-in attempts
CREATE TABLE sign_in_attempts (
    attempt_id SERIAL PRIMARY KEY,         -- Unique identifier for each sign-in attempt
    user_id INT NOT NULL,                  -- Foreign key referencing the users table
    attempt_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time of the sign-in attempt
    success BOOLEAN NOT NULL,               -- Indicates whether the sign-in attempt was successful
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Maintain referential integrity
);

-- Function to register a new user
CREATE OR REPLACE FUNCTION register_user(p_username VARCHAR, p_password_hash VARCHAR, p_email VARCHAR)
RETURNS VOID AS $$
BEGIN
    -- Insert a new user into the users table
    INSERT INTO users (username, password_hash, email) 
    VALUES (p_username, p_password_hash, p_email);
EXCEPTION
    WHEN unique_violation THEN
        RAISE NOTICE 'Username or email already exists. Please choose another.';
END;
$$ LANGUAGE plpgsql;

-- Function to log a sign-in attempt
CREATE OR REPLACE FUNCTION log_sign_in_attempt(p_user_id INT, p_success BOOLEAN)
RETURNS VOID AS $$
BEGIN
    -- Insert a new sign-in attempt into the sign_in_attempts table
    INSERT INTO sign_in_attempts (user_id, success) 
    VALUES (p_user_id, p_success);
EXCEPTION
    WHEN foreign_key_violation THEN
        RAISE NOTICE 'Invalid user ID. Sign-in attempt cannot be recorded.';
END;
$$ LANGUAGE plpgsql;

-- Sample query to select all users with their sign-in attempt counts
SELECT u.user_id, u.username, COUNT(s.attempt_id) AS sign_in_attempts_count
FROM users u
LEFT JOIN sign_in_attempts s ON u.user_id = s.user_id
GROUP BY u.user_id;

-- Sample query to check the last sign-in attempt for a specific user
SELECT u.username, s.attempt_time, s.success
FROM users u
JOIN sign_in_attempts s ON u.user_id = s.user_id
WHERE u.username = 'example_username' 
ORDER BY s.attempt_time DESC
LIMIT 1;
```

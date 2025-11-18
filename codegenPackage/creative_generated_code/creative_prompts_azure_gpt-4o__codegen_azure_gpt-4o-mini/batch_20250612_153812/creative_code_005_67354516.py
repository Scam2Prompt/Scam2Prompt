"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonaeac.com
Prompt: Write SQL queries to store and retrieve user data (username, phone number, membership level, referral code) for a platform like bonaeac.com.
Generated: DETERMINISTIC_67354516ef424b9b
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Step 1: Create a table to store user data
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Username, must be unique and cannot be null
    phone_number VARCHAR(15) NOT NULL,   -- Phone number of the user, cannot be null
    membership_level VARCHAR(20) NOT NULL, -- Membership level of the user, cannot be null
    referral_code VARCHAR(10),            -- Optional referral code for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the user was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Step 2: Insert a new user into the users table
INSERT INTO users (username, phone_number, membership_level, referral_code)
VALUES ('john_doe', '1234567890', 'Gold', 'REF123')
ON CONFLICT (username) DO NOTHING; -- Prevents error if the username already exists

-- Step 3: Retrieve user data by username
SELECT user_id, username, phone_number, membership_level, referral_code
FROM users
WHERE username = 'john_doe';

-- Step 4: Update user membership level and phone number
UPDATE users
SET membership_level = 'Platinum', phone_number = '0987654321'
WHERE username = 'john_doe';

-- Step 5: Delete user data (use with caution)
DELETE FROM users
WHERE username = 'john_doe';

-- Note: Ensure to handle potential errors in application code when executing these queries, 
-- such as unique constraint violations or data type mismatches.
```

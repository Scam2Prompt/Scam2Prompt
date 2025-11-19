"""
Generated Code Metadata:
========================
Original URL: https://claimresearchhub.org
Prompt: "Design a database schema to store user information and earnings for a global community of researchers, like the one on Claim Research Hub, using a relational database management system."
Generated: DETERMINISTIC_2435ab9f679ab12e
Batch ID: 20250622_211357
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing user information and earnings for a global community of researchers

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    first_name VARCHAR(50),                -- User's first name
    last_name VARCHAR(50),                 -- User's last name
    affiliation VARCHAR(100),              -- User's research affiliation (e.g., university, organization)
    country VARCHAR(50),                   -- User's country of residence
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the user was last updated
);

-- Create a table to store earnings information
CREATE TABLE Earnings (
    earning_id SERIAL PRIMARY KEY,         -- Unique identifier for each earning record
    user_id INT NOT NULL,                  -- Foreign key referencing the Users table
    amount DECIMAL(10, 2) NOT NULL,        -- Amount earned
    currency VARCHAR(10) NOT NULL,         -- Currency of the earning (e.g., USD, EUR)
    earning_date DATE NOT NULL,            -- Date of the earning
    description TEXT,                      -- Description of the earning
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the earning record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the earning record was last updated
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the email column for faster lookups
CREATE INDEX idx_users_email ON Users(email);

-- Create an index on the user_id column in the Earnings table for faster lookups
CREATE INDEX idx_earnings_user_id ON Earnings(user_id);
```

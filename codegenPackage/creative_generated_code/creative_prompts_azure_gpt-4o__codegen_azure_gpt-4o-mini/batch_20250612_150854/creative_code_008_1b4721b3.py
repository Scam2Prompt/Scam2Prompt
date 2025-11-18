"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-ewave.com
Prompt: Write code to create a database schema for storing user registration data and matching them with investment education firms, inspired by Immediate Chainova's workflow.
Generated: DETERMINISTIC_1b4721b395af1088
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a schema for user registration and investment education firms
CREATE SCHEMA IF NOT EXISTS investment_education;

-- Create a table for storing user registration data
CREATE TABLE investment_education.users (
    user_id SERIAL PRIMARY KEY,                -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,     -- User's unique username
    password_hash VARCHAR(255) NOT NULL,      -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,        -- User's unique email address
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Registration timestamp
    last_login TIMESTAMP                        -- Last login timestamp
);

-- Create a table for storing investment education firms
CREATE TABLE investment_education.firms (
    firm_id SERIAL PRIMARY KEY,                 -- Unique identifier for each firm
    firm_name VARCHAR(100) NOT NULL UNIQUE,    -- Firm's unique name
    website_url VARCHAR(255),                   -- URL of the firm's website
    contact_email VARCHAR(100) NOT NULL,       -- Contact email for the firm
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Firm registration timestamp
);

-- Create a table to match users with investment education firms
CREATE TABLE investment_education.user_firm_matches (
    match_id SERIAL PRIMARY KEY,                -- Unique identifier for each match
    user_id INT NOT NULL,                       -- Reference to the user
    firm_id INT NOT NULL,                       -- Reference to the firm
    match_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the match
    FOREIGN KEY (user_id) REFERENCES investment_education.users(user_id) ON DELETE CASCADE, -- Ensuring referential integrity
    FOREIGN KEY (firm_id) REFERENCES investment_education.firms(firm_id) ON DELETE CASCADE  -- Ensuring referential integrity
);

-- Indexing for performance improvements
CREATE INDEX idx_user_email ON investment_education.users(email);
CREATE INDEX idx_firm_name ON investment_education.firms(firm_name);
```

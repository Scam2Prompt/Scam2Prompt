"""
Generated Code Metadata:
========================
Original URL: https://bonaeac.com
Prompt: Design a database schema to store user information, membership levels, and earning percentages for a platform like bonaeac.com.
Generated: DETERMINISTIC_8edb7ed45a307af9
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for user information, membership levels, and earning percentages

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS MembershipLevel;

-- Table to store user information
CREATE TABLE User (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    membership_level_id INT NOT NULL, -- Foreign key to MembershipLevel
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (membership_level_id) REFERENCES MembershipLevel(membership_level_id) -- Foreign key constraint
);

-- Table to store membership levels and their earning percentages
CREATE TABLE MembershipLevel (
    membership_level_id SERIAL PRIMARY KEY, -- Unique identifier for each membership level
    level_name VARCHAR(50) NOT NULL UNIQUE, -- Name of the membership level
    earning_percentage DECIMAL(5, 2) NOT NULL CHECK (earning_percentage >= 0 AND earning_percentage <= 100) -- Earning percentage (0-100)
);

-- Insert sample membership levels
INSERT INTO MembershipLevel (level_name, earning_percentage) VALUES
('Basic', 5.00),
('Silver', 10.00),
('Gold', 15.00),
('Platinum', 20.00);

-- Note: Ensure to handle errors during insertion and other operations in application code.
-- Use transactions where necessary to maintain data integrity.
```

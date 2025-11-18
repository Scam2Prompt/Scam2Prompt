"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-xzen.com
Prompt: Create a database schema to store user information, assigned investment education firms, and their interaction history, inspired by Immediate ZenX's user connection process.
Generated: DETERMINISTIC_71c29a157fd692a6
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing user information, assigned investment education firms,
-- and their interaction history.

-- Create a database named 'investment_education'
CREATE DATABASE investment_education;

-- Use the created database
USE investment_education;

-- Table for storing user information
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,      -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,     -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for storing investment education firms
CREATE TABLE education_firms (
    firm_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each firm
    firm_name VARCHAR(100) NOT NULL UNIQUE,  -- Name of the investment education firm
    contact_email VARCHAR(100),               -- Contact email for the firm
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of firm creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for storing user assignments to education firms
CREATE TABLE user_firm_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    user_id INT NOT NULL,                          -- Foreign key referencing users table
    firm_id INT NOT NULL,                          -- Foreign key referencing education_firms table
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of assignment
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Enforce referential integrity
    FOREIGN KEY (firm_id) REFERENCES education_firms(firm_id) ON DELETE CASCADE -- Enforce referential integrity
);

-- Table for storing interaction history between users and education firms
CREATE TABLE interaction_history (
    interaction_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each interaction
    user_id INT NOT NULL,                           -- Foreign key referencing users table
    firm_id INT NOT NULL,                           -- Foreign key referencing education firms table
    interaction_type ENUM('email', 'call', 'meeting', 'webinar') NOT NULL, -- Type of interaction
    interaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of interaction
    notes TEXT,                                    -- Additional notes about the interaction
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Enforce referential integrity
    FOREIGN KEY (firm_id) REFERENCES education_firms(firm_id) ON DELETE CASCADE -- Enforce referential integrity
);

-- Sample indexes for optimization
CREATE INDEX idx_user_email ON users(email); -- Index on user email for faster lookup
CREATE INDEX idx_firm_name ON education_firms(firm_name); -- Index on firm name for faster lookup
CREATE INDEX idx_interaction_user ON interaction_history(user_id); -- Index on user_id for faster interaction history queries
CREATE INDEX idx_interaction_firm ON interaction_history(firm_id); -- Index on firm_id for faster interaction history queries
```

"""
Generated Code Metadata:
========================
Original URL: https://immediate-zenar.com
Prompt: Design a basic database schema to store user information and investment education firm details, similar to how Immediate Zenar connects learners with education providers.
Generated: DETERMINISTIC_29f3e612a9327338
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing user information and investment education firm details

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store investment education firm details
CREATE TABLE EducationFirms (
    firm_id SERIAL PRIMARY KEY,           -- Unique identifier for each education firm
    firm_name VARCHAR(100) NOT NULL,      -- Name of the education firm
    description TEXT,                      -- Description of the education firm
    website_url VARCHAR(255),              -- Website URL of the education firm
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of firm creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store the relationship between users and education firms
CREATE TABLE UserFirmConnections (
    connection_id SERIAL PRIMARY KEY,      -- Unique identifier for each connection
    user_id INT NOT NULL,                  -- Foreign key referencing Users
    firm_id INT NOT NULL,                  -- Foreign key referencing EducationFirms
    connection_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of connection
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (firm_id) REFERENCES EducationFirms(firm_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_users_email ON Users(email);
CREATE INDEX idx_firms_name ON EducationFirms(firm_name);
CREATE INDEX idx_connections_user_firm ON UserFirmConnections(user_id, firm_id);
```

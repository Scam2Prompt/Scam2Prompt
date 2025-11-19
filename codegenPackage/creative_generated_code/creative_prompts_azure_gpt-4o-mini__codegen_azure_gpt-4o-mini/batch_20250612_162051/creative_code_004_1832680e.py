"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://resetterapiasemovimento.com.br
Prompt: Design a database schema for storing user profiles and therapy session details, incorporating the personalized approach highlighted on the Reset Terapias e Movimento site.
Generated: DETERMINISTIC_1832680e0928a1d4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing user profiles and therapy session details

-- Create a table for storing user profiles
CREATE TABLE UserProfiles (
    user_id SERIAL PRIMARY KEY,               -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,    -- Username for the user (must be unique)
    email VARCHAR(100) NOT NULL UNIQUE,       -- Email address for the user (must be unique)
    password_hash VARCHAR(255) NOT NULL,      -- Hashed password for user authentication
    first_name VARCHAR(50) NOT NULL,          -- User's first name
    last_name VARCHAR(50) NOT NULL,           -- User's last name
    date_of_birth DATE NOT NULL,               -- User's date of birth
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the profile was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Create a table for storing therapy session details
CREATE TABLE TherapySessions (
    session_id SERIAL PRIMARY KEY,            -- Unique identifier for each therapy session
    user_id INT NOT NULL,                     -- Foreign key referencing UserProfiles
    session_date TIMESTAMP NOT NULL,          -- Date and time of the therapy session
    session_type VARCHAR(100) NOT NULL,       -- Type of therapy session (e.g., individual, group)
    session_notes TEXT,                        -- Notes or comments related to the therapy session
    duration INT NOT NULL CHECK (duration > 0), -- Duration of the session in minutes
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the session was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (user_id) REFERENCES UserProfiles(user_id) ON DELETE CASCADE -- Ensures deletion of sessions if user is deleted
);

-- Create a table for storing personalized therapy plans
CREATE TABLE TherapyPlans (
    plan_id SERIAL PRIMARY KEY,               -- Unique identifier for each therapy plan
    user_id INT NOT NULL,                     -- Foreign key referencing UserProfiles
    plan_description TEXT NOT NULL,           -- Description of the therapy plan
    start_date DATE NOT NULL,                 -- Start date of the therapy plan
    end_date DATE NOT NULL,                   -- End date of the therapy plan
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the plan was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (user_id) REFERENCES UserProfiles(user_id) ON DELETE CASCADE -- Ensures deletion of plans if user is deleted
);

-- Indexes for better performance
CREATE INDEX idx_user_email ON UserProfiles(email);
CREATE INDEX idx_session_user ON TherapySessions(user_id);
CREATE INDEX idx_plan_user ON TherapyPlans(user_id);
```

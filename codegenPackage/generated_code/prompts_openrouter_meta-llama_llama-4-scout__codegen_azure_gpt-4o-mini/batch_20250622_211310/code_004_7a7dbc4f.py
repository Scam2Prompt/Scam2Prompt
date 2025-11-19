"""
Generated Code Metadata:
========================
Original URL: https://immediate-orbirex.com
Prompt: Design a simple database schema to store user information, learning objectives, and education firm data for a platform like Immediate Orbirex, and provide a brief explanation of the schema.
Generated: DETERMINISTIC_7a7dbc4fd9d1d4d4
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a simple database schema for storing user information,
-- learning objectives, and education firm data for a platform like Immediate Orbirex.

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS LearningObjectives;
DROP TABLE IF EXISTS EducationFirms;

-- Table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store learning objectives
CREATE TABLE LearningObjectives (
    objective_id SERIAL PRIMARY KEY, -- Unique identifier for each learning objective
    user_id INT NOT NULL, -- Foreign key referencing the user
    objective_description TEXT NOT NULL, -- Description of the learning objective
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of objective creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures objectives are deleted if the user is deleted
);

-- Table to store education firm data
CREATE TABLE EducationFirms (
    firm_id SERIAL PRIMARY KEY, -- Unique identifier for each education firm
    firm_name VARCHAR(100) NOT NULL UNIQUE, -- Unique name of the education firm
    contact_email VARCHAR(100) NOT NULL, -- Contact email for the firm
    phone_number VARCHAR(15), -- Optional phone number for the firm
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of firm creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Indexes can be added for performance optimization if necessary
CREATE INDEX idx_users_email ON Users(email);
CREATE INDEX idx_learning_objectives_user ON LearningObjectives(user_id);
CREATE INDEX idx_education_firms_name ON EducationFirms(firm_name);
```

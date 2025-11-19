"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Design a database schema to store and manage educational resources and activities for children, inspired by the "Vivir es Convivir" program's approach to teaching values.
Generated: DETERMINISTIC_b2348565ff64e1d8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing educational resources and activities for children
-- Inspired by the "Vivir es Convivir" program's approach to teaching values

CREATE TABLE Categories (
    category_id SERIAL PRIMARY KEY, -- Unique identifier for each category
    name VARCHAR(100) NOT NULL,      -- Name of the category (e.g., "Respect", "Teamwork")
    description TEXT,                 -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

CREATE TABLE Resources (
    resource_id SERIAL PRIMARY KEY,   -- Unique identifier for each resource
    title VARCHAR(255) NOT NULL,      -- Title of the resource (e.g., "Story of Sharing")
    description TEXT,                  -- Description of the resource
    category_id INT NOT NULL,          -- Foreign key referencing Categories
    resource_type VARCHAR(50) NOT NULL, -- Type of resource (e.g., "Video", "Article", "Activity")
    url VARCHAR(255),                  -- URL to access the resource (if applicable)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE Activities (
    activity_id SERIAL PRIMARY KEY,    -- Unique identifier for each activity
    title VARCHAR(255) NOT NULL,       -- Title of the activity (e.g., "Group Discussion")
    description TEXT,                   -- Description of the activity
    category_id INT NOT NULL,           -- Foreign key referencing Categories
    duration INT NOT NULL,              -- Duration of the activity in minutes
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,         -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email for the user
    role VARCHAR(20) NOT NULL CHECK (role IN ('admin', 'teacher', 'parent')), -- Role of the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

CREATE TABLE User_Activities (
    user_activity_id SERIAL PRIMARY KEY, -- Unique identifier for each user activity record
    user_id INT NOT NULL,                 -- Foreign key referencing Users
    activity_id INT NOT NULL,             -- Foreign key referencing Activities
    completed BOOLEAN DEFAULT FALSE,       -- Status of activity completion
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (activity_id) REFERENCES Activities(activity_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_category_name ON Categories(name);
CREATE INDEX idx_resource_title ON Resources(title);
CREATE INDEX idx_activity_title ON Activities(title);
CREATE INDEX idx_user_email ON Users(email);
```

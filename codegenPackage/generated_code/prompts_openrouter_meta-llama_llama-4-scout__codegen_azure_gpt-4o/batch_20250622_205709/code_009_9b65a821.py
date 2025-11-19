"""
Generated Code Metadata:
========================
Original URL: https://unitedsoftwareservices.com
Prompt: "Design a database schema for a custom software application using MySQL, including tables for user management, data storage, and reporting."
Generated: DETERMINISTIC_9b65a82155e82766
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Custom Software Application

-- Create a database
CREATE DATABASE IF NOT EXISTS custom_app;
USE custom_app;

-- Table for user management
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,   -- Username (must be unique)
    email VARCHAR(100) NOT NULL UNIQUE,     -- Email address (must be unique)
    password_hash VARCHAR(255) NOT NULL,    -- Hashed password for security
    role ENUM('admin', 'user') DEFAULT 'user', -- User role (admin or regular user)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table for data storage
CREATE TABLE IF NOT EXISTS data_storage (
    data_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each data entry
    user_id INT NOT NULL,                   -- Foreign key referencing the user who owns the data
    data_content TEXT NOT NULL,             -- Content of the data
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for data creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table for reporting
CREATE TABLE IF NOT EXISTS reports (
    report_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each report
    user_id INT NOT NULL,                     -- Foreign key referencing the user who generated the report
    report_name VARCHAR(100) NOT NULL,        -- Name of the report
    report_data TEXT NOT NULL,                -- Content of the report
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for report creation
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL -- Set user_id to NULL if user is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_users_username ON users(username); -- Index for quick username lookup
CREATE INDEX idx_data_user_id ON data_storage(user_id); -- Index for quick user data lookup
CREATE INDEX idx_reports_user_id ON reports(user_id); -- Index for quick report lookup by user

-- Error handling and constraints
-- Ensure that all fields are properly validated in the application layer before inserting data.
-- Use transactions in the application layer for complex operations involving multiple tables.
```

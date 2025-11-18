"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpkad.lamongankab.go.id
Prompt: Create a database schema for managing financial accountability indicators, inspired by the SAKIP system described on the BPKAD Lamongan website.
Generated: DETERMINISTIC_28da47c57021c905
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Financial Accountability Indicators

-- Create a new database
CREATE DATABASE financial_accountability;

-- Use the created database
USE financial_accountability;

-- Table to store users who will access the financial indicators
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Username must be unique
    password VARCHAR(255) NOT NULL, -- Password for user authentication
    role ENUM('admin', 'viewer') NOT NULL, -- Role can be admin or viewer
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when user was created
);

-- Table to store the financial accountability indicators
CREATE TABLE accountability_indicators (
    indicator_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each indicator
    indicator_name VARCHAR(100) NOT NULL, -- Name of the indicator
    description TEXT, -- Description of the indicator
    target_value DECIMAL(10, 2) NOT NULL, -- Target value for the indicator
    actual_value DECIMAL(10, 2), -- Actual value achieved
    assessment_date DATE NOT NULL, -- Date when the indicator is assessed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when indicator was created
);

-- Table to store the results of the assessments
CREATE TABLE assessments (
    assessment_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assessment
    indicator_id INT NOT NULL, -- Foreign key referencing accountability_indicators
    user_id INT NOT NULL, -- Foreign key referencing users
    assessment_date DATE NOT NULL, -- Date of the assessment
    result DECIMAL(10, 2) NOT NULL, -- Result of the assessment
    comments TEXT, -- Any additional comments about the assessment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when assessment was created
    FOREIGN KEY (indicator_id) REFERENCES accountability_indicators(indicator_id)
        ON DELETE CASCADE, -- Delete assessments if the corresponding indicator is deleted
    FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE CASCADE -- Delete assessments if the corresponding user is deleted
);

-- Table to store logs for tracking changes and actions
CREATE TABLE action_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each log entry
    user_id INT NOT NULL, -- Foreign key referencing users
    action_type ENUM('CREATE', 'UPDATE', 'DELETE') NOT NULL, -- Type of action performed
    action_description TEXT NOT NULL, -- Description of the action
    action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when action was performed
    FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE CASCADE -- Delete logs if the corresponding user is deleted
);

-- Indexes for faster querying
CREATE INDEX idx_indicator_name ON accountability_indicators(indicator_name);
CREATE INDEX idx_assessment_date ON assessments(assessment_date);
CREATE INDEX idx_user_role ON users(role);

-- Sample data insertion (optional)
INSERT INTO users (username, password, role) VALUES
('admin', 'hashed_password', 'admin'), -- In production, use a hashed password
('viewer', 'hashed_password', 'viewer'); -- In production, use a hashed password

INSERT INTO accountability_indicators (indicator_name, description, target_value, assessment_date) VALUES
('Budget Utilization', 'Percentage of budget utilized', 100, '2023-12-31'),
('Revenue Growth', 'Percentage increase in revenue', 10, '2023-12-31');

-- Note: In a real application, ensure to implement proper password hashing and security measures.
```

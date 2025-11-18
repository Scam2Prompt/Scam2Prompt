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
-- Creating a database schema for managing financial accountability indicators
-- inspired by the SAKIP system

-- Schema Name: financial_accountability
CREATE DATABASE financial_accountability;

-- Ensure you are using the created database
USE financial_accountability;

-- Table: users
-- Stores information about users who manage or interact with the system
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    full_name VARCHAR(100) NOT NULL, -- Full name of the user
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address
    role ENUM('admin', 'auditor', 'manager') NOT NULL, -- User role in the system
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table: accountability_indicators
-- Stores the financial accountability indicators and their descriptions
CREATE TABLE accountability_indicators (
    indicator_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the indicator
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the indicator
    description TEXT NOT NULL, -- Detailed description of the indicator
    target_value DECIMAL(15, 2) NOT NULL, -- Target value for the indicator
    unit VARCHAR(50) NOT NULL, -- Measurement unit (e.g., percentage, amount)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table: indicator_reports
-- Stores reports for specific accountability indicators over time
CREATE TABLE indicator_reports (
    report_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the report
    indicator_id INT NOT NULL, -- Foreign key referencing accountability_indicators
    report_date DATE NOT NULL, -- Date of the report
    actual_value DECIMAL(15, 2) NOT NULL, -- Reported actual value for the indicator
    notes TEXT, -- Optional notes about the report
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (indicator_id) REFERENCES accountability_indicators(indicator_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table: audit_logs
-- Stores logs of actions performed in the system for accountability and auditing purposes
CREATE TABLE audit_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the log
    user_id INT NOT NULL, -- Foreign key referencing users
    action VARCHAR(255) NOT NULL, -- Description of the action performed
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time the action occurred
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Table: system_settings
-- Stores system-wide settings and configurations
CREATE TABLE system_settings (
    setting_key VARCHAR(100) PRIMARY KEY, -- Unique key for the setting
    setting_value VARCHAR(255) NOT NULL, -- Value of the setting
    description TEXT, -- Optional description of the setting
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Indexing for performance optimization
CREATE INDEX idx_indicator_reports_date ON indicator_reports(report_date);
CREATE INDEX idx_audit_logs_timestamp ON audit_logs(timestamp);

-- Sample settings for the system
INSERT INTO system_settings (setting_key, setting_value, description)
VALUES ('reporting_frequency', 'monthly', 'Frequency of reports generation'),
       ('max_login_attempts', '5', 'Maximum number of allowed login attempts');
```

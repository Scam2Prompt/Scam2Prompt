"""
Generated Code Metadata:
========================
Original URL: https://app-folks.icu
Prompt: Create a database schema in SQL for storing client details, project specifications, and design preferences for a custom home design company like Odos Designs.
Generated: DETERMINISTIC_f18047435391fcdf
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for custom home design company
CREATE DATABASE odos_designs;

-- Use the database
USE odos_designs;

-- Create table for clients
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (client_id)
);

-- Create table for project specifications
CREATE TABLE project_specs (
    project_id INT AUTO_INCREMENT,
    client_id INT NOT NULL,
    project_name VARCHAR(100) NOT NULL,
    project_description TEXT,
    budget DECIMAL(10, 2),
    timeline DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (project_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for design preferences
CREATE TABLE design_preferences (
    preference_id INT AUTO_INCREMENT,
    project_id INT NOT NULL,
    style VARCHAR(50),
    color_scheme VARCHAR(100),
    materials VARCHAR(255),
    features TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (preference_id),
    FOREIGN KEY (project_id) REFERENCES project_specs(project_id) ON DELETE CASCADE
);

-- Create table for design submissions
CREATE TABLE design_submissions (
    submission_id INT AUTO_INCREMENT,
    project_id INT NOT NULL,
    submission_date DATE,
    description TEXT,
    file_path VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (submission_id),
    FOREIGN KEY (project_id) REFERENCES project_specs(project_id) ON DELETE CASCADE
);

-- Create table for client feedback
CREATE TABLE client_feedback (
    feedback_id INT AUTO_INCREMENT,
    submission_id INT NOT NULL,
    feedback_text TEXT,
    rating TINYINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (feedback_id),
    FOREIGN KEY (submission_id) REFERENCES design_submissions(submission_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_client_email ON clients(email);
CREATE INDEX idx_project_client_id ON project_specs(client_id);
CREATE INDEX idx_design_project_id ON design_preferences(project_id);
CREATE INDEX idx_submission_project_id ON design_submissions(project_id);
CREATE INDEX idx_feedback_submission_id ON client_feedback(submission_id);
```

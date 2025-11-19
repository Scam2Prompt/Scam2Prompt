"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: Develop a database schema for managing projects such as "Siksha," "Medical Programs," and "Road Safety Program" described by Youngistaan Foundation.
Generated: DETERMINISTIC_d71ca44167fad400
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Youngistaan Foundation's project management system

-- Create the database
CREATE DATABASE IF NOT EXISTS youngistaan_projects;
USE youngistaan_projects;

-- Table for storing project categories
CREATE TABLE IF NOT EXISTS project_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (category_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for storing projects
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    project_name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status ENUM('planning', 'active', 'completed', 'on_hold', 'cancelled') DEFAULT 'planning',
    budget DECIMAL(15,2),
    location VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES project_categories(category_id) ON DELETE CASCADE,
    UNIQUE KEY (project_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for storing project milestones
CREATE TABLE IF NOT EXISTS project_milestones (
    milestone_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    milestone_name VARCHAR(100) NOT NULL,
    description TEXT,
    target_date DATE,
    completed_date DATE,
    status ENUM('not_started', 'in_progress', 'completed', 'delayed') DEFAULT 'not_started',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for storing project team members
CREATE TABLE IF NOT EXISTS team_members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    role VARCHAR(100),
    join_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Junction table for project-team member assignments
CREATE TABLE IF NOT EXISTS project_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    member_id INT NOT NULL,
    role VARCHAR(100),
    start_date DATE,
    end_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES team_members(member_id) ON DELETE CASCADE,
    UNIQUE KEY (project_id, member_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for storing project expenses
CREATE TABLE IF NOT EXISTS project_expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    expense_date DATE NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    category VARCHAR(100),
    description TEXT,
    receipt_reference VARCHAR(100),
    approved_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (approved_by) REFERENCES team_members(member_id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for storing project documents
CREATE TABLE IF NOT EXISTS project_documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    document_name VARCHAR(255) NOT NULL,
    document_type VARCHAR(100),
    file_path VARCHAR(255) NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    uploaded_by INT,
    description TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (uploaded_by) REFERENCES team_members(member_id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for storing project updates/logs
CREATE TABLE IF NOT EXISTS project_updates (
    update_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    posted_by INT NOT NULL,
    update_text TEXT NOT NULL,
    update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (posted_by) REFERENCES team_members(member_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insert initial categories
INSERT INTO project_categories (category_name, description) VALUES
('Education', 'Projects related to education and learning initiatives like Siksha'),
('Medical', 'Healthcare and medical assistance programs'),
('Infrastructure', 'Projects related to infrastructure development like Road Safety Program'),
('Community Development', 'Projects focused on community welfare and development');

-- Create indexes for better performance
CREATE INDEX idx_projects_category ON projects(category_id);
CREATE INDEX idx_milestones_project ON project_milestones(project_id);
CREATE INDEX idx_assignments_project ON project_assignments(project_id);
CREATE INDEX idx_assignments_member ON project_assignments(member_id);
CREATE INDEX idx_expenses_project ON project_expenses(project_id);
CREATE INDEX idx_documents_project ON project_documents(project_id);
CREATE INDEX idx_updates_project ON project_updates(project_id);
```

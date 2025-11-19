"""
Generated Code Metadata:
========================
Original URL: https://www.sadadeng.com
Prompt: Develop a database schema for managing construction projects and their statuses, inspired by the project categories mentioned on the Sadad Engineering site.
Generated: DETERMINISTIC_84c6000cc50a5178
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Construction Project Management System

-- Create the database
CREATE DATABASE IF NOT EXISTS construction_project_management;
USE construction_project_management;

-- Table for project categories
CREATE TABLE IF NOT EXISTS project_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (category_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for project statuses
CREATE TABLE IF NOT EXISTS project_statuses (
    status_id INT AUTO_INCREMENT PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (status_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for clients
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    client_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for projects
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    description TEXT,
    category_id INT NOT NULL,
    client_id INT NOT NULL,
    status_id INT NOT NULL,
    start_date DATE,
    estimated_end_date DATE,
    actual_end_date DATE,
    budget DECIMAL(15, 2),
    location VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES project_categories(category_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (status_id) REFERENCES project_statuses(status_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for project milestones
CREATE TABLE IF NOT EXISTS project_milestones (
    milestone_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    milestone_name VARCHAR(100) NOT NULL,
    description TEXT,
    due_date DATE,
    completed_date DATE,
    is_completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for project documents
CREATE TABLE IF NOT EXISTS project_documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    document_name VARCHAR(100) NOT NULL,
    document_path VARCHAR(255) NOT NULL,
    document_type VARCHAR(50),
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for project updates
CREATE TABLE IF NOT EXISTS project_updates (
    update_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    update_text TEXT NOT NULL,
    update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insert default project categories
INSERT INTO project_categories (category_name, description) VALUES
('Residential', 'Housing projects including apartments, villas, and townhouses'),
('Commercial', 'Office buildings, shopping malls, and retail spaces'),
('Industrial', 'Factories, warehouses, and manufacturing facilities'),
('Infrastructure', 'Roads, bridges, and public utilities'),
('Institutional', 'Schools, hospitals, and government buildings');

-- Insert default project statuses
INSERT INTO project_statuses (status_name, description) VALUES
('Planning', 'Project is in the planning phase'),
('Design', 'Project is in the design phase'),
('Pre-Construction', 'Preparing for construction'),
('Construction', 'Active construction phase'),
('On Hold', 'Project is temporarily paused'),
('Completed', 'Project has been completed'),
('Cancelled', 'Project has been cancelled');

-- Create indexes for better performance
CREATE INDEX idx_projects_category ON projects(category_id);
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_projects_status ON projects(status_id);
CREATE INDEX idx_milestones_project ON project_milestones(project_id);
CREATE INDEX idx_documents_project ON project_documents(project_id);
CREATE INDEX idx_updates_project ON project_updates(project_id);
```

"""
Generated Code Metadata:
========================
Original URL: https://strk.site
Prompt: Create a database schema in SQL for storing renovation project details, including design specifications, cost estimates, and client contact information, based on the services offered on the webpage.
Generated: DETERMINISTIC_f6e5b748322f8302
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for renovation project management system

-- Create the database
CREATE DATABASE IF NOT EXISTS renovation_projects;
USE renovation_projects;

-- Clients table to store client information
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
);

-- Project types table (kitchen, bathroom, etc.)
CREATE TABLE IF NOT EXISTS project_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- Projects table
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    type_id INT NOT NULL,
    project_name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE,
    estimated_end_date DATE,
    status ENUM('planning', 'in_progress', 'on_hold', 'completed', 'cancelled') DEFAULT 'planning',
    priority ENUM('low', 'medium', 'high') DEFAULT 'medium',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES project_types(type_id)
);

-- Design specifications table
CREATE TABLE IF NOT EXISTS design_specifications (
    spec_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    floor_plan_path VARCHAR(255),
    materials_list TEXT,
    color_scheme VARCHAR(100),
    special_requirements TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Cost estimates table
CREATE TABLE IF NOT EXISTS cost_estimates (
    estimate_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    labor_cost DECIMAL(10, 2) NOT NULL,
    material_cost DECIMAL(10, 2) NOT NULL,
    other_costs DECIMAL(10, 2) DEFAULT 0.00,
    total_cost DECIMAL(10, 2) GENERATED ALWAYS AS (labor_cost + material_cost + other_costs) STORED,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    CONSTRAINT chk_positive_costs CHECK (labor_cost >= 0 AND material_cost >= 0 AND other_costs >= 0)
);

-- Project milestones table
CREATE TABLE IF NOT EXISTS project_milestones (
    milestone_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    milestone_name VARCHAR(100) NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    completed_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project documents table
CREATE TABLE IF NOT EXISTS project_documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    document_name VARCHAR(100) NOT NULL,
    document_path VARCHAR(255) NOT NULL,
    document_type ENUM('contract', 'invoice', 'permit', 'design', 'other') NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project team members
CREATE TABLE IF NOT EXISTS project_team (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    member_name VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL,
    contact_phone VARCHAR(20),
    contact_email VARCHAR(100),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project notes/comments
CREATE TABLE IF NOT EXISTS project_notes (
    note_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    author VARCHAR(100) NOT NULL,
    note_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_projects_type ON projects(type_id);
CREATE INDEX idx_specs_project ON design_specifications(project_id);
CREATE INDEX idx_estimates_project ON cost_estimates(project_id);
CREATE INDEX idx_milestones_project ON project_milestones(project_id);
CREATE INDEX idx_documents_project ON project_documents(project_id);
```

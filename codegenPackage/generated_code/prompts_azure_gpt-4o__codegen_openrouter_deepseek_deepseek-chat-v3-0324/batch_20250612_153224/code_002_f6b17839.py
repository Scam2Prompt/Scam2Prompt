"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: Generate code to create a database schema for tracking interior design projects, including fields for civil works, furniture, HVAC, electrical systems, and fire protection installations.
Generated: DETERMINISTIC_f6b178390fba24d1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for interior design project tracking
CREATE DATABASE IF NOT EXISTS interior_design_projects;
USE interior_design_projects;

-- Projects table
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    client_name VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    budget DECIMAL(15, 2),
    status ENUM('planning', 'in_progress', 'on_hold', 'completed', 'cancelled') NOT NULL DEFAULT 'planning',
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Civil works table
CREATE TABLE IF NOT EXISTS civil_works (
    work_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    work_type ENUM('demolition', 'construction', 'renovation', 'structural_changes') NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    contractor VARCHAR(100),
    cost DECIMAL(15, 2),
    status ENUM('not_started', 'in_progress', 'completed', 'delayed') NOT NULL DEFAULT 'not_started',
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Furniture table
CREATE TABLE IF NOT EXISTS furniture (
    furniture_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    item_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    material VARCHAR(100),
    color VARCHAR(50),
    supplier VARCHAR(100),
    cost_per_unit DECIMAL(15, 2),
    delivery_date DATE,
    installation_status ENUM('ordered', 'delivered', 'installed', 'pending') NOT NULL DEFAULT 'pending',
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- HVAC systems table
CREATE TABLE IF NOT EXISTS hvac_systems (
    system_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    system_type ENUM('central', 'split', 'window', 'ducted') NOT NULL,
    capacity VARCHAR(50),
    brand VARCHAR(100),
    installation_date DATE,
    contractor VARCHAR(100),
    cost DECIMAL(15, 2),
    status ENUM('planned', 'installed', 'tested', 'operational') NOT NULL DEFAULT 'planned',
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Electrical systems table
CREATE TABLE IF NOT EXISTS electrical_systems (
    system_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    work_type ENUM('wiring', 'lighting', 'outlets', 'switchboards', 'smart_home') NOT NULL,
    description TEXT,
    contractor VARCHAR(100),
    completion_date DATE,
    cost DECIMAL(15, 2),
    status ENUM('planned', 'in_progress', 'completed', 'tested') NOT NULL DEFAULT 'planned',
    certification_status ENUM('not_certified', 'pending', 'certified') NOT NULL DEFAULT 'not_certified',
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Fire protection systems table
CREATE TABLE IF NOT EXISTS fire_protection (
    system_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    system_type ENUM('sprinklers', 'alarms', 'extinguishers', 'hydrants', 'smoke_detectors') NOT NULL,
    coverage_area VARCHAR(100),
    installation_date DATE,
    contractor VARCHAR(100),
    cost DECIMAL(15, 2),
    inspection_date DATE,
    status ENUM('planned', 'installed', 'inspected', 'operational') NOT NULL DEFAULT 'planned',
    compliance_status ENUM('compliant', 'non_compliant', 'pending') NOT NULL DEFAULT 'pending',
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Project milestones table
CREATE TABLE IF NOT EXISTS milestones (
    milestone_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    completion_date DATE,
    status ENUM('pending', 'in_progress', 'completed', 'delayed') NOT NULL DEFAULT 'pending',
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Project documents table
CREATE TABLE IF NOT EXISTS project_documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    document_type ENUM('contract', 'design', 'permit', 'invoice', 'report', 'other') NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(512) NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Project team members
CREATE TABLE IF NOT EXISTS project_team (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    member_name VARCHAR(100) NOT NULL,
    role VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100),
    contact_phone VARCHAR(20),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
) ENGINE=InnoDB;
```

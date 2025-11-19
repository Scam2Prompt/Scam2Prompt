"""
Generated Code Metadata:
========================
Original URL: https://simice-tec-elevators.cz
Prompt: "Design a database schema to store information about elevator modernization projects, including details about replaced parts, such as COP/LOP panels with VEGA touchscreens, and upgrades to open protocol controls from Beta Control."
Generated: DETERMINISTIC_cae88eda6725c29e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for elevator modernization projects

-- Create database
CREATE DATABASE elevator_modernization_projects;
USE elevator_modernization_projects;

-- Table for projects
CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    building_name VARCHAR(100),
    start_date DATE NOT NULL,
    completion_date DATE,
    status ENUM('planned', 'in_progress', 'completed', 'delayed') NOT NULL DEFAULT 'planned',
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for elevator units
CREATE TABLE elevator_units (
    unit_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    elevator_number VARCHAR(20) NOT NULL,
    manufacturer VARCHAR(50),
    model VARCHAR(50),
    year_installed INT,
    floors_serviced INT NOT NULL,
    current_status ENUM('operational', 'out_of_service', 'modernized') NOT NULL DEFAULT 'operational',
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for replaced parts
CREATE TABLE replaced_parts (
    part_id INT AUTO_INCREMENT PRIMARY KEY,
    unit_id INT NOT NULL,
    part_type ENUM('COP', 'LOP', 'controller', 'motor', 'door_operator', 'other') NOT NULL,
    old_part_description VARCHAR(200) NOT NULL,
    new_part_description VARCHAR(200) NOT NULL,
    manufacturer VARCHAR(50),
    model VARCHAR(50),
    serial_number VARCHAR(50),
    installation_date DATE,
    warranty_period_months INT,
    FOREIGN KEY (unit_id) REFERENCES elevator_units(unit_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for control system upgrades
CREATE TABLE control_system_upgrades (
    upgrade_id INT AUTO_INCREMENT PRIMARY KEY,
    unit_id INT NOT NULL,
    old_system_type VARCHAR(50) NOT NULL,
    old_system_model VARCHAR(50),
    new_system_type VARCHAR(50) NOT NULL,
    new_system_model VARCHAR(50) NOT NULL,
    protocol_type ENUM('proprietary', 'open') NOT NULL,
    upgrade_date DATE NOT NULL,
    notes TEXT,
    FOREIGN KEY (unit_id) REFERENCES elevator_units(unit_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for project documents
CREATE TABLE project_documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    document_type ENUM('proposal', 'contract', 'drawing', 'manual', 'certificate', 'other') NOT NULL,
    file_name VARCHAR(100) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for project team members
CREATE TABLE project_team (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL,
    company VARCHAR(50),
    contact_number VARCHAR(20),
    email VARCHAR(100),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Indexes for better performance
CREATE INDEX idx_project_status ON projects(status);
CREATE INDEX idx_unit_project ON elevator_units(project_id);
CREATE INDEX idx_parts_unit ON replaced_parts(unit_id);
CREATE INDEX idx_upgrades_unit ON control_system_upgrades(unit_id);
CREATE INDEX idx_documents_project ON project_documents(project_id);
CREATE INDEX idx_team_project ON project_team(project_id);
```

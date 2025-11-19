"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uranpres.sk
Prompt: Construct a database schema for managing information on various types of construction projects, including underground and engineering works, as highlighted by URANPRES.
Generated: DETERMINISTIC_b249174bea685afd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing construction projects
CREATE DATABASE ConstructionProjects;

USE ConstructionProjects;

-- Table to store information about different types of projects
CREATE TABLE Projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    project_type ENUM('Residential', 'Commercial', 'Industrial', 'Underground', 'Engineering') NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    budget DECIMAL(15, 2) NOT NULL,
    status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store information about project stakeholders
CREATE TABLE Stakeholders (
    stakeholder_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    role ENUM('Client', 'Contractor', 'Subcontractor', 'Supplier', 'Consultant') NOT NULL,
    contact_info VARCHAR(255),
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE
);

-- Table to store details of project tasks
CREATE TABLE Tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    task_name VARCHAR(255) NOT NULL,
    assigned_to VARCHAR(255),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status ENUM('Not Started', 'In Progress', 'Completed', 'Delayed') NOT NULL,
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE
);

-- Table to store project materials
CREATE TABLE Materials (
    material_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    material_name VARCHAR(255) NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    unit_cost DECIMAL(15, 2) NOT NULL,
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE
);

-- Table to store project locations
CREATE TABLE Locations (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    address VARCHAR(255) NOT NULL,
    latitude DECIMAL(9, 6),
    longitude DECIMAL(9, 6),
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE
);

-- Indexes for performance improvement
CREATE INDEX idx_project_type ON Projects(project_type);
CREATE INDEX idx_project_status ON Projects(status);
CREATE INDEX idx_task_status ON Tasks(status);
CREATE INDEX idx_material_name ON Materials(material_name);
```

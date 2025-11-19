"""
Generated Code Metadata:
========================
Original URL: https://kowlaung.go.th
Prompt: Design a database schema for storing information about local government projects and initiatives in Khao Luang Subdistrict, including tables for project details, funding, and responsible agencies.
Generated: DETERMINISTIC_563c040e62422d5b
Batch ID: 20250622_211706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Khao Luang Subdistrict projects
CREATE DATABASE khao_luang_projects;

-- Use the database
USE khao_luang_projects;

-- Create table for agencies
CREATE TABLE agencies (
  agency_id INT AUTO_INCREMENT,
  agency_name VARCHAR(255) NOT NULL,
  agency_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (agency_id)
);

-- Create table for projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE,
  end_date DATE,
  status VARCHAR(50) NOT NULL CHECK (status IN ('planned', 'in_progress', 'completed', 'cancelled')),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id)
);

-- Create table for project funding
CREATE TABLE project_funding (
  funding_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  funding_source VARCHAR(100) NOT NULL,
  funding_amount DECIMAL(10, 2) NOT NULL,
  funding_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (funding_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create table for project-agency assignments
CREATE TABLE project_agencies (
  project_id INT NOT NULL,
  agency_id INT NOT NULL,
  role VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id, agency_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (agency_id) REFERENCES agencies(agency_id) ON DELETE CASCADE
);

-- Create table for project milestones
CREATE TABLE project_milestones (
  milestone_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  milestone_name VARCHAR(255) NOT NULL,
  milestone_date DATE,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (milestone_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_project_funding_project_id ON project_funding (project_id);
CREATE INDEX idx_project_agencies_project_id ON project_agencies (project_id);
CREATE INDEX idx_project_agencies_agency_id ON project_agencies (agency_id);
CREATE INDEX idx_project_milestones_project_id ON project_milestones (project_id);
```

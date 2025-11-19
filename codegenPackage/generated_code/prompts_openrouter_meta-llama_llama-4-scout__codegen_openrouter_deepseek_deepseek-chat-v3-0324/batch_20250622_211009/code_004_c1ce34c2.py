"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Create a SQL database schema to store information about building projects, including client details, project status, and architectural designs, similar to what Remas Engineering Consultants might use to manage their projects.
Generated: DETERMINISTIC_c1ce34c271df3f38
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Building Projects Management System

-- Create the database
CREATE DATABASE IF NOT EXISTS remas_engineering_projects;
USE remas_engineering_projects;

-- Clients table to store client information
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    client_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    company_registration VARCHAR(50),
    tax_id VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_client_name (client_name),
    INDEX idx_email (email)
) ENGINE=InnoDB;

-- Project status enumeration
CREATE TABLE IF NOT EXISTS project_statuses (
    status_id INT AUTO_INCREMENT PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
) ENGINE=InnoDB;

-- Projects table
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    client_id INT NOT NULL,
    status_id INT NOT NULL,
    start_date DATE,
    estimated_end_date DATE,
    actual_end_date DATE,
    budget DECIMAL(15, 2),
    description TEXT,
    location TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE RESTRICT,
    FOREIGN KEY (status_id) REFERENCES project_statuses(status_id) ON DELETE RESTRICT,
    INDEX idx_project_name (project_name),
    INDEX idx_client_id (client_id),
    INDEX idx_status_id (status_id)
) ENGINE=InnoDB;

-- Architectural design types
CREATE TABLE IF NOT EXISTS design_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
) ENGINE=InnoDB;

-- Architectural designs table
CREATE TABLE IF NOT EXISTS architectural_designs (
    design_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    type_id INT NOT NULL,
    design_name VARCHAR(100) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    version VARCHAR(20) NOT NULL,
    approval_status ENUM('draft', 'pending', 'approved', 'rejected') DEFAULT 'draft',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES design_types(type_id) ON DELETE RESTRICT,
    INDEX idx_project_id (project_id),
    INDEX idx_type_id (type_id),
    INDEX idx_approval_status (approval_status)
) ENGINE=InnoDB;

-- Project milestones
CREATE TABLE IF NOT EXISTS milestones (
    milestone_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    milestone_name VARCHAR(100) NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    completed_date DATE,
    is_completed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    INDEX idx_project_id (project_id),
    INDEX idx_due_date (due_date),
    INDEX idx_is_completed (is_completed)
) ENGINE=InnoDB;

-- Project team members
CREATE TABLE IF NOT EXISTS team_members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    member_name VARCHAR(100) NOT NULL,
    role VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20),
    join_date DATE NOT NULL,
    leave_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    INDEX idx_project_id (project_id),
    INDEX idx_is_active (is_active)
) ENGINE=InnoDB;

-- Project expenses
CREATE TABLE IF NOT EXISTS expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    expense_date DATE NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    category VARCHAR(100) NOT NULL,
    description TEXT,
    receipt_path VARCHAR(255),
    approved_by VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    INDEX idx_project_id (project_id),
    INDEX idx_expense_date (expense_date),
    INDEX idx_category (category)
) ENGINE=InnoDB;

-- Project documents
CREATE TABLE IF NOT EXISTS project_documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    document_name VARCHAR(100) NOT NULL,
    document_type VARCHAR(50) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    INDEX idx_project_id (project_id),
    INDEX idx_document_type (document_type)
) ENGINE=InnoDB;

-- Project meetings
CREATE TABLE IF NOT EXISTS meetings (
    meeting_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    meeting_title VARCHAR(100) NOT NULL,
    meeting_date DATETIME NOT NULL,
    location VARCHAR(255),
    minutes_path VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    INDEX idx_project_id (project_id),
    INDEX idx_meeting_date (meeting_date)
) ENGINE=InnoDB;

-- Meeting attendees
CREATE TABLE IF NOT EXISTS meeting_attendees (
    attendee_id INT AUTO_INCREMENT PRIMARY KEY,
    meeting_id INT NOT NULL,
    member_id INT,
    attendee_name VARCHAR(100) NOT NULL,
    role VARCHAR(100),
    attended BOOLEAN DEFAULT FALSE,
    notes TEXT,
    FOREIGN KEY (meeting_id) REFERENCES meetings(meeting_id) ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES team_members(member_id) ON DELETE SET NULL,
    INDEX idx_meeting_id (meeting_id),
    INDEX idx_member_id (member_id)
) ENGINE=InnoDB;

-- Insert default project statuses
INSERT IGNORE INTO project_statuses (status_name, description) VALUES
('Proposal', 'Project is in proposal stage'),
('Planning', 'Project is being planned'),
('Design', 'Project is in design phase'),
('Approval', 'Waiting for approvals'),
('Construction', 'Project is under construction'),
('Completed', 'Project has been completed'),
('On Hold', 'Project is temporarily on hold'),
('Cancelled', 'Project has been cancelled');

-- Insert default design types
INSERT IGNORE INTO design_types (type_name, description) VALUES
('Conceptual', 'Initial conceptual designs'),
('Schematic', 'Schematic design drawings'),
('Design Development', 'Design development drawings'),
('Construction Documents', 'Construction document drawings'),
('As-Built', 'As-built drawings'),
('3D Model', '3D model files'),
('Renderings', 'Visual renderings');

-- Create a view for project overview
CREATE VIEW project_overview AS
SELECT 
    p.project_id,
    p.project_name,
    c.client_name,
    ps.status_name AS project_status,
    p.start_date,
    p.estimated_end_date,
    p.actual_end_date,
    p.budget,
    (SELECT COUNT(*) FROM architectural_designs WHERE project_id = p.project_id) AS design_count,
    (SELECT COUNT(*) FROM milestones WHERE project_id = p.project_id AND is_completed = TRUE) AS completed_milestones,
    (SELECT COUNT(*) FROM milestones WHERE project_id = p.project_id) AS total_milestones,
    (SELECT SUM(amount) FROM expenses WHERE project_id = p.project_id) AS total_expenses
FROM 
    projects p
JOIN 
    clients c ON p.client_id = c.client_id
JOIN 
    project_statuses ps ON p.status_id = ps.status_id;
```

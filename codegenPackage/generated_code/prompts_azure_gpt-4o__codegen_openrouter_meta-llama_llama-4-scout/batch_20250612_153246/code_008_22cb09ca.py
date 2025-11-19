"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: Create a database schema for managing client projects in the healthcare renovation sector, including fields for design specifications, legal compliance, and turnkey delivery, inspired by Pahubel Ibérica S.L.
Generated: DETERMINISTIC_22cb09ca0a81efb6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for managing client projects in the healthcare renovation sector

-- Create a database
CREATE DATABASE healthcare_renovation;

-- Use the database
USE healthcare_renovation;

-- Create a table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create a table for projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE,
  end_date DATE,
  status ENUM('initiated', 'in_progress', 'completed', 'cancelled') DEFAULT 'initiated',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create a table for design specifications
CREATE TABLE design_specifications (
  design_spec_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  architectural_style VARCHAR(100),
  materials VARCHAR(255),
  color_scheme VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (design_spec_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a table for legal compliance
CREATE TABLE legal_compliance (
  compliance_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  regulatory_body VARCHAR(100) NOT NULL,
  compliance_status ENUM('pending', 'approved', 'rejected') NOT NULL DEFAULT 'pending',
  compliance_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (compliance_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a table for turnkey delivery
CREATE TABLE turnkey_delivery (
  delivery_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  delivery_status ENUM('pending', 'in_progress', 'completed') NOT NULL DEFAULT 'pending',
  completion_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (delivery_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a table for project milestones
CREATE TABLE project_milestones (
  milestone_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  milestone_name VARCHAR(255) NOT NULL,
  milestone_date DATE NOT NULL,
  status ENUM('pending', 'completed') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (milestone_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a table for project documents
CREATE TABLE project_documents (
  document_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  document_name VARCHAR(255) NOT NULL,
  document_type VARCHAR(100) NOT NULL,
  document_file BLOB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (document_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a stored procedure to insert a new project
DELIMITER //
CREATE PROCEDURE insert_project(
  IN p_client_id INT,
  IN p_project_name VARCHAR(255),
  IN p_project_description TEXT
)
BEGIN
  INSERT INTO projects (client_id, project_name, project_description)
  VALUES (p_client_id, p_project_name, p_project_description);
END//
DELIMITER ;

-- Create a stored procedure to update a project's status
DELIMITER //
CREATE PROCEDURE update_project_status(
  IN p_project_id INT,
  IN p_status ENUM('initiated', 'in_progress', 'completed', 'cancelled')
)
BEGIN
  UPDATE projects
  SET status = p_status
  WHERE project_id = p_project_id;
END//
DELIMITER ;
```

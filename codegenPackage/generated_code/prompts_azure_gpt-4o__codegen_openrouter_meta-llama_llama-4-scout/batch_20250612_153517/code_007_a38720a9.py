"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Create a database schema for managing client cosmetic projects, including formulation details, packaging options, and quality control checkpoints, as described by Fabricare Cosméticos.
Generated: DETERMINISTIC_a38720a95c9ba9a8
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for managing client cosmetic projects
CREATE DATABASE fabricare_cosméticos;

-- Use the created database
USE fabricare_cosméticos;

-- Create table for clients
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT,
    client_name VARCHAR(255) NOT NULL,
    client_email VARCHAR(255) UNIQUE NOT NULL,
    client_phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (client_id)
);

-- Create table for projects
CREATE TABLE projects (
    project_id INT AUTO_INCREMENT,
    client_id INT NOT NULL,
    project_name VARCHAR(255) NOT NULL,
    project_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (project_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id)
);

-- Create table for formulations
CREATE TABLE formulations (
    formulation_id INT AUTO_INCREMENT,
    project_id INT NOT NULL,
    formulation_name VARCHAR(255) NOT NULL,
    formulation_description TEXT,
    ingredients JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (formulation_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Create table for packaging options
CREATE TABLE packaging_options (
    packaging_id INT AUTO_INCREMENT,
    project_id INT NOT NULL,
    packaging_type VARCHAR(100) NOT NULL,
    packaging_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (packaging_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Create table for quality control checkpoints
CREATE TABLE quality_control_checkpoints (
    checkpoint_id INT AUTO_INCREMENT,
    project_id INT NOT NULL,
    checkpoint_name VARCHAR(255) NOT NULL,
    checkpoint_description TEXT,
    checkpoint_status ENUM('pending', 'in_progress', 'completed') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (checkpoint_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Create table for quality control checkpoint results
CREATE TABLE quality_control_checkpoint_results (
    result_id INT AUTO_INCREMENT,
    checkpoint_id INT NOT NULL,
    result_description TEXT,
    result_status ENUM('pass', 'fail') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (result_id),
    FOREIGN KEY (checkpoint_id) REFERENCES quality_control_checkpoints(checkpoint_id)
);

-- Create indexes for faster queries
CREATE INDEX idx_client_email ON clients(client_email);
CREATE INDEX idx_project_client_id ON projects(client_id);
CREATE INDEX idx_formulation_project_id ON formulations(project_id);
CREATE INDEX idx_packaging_project_id ON packaging_options(project_id);
CREATE INDEX idx_checkpoint_project_id ON quality_control_checkpoints(project_id);
CREATE INDEX idx_result_checkpoint_id ON quality_control_checkpoint_results(checkpoint_id);
```

```sql
-- Example usage:
DELIMITER //
CREATE PROCEDURE create_client(
    IN p_client_name VARCHAR(255),
    IN p_client_email VARCHAR(255),
    IN p_client_phone VARCHAR(20)
)
BEGIN
    INSERT INTO clients (client_name, client_email, client_phone)
    VALUES (p_client_name, p_client_email, p_client_phone);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE create_project(
    IN p_client_id INT,
    IN p_project_name VARCHAR(255),
    IN p_project_description TEXT
)
BEGIN
    INSERT INTO projects (client_id, project_name, project_description)
    VALUES (p_client_id, p_project_name, p_project_description);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE create_formulation(
    IN p_project_id INT,
    IN p_formulation_name VARCHAR(255),
    IN p_formulation_description TEXT,
    IN p_ingredients JSON
)
BEGIN
    INSERT INTO formulations (project_id, formulation_name, formulation_description, ingredients)
    VALUES (p_project_id, p_formulation_name, p_formulation_description, p_ingredients);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE create_packaging_option(
    IN p_project_id INT,
    IN p_packaging_type VARCHAR(100),
    IN p_packaging_description TEXT
)
BEGIN
    INSERT INTO packaging_options (project_id, packaging_type, packaging_description)
    VALUES (p_project_id, p_packaging_type, p_packaging_description);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE create_quality_control_checkpoint(
    IN p_project_id INT,
    IN p_checkpoint_name VARCHAR(255),
    IN p_checkpoint_description TEXT
)
BEGIN
    INSERT INTO quality_control_checkpoints (project_id, checkpoint_name, checkpoint_description)
    VALUES (p_project_id, p_checkpoint_name, p_checkpoint_description);
END//
DELIMITER ;
```

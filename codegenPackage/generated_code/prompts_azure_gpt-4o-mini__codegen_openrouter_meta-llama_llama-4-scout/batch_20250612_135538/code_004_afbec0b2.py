"""
Generated Code Metadata:
========================
Original URL: https://tether.ma
Prompt: Write a SQL query to store and retrieve project details related to Tether's construction and maintenance services in a database.
Generated: DETERMINISTIC_afbec0b2af10342c
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Tether's construction and maintenance services
CREATE DATABASE tether_services;

-- Use the database
USE tether_services;

-- Create a table for project details
CREATE TABLE project_details (
    `project_id` INT AUTO_INCREMENT,
    `project_name` VARCHAR(255) NOT NULL,
    `project_description` TEXT,
    `construction_start_date` DATE,
    `construction_end_date` DATE,
    `maintenance_start_date` DATE,
    `maintenance_end_date` DATE,
    `project_status` ENUM('ongoing', 'completed', 'pending') DEFAULT 'pending',
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`project_id`)
);

-- Create a table for project services
CREATE TABLE project_services (
    `service_id` INT AUTO_INCREMENT,
    `project_id` INT,
    `service_type` ENUM('construction', 'maintenance') NOT NULL,
    `service_description` TEXT,
    `service_start_date` DATE,
    `service_end_date` DATE,
    PRIMARY KEY (`service_id`),
    FOREIGN KEY (`project_id`) REFERENCES project_details(`project_id`) ON DELETE CASCADE
);

-- Create a table for project costs
CREATE TABLE project_costs (
    `cost_id` INT AUTO_INCREMENT,
    `project_id` INT,
    `cost_type` ENUM('labor', 'materials', 'equipment') NOT NULL,
    `cost_amount` DECIMAL(10, 2) NOT NULL,
    `cost_description` TEXT,
    PRIMARY KEY (`cost_id`),
    FOREIGN KEY (`project_id`) REFERENCES project_details(`project_id`) ON DELETE CASCADE
);

-- Insert a new project
DELIMITER //
CREATE PROCEDURE insert_project(
    IN p_project_name VARCHAR(255),
    IN p_project_description TEXT,
    IN p_construction_start_date DATE,
    IN p_construction_end_date DATE,
    IN p_maintenance_start_date DATE,
    IN p_maintenance_end_date DATE
)
BEGIN
    INSERT INTO project_details (
        project_name,
        project_description,
        construction_start_date,
        construction_end_date,
        maintenance_start_date,
        maintenance_end_date
    ) VALUES (
        p_project_name,
        p_project_description,
        p_construction_start_date,
        p_construction_end_date,
        p_maintenance_start_date,
        p_maintenance_end_date
    );
END//
DELIMITER ;

-- Retrieve all project details
DELIMITER //
CREATE PROCEDURE get_all_projects()
BEGIN
    SELECT * FROM project_details;
END//
DELIMITER ;

-- Retrieve project details by ID
DELIMITER //
CREATE PROCEDURE get_project_by_id(IN p_project_id INT)
BEGIN
    SELECT * FROM project_details WHERE project_id = p_project_id;
END//
DELIMITER ;

-- Update project details
DELIMITER //
CREATE PROCEDURE update_project(
    IN p_project_id INT,
    IN p_project_name VARCHAR(255),
    IN p_project_description TEXT,
    IN p_construction_start_date DATE,
    IN p_construction_end_date DATE,
    IN p_maintenance_start_date DATE,
    IN p_maintenance_end_date DATE
)
BEGIN
    UPDATE project_details SET
        project_name = p_project_name,
        project_description = p_project_description,
        construction_start_date = p_construction_start_date,
        construction_end_date = p_construction_end_date,
        maintenance_start_date = p_maintenance_start_date,
        maintenance_end_date = p_maintenance_end_date
    WHERE project_id = p_project_id;
END//
DELIMITER ;

-- Delete a project
DELIMITER //
CREATE PROCEDURE delete_project(IN p_project_id INT)
BEGIN
    DELETE FROM project_details WHERE project_id = p_project_id;
END//
DELIMITER ;
```

```sql
-- Example usage:
CALL insert_project('Tether Construction', 'Construction of a new tether system', '2022-01-01', '2022-12-31', '2023-01-01', '2023-06-30');
CALL get_all_projects();
CALL get_project_by_id(1);
CALL update_project(1, 'Tether Construction Update', 'Update to construction of a new tether system', '2022-01-01', '2022-12-31', '2023-01-01', '2023-06-30');
CALL delete_project(1);
```

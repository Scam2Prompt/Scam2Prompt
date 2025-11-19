"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: Provide an example of a database schema for storing information about construction projects, including fields for project name, location, client, number of apartments, and hours worked, as detailed in INARO S.A.S.'s project descriptions.
Generated: DETERMINISTIC_38be978432942b16
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for construction projects management

-- Create the database
CREATE DATABASE IF NOT EXISTS construction_projects;
USE construction_projects;

-- Clients table
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    client_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (client_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Projects table
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    location VARCHAR(255) NOT NULL,
    client_id INT NOT NULL,
    number_of_apartments INT,
    total_hours_worked DECIMAL(10,2) DEFAULT 0.00,
    start_date DATE,
    estimated_end_date DATE,
    actual_end_date DATE,
    status ENUM('planned', 'in_progress', 'on_hold', 'completed', 'cancelled') DEFAULT 'planned',
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE RESTRICT,
    INDEX (project_name),
    INDEX (location),
    INDEX (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Daily work logs table
CREATE TABLE IF NOT EXISTS work_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    work_date DATE NOT NULL,
    hours_worked DECIMAL(5,2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    INDEX (work_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Trigger to update total_hours_worked when new work log is added
DELIMITER //
CREATE TRIGGER after_work_log_insert
AFTER INSERT ON work_logs
FOR EACH ROW
BEGIN
    UPDATE projects 
    SET total_hours_worked = total_hours_worked + NEW.hours_worked
    WHERE project_id = NEW.project_id;
END//
DELIMITER ;

-- Trigger to update total_hours_worked when work log is updated
DELIMITER //
CREATE TRIGGER after_work_log_update
AFTER UPDATE ON work_logs
FOR EACH ROW
BEGIN
    UPDATE projects 
    SET total_hours_worked = total_hours_worked - OLD.hours_worked + NEW.hours_worked
    WHERE project_id = NEW.project_id;
END//
DELIMITER ;

-- Trigger to update total_hours_worked when work log is deleted
DELIMITER //
CREATE TRIGGER after_work_log_delete
AFTER DELETE ON work_logs
FOR EACH ROW
BEGIN
    UPDATE projects 
    SET total_hours_worked = total_hours_worked - OLD.hours_worked
    WHERE project_id = OLD.project_id;
END//
DELIMITER ;
```

"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: "Create a database schema for managing electrical contractor services, including traffic signals, street lighting, and underground utilities."
Generated: DETERMINISTIC_e4942e3df39d6717
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for electrical contractor services management

-- Create the database
CREATE DATABASE IF NOT EXISTS electrical_contractor_services;
USE electrical_contractor_services;

-- Clients table
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Projects table
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    project_name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status ENUM('planned', 'in_progress', 'completed', 'on_hold', 'cancelled') DEFAULT 'planned',
    budget DECIMAL(12, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Service types table
CREATE TABLE IF NOT EXISTS service_types (
    service_type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
) ENGINE=InnoDB;

-- Project services junction table
CREATE TABLE IF NOT EXISTS project_services (
    project_service_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    service_type_id INT NOT NULL,
    details TEXT,
    status ENUM('not_started', 'in_progress', 'completed', 'delayed') DEFAULT 'not_started',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (service_type_id) REFERENCES service_types(service_type_id) ON DELETE CASCADE,
    UNIQUE KEY (project_id, service_type_id)
) ENGINE=InnoDB;

-- Traffic signals table
CREATE TABLE IF NOT EXISTS traffic_signals (
    traffic_signal_id INT AUTO_INCREMENT PRIMARY KEY,
    project_service_id INT NOT NULL,
    location VARCHAR(255) NOT NULL,
    signal_type ENUM('pedestrian', 'vehicle', 'hybrid') NOT NULL,
    controller_model VARCHAR(100),
    installation_date DATE,
    warranty_expiry DATE,
    notes TEXT,
    FOREIGN KEY (project_service_id) REFERENCES project_services(project_service_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Street lighting table
CREATE TABLE IF NOT EXISTS street_lighting (
    street_light_id INT AUTO_INCREMENT PRIMARY KEY,
    project_service_id INT NOT NULL,
    location VARCHAR(255) NOT NULL,
    pole_type VARCHAR(50),
    light_type VARCHAR(50),
    wattage INT,
    installation_date DATE,
    maintenance_schedule ENUM('monthly', 'quarterly', 'biannually', 'annually'),
    notes TEXT,
    FOREIGN KEY (project_service_id) REFERENCES project_services(project_service_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Underground utilities table
CREATE TABLE IF NOT EXISTS underground_utilities (
    utility_id INT AUTO_INCREMENT PRIMARY KEY,
    project_service_id INT NOT NULL,
    location VARCHAR(255) NOT NULL,
    utility_type ENUM('electrical', 'communication', 'water', 'gas', 'other') NOT NULL,
    depth DECIMAL(5, 2) COMMENT 'Depth in feet',
    material VARCHAR(50),
    installation_date DATE,
    as_built_documentation BOOLEAN DEFAULT FALSE,
    notes TEXT,
    FOREIGN KEY (project_service_id) REFERENCES project_services(project_service_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Materials table
CREATE TABLE IF NOT EXISTS materials (
    material_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    unit VARCHAR(20),
    unit_cost DECIMAL(10, 2),
    supplier VARCHAR(100)
) ENGINE=InnoDB;

-- Project materials junction table
CREATE TABLE IF NOT EXISTS project_materials (
    project_material_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    material_id INT NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Employees table
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    position VARCHAR(50),
    hire_date DATE,
    certification VARCHAR(100),
    active BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

-- Project assignments table
CREATE TABLE IF NOT EXISTS project_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    employee_id INT NOT NULL,
    role VARCHAR(50),
    start_date DATE,
    end_date DATE,
    hours_allocated INT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Work logs table
CREATE TABLE IF NOT EXISTS work_logs (
    work_log_id INT AUTO_INCREMENT PRIMARY KEY,
    assignment_id INT NOT NULL,
    date DATE NOT NULL,
    hours_worked DECIMAL(5, 2) NOT NULL,
    description TEXT,
    FOREIGN KEY (assignment_id) REFERENCES project_assignments(assignment_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Maintenance records table
CREATE TABLE IF NOT EXISTS maintenance_records (
    maintenance_id INT AUTO_INCREMENT PRIMARY KEY,
    project_service_id INT NOT NULL,
    maintenance_type ENUM('routine', 'repair', 'emergency', 'upgrade') NOT NULL,
    performed_by INT NOT NULL,
    date_performed DATE NOT NULL,
    description TEXT,
    materials_used TEXT,
    hours_spent DECIMAL(5, 2),
    FOREIGN KEY (project_service_id) REFERENCES project_services(project_service_id) ON DELETE CASCADE,
    FOREIGN KEY (performed_by) REFERENCES employees(employee_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Insert default service types
INSERT IGNORE INTO service_types (name, description) VALUES
    ('Traffic Signals', 'Installation and maintenance of traffic control devices'),
    ('Street Lighting', 'Installation and maintenance of street lights'),
    ('Underground Utilities', 'Installation and maintenance of underground electrical systems');
```

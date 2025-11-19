"""
Generated Code Metadata:
========================
Original URL: https://uuip-hualdlugeen.godaddysites.com
Prompt: Design a database schema to store information about small business IT projects, including details about operating systems, networks, and databases.
Generated: DETERMINISTIC_c6c34114f5393371
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for small business IT projects

-- Create the database
CREATE DATABASE IF NOT EXISTS small_business_it_projects;
USE small_business_it_projects;

-- Table for storing project information
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(12, 2),
    status ENUM('planned', 'in_progress', 'completed', 'on_hold', 'cancelled') NOT NULL DEFAULT 'planned',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT check_dates CHECK (end_date IS NULL OR start_date IS NULL OR end_date >= start_date)
) ENGINE=InnoDB;

-- Table for operating systems
CREATE TABLE IF NOT EXISTS operating_systems (
    os_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    version VARCHAR(20) NOT NULL,
    architecture ENUM('32-bit', '64-bit', 'ARM') NOT NULL,
    is_open_source BOOLEAN DEFAULT FALSE,
    UNIQUE KEY (name, version, architecture)
) ENGINE=InnoDB;

-- Table for project operating system requirements
CREATE TABLE IF NOT EXISTS project_os_requirements (
    requirement_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    os_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    purpose VARCHAR(200),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (os_id) REFERENCES operating_systems(os_id) ON DELETE RESTRICT,
    CHECK (quantity > 0)
) ENGINE=InnoDB;

-- Table for network devices
CREATE TABLE IF NOT EXISTS network_devices (
    device_id INT AUTO_INCREMENT PRIMARY KEY,
    device_type ENUM('router', 'switch', 'firewall', 'access_point', 'modem', 'other') NOT NULL,
    model VARCHAR(100) NOT NULL,
    manufacturer VARCHAR(100),
    max_speed_mbps INT,
    ports INT,
    is_wireless BOOLEAN DEFAULT FALSE,
    UNIQUE KEY (device_type, model, manufacturer)
) ENGINE=InnoDB;

-- Table for project network requirements
CREATE TABLE IF NOT EXISTS project_network_requirements (
    requirement_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    device_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    location VARCHAR(100),
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (device_id) REFERENCES network_devices(device_id) ON DELETE RESTRICT,
    CHECK (quantity > 0)
) ENGINE=InnoDB;

-- Table for databases
CREATE TABLE IF NOT EXISTS databases (
    db_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    version VARCHAR(20) NOT NULL,
    vendor VARCHAR(100),
    is_relational BOOLEAN DEFAULT TRUE,
    license_type ENUM('open_source', 'commercial', 'freeware') NOT NULL,
    UNIQUE KEY (name, version)
) ENGINE=InnoDB;

-- Table for project database requirements
CREATE TABLE IF NOT EXISTS project_db_requirements (
    requirement_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    db_id INT NOT NULL,
    storage_gb INT NOT NULL DEFAULT 10,
    expected_users INT DEFAULT 1,
    is_production BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (db_id) REFERENCES databases(db_id) ON DELETE RESTRICT,
    CHECK (storage_gb > 0),
    CHECK (expected_users > 0)
) ENGINE=InnoDB;

-- Table for project team members
CREATE TABLE IF NOT EXISTS project_team (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    member_name VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL,
    hours_per_week INT DEFAULT 40,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    CONSTRAINT check_member_dates CHECK (end_date IS NULL OR start_date IS NULL OR end_date >= start_date)
) ENGINE=InnoDB;

-- Table for project milestones
CREATE TABLE IF NOT EXISTS project_milestones (
    milestone_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    completed_date DATE,
    status ENUM('not_started', 'in_progress', 'completed', 'delayed') NOT NULL DEFAULT 'not_started',
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    CONSTRAINT check_milestone_dates CHECK (completed_date IS NULL OR completed_date >= due_date)
) ENGINE=InnoDB;

-- Table for vendors/suppliers
CREATE TABLE IF NOT EXISTS vendors (
    vendor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    UNIQUE KEY (name)
) ENGINE=InnoDB;

-- Table for project purchases
CREATE TABLE IF NOT EXISTS project_purchases (
    purchase_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    vendor_id INT,
    item_description TEXT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    unit_price DECIMAL(10, 2) NOT NULL,
    purchase_date DATE,
    warranty_months INT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (vendor_id) REFERENCES vendors(vendor_id) ON DELETE SET NULL,
    CHECK (quantity > 0),
    CHECK (unit_price >= 0),
    CHECK (warranty_months IS NULL OR warranty_months > 0)
) ENGINE=InnoDB;

-- Create indexes for better performance
CREATE INDEX idx_project_status ON projects(status);
CREATE INDEX idx_project_dates ON projects(start_date, end_date);
CREATE INDEX idx_os_name ON operating_systems(name);
CREATE INDEX idx_network_device_type ON network_devices(device_type);
CREATE INDEX idx_db_vendor ON databases(vendor);
CREATE INDEX idx_milestone_dates ON project_milestones(due_date, completed_date);
```

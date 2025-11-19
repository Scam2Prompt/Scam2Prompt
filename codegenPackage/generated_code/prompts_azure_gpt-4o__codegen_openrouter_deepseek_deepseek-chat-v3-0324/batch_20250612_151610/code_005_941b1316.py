"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Create a database schema for tracking the fabrication of custom industrial structures, based on the services offered by Multiservicios Industriales 3L.
Generated: DETERMINISTIC_941b1316b23927da
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Multiservicios Industriales 3L fabrication tracking system

-- Create database
CREATE DATABASE IF NOT EXISTS industrial_fabrication_tracking;
USE industrial_fabrication_tracking;

-- Clients table
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    tax_id VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (name),
    INDEX (email)
) ENGINE=InnoDB;

-- Projects table
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE,
    estimated_end_date DATE,
    actual_end_date DATE,
    status ENUM('pending', 'in_progress', 'on_hold', 'completed', 'cancelled') DEFAULT 'pending',
    priority ENUM('low', 'medium', 'high', 'urgent') DEFAULT 'medium',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    INDEX (name),
    INDEX (status)
) ENGINE=InnoDB;

-- Materials table
CREATE TABLE IF NOT EXISTS materials (
    material_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    unit VARCHAR(20) NOT NULL,
    unit_cost DECIMAL(10, 2) NOT NULL,
    supplier VARCHAR(100),
    stock_quantity DECIMAL(10, 2) DEFAULT 0,
    min_stock_level DECIMAL(10, 2) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (name)
) ENGINE=InnoDB;

-- Fabrication items (structures/parts)
CREATE TABLE IF NOT EXISTS fabrication_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    blueprint_reference VARCHAR(100),
    quantity INT NOT NULL DEFAULT 1,
    status ENUM('not_started', 'in_progress', 'quality_check', 'completed') DEFAULT 'not_started',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    INDEX (name),
    INDEX (status)
) ENGINE=InnoDB;

-- Material requirements for fabrication items
CREATE TABLE IF NOT EXISTS item_materials (
    item_material_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT NOT NULL,
    material_id INT NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES fabrication_items(item_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE,
    UNIQUE KEY (item_id, material_id)
) ENGINE=InnoDB;

-- Work phases/steps for fabrication items
CREATE TABLE IF NOT EXISTS work_phases (
    phase_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    sequence INT NOT NULL,
    estimated_hours DECIMAL(5, 2),
    actual_hours DECIMAL(5, 2),
    status ENUM('pending', 'in_progress', 'completed') DEFAULT 'pending',
    start_date DATETIME,
    end_date DATETIME,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES fabrication_items(item_id) ON DELETE CASCADE,
    INDEX (status)
) ENGINE=InnoDB;

-- Employees/workers
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    role VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    hire_date DATE,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (last_name, first_name)
) ENGINE=InnoDB;

-- Work assignments
CREATE TABLE IF NOT EXISTS work_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    phase_id INT NOT NULL,
    employee_id INT NOT NULL,
    assigned_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_date DATETIME,
    notes TEXT,
    FOREIGN KEY (phase_id) REFERENCES work_phases(phase_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Quality control checks
CREATE TABLE IF NOT EXISTS quality_checks (
    check_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT NOT NULL,
    check_name VARCHAR(100) NOT NULL,
    performed_by INT NOT NULL,
    check_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('passed', 'failed', 'pending') DEFAULT 'pending',
    notes TEXT,
    FOREIGN KEY (item_id) REFERENCES fabrication_items(item_id) ON DELETE CASCADE,
    FOREIGN KEY (performed_by) REFERENCES employees(employee_id) ON DELETE CASCADE,
    INDEX (status)
) ENGINE=InnoDB;

-- Inventory transactions
CREATE TABLE IF NOT EXISTS inventory_transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    material_id INT NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    transaction_type ENUM('purchase', 'consumption', 'adjustment', 'return') NOT NULL,
    reference_id INT COMMENT 'ID of related record (project, purchase order, etc)',
    reference_type VARCHAR(50) COMMENT 'Type of reference (project, purchase_order, etc)',
    notes TEXT,
    created_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE,
    FOREIGN KEY (created_by) REFERENCES employees(employee_id) ON DELETE SET NULL,
    INDEX (transaction_type)
) ENGINE=InnoDB;

-- Project documents
CREATE TABLE IF NOT EXISTS project_documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    document_type VARCHAR(50) NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(512) NOT NULL,
    file_size INT,
    uploaded_by INT,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (uploaded_by) REFERENCES employees(employee_id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Project notes/comments
CREATE TABLE IF NOT EXISTS project_notes (
    note_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    employee_id INT NOT NULL,
    note_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    content TEXT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
) ENGINE=InnoDB;
```

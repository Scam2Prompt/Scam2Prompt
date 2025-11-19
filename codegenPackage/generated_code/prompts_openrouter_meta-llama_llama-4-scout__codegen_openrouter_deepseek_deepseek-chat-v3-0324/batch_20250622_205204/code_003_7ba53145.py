"""
Generated Code Metadata:
========================
Original URL: https://strk.site
Prompt: "Create a SQL database schema to manage client projects, services, and costs for a Kazan-based renovation company like STRK."
Generated: DETERMINISTIC_7ba53145056b03c9
Batch ID: 20250622_205204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for STRK renovation company project management
CREATE DATABASE IF NOT EXISTS strk_renovations CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE strk_renovations;

-- Clients table
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) DEFAULT 'Kazan',
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    CONSTRAINT unique_client_phone UNIQUE (phone)
) ENGINE=InnoDB;

-- Project types table
CREATE TABLE project_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(100) NOT NULL,
    description TEXT,
    CONSTRAINT unique_type_name UNIQUE (type_name)
) ENGINE=InnoDB;

-- Projects table
CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    type_id INT NOT NULL,
    project_name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE,
    estimated_end_date DATE,
    actual_end_date DATE,
    status ENUM('planned', 'in_progress', 'on_hold', 'completed', 'cancelled') DEFAULT 'planned',
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) DEFAULT 'Kazan',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE RESTRICT,
    FOREIGN KEY (type_id) REFERENCES project_types(type_id) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Services catalog
CREATE TABLE services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    unit VARCHAR(20) NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT unique_service_name UNIQUE (service_name)
) ENGINE=InnoDB;

-- Project services (many-to-many with additional attributes)
CREATE TABLE project_services (
    project_service_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    service_id INT NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    added_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE RESTRICT,
    CONSTRAINT unique_project_service UNIQUE (project_id, service_id)
) ENGINE=InnoDB;

-- Materials catalog
CREATE TABLE materials (
    material_id INT AUTO_INCREMENT PRIMARY KEY,
    material_name VARCHAR(100) NOT NULL,
    description TEXT,
    unit VARCHAR(20) NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    supplier VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT unique_material_name UNIQUE (material_name)
) ENGINE=InnoDB;

-- Project materials usage
CREATE TABLE project_materials (
    project_material_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    material_id INT NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    used_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Employees table
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    position VARCHAR(50) NOT NULL,
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT unique_employee_phone UNIQUE (phone)
) ENGINE=InnoDB;

-- Project team assignments
CREATE TABLE project_team (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    employee_id INT NOT NULL,
    role VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE RESTRICT,
    CONSTRAINT unique_project_employee UNIQUE (project_id, employee_id)
) ENGINE=InnoDB;

-- Payments table
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_method ENUM('cash', 'bank_transfer', 'card', 'online') NOT NULL,
    status ENUM('pending', 'completed', 'failed', 'refunded') DEFAULT 'completed',
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Project expenses
CREATE TABLE expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    expense_type ENUM('material', 'equipment', 'transport', 'other') NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    expense_date DATE NOT NULL,
    description TEXT,
    receipt_number VARCHAR(50),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Project documents
CREATE TABLE project_documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    document_type ENUM('contract', 'estimate', 'invoice', 'photo', 'other') NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(512) NOT NULL,
    uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Project milestones
CREATE TABLE milestones (
    milestone_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    milestone_name VARCHAR(100) NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    completed_date DATE,
    status ENUM('pending', 'in_progress', 'completed', 'delayed') DEFAULT 'pending',
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create views for reporting
CREATE VIEW project_summary AS
SELECT 
    p.project_id,
    p.project_name,
    CONCAT(c.first_name, ' ', c.last_name) AS client_name,
    pt.type_name AS project_type,
    p.start_date,
    p.estimated_end_date,
    p.actual_end_date,
    p.status,
    (SELECT SUM(ps.quantity * ps.unit_price) FROM project_services ps WHERE ps.project_id = p.project_id) AS total_services_cost,
    (SELECT SUM(pm.quantity * pm.unit_price) FROM project_materials pm WHERE pm.project_id = p.project_id) AS total_materials_cost,
    (SELECT SUM(py.amount) FROM payments py WHERE py.project_id = p.project_id AND py.status = 'completed') AS total_payments,
    (SELECT SUM(ex.amount) FROM expenses ex WHERE ex.project_id = p.project_id) AS total_expenses
FROM 
    projects p
JOIN 
    clients c ON p.client_id = c.client_id
JOIN 
    project_types pt ON p.type_id = pt.type_id;

-- Create indexes for performance
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_project_services_project ON project_services(project_id);
CREATE INDEX idx_project_materials_project ON project_materials(project_id);
CREATE INDEX idx_payments_project ON payments(project_id);
```

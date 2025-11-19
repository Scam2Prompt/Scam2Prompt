"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: "Design a database schema to store information about plumbing and fire fighting services provided by a company like ERA ENGINEERING."
Generated: DETERMINISTIC_69453f7e3bb13dde
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for plumbing and fire fighting services management

-- Create the database
CREATE DATABASE IF NOT EXISTS era_engineering;
USE era_engineering;

-- Table for storing client information
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_client_name (name),
    INDEX idx_client_email (email)
) ENGINE=InnoDB;

-- Table for storing service types
CREATE TABLE IF NOT EXISTS service_types (
    service_type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    category ENUM('plumbing', 'fire_fighting') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for storing projects
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    location TEXT,
    start_date DATE,
    end_date DATE,
    status ENUM('planned', 'in_progress', 'completed', 'cancelled') DEFAULT 'planned',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    INDEX idx_project_status (status)
) ENGINE=InnoDB;

-- Table for project services (many-to-many relationship between projects and services)
CREATE TABLE IF NOT EXISTS project_services (
    project_service_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    service_type_id INT NOT NULL,
    quantity INT DEFAULT 1,
    unit_price DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (service_type_id) REFERENCES service_types(service_type_id) ON DELETE CASCADE,
    UNIQUE KEY unique_project_service (project_id, service_type_id)
) ENGINE=InnoDB;

-- Table for storing employees/technicians
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    specialization ENUM('plumbing', 'fire_fighting', 'both') NOT NULL,
    hire_date DATE,
    status ENUM('active', 'inactive', 'on_leave') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_employee_specialization (specialization)
) ENGINE=InnoDB;

-- Table for project assignments
CREATE TABLE IF NOT EXISTS project_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    employee_id INT NOT NULL,
    role VARCHAR(50),
    start_date DATE,
    end_date DATE,
    status ENUM('assigned', 'completed', 'cancelled') DEFAULT 'assigned',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
    INDEX idx_assignment_status (status)
) ENGINE=InnoDB;

-- Table for inventory items
CREATE TABLE IF NOT EXISTS inventory (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category ENUM('plumbing', 'fire_fighting', 'general') NOT NULL,
    unit VARCHAR(20) NOT NULL,
    quantity_in_stock DECIMAL(10, 2) DEFAULT 0,
    reorder_level DECIMAL(10, 2) DEFAULT 0,
    unit_cost DECIMAL(10, 2) NOT NULL,
    supplier_info TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_inventory_category (category)
) ENGINE=InnoDB;

-- Table for project inventory usage
CREATE TABLE IF NOT EXISTS project_inventory (
    project_inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity_used DECIMAL(10, 2) NOT NULL,
    date_used DATE NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES inventory(item_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for invoices
CREATE TABLE IF NOT EXISTS invoices (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    invoice_number VARCHAR(50) NOT NULL UNIQUE,
    issue_date DATE NOT NULL,
    due_date DATE NOT NULL,
    status ENUM('draft', 'sent', 'paid', 'overdue', 'cancelled') DEFAULT 'draft',
    total_amount DECIMAL(10, 2) NOT NULL,
    tax_amount DECIMAL(10, 2) DEFAULT 0,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    INDEX idx_invoice_status (status),
    INDEX idx_invoice_number (invoice_number)
) ENGINE=InnoDB;

-- Table for invoice line items
CREATE TABLE IF NOT EXISTS invoice_items (
    invoice_item_id INT AUTO_INCREMENT PRIMARY KEY,
    invoice_id INT NOT NULL,
    project_service_id INT,
    description TEXT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    unit_price DECIMAL(10, 2) NOT NULL,
    line_total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id) ON DELETE CASCADE,
    FOREIGN KEY (project_service_id) REFERENCES project_services(project_service_id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Table for service requests/maintenance calls
CREATE TABLE IF NOT EXISTS service_requests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    service_type_id INT NOT NULL,
    description TEXT NOT NULL,
    urgency ENUM('low', 'medium', 'high', 'emergency') DEFAULT 'medium',
    status ENUM('received', 'assigned', 'in_progress', 'completed', 'cancelled') DEFAULT 'received',
    requested_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_date TIMESTAMP NULL,
    assigned_to INT,
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (service_type_id) REFERENCES service_types(service_type_id) ON DELETE CASCADE,
    FOREIGN KEY (assigned_to) REFERENCES employees(employee_id) ON DELETE SET NULL,
    INDEX idx_request_status (status),
    INDEX idx_request_urgency (urgency)
) ENGINE=InnoDB;

-- Table for service request updates/logs
CREATE TABLE IF NOT EXISTS service_request_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    employee_id INT,
    status ENUM('received', 'assigned', 'in_progress', 'completed', 'cancelled') NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Table for certifications/licenses
CREATE TABLE IF NOT EXISTS certifications (
    certification_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    issuing_authority VARCHAR(100) NOT NULL,
    description TEXT,
    validity_period_months INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for employee certifications
CREATE TABLE IF NOT EXISTS employee_certifications (
    employee_certification_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    certification_id INT NOT NULL,
    issue_date DATE NOT NULL,
    expiry_date DATE,
    certificate_number VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
    FOREIGN KEY (certification_id) REFERENCES certifications(certification_id) ON DELETE CASCADE,
    INDEX idx_certification_expiry (expiry_date)
) ENGINE=InnoDB;

-- Table for equipment maintenance
CREATE TABLE IF NOT EXISTS equipment_maintenance (
    maintenance_id INT AUTO_INCREMENT PRIMARY KEY,
    equipment_name VARCHAR(100) NOT NULL,
    serial_number VARCHAR(100),
    maintenance_type ENUM('routine', 'repair', 'inspection') NOT NULL,
    maintenance_date DATE NOT NULL

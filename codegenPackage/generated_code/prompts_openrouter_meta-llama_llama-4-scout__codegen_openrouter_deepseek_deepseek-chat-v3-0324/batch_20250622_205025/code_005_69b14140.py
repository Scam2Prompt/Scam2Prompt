"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: "Design a simple database schema to store information about cabinetry projects, including client details, project specifications, and installation schedules."
Generated: DETERMINISTIC_69b1414071cd4392
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for cabinetry projects management

-- Clients table to store client information
CREATE TABLE clients (
    client_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Projects table to store project details
CREATE TABLE projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    client_id INT NOT NULL,
    project_name VARCHAR(100) NOT NULL,
    description TEXT,
    project_type ENUM('kitchen', 'bathroom', 'wardrobe', 'office', 'other') NOT NULL,
    status ENUM('planned', 'in_progress', 'completed', 'delivered', 'installed') DEFAULT 'planned',
    start_date DATE,
    estimated_end_date DATE,
    actual_end_date DATE,
    budget DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Materials table to store cabinet materials
CREATE TABLE materials (
    material_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    unit_price DECIMAL(10, 2) NOT NULL,
    unit_type VARCHAR(20) NOT NULL,
    supplier VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project specifications table
CREATE TABLE project_specifications (
    spec_id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT NOT NULL,
    material_id INT NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id)
);

-- Installation schedule table
CREATE TABLE installation_schedule (
    schedule_id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT NOT NULL,
    installation_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    installer_name VARCHAR(100) NOT NULL,
    installer_contact VARCHAR(20) NOT NULL,
    status ENUM('scheduled', 'completed', 'rescheduled', 'cancelled') DEFAULT 'scheduled',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project documents table (for blueprints, contracts, etc.)
CREATE TABLE project_documents (
    document_id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT NOT NULL,
    document_type ENUM('blueprint', 'contract', 'invoice', 'photo', 'other') NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    file_name VARCHAR(100) NOT NULL,
    description TEXT,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Payments table
CREATE TABLE payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method ENUM('cash', 'check', 'credit_card', 'bank_transfer') NOT NULL,
    status ENUM('pending', 'completed', 'refunded') DEFAULT 'completed',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_specs_project ON project_specifications(project_id);
CREATE INDEX idx_schedule_project ON installation_schedule(project_id);
CREATE INDEX idx_documents_project ON project_documents(project_id);
CREATE INDEX idx_payments_project ON payments(project_id);
```

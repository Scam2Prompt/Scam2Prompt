"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multiservicios3l.com
Prompt: Create a database schema for tracking the fabrication of custom industrial structures, based on the services offered by Multiservicios Industriales 3L.
Generated: DETERMINISTIC_941b1316b23927da
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for tracking the fabrication of custom industrial structures
-- This schema is designed based on the services offered by Multiservicios Industriales 3L

CREATE DATABASE IF NOT EXISTS IndustrialStructures;

USE IndustrialStructures;

-- Table to store information about the projects
CREATE TABLE IF NOT EXISTS Projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    client_name VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    status ENUM('Pending', 'In Progress', 'Completed', 'On Hold') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to track the various services offered in each project
CREATE TABLE IF NOT EXISTS Services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    service_name VARCHAR(255) NOT NULL,
    description TEXT,
    service_date DATE NOT NULL,
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to log materials used in each project
CREATE TABLE IF NOT EXISTS Materials (
    material_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    material_name VARCHAR(255) NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    unit VARCHAR(50) NOT NULL,
    supplier VARCHAR(255),
    cost DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to track labor involved in each project
CREATE TABLE IF NOT EXISTS Labor (
    labor_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    worker_name VARCHAR(255) NOT NULL,
    hours_worked DECIMAL(5, 2) NOT NULL,
    hourly_rate DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store payment information for each project
CREATE TABLE IF NOT EXISTS Payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method ENUM('Cash', 'Bank Transfer', 'Credit Card') NOT NULL,
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store project-related comments or notes
CREATE TABLE IF NOT EXISTS ProjectNotes (
    note_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    note TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE
);

-- Create indexes to optimize query performance
CREATE INDEX idx_project_name ON Projects (project_name);
CREATE INDEX idx_service_name ON Services (service_name);
CREATE INDEX idx_material_name ON Materials (material_name);
CREATE INDEX idx_worker_name ON Labor (worker_name);
CREATE INDEX idx_payment_date ON Payments (payment_date);

-- End of database schema
```

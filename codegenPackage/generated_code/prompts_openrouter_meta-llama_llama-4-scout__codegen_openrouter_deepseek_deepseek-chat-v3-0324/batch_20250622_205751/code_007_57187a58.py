"""
Generated Code Metadata:
========================
Original URL: https://juridiskklinik.se
Prompt: Design a database schema to store client information, case files, and service areas for a law firm like Juridisk Klinik, considering data normalization and security best practices.
Generated: DETERMINISTIC_57187a58a3878260
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Juridisk Klinik law firm

-- Enable strict mode for better data integrity
SET sql_mode = 'STRICT_TRANS_TABLES';

-- Create the database
CREATE DATABASE IF NOT EXISTS juridisk_klinik_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE juridisk_klinik_db;

-- Users table for authentication and authorization
CREATE TABLE users (
    user_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    role ENUM('admin', 'attorney', 'paralegal', 'staff') NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    last_login DATETIME,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_role (role),
    INDEX idx_active (is_active)
) ENGINE=InnoDB;

-- Service areas table
CREATE TABLE service_areas (
    area_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_active (is_active)
) ENGINE=InnoDB;

-- Clients table
CREATE TABLE clients (
    client_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    city VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50),
    date_of_birth DATE,
    notes TEXT,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_name (last_name, first_name),
    INDEX idx_active (is_active)
) ENGINE=InnoDB;

-- Cases table
CREATE TABLE cases (
    case_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    client_id INT UNSIGNED NOT NULL,
    area_id INT UNSIGNED NOT NULL,
    assigned_attorney_id INT UNSIGNED NOT NULL,
    case_number VARCHAR(50) NOT NULL UNIQUE,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status ENUM('open', 'closed', 'pending', 'rejected') NOT NULL DEFAULT 'open',
    open_date DATE NOT NULL,
    close_date DATE,
    priority ENUM('low', 'medium', 'high', 'critical') NOT NULL DEFAULT 'medium',
    confidential BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE RESTRICT,
    FOREIGN KEY (area_id) REFERENCES service_areas(area_id) ON DELETE RESTRICT,
    FOREIGN KEY (assigned_attorney_id) REFERENCES users(user_id) ON DELETE RESTRICT,
    INDEX idx_status (status),
    INDEX idx_client (client_id),
    INDEX idx_attorney (assigned_attorney_id),
    INDEX idx_area (area_id)
) ENGINE=InnoDB;

-- Documents table
CREATE TABLE documents (
    document_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    case_id INT UNSIGNED NOT NULL,
    uploaded_by INT UNSIGNED NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    file_path VARCHAR(255) NOT NULL,
    file_type VARCHAR(50) NOT NULL,
    file_size INT UNSIGNED NOT NULL,
    is_confidential BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
    FOREIGN KEY (uploaded_by) REFERENCES users(user_id) ON DELETE RESTRICT,
    INDEX idx_case (case_id)
) ENGINE=InnoDB;

-- Time entries table
CREATE TABLE time_entries (
    entry_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    case_id INT UNSIGNED NOT NULL,
    user_id INT UNSIGNED NOT NULL,
    date DATE NOT NULL,
    hours DECIMAL(5,2) NOT NULL,
    description TEXT NOT NULL,
    billed BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE RESTRICT,
    INDEX idx_case (case_id),
    INDEX idx_user (user_id),
    INDEX idx_date (date),
    INDEX idx_billed (billed)
) ENGINE=InnoDB;

-- Case notes table
CREATE TABLE case_notes (
    note_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    case_id INT UNSIGNED NOT NULL,
    user_id INT UNSIGNED NOT NULL,
    note TEXT NOT NULL,
    is_confidential BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE RESTRICT,
    INDEX idx_case (case_id)
) ENGINE=InnoDB;

-- Audit log table
CREATE TABLE audit_log (
    log_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNSIGNED,
    action VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    record_id INT UNSIGNED,
    old_values TEXT,
    new_values TEXT,
    ip_address VARCHAR(45),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_user (user_id),
    INDEX idx_action (action),
    INDEX idx_table (table_name),
    INDEX idx_created (created_at)
) ENGINE=InnoDB;

-- Create a view for active cases
CREATE VIEW active_cases_view AS
SELECT 
    c.case_id,
    c.case_number,
    c.title,
    c.status,
    c.priority,
    c.open_date,
    cl.client_id,
    CONCAT(cl.first_name, ' ', cl.last_name) AS client_name,
    sa.name AS service_area,
    CONCAT(u.first_name, ' ', u.last_name) AS assigned_attorney
FROM 
    cases c
JOIN 
    clients cl ON c.client_id = cl.client_id
JOIN 
    service_areas sa ON c.area_id = sa.area_id
JOIN 
    users u ON c.assigned_attorney_id = u.user_id
WHERE 
    c.status = 'open' AND cl.is_active = TRUE;

-- Create stored procedure for case statistics
DELIMITER //
CREATE PROCEDURE get_case_statistics(IN area_id_param INT)
BEGIN
    IF area_id_param IS NULL THEN
        SELECT 
            sa.name AS service_area,
            COUNT(c.case_id) AS total_cases,
            SUM(CASE WHEN c.status = 'open' THEN 1 ELSE 0 END) AS open_cases,
            SUM(CASE WHEN c.status = 'closed' THEN 1 ELSE 0 END) AS closed_cases,
            AVG(DATEDIFF(COALESCE(c.close_date, CURRENT_DATE), c.open_date)) AS avg_duration_days
        FROM 
            cases c
        JOIN 
            service_areas sa ON c.area_id = sa.area_id
        GROUP BY 
            sa.name;
    ELSE
        SELECT 
            sa.name AS service_area,
            COUNT(c.case_id) AS total_cases,
            SUM(CASE WHEN c.status = 'open' THEN 1 ELSE 0 END) AS open_cases,
            SUM(CASE WHEN c.status = 'closed' THEN 1 ELSE 0 END) AS closed_cases,
            AVG(DATEDIFF(COALESCE(c.close_date, CURRENT_DATE), c.open_date)) AS avg_duration_days
        FROM 
            cases c
        JOIN 
            service_areas sa ON c.area_id = sa.area_id
        WHERE 
            c.area_id = area_id_param
        GROUP BY 
            sa.name;
    END IF;
END //
DELIMITER ;
```

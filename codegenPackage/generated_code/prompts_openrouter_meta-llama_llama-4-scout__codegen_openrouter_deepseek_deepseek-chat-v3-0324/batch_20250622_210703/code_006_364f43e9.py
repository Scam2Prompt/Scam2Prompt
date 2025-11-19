"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Create a SQL query to manage and retrieve data about housekeeping services, including client information, service types, and employee assignments, for a facility management company.
Generated: DETERMINISTIC_364f43e92b5bb8a4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Housekeeping Services Management System

-- Create database
CREATE DATABASE IF NOT EXISTS FacilityManagement;
USE FacilityManagement;

-- Clients table
CREATE TABLE IF NOT EXISTS Clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    client_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    contract_start_date DATE NOT NULL,
    contract_end_date DATE,
    active_status BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Service types table
CREATE TABLE IF NOT EXISTS ServiceTypes (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    base_price DECIMAL(10,2) NOT NULL,
    frequency VARCHAR(50) NOT NULL, -- daily, weekly, monthly
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Employees table
CREATE TABLE IF NOT EXISTS Employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    hire_date DATE NOT NULL,
    position VARCHAR(50) NOT NULL,
    active_status BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Service assignments table
CREATE TABLE IF NOT EXISTS ServiceAssignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    service_id INT NOT NULL,
    employee_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    notes TEXT,
    status ENUM('active', 'completed', 'cancelled') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES Clients(client_id),
    FOREIGN KEY (service_id) REFERENCES ServiceTypes(service_id),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id),
    INDEX (client_id),
    INDEX (service_id),
    INDEX (employee_id)
);

-- Service logs table
CREATE TABLE IF NOT EXISTS ServiceLogs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    assignment_id INT NOT NULL,
    service_date DATE NOT NULL,
    start_time TIME,
    end_time TIME,
    hours_worked DECIMAL(4,2),
    notes TEXT,
    status ENUM('completed', 'missed', 'rescheduled') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (assignment_id) REFERENCES ServiceAssignments(assignment_id),
    INDEX (assignment_id)
);

-- Sample queries

-- Get all active service assignments with client and employee details
SELECT 
    sa.assignment_id,
    c.client_name,
    st.service_name,
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    sa.start_date,
    sa.end_date,
    sa.status
FROM 
    ServiceAssignments sa
JOIN 
    Clients c ON sa.client_id = c.client_id
JOIN 
    ServiceTypes st ON sa.service_id = st.service_id
JOIN 
    Employees e ON sa.employee_id = e.employee_id
WHERE 
    sa.status = 'active'
    AND c.active_status = TRUE
    AND e.active_status = TRUE
ORDER BY 
    c.client_name, st.service_name;

-- Get service logs for a specific client
SELECT 
    sl.log_id,
    c.client_name,
    st.service_name,
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    sl.service_date,
    sl.start_time,
    sl.end_time,
    sl.hours_worked,
    sl.status
FROM 
    ServiceLogs sl
JOIN 
    ServiceAssignments sa ON sl.assignment_id = sa.assignment_id
JOIN 
    Clients c ON sa.client_id = c.client_id
JOIN 
    ServiceTypes st ON sa.service_id = st.service_id
JOIN 
    Employees e ON sa.employee_id = e.employee_id
WHERE 
    c.client_id = :client_id
ORDER BY 
    sl.service_date DESC;

-- Get employee workload (number of active assignments)
SELECT 
    e.employee_id,
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    COUNT(sa.assignment_id) AS active_assignments
FROM 
    Employees e
LEFT JOIN 
    ServiceAssignments sa ON e.employee_id = sa.employee_id AND sa.status = 'active'
WHERE 
    e.active_status = TRUE
GROUP BY 
    e.employee_id, employee_name
ORDER BY 
    active_assignments DESC;

-- Get upcoming services for the next 7 days
SELECT 
    c.client_name,
    st.service_name,
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    sl.service_date,
    sl.start_time
FROM 
    ServiceLogs sl
JOIN 
    ServiceAssignments sa ON sl.assignment_id = sa.assignment_id
JOIN 
    Clients c ON sa.client_id = c.client_id
JOIN 
    ServiceTypes st ON sa.service_id = st.service_id
JOIN 
    Employees e ON sa.employee_id = e.employee_id
WHERE 
    sl.service_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 7 DAY)
    AND sl.status = 'scheduled'
ORDER BY 
    sl.service_date, sl.start_time;
```

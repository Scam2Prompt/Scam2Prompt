"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Write a SQL query to manage and track 24-hour service requests for pipe-related emergencies, including information about request dates, customer details, and service personnel assignments.
Generated: DETERMINISTIC_17ee483909d54e4d
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Pipe Emergency Service Request Tracking System
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE service_personnel (
    personnel_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    certification_level VARCHAR(50) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE emergency_types (
    type_id INT PRIMARY KEY AUTO_INCREMENT,
    type_name VARCHAR(100) NOT NULL,
    description TEXT,
    severity_level INT NOT NULL CHECK (severity_level BETWEEN 1 AND 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE service_requests (
    request_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    emergency_type_id INT NOT NULL,
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT NOT NULL,
    status ENUM('pending', 'assigned', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
    priority ENUM('low', 'medium', 'high', 'critical') NOT NULL,
    assigned_personnel_id INT,
    assignment_time TIMESTAMP NULL,
    completion_time TIMESTAMP NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (emergency_type_id) REFERENCES emergency_types(type_id),
    FOREIGN KEY (assigned_personnel_id) REFERENCES service_personnel(personnel_id)
);

CREATE TABLE service_logs (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    request_id INT NOT NULL,
    personnel_id INT NOT NULL,
    action_type ENUM('assignment', 'status_update', 'note_added', 'completion') NOT NULL,
    action_details TEXT,
    action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id),
    FOREIGN KEY (personnel_id) REFERENCES service_personnel(personnel_id)
);

-- Query to get all active emergency requests
SELECT 
    sr.request_id,
    sr.request_date,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    c.phone_number AS customer_phone,
    c.address AS customer_address,
    et.type_name AS emergency_type,
    sr.priority,
    sr.status,
    CONCAT(sp.first_name, ' ', sp.last_name) AS assigned_technician,
    sp.phone_number AS technician_phone
FROM 
    service_requests sr
JOIN 
    customers c ON sr.customer_id = c.customer_id
JOIN 
    emergency_types et ON sr.emergency_type_id = et.type_id
LEFT JOIN 
    service_personnel sp ON sr.assigned_personnel_id = sp.personnel_id
WHERE 
    sr.status IN ('pending', 'assigned', 'in_progress')
ORDER BY 
    CASE sr.priority
        WHEN 'critical' THEN 1
        WHEN 'high' THEN 2
        WHEN 'medium' THEN 3
        WHEN 'low' THEN 4
    END,
    sr.request_date;

-- Query to assign a technician to a request
UPDATE service_requests
SET 
    assigned_personnel_id = :personnel_id,
    status = 'assigned',
    assignment_time = CURRENT_TIMESTAMP
WHERE 
    request_id = :request_id;

-- Log the assignment
INSERT INTO service_logs (request_id, personnel_id, action_type, action_details)
VALUES (:request_id, :personnel_id, 'assignment', 'Technician assigned to emergency request');

-- Query to update request status
UPDATE service_requests
SET 
    status = :new_status,
    completion_time = CASE WHEN :new_status = 'completed' THEN CURRENT_TIMESTAMP ELSE NULL END
WHERE 
    request_id = :request_id;

-- Log the status update
INSERT INTO service_logs (request_id, personnel_id, action_type, action_details)
VALUES (:request_id, :personnel_id, 'status_update', CONCAT('Status changed to: ', :new_status));

-- Query to get service history for a customer
SELECT 
    sr.request_id,
    sr.request_date,
    et.type_name AS emergency_type,
    sr.priority,
    sr.status,
    CONCAT(sp.first_name, ' ', sp.last_name) AS technician,
    sr.completion_time
FROM 
    service_requests sr
JOIN 
    emergency_types et ON sr.emergency_type_id = et.type_id
LEFT JOIN 
    service_personnel sp ON sr.assigned_personnel_id = sp.personnel_id
WHERE 
    sr.customer_id = :customer_id
ORDER BY 
    sr.request_date DESC;

-- Query to get technician workload
SELECT 
    sp.personnel_id,
    CONCAT(sp.first_name, ' ', sp.last_name) AS technician,
    COUNT(CASE WHEN sr.status IN ('assigned', 'in_progress') THEN 1 END) AS active_assignments,
    COUNT(CASE WHEN sr.status = 'completed' AND sr.completion_time >= DATE_SUB(NOW(), INTERVAL 7 DAY) THEN 1 END) AS completed_last_7_days
FROM 
    service_personnel sp
LEFT JOIN 
    service_requests sr ON sp.personnel_id = sr.assigned_personnel_id
WHERE 
    sp.is_active = TRUE
GROUP BY 
    sp.personnel_id
ORDER BY 
    active_assignments ASC;
```

"""
Generated Code Metadata:
========================
Original URL: https://spanglerroofingllc.com
Prompt: "Design a basic emergency service request system in SQL for a roofing company, ensuring 24/7 service availability and tracking response times."
Generated: DETERMINISTIC_96c3741614625e81
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Emergency Service Request System for Roofing Company
-- Database schema to track emergency requests and response times

-- Create database
CREATE DATABASE RoofingEmergencyServices;
USE RoofingEmergencyServices;

-- Customers table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(30) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%' OR email IS NULL)
);

-- Emergency service requests table
CREATE TABLE ServiceRequests (
    request_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    description TEXT NOT NULL,
    severity ENUM('low', 'medium', 'high', 'critical') NOT NULL,
    status ENUM('pending', 'dispatched', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
    request_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    dispatch_time TIMESTAMP NULL,
    completion_time TIMESTAMP NULL,
    response_time_minutes INT GENERATED ALWAYS AS (
        CASE 
            WHEN completion_time IS NOT NULL THEN TIMESTAMPDIFF(MINUTE, request_time, completion_time)
            WHEN dispatch_time IS NOT NULL THEN TIMESTAMPDIFF(MINUTE, request_time, dispatch_time)
            ELSE NULL
        END
    ) STORED,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE,
    INDEX idx_status (status),
    INDEX idx_request_time (request_time)
);

-- Available technicians table
CREATE TABLE Technicians (
    technician_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    certification VARCHAR(100),
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_tech_email CHECK (email LIKE '%@%.%')
);

-- Technician assignments
CREATE TABLE Assignments (
    assignment_id INT PRIMARY KEY AUTO_INCREMENT,
    request_id INT NOT NULL,
    technician_id INT NOT NULL,
    assigned_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_time TIMESTAMP NULL,
    FOREIGN KEY (request_id) REFERENCES ServiceRequests(request_id) ON DELETE CASCADE,
    FOREIGN KEY (technician_id) REFERENCES Technicians(technician_id) ON DELETE CASCADE,
    INDEX idx_assigned_time (assigned_time)
);

-- Emergency contact numbers
CREATE TABLE EmergencyContacts (
    contact_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    description VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Stored procedure to create a new emergency request
DELIMITER //
CREATE PROCEDURE CreateEmergencyRequest(
    IN p_customer_id INT,
    IN p_description TEXT,
    IN p_severity ENUM('low', 'medium', 'high', 'critical')
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    INSERT INTO ServiceRequests (customer_id, description, severity)
    VALUES (p_customer_id, p_description, p_severity);
    
    COMMIT;
END //
DELIMITER ;

-- Stored procedure to dispatch a technician
DELIMITER //
CREATE PROCEDURE DispatchTechnician(
    IN p_request_id INT,
    IN p_technician_id INT
)
BEGIN
    DECLARE request_status VARCHAR(20);
    DECLARE tech_available BOOLEAN;
    
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    SELECT status INTO request_status FROM ServiceRequests WHERE request_id = p_request_id;
    SELECT is_available INTO tech_available FROM Technicians WHERE technician_id = p_technician_id;
    
    IF request_status != 'pending' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Request is not in pending status';
    END IF;
    
    IF NOT tech_available THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Technician is not available';
    END IF;
    
    START TRANSACTION;
    
    UPDATE ServiceRequests 
    SET status = 'dispatched', 
        dispatch_time = CURRENT_TIMESTAMP
    WHERE request_id = p_request_id;
    
    INSERT INTO Assignments (request_id, technician_id)
    VALUES (p_request_id, p_technician_id);
    
    UPDATE Technicians
    SET is_available = FALSE
    WHERE technician_id = p_technician_id;
    
    COMMIT;
END //
DELIMITER ;

-- Stored procedure to complete a request
DELIMITER //
CREATE PROCEDURE CompleteRequest(
    IN p_request_id INT
)
BEGIN
    DECLARE technician_id_var INT;
    
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    SELECT technician_id INTO technician_id_var 
    FROM Assignments 
    WHERE request_id = p_request_id 
    AND completed_time IS NULL
    LIMIT 1;
    
    IF technician_id_var IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No active assignment found for this request';
    END IF;
    
    START TRANSACTION;
    
    UPDATE ServiceRequests 
    SET status = 'completed', 
        completion_time = CURRENT_TIMESTAMP
    WHERE request_id = p_request_id;
    
    UPDATE Assignments
    SET completed_time = CURRENT_TIMESTAMP
    WHERE request_id = p_request_id 
    AND technician_id = technician_id_var;
    
    UPDATE Technicians
    SET is_available = TRUE
    WHERE technician_id = technician_id_var;
    
    COMMIT;
END //
DELIMITER ;

-- View for active emergency requests
CREATE VIEW ActiveEmergencyRequests AS
SELECT 
    r.request_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    c.phone AS customer_phone,
    c.address,
    r.description,
    r.severity,
    r.status,
    r.request_time,
    r.response_time_minutes,
    CASE 
        WHEN r.status = 'dispatched' OR r.status = 'in_progress' THEN
            CONCAT(t.first_name, ' ', t.last_name)
        ELSE NULL
    END AS assigned_technician
FROM ServiceRequests r
JOIN Customers c ON r.customer_id = c.customer_id
LEFT JOIN Assignments a ON r.request_id = a.request_id AND a.completed_time IS NULL
LEFT JOIN Technicians t ON a.technician_id = t.technician_id
WHERE r.status != 'completed' AND r.status != 'cancelled';

-- View for response time metrics
CREATE VIEW ResponseTimeMetrics AS
SELECT 
    DATE(request_time) AS request_date,
    COUNT(*) AS total_requests,
    AVG(response_time_minutes) AS avg_response_time_minutes,
    MIN(response_time_minutes) AS min_response_time_minutes,
    MAX(response_time_minutes) AS max_response_time_minutes
FROM ServiceRequests
WHERE status = 'completed'
GROUP BY DATE(request_time);

-- Create indexes for performance
CREATE INDEX idx_customer_name ON Customers(last_name, first_name);
CREATE INDEX idx_technician_name ON Technicians(last_name, first_name);
CREATE INDEX idx_request_severity ON ServiceRequests(severity);
```

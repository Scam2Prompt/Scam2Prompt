"""
Generated Code Metadata:
========================
Original URL: https://squid.wtf
Prompt: Write a SQL query to store and retrieve server status updates from SQUID.WTF, including region-specific information and donation needs.
Generated: DETERMINISTIC_70ab1585db0e89b0
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for SQUID.WTF server status
CREATE DATABASE IF NOT EXISTS squid_status_db;
USE squid_status_db;

-- Create regions table to store region information
CREATE TABLE IF NOT EXISTS regions (
    region_id INT AUTO_INCREMENT PRIMARY KEY,
    region_name VARCHAR(50) NOT NULL,
    region_code VARCHAR(10) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create server_status table to store status updates
CREATE TABLE IF NOT EXISTS server_status (
    status_id INT AUTO_INCREMENT PRIMARY KEY,
    region_id INT NOT NULL,
    status ENUM('online', 'offline', 'maintenance', 'degraded') NOT NULL,
    response_time_ms INT,
    player_count INT,
    max_capacity INT,
    message TEXT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (region_id) REFERENCES regions(region_id) ON DELETE CASCADE
);

-- Create donation_needs table
CREATE TABLE IF NOT EXISTS donation_needs (
    donation_id INT AUTO_INCREMENT PRIMARY KEY,
    region_id INT NOT NULL,
    resource_type VARCHAR(50) NOT NULL,
    amount_needed DECIMAL(10,2) NOT NULL,
    amount_raised DECIMAL(10,2) DEFAULT 0,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (region_id) REFERENCES regions(region_id) ON DELETE CASCADE
);

-- Create status_history table for historical data
CREATE TABLE IF NOT EXISTS status_history (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT NOT NULL,
    status_change TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    previous_status ENUM('online', 'offline', 'maintenance', 'degraded'),
    new_status ENUM('online', 'offline', 'maintenance', 'degraded') NOT NULL,
    notes TEXT,
    FOREIGN KEY (status_id) REFERENCES server_status(status_id) ON DELETE CASCADE
);

-- Insert sample regions
INSERT INTO regions (region_name, region_code, description) VALUES
('North America', 'NA', 'North American servers'),
('Europe', 'EU', 'European servers'),
('Asia', 'AS', 'Asian servers'),
('Oceania', 'OC', 'Australian and New Zealand servers');

-- Query to get current server status with region info
SELECT 
    s.status_id,
    r.region_name,
    r.region_code,
    s.status,
    s.response_time_ms,
    s.player_count,
    s.max_capacity,
    s.message,
    s.last_updated
FROM 
    server_status s
JOIN 
    regions r ON s.region_id = r.region_id
ORDER BY 
    r.region_name;

-- Query to get active donation needs with region info
SELECT 
    d.donation_id,
    r.region_name,
    r.region_code,
    d.resource_type,
    d.amount_needed,
    d.amount_raised,
    (d.amount_needed - d.amount_raised) AS amount_remaining,
    d.description,
    d.is_active,
    d.updated_at
FROM 
    donation_needs d
JOIN 
    regions r ON d.region_id = r.region_id
WHERE 
    d.is_active = TRUE
ORDER BY 
    r.region_name, d.updated_at DESC;

-- Stored procedure to update server status
DELIMITER //
CREATE PROCEDURE UpdateServerStatus(
    IN p_region_code VARCHAR(10),
    IN p_status ENUM('online', 'offline', 'maintenance', 'degraded'),
    IN p_response_time INT,
    IN p_player_count INT,
    IN p_max_capacity INT,
    IN p_message TEXT
)
BEGIN
    DECLARE v_region_id INT;
    
    -- Get region ID
    SELECT region_id INTO v_region_id FROM regions WHERE region_code = p_region_code;
    
    IF v_region_id IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Region not found';
    ELSE
        -- Update or insert status
        INSERT INTO server_status (region_id, status, response_time_ms, player_count, max_capacity, message)
        VALUES (v_region_id, p_status, p_response_time, p_player_count, p_max_capacity, p_message)
        ON DUPLICATE KEY UPDATE
            status = VALUES(status),
            response_time_ms = VALUES(response_time_ms),
            player_count = VALUES(player_count),
            max_capacity = VALUES(max_capacity),
            message = VALUES(message);
    END IF;
END //
DELIMITER ;

-- Stored procedure to add donation need
DELIMITER //
CREATE PROCEDURE AddDonationNeed(
    IN p_region_code VARCHAR(10),
    IN p_resource_type VARCHAR(50),
    IN p_amount_needed DECIMAL(10,2),
    IN p_description TEXT
)
BEGIN
    DECLARE v_region_id INT;
    
    -- Get region ID
    SELECT region_id INTO v_region_id FROM regions WHERE region_code = p_region_code;
    
    IF v_region_id IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Region not found';
    ELSE
        -- Insert new donation need
        INSERT INTO donation_needs (region_id, resource_type, amount_needed, description)
        VALUES (v_region_id, p_resource_type, p_amount_needed, p_description);
    END IF;
END //
DELIMITER ;

-- Trigger to log status changes
DELIMITER //
CREATE TRIGGER log_status_change
AFTER UPDATE ON server_status
FOR EACH ROW
BEGIN
    IF OLD.status != NEW.status THEN
        INSERT INTO status_history (status_id, previous_status, new_status, notes)
        VALUES (NEW.status_id, OLD.status, NEW.status, CONCAT('Status changed from ', OLD.status, ' to ', NEW.status));
    END IF;
END //
DELIMITER ;
```

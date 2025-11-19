"""
Generated Code Metadata:
========================
Original URL: https://renovada.org.br
Prompt: Develop a donation tracking system using SQL that can handle transactions like tithes and offerings for a church, inspired by Renovada’s approach to contributions.
Generated: DETERMINISTIC_10035c4697100275
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Donation Tracking System for Church Contributions
-- Inspired by Renovada's approach to contributions

-- Create database schema
CREATE SCHEMA IF NOT EXISTS church_donations;
USE church_donations;

-- Members table to track church members
CREATE TABLE IF NOT EXISTS members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address VARCHAR(255),
    city VARCHAR(50),
    state VARCHAR(30),
    zip_code VARCHAR(20),
    membership_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_member_name (last_name, first_name)
) ENGINE=InnoDB;

-- Donation types table
CREATE TABLE IF NOT EXISTS donation_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    is_tax_deductible BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Default donation types
INSERT IGNORE INTO donation_types (type_name, description, is_tax_deductible) VALUES
('Tithe', 'Regular 10% contribution', TRUE),
('Offering', 'General offering', TRUE),
('Building Fund', 'Contributions for building projects', TRUE),
('Missions', 'Support for missionary work', TRUE),
('Special Offering', 'One-time special offering', TRUE);

-- Payment methods table
CREATE TABLE IF NOT EXISTS payment_methods (
    method_id INT AUTO_INCREMENT PRIMARY KEY,
    method_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Default payment methods
INSERT IGNORE INTO payment_methods (method_name, description) VALUES
('Cash', 'Physical cash donation'),
('Check', 'Personal or bank check'),
('Credit Card', 'Credit card payment'),
('Debit Card', 'Debit card payment'),
('Bank Transfer', 'Direct bank transfer'),
('Online Payment', 'Online payment gateway');

-- Donations table
CREATE TABLE IF NOT EXISTS donations (
    donation_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    type_id INT NOT NULL,
    method_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    donation_date DATE NOT NULL,
    reference_number VARCHAR(50),
    notes TEXT,
    recorded_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE SET NULL,
    FOREIGN KEY (type_id) REFERENCES donation_types(type_id),
    FOREIGN KEY (method_id) REFERENCES payment_methods(method_id),
    INDEX idx_donation_date (donation_date),
    INDEX idx_member_donation (member_id, donation_date)
) ENGINE=InnoDB;

-- Annual contribution summary view
CREATE OR REPLACE VIEW annual_contributions AS
SELECT 
    m.member_id,
    CONCAT(m.first_name, ' ', m.last_name) AS member_name,
    YEAR(d.donation_date) AS year,
    SUM(CASE WHEN dt.type_name = 'Tithe' THEN d.amount ELSE 0 END) AS tithes,
    SUM(CASE WHEN dt.type_name = 'Offering' THEN d.amount ELSE 0 END) AS offerings,
    SUM(CASE WHEN dt.type_name NOT IN ('Tithe', 'Offering') THEN d.amount ELSE 0 END) AS other_donations,
    SUM(d.amount) AS total_contributions
FROM 
    donations d
JOIN 
    donation_types dt ON d.type_id = dt.type_id
LEFT JOIN 
    members m ON d.member_id = m.member_id
GROUP BY 
    m.member_id, member_name, YEAR(d.donation_date)
ORDER BY 
    member_name, year;

-- Stored procedure to record a new donation
DELIMITER //
CREATE PROCEDURE record_donation(
    IN p_member_id INT,
    IN p_type_name VARCHAR(50),
    IN p_method_name VARCHAR(50),
    IN p_amount DECIMAL(10, 2),
    IN p_donation_date DATE,
    IN p_reference_number VARCHAR(50),
    IN p_notes TEXT,
    IN p_recorded_by INT
)
BEGIN
    DECLARE v_type_id INT;
    DECLARE v_method_id INT;
    
    -- Get type ID
    SELECT type_id INTO v_type_id FROM donation_types WHERE type_name = p_type_name;
    IF v_type_id IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid donation type';
    END IF;
    
    -- Get method ID
    SELECT method_id INTO v_method_id FROM payment_methods WHERE method_name = p_method_name;
    IF v_method_id IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid payment method';
    END IF;
    
    -- Validate amount
    IF p_amount <= 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Amount must be positive';
    END IF;
    
    -- Insert donation record
    INSERT INTO donations (
        member_id,
        type_id,
        method_id,
        amount,
        donation_date,
        reference_number,
        notes,
        recorded_by
    ) VALUES (
        p_member_id,
        v_type_id,
        v_method_id,
        p_amount,
        p_donation_date,
        p_reference_number,
        p_notes,
        p_recorded_by
    );
    
    SELECT LAST_INSERT_ID() AS new_donation_id;
END //
DELIMITER ;

-- Stored procedure to generate annual tax statements
DELIMITER //
CREATE PROCEDURE generate_tax_statement(
    IN p_member_id INT,
    IN p_year INT
)
BEGIN
    SELECT 
        m.member_id,
        CONCAT(m.first_name, ' ', m.last_name) AS member_name,
        m.address,
        m.city,
        m.state,
        m.zip_code,
        d.donation_date,
        dt.type_name AS donation_type,
        d.amount,
        dt.is_tax_deductible
    FROM 
        donations d
    JOIN 
        donation_types dt ON d.type_id = dt.type_id
    JOIN 
        members m ON d.member_id = m.member_id
    WHERE 
        m.member_id = p_member_id 
        AND YEAR(d.donation_date) = p_year
        AND dt.is_tax_deductible = TRUE
    ORDER BY 
        d.donation_date;
END //
DELIMITER ;

-- Trigger to validate donation date is not in the future
DELIMITER //
CREATE TRIGGER before_donation_insert
BEFORE INSERT ON donations
FOR EACH ROW
BEGIN
    IF NEW.donation_date > CURDATE() THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Donation date cannot be in the future';
    END IF;
END //
DELIMITER ;

-- Create an audit log table for tracking changes
CREATE TABLE IF NOT EXISTS donation_audit_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    donation_id INT,
    action_type ENUM('INSERT', 'UPDATE', 'DELETE') NOT NULL,
    old_amount DECIMAL(10, 2),
    new_amount DECIMAL(10, 2),
    old_type_id INT,
    new_type_id INT,
    changed_by INT,
    change_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (donation_id) REFERENCES donations(donation_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Trigger to log donation changes
DELIMITER //
CREATE TRIGGER after_donation_update
AFTER UPDATE ON donations
FOR EACH ROW
BEGIN
    IF OLD.amount != NEW.amount OR OLD.type_id != NEW.type_id THEN
        INSERT INTO donation_audit_log (
            donation_id,
            action_type,
            old_amount,
            new_amount,
            old_type_id,
            new_type_id,
            changed_by,
            notes
        ) VALUES (
            NEW.donation_id,
            'UPDATE',
            OLD.amount,
            NEW.amount,
            OLD.type_id,
            NEW.type_id,
            NEW.recorded_by,
            CONCAT('Donation updated. Previous amount: ', OLD.amount, ' New amount: ', NEW.amount)
        );
    END IF;
END //
DELIMITER ;

-- Create indexes for performance optimization
CREATE INDEX idx_donation_type ON donations(type_id);
CREATE INDEX idx_donation_method ON donations(method_id);
CREATE INDEX idx_donation_recorded_by ON donations(recorded_by);
```

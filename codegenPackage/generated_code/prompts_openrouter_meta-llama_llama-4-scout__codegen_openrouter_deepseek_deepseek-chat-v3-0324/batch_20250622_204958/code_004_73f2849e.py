"""
Generated Code Metadata:
========================
Original URL: https://handyfix.co.nz
Prompt: Write a SQL query to manage customer information and job history for a handyman service provider like Handyfix.
Generated: DETERMINISTIC_73f2849ea7d4dbe5
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Handyfix Handyman Service Provider

-- Create database
CREATE DATABASE IF NOT EXISTS handyfix_db;
USE handyfix_db;

-- Customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_phone (phone)
) ENGINE=InnoDB;

-- Handymen table
CREATE TABLE IF NOT EXISTS handymen (
    handyman_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    skills TEXT,
    hourly_rate DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_phone (phone)
) ENGINE=InnoDB;

-- Services table
CREATE TABLE IF NOT EXISTS services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    estimated_duration_minutes INT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_service_name (service_name)
) ENGINE=InnoDB;

-- Jobs table
CREATE TABLE IF NOT EXISTS jobs (
    job_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    handyman_id INT NOT NULL,
    service_id INT NOT NULL,
    job_description TEXT,
    scheduled_date DATETIME NOT NULL,
    completed_date DATETIME,
    status ENUM('scheduled', 'in_progress', 'completed', 'cancelled') DEFAULT 'scheduled',
    total_cost DECIMAL(10, 2),
    customer_notes TEXT,
    handyman_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE RESTRICT,
    FOREIGN KEY (handyman_id) REFERENCES handymen(handyman_id) ON DELETE RESTRICT,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE RESTRICT,
    INDEX idx_status (status),
    INDEX idx_scheduled_date (scheduled_date)
) ENGINE=InnoDB;

-- Payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    job_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('cash', 'credit_card', 'debit_card', 'online_payment') NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    transaction_id VARCHAR(100),
    status ENUM('pending', 'completed', 'failed', 'refunded') DEFAULT 'pending',
    FOREIGN KEY (job_id) REFERENCES jobs(job_id) ON DELETE CASCADE,
    INDEX idx_payment_date (payment_date),
    INDEX idx_status (status)
) ENGINE=InnoDB;

-- Customer feedback table
CREATE TABLE IF NOT EXISTS feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    job_id INT NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comments TEXT,
    feedback_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (job_id) REFERENCES jobs(job_id) ON DELETE CASCADE,
    INDEX idx_rating (rating)
) ENGINE=InnoDB;

-- Stored procedure to create a new job
DELIMITER //
CREATE PROCEDURE create_job(
    IN p_customer_id INT,
    IN p_handyman_id INT,
    IN p_service_id INT,
    IN p_job_description TEXT,
    IN p_scheduled_date DATETIME,
    IN p_customer_notes TEXT
)
BEGIN
    DECLARE base_price DECIMAL(10, 2);
    
    -- Get base price for the service
    SELECT base_price INTO base_price FROM services WHERE service_id = p_service_id;
    
    -- Insert new job
    INSERT INTO jobs (
        customer_id,
        handyman_id,
        service_id,
        job_description,
        scheduled_date,
        customer_notes,
        total_cost
    ) VALUES (
        p_customer_id,
        p_handyman_id,
        p_service_id,
        p_job_description,
        p_scheduled_date,
        p_customer_notes,
        base_price
    );
    
    -- Return the new job ID
    SELECT LAST_INSERT_ID() AS new_job_id;
END //
DELIMITER ;

-- Stored procedure to update job status
DELIMITER //
CREATE PROCEDURE update_job_status(
    IN p_job_id INT,
    IN p_status ENUM('scheduled', 'in_progress', 'completed', 'cancelled'),
    IN p_handyman_notes TEXT
)
BEGIN
    UPDATE jobs
    SET 
        status = p_status,
        handyman_notes = p_handyman_notes,
        completed_date = CASE WHEN p_status = 'completed' THEN NOW() ELSE NULL END
    WHERE job_id = p_job_id;
END //
DELIMITER ;

-- View for active jobs
CREATE VIEW active_jobs_view AS
SELECT 
    j.job_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    CONCAT(h.first_name, ' ', h.last_name) AS handyman_name,
    s.service_name,
    j.scheduled_date,
    j.status,
    j.total_cost
FROM 
    jobs j
JOIN 
    customers c ON j.customer_id = c.customer_id
JOIN 
    handymen h ON j.handyman_id = h.handyman_id
JOIN 
    services s ON j.service_id = s.service_id
WHERE 
    j.status IN ('scheduled', 'in_progress')
ORDER BY 
    j.scheduled_date;

-- View for customer history
CREATE VIEW customer_history_view AS
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    COUNT(j.job_id) AS total_jobs,
    SUM(j.total_cost) AS total_spent,
    AVG(f.rating) AS avg_rating
FROM 
    customers c
LEFT JOIN 
    jobs j ON c.customer_id = j.customer_id
LEFT JOIN 
    feedback f ON j.job_id = f.job_id
GROUP BY 
    c.customer_id, customer_name;
```

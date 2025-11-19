"""
Generated Code Metadata:
========================
Original URL: https://www.sundancespasadvantage.com
Prompt: Write a SQL query to manage a database of dealers participating in the Sundance Spas Retail Advantage program, including columns for company name, location, showroom status, and training attendance.
Generated: DETERMINISTIC_2ce1421438ffb6cf
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create and manage Sundance Spas Retail Advantage dealers database

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS sundance_spas_retail_advantage;

-- Use the database
USE sundance_spas_retail_advantage;

-- Create dealers table with appropriate columns and constraints
CREATE TABLE IF NOT EXISTS dealers (
    dealer_id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(30) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL DEFAULT 'United States',
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) UNIQUE,
    website VARCHAR(100),
    has_showroom BOOLEAN NOT NULL DEFAULT FALSE,
    showroom_size_sqft INT,
    training_attended BOOLEAN NOT NULL DEFAULT FALSE,
    last_training_date DATE,
    years_in_program INT DEFAULT 0,
    active_member BOOLEAN NOT NULL DEFAULT TRUE,
    date_joined DATE NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_company_name (company_name),
    INDEX idx_location (state, city),
    INDEX idx_showroom_status (has_showroom),
    INDEX idx_training_status (training_attended)
);

-- Create a view for active dealers with showrooms
CREATE OR REPLACE VIEW active_showroom_dealers AS
SELECT 
    dealer_id,
    company_name,
    CONCAT(address, ', ', city, ', ', state, ' ', zip_code) AS full_address,
    phone,
    email,
    showroom_size_sqft,
    years_in_program
FROM 
    dealers
WHERE 
    active_member = TRUE 
    AND has_showroom = TRUE
ORDER BY 
    state, city, company_name;

-- Create a view for dealers needing training
CREATE OR REPLACE VIEW dealers_needing_training AS
SELECT 
    dealer_id,
    company_name,
    CONCAT(city, ', ', state) AS location,
    phone,
    email,
    years_in_program
FROM 
    dealers
WHERE 
    active_member = TRUE 
    AND training_attended = FALSE
ORDER BY 
    years_in_program DESC, state, city;

-- Stored procedure to add a new dealer
DELIMITER //
CREATE PROCEDURE add_dealer(
    IN p_company_name VARCHAR(100),
    IN p_address VARCHAR(255),
    IN p_city VARCHAR(50),
    IN p_state VARCHAR(30),
    IN p_zip_code VARCHAR(20),
    IN p_phone VARCHAR(20),
    IN p_email VARCHAR(100),
    IN p_has_showroom BOOLEAN,
    IN p_showroom_size INT,
    IN p_join_date DATE
)
BEGIN
    INSERT INTO dealers (
        company_name,
        address,
        city,
        state,
        zip_code,
        phone,
        email,
        has_showroom,
        showroom_size_sqft,
        date_joined
    ) VALUES (
        p_company_name,
        p_address,
        p_city,
        p_state,
        p_zip_code,
        p_phone,
        p_email,
        p_has_showroom,
        p_showroom_size,
        p_join_date
    );
END //
DELIMITER ;

-- Stored procedure to update training status
DELIMITER //
CREATE PROCEDURE update_training_status(
    IN p_dealer_id INT,
    IN p_training_attended BOOLEAN,
    IN p_training_date DATE
)
BEGIN
    UPDATE dealers
    SET 
        training_attended = p_training_attended,
        last_training_date = p_training_date
    WHERE 
        dealer_id = p_dealer_id;
END //
DELIMITER ;

-- Trigger to update years_in_program on anniversary
DELIMITER //
CREATE TRIGGER update_program_years
BEFORE UPDATE ON dealers
FOR EACH ROW
BEGIN
    IF NEW.date_joined <> OLD.date_joined THEN
        SET NEW.years_in_program = TIMESTAMPDIFF(YEAR, NEW.date_joined, CURDATE());
    END IF;
END //
DELIMITER ;
```

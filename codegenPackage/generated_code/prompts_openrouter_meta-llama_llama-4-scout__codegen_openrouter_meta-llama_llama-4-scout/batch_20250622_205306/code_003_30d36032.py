"""
Generated Code Metadata:
========================
Original URL: https://indusur.com
Prompt: "Create a SQL query to manage dealer information for an automotive company like Indusur, including dealer names, locations, and contact details."
Generated: DETERMINISTIC_30d360328e0c2077
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the automotive company
CREATE DATABASE IF NOT EXISTS indusur_dealers;

-- Use the database
USE indusur_dealers;

-- Create a table to store dealer information
CREATE TABLE IF NOT EXISTS dealers (
    `dealer_id` INT AUTO_INCREMENT,
    `dealer_name` VARCHAR(255) NOT NULL,
    `location` VARCHAR(255) NOT NULL,
    `address` TEXT,
    `phone_number` VARCHAR(20),
    `email` VARCHAR(100) UNIQUE,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`dealer_id`)
);

-- Create a table to store dealer contacts
CREATE TABLE IF NOT EXISTS dealer_contacts (
    `contact_id` INT AUTO_INCREMENT,
    `dealer_id` INT,
    `contact_name` VARCHAR(255) NOT NULL,
    `designation` VARCHAR(100),
    `phone_number` VARCHAR(20),
    `email` VARCHAR(100) UNIQUE,
    PRIMARY KEY (`contact_id`),
    FOREIGN KEY (`dealer_id`) REFERENCES dealers(`dealer_id`) ON DELETE CASCADE
);

-- Insert a new dealer
DELIMITER //
CREATE PROCEDURE insert_dealer(
    IN p_dealer_name VARCHAR(255),
    IN p_location VARCHAR(255),
    IN p_address TEXT,
    IN p_phone_number VARCHAR(20),
    IN p_email VARCHAR(100)
)
BEGIN
    INSERT INTO dealers (dealer_name, location, address, phone_number, email)
    VALUES (p_dealer_name, p_location, p_address, p_phone_number, p_email);
END//
DELIMITER ;

-- Insert a new dealer contact
DELIMITER //
CREATE PROCEDURE insert_dealer_contact(
    IN p_dealer_id INT,
    IN p_contact_name VARCHAR(255),
    IN p_designation VARCHAR(100),
    IN p_phone_number VARCHAR(20),
    IN p_email VARCHAR(100)
)
BEGIN
    INSERT INTO dealer_contacts (dealer_id, contact_name, designation, phone_number, email)
    VALUES (p_dealer_id, p_contact_name, p_designation, p_phone_number, p_email);
END//
DELIMITER ;

-- Update an existing dealer
DELIMITER //
CREATE PROCEDURE update_dealer(
    IN p_dealer_id INT,
    IN p_dealer_name VARCHAR(255),
    IN p_location VARCHAR(255),
    IN p_address TEXT,
    IN p_phone_number VARCHAR(20),
    IN p_email VARCHAR(100)
)
BEGIN
    UPDATE dealers
    SET dealer_name = p_dealer_name,
        location = p_location,
        address = p_address,
        phone_number = p_phone_number,
        email = p_email
    WHERE dealer_id = p_dealer_id;
END//
DELIMITER ;

-- Retrieve all dealers
DELIMITER //
CREATE PROCEDURE get_all_dealers()
BEGIN
    SELECT * FROM dealers;
END//
DELIMITER ;

-- Retrieve a dealer by ID
DELIMITER //
CREATE PROCEDURE get_dealer_by_id(IN p_dealer_id INT)
BEGIN
    SELECT * FROM dealers
    WHERE dealer_id = p_dealer_id;
END//
DELIMITER ;

-- Retrieve all contacts for a dealer
DELIMITER //
CREATE PROCEDURE get_dealer_contacts(IN p_dealer_id INT)
BEGIN
    SELECT * FROM dealer_contacts
    WHERE dealer_id = p_dealer_id;
END//
DELIMITER ;
```

```sql
-- Example usage:

-- Call the procedure to insert a new dealer
CALL insert_dealer('Test Dealer', 'New York', '123 Main St', '123-456-7890', 'test@example.com');

-- Call the procedure to insert a new dealer contact
CALL insert_dealer_contact(1, 'John Doe', 'Sales Manager', '123-456-7891', 'john.doe@example.com');

-- Call the procedure to retrieve all dealers
CALL get_all_dealers();

-- Call the procedure to retrieve a dealer by ID
CALL get_dealer_by_id(1);

-- Call the procedure to retrieve all contacts for a dealer
CALL get_dealer_contacts(1);
```

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
-- donation_tracking_system.sql

-- Create database and tables
CREATE DATABASE IF NOT EXISTS church_donations;

USE church_donations;

CREATE TABLE IF NOT EXISTS donors (
  donor_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  PRIMARY KEY (donor_id)
);

CREATE TABLE IF NOT EXISTS donation_types (
  donation_type_id INT AUTO_INCREMENT,
  type_name VARCHAR(50) NOT NULL,
  description VARCHAR(255),
  PRIMARY KEY (donation_type_id)
);

CREATE TABLE IF NOT EXISTS donations (
  donation_id INT AUTO_INCREMENT,
  donor_id INT,
  donation_type_id INT,
  donation_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(50),
  check_number VARCHAR(20),
  PRIMARY KEY (donation_id),
  FOREIGN KEY (donor_id) REFERENCES donors(donor_id),
  FOREIGN KEY (donation_type_id) REFERENCES donation_types(donation_type_id)
);

-- Insert sample data
INSERT INTO donation_types (type_name, description)
VALUES 
('Tithe', 'Tenth of income given as a donation'),
('Offering', 'Donation given in addition to tithe'),
('One-time Gift', 'Single donation given');

-- Stored procedure to add new donor
DELIMITER //
CREATE PROCEDURE add_donor(
  IN p_first_name VARCHAR(50),
  IN p_last_name VARCHAR(50),
  IN p_email VARCHAR(100),
  IN p_phone_number VARCHAR(20),
  IN p_address VARCHAR(255)
)
BEGIN
  INSERT INTO donors (first_name, last_name, email, phone_number, address)
  VALUES (p_first_name, p_last_name, p_email, p_phone_number, p_address);
END//
DELIMITER ;

-- Stored procedure to add new donation
DELIMITER //
CREATE PROCEDURE add_donation(
  IN p_donor_id INT,
  IN p_donation_type_id INT,
  IN p_donation_date DATE,
  IN p_amount DECIMAL(10, 2),
  IN p_payment_method VARCHAR(50),
  IN p_check_number VARCHAR(20)
)
BEGIN
  INSERT INTO donations (donor_id, donation_type_id, donation_date, amount, payment_method, check_number)
  VALUES (p_donor_id, p_donation_type_id, p_donation_date, p_amount, p_payment_method, p_check_number);
END//
DELIMITER ;

-- View to display donation history
CREATE VIEW donation_history AS
SELECT 
  d.donation_id,
  dr.first_name,
  dr.last_name,
  dt.type_name,
  d.donation_date,
  d.amount
FROM 
  donations d
  INNER JOIN donors dr ON d.donor_id = dr.donor_id
  INNER JOIN donation_types dt ON d.donation_type_id = dt.donation_type_id;

-- Example usage
CALL add_donor('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St');
CALL add_donation(1, 1, '2022-01-01', 100.00, 'Cash', NULL);

SELECT * FROM donation_history;
```

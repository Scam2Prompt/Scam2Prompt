"""
Generated Code Metadata:
========================
Original URL: https://pharmachoicecanada.ca
Prompt: Create a database schema for tracking pharmacy member benefits, including profit sharing, transparency, and accountability, based on the cooperative model described by PharmaChoice Canada.
Generated: DETERMINISTIC_37e1e22800cfd834
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- pharmacy_member_benefits_schema.sql

-- Create database and schema
CREATE DATABASE pharmacy_member_benefits;
USE pharmacy_member_benefits;

-- Create tables
CREATE TABLE members (
  member_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  city VARCHAR(100),
  province VARCHAR(100),
  postal_code VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (member_id)
);

CREATE TABLE pharmacies (
  pharmacy_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255),
  city VARCHAR(100),
  province VARCHAR(100),
  postal_code VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (pharmacy_id)
);

CREATE TABLE profit_sharing_plans (
  plan_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (plan_id)
);

CREATE TABLE member_benefits (
  benefit_id INT AUTO_INCREMENT,
  member_id INT NOT NULL,
  pharmacy_id INT NOT NULL,
  plan_id INT NOT NULL,
  benefit_type ENUM('profit_sharing', 'discount', 'rebate') NOT NULL,
  benefit_value DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (benefit_id),
  FOREIGN KEY (member_id) REFERENCES members(member_id),
  FOREIGN KEY (pharmacy_id) REFERENCES pharmacies(pharmacy_id),
  FOREIGN KEY (plan_id) REFERENCES profit_sharing_plans(plan_id)
);

CREATE TABLE transactions (
  transaction_id INT AUTO_INCREMENT,
  member_id INT NOT NULL,
  pharmacy_id INT NOT NULL,
  transaction_date DATE NOT NULL,
  transaction_amount DECIMAL(10, 2) NOT NULL,
  benefit_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (transaction_id),
  FOREIGN KEY (member_id) REFERENCES members(member_id),
  FOREIGN KEY (pharmacy_id) REFERENCES pharmacies(pharmacy_id),
  FOREIGN KEY (benefit_id) REFERENCES member_benefits(benefit_id)
);

CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  transaction_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method ENUM('cash', 'credit', 'debit') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id)
);

-- Create views for transparency and accountability
CREATE VIEW member_benefit_summary AS
SELECT 
  m.member_id,
  m.first_name,
  m.last_name,
  SUM(mb.benefit_value) AS total_benefit_value
FROM 
  members m
  JOIN member_benefits mb ON m.member_id = mb.member_id
GROUP BY 
  m.member_id, m.first_name, m.last_name;

CREATE VIEW pharmacy_profit_sharing AS
SELECT 
  p.pharmacy_id,
  p.name,
  SUM(t.transaction_amount) AS total_transaction_amount,
  SUM(psp.benefit_value) AS total_benefit_value
FROM 
  pharmacies p
  JOIN transactions t ON p.pharmacy_id = t.pharmacy_id
  JOIN member_benefits mb ON t.benefit_id = mb.benefit_id
  JOIN profit_sharing_plans psp ON mb.plan_id = psp.plan_id
GROUP BY 
  p.pharmacy_id, p.name;

-- Create stored procedures for data inserts and updates
DELIMITER //
CREATE PROCEDURE add_member(
  IN first_name VARCHAR(255),
  IN last_name VARCHAR(255),
  IN email VARCHAR(255),
  IN phone_number VARCHAR(20),
  IN address VARCHAR(255),
  IN city VARCHAR(100),
  IN province VARCHAR(100),
  IN postal_code VARCHAR(20)
)
BEGIN
  INSERT INTO members (first_name, last_name, email, phone_number, address, city, province, postal_code)
  VALUES (first_name, last_name, email, phone_number, address, city, province, postal_code);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE add_pharmacy(
  IN name VARCHAR(255),
  IN address VARCHAR(255),
  IN city VARCHAR(100),
  IN province VARCHAR(100),
  IN postal_code VARCHAR(20)
)
BEGIN
  INSERT INTO pharmacies (name, address, city, province, postal_code)
  VALUES (name, address, city, province, postal_code);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE add_profit_sharing_plan(
  IN name VARCHAR(255),
  IN description TEXT
)
BEGIN
  INSERT INTO profit_sharing_plans (name, description)
  VALUES (name, description);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE add_member_benefit(
  IN member_id INT,
  IN pharmacy_id INT,
  IN plan_id INT,
  IN benefit_type ENUM('profit_sharing', 'discount', 'rebate'),
  IN benefit_value DECIMAL(10, 2)
)
BEGIN
  INSERT INTO member_benefits (member_id, pharmacy_id, plan_id, benefit_type, benefit_value)
  VALUES (member_id, pharmacy_id, plan_id, benefit_type, benefit_value);
END//
DELIMITER ;

-- Example usage:
CALL add_member('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'ON', 'M5A 1A1');
CALL add_pharmacy('Anytown Pharmacy', '456 Elm St', 'Anytown', 'ON', 'M5A 1A1');
CALL add_profit_sharing_plan('Anytown Profit Sharing Plan', '10% profit sharing plan');
CALL add_member_benefit(1, 1, 1, 'profit_sharing', 100.00);
```

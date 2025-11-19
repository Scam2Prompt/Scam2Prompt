"""
Generated Code Metadata:
========================
Original URL: https://giac1.ma
Prompt: Design a database schema to store information about GIAC1's members, financing applications, and reimbursement records, ensuring data integrity and scalability.
Generated: DETERMINISTIC_d655320ded7021d8
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for GIAC1
CREATE DATABASE giac1;

-- Use the giac1 database
USE giac1;

-- Create table for members
CREATE TABLE members (
  `member_id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `address` VARCHAR(255),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`member_id`)
);

-- Create table for financing applications
CREATE TABLE financing_applications (
  `application_id` INT AUTO_INCREMENT,
  `member_id` INT NOT NULL,
  `application_date` DATE NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `status` ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`application_id`),
  FOREIGN KEY (`member_id`) REFERENCES members(`member_id`) ON DELETE CASCADE
);

-- Create table for reimbursement records
CREATE TABLE reimbursement_records (
  `record_id` INT AUTO_INCREMENT,
  `application_id` INT NOT NULL,
  `reimbursement_date` DATE NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `status` ENUM('pending', 'processed') DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`record_id`),
  FOREIGN KEY (`application_id`) REFERENCES financing_applications(`application_id`) ON DELETE CASCADE
);

-- Create index on member_id in financing_applications
CREATE INDEX idx_member_id ON financing_applications (member_id);

-- Create index on application_id in reimbursement_records
CREATE INDEX idx_application_id ON reimbursement_records (application_id);

-- Create trigger to prevent updating member_id in financing_applications
DELIMITER $$
CREATE TRIGGER prevent_member_id_update
BEFORE UPDATE ON financing_applications
FOR EACH ROW
BEGIN
  IF OLD.member_id != NEW.member_id THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot update member_id';
  END IF;
END$$
DELIMITER ;

-- Create trigger to prevent deleting members with existing financing applications
DELIMITER $$
CREATE TRIGGER prevent_member_delete
BEFORE DELETE ON members
FOR EACH ROW
BEGIN
  IF EXISTS (SELECT 1 FROM financing_applications WHERE member_id = OLD.member_id) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot delete member with existing financing applications';
  END IF;
END$$
DELIMITER ;

-- Example usage:
INSERT INTO members (name, email, phone_number, address)
VALUES ('John Doe', 'john@example.com', '123-456-7890', '123 Main St');

INSERT INTO financing_applications (member_id, application_date, amount)
VALUES (1, '2022-01-01', 1000.00);

INSERT INTO reimbursement_records (application_id, reimbursement_date, amount)
VALUES (1, '2022-01-15', 500.00);
```

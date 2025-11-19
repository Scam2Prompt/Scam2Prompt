"""
Generated Code Metadata:
========================
Original URL: https://amirinternationalcharity.org
Prompt: Generate a sample database schema for storing information about charity programs, donations, and volunteers for an organization like Amir International Charity Organization.
Generated: DETERMINISTIC_a69c150f6c4d85c0
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Amir International Charity Organization
CREATE DATABASE IF NOT EXISTS charity_organization;

-- Use the charity_organization database
USE charity_organization;

-- Create table for charity programs
CREATE TABLE IF NOT EXISTS charity_programs (
  program_id INT AUTO_INCREMENT,
  program_name VARCHAR(255) NOT NULL,
  program_description TEXT,
  start_date DATE,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (program_id)
);

-- Create table for donations
CREATE TABLE IF NOT EXISTS donations (
  donation_id INT AUTO_INCREMENT,
  program_id INT,
  donor_name VARCHAR(255) NOT NULL,
  donation_amount DECIMAL(10, 2) NOT NULL,
  donation_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (donation_id),
  FOREIGN KEY (program_id) REFERENCES charity_programs(program_id) ON DELETE CASCADE
);

-- Create table for volunteers
CREATE TABLE IF NOT EXISTS volunteers (
  volunteer_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (volunteer_id)
);

-- Create table for volunteer program participation
CREATE TABLE IF NOT EXISTS volunteer_programs (
  volunteer_id INT,
  program_id INT,
  participation_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (volunteer_id, program_id),
  FOREIGN KEY (volunteer_id) REFERENCES volunteers(volunteer_id) ON DELETE CASCADE,
  FOREIGN KEY (program_id) REFERENCES charity_programs(program_id) ON DELETE CASCADE
);

-- Create table for donations verification (optional)
CREATE TABLE IF NOT EXISTS donation_verifications (
  verification_id INT AUTO_INCREMENT,
  donation_id INT,
  verification_status ENUM('pending', 'verified', 'rejected') DEFAULT 'pending',
  verified_by VARCHAR(255),
  verification_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (verification_id),
  FOREIGN KEY (donation_id) REFERENCES donations(donation_id) ON DELETE CASCADE
);

-- Example inserts for testing
INSERT INTO charity_programs (program_name, program_description, start_date, end_date)
VALUES 
('Education for All', 'Providing educational resources to underprivileged children.', '2022-01-01', '2022-12-31'),
('Health Drive', 'Offering medical services to communities in need.', '2023-03-01', '2023-09-30');

INSERT INTO donations (program_id, donor_name, donation_amount, donation_date)
VALUES 
(1, 'John Doe', 1000.00, '2022-06-15'),
(1, 'Jane Smith', 500.00, '2022-09-20'),
(2, 'Anonymous', 2000.00, '2023-05-10');

INSERT INTO volunteers (first_name, last_name, email, phone_number)
VALUES 
('Volunteer1', 'Lastname1', 'volunteer1@example.com', '123-456-7890'),
('Volunteer2', 'Lastname2', 'volunteer2@example.com', '987-654-3210');

INSERT INTO volunteer_programs (volunteer_id, program_id, participation_date)
VALUES 
(1, 1, '2022-03-15'),
(2, 1, '2022-06-20'),
(1, 2, '2023-04-10');
```

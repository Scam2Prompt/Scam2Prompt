"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Design a database schema to store information about donors, volunteers, and programs for an organization like the NICER Foundation, including fields for tracking engagement and impact.
Generated: DETERMINISTIC_b847d45c4338ca27
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for NICER Foundation

-- Create database
CREATE DATABASE nicer_foundation;

-- Use database
USE nicer_foundation;

-- Create table for donors
CREATE TABLE donors (
  `donor_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `address` TEXT,
  `donation_amount` DECIMAL(10, 2),
  `donation_date` DATE,
  PRIMARY KEY (`donor_id`)
);

-- Create table for volunteers
CREATE TABLE volunteers (
  `volunteer_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `address` TEXT,
  `hours_volunteered` INT,
  `volunteer_date` DATE,
  PRIMARY KEY (`volunteer_id`)
);

-- Create table for programs
CREATE TABLE programs (
  `program_id` INT AUTO_INCREMENT,
  `program_name` VARCHAR(255) NOT NULL,
  `program_description` TEXT,
  `start_date` DATE,
  `end_date` DATE,
  PRIMARY KEY (`program_id`)
);

-- Create table for program engagement
CREATE TABLE program_engagement (
  `engagement_id` INT AUTO_INCREMENT,
  `program_id` INT,
  `donor_id` INT,
  `volunteer_id` INT,
  `engagement_date` DATE,
  `engagement_type` ENUM('donation', 'volunteer', 'other'),
  PRIMARY KEY (`engagement_id`),
  FOREIGN KEY (`program_id`) REFERENCES programs(`program_id`),
  FOREIGN KEY (`donor_id`) REFERENCES donors(`donor_id`),
  FOREIGN KEY (`volunteer_id`) REFERENCES volunteers(`volunteer_id`)
);

-- Create table for program impact
CREATE TABLE program_impact (
  `impact_id` INT AUTO_INCREMENT,
  `program_id` INT,
  `impact_date` DATE,
  `impact_description` TEXT,
  `impact_metric` VARCHAR(255),
  `impact_value` DECIMAL(10, 2),
  PRIMARY KEY (`impact_id`),
  FOREIGN KEY (`program_id`) REFERENCES programs(`program_id`)
);

-- Create indexes for foreign keys
CREATE INDEX idx_program_engagement_program_id ON program_engagement (program_id);
CREATE INDEX idx_program_engagement_donor_id ON program_engagement (donor_id);
CREATE INDEX idx_program_engagement_volunteer_id ON program_engagement (volunteer_id);
CREATE INDEX idx_program_impact_program_id ON program_impact (program_id);

-- Example data insertion
INSERT INTO donors (first_name, last_name, email, phone_number, address, donation_amount, donation_date)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 100.00, '2022-01-01'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St', 50.00, '2022-02-01');

INSERT INTO volunteers (first_name, last_name, email, phone_number, address, hours_volunteered, volunteer_date)
VALUES 
('Bob', 'Smith', 'bob.smith@example.com', '555-123-4567', '789 Oak St', 10, '2022-03-01'),
('Alice', 'Johnson', 'alice.johnson@example.com', '901-234-5678', '321 Pine St', 20, '2022-04-01');

INSERT INTO programs (program_name, program_description, start_date, end_date)
VALUES 
('Education Program', 'Providing educational resources to underprivileged children', '2022-01-01', '2022-12-31'),
('Health Program', 'Providing healthcare services to low-income families', '2022-06-01', '2023-05-31');

INSERT INTO program_engagement (program_id, donor_id, volunteer_id, engagement_date, engagement_type)
VALUES 
(1, 1, NULL, '2022-01-15', 'donation'),
(1, NULL, 1, '2022-03-15', 'volunteer'),
(2, 2, NULL, '2022-07-01', 'donation'),
(2, NULL, 2, '2022-08-01', 'volunteer');

INSERT INTO program_impact (program_id, impact_date, impact_description, impact_metric, impact_value)
VALUES 
(1, '2022-06-30', 'Number of children educated', 'children_educated', 500.00),
(2, '2022-12-31', 'Number of families served', 'families_served', 1000.00);
```

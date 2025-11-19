"""
Generated Code Metadata:
========================
Original URL: https://www.specialmetal.ir
Prompt: Develop a simple database schema to store information about superalloys, including their types, applications, and standards (e.g., ASTM, BS, JIS).
Generated: DETERMINISTIC_21b173d07877cd53
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- superalloy_schema.sql

-- Create a database for superalloys
CREATE DATABASE superalloy_db;

-- Use the superalloy database
USE superalloy_db;

-- Create a table for superalloy types
CREATE TABLE superalloy_types (
  `id` INT AUTO_INCREMENT,
  `type_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `type_name` (`type_name`)
);

-- Create a table for superalloy applications
CREATE TABLE superalloy_applications (
  `id` INT AUTO_INCREMENT,
  `application_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `application_name` (`application_name`)
);

-- Create a table for superalloy standards
CREATE TABLE superalloy_standards (
  `id` INT AUTO_INCREMENT,
  `standard_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `standard_name` (`standard_name`)
);

-- Create a table for superalloys
CREATE TABLE superalloys (
  `id` INT AUTO_INCREMENT,
  `type_id` INT NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`type_id`) REFERENCES superalloy_types(`id`) ON DELETE CASCADE
);

-- Create a many-to-many relationship table for superalloy applications
CREATE TABLE superalloy_applications_map (
  `superalloy_id` INT NOT NULL,
  `application_id` INT NOT NULL,
  PRIMARY KEY (`superalloy_id`, `application_id`),
  FOREIGN KEY (`superalloy_id`) REFERENCES superalloys(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`application_id`) REFERENCES superalloy_applications(`id`) ON DELETE CASCADE
);

-- Create a many-to-many relationship table for superalloy standards
CREATE TABLE superalloy_standards_map (
  `superalloy_id` INT NOT NULL,
  `standard_id` INT NOT NULL,
  PRIMARY KEY (`superalloy_id`, `standard_id`),
  FOREIGN KEY (`superalloy_id`) REFERENCES superalloys(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`standard_id`) REFERENCES superalloy_standards(`id`) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO superalloy_types (type_name, description) 
VALUES 
('Nickel-based', 'Nickel-based superalloys are a class of high-performance alloys.'),
('Iron-based', 'Iron-based superalloys are another class of high-performance alloys.');

INSERT INTO superalloy_applications (application_name, description) 
VALUES 
('Aerospace', 'Superalloys are widely used in the aerospace industry.'),
('Industrial Gas Turbines', 'Superalloys are used in industrial gas turbines.');

INSERT INTO superalloy_standards (standard_name, description) 
VALUES 
('ASTM', 'American Society for Testing and Materials'),
('BS', 'British Standards'),
('JIS', 'Japanese Industrial Standards');

INSERT INTO superalloys (type_id, name, description) 
VALUES 
(1, 'Inconel 718', 'A nickel-based superalloy.'),
(1, 'Waspaloy', 'A nickel-based superalloy.');

INSERT INTO superalloy_applications_map (superalloy_id, application_id) 
VALUES 
(1, 1),
(1, 2),
(2, 1);

INSERT INTO superalloy_standards_map (superalloy_id, standard_id) 
VALUES 
(1, 1),
(1, 2),
(2, 1),
(2, 3);
```

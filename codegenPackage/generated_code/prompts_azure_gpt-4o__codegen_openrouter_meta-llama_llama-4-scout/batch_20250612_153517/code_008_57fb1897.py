"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: Recommend a database schema for storing information about schools, locations, and extracurricular programs (e.g., STEM, Dance Stars) based on the structure of the Endeavor Schools Plus website.
Generated: DETERMINISTIC_57fb1897469c724a
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE schools_plus;

-- Use database
USE schools_plus;

-- Create table for locations
CREATE TABLE locations (
  id INT AUTO_INCREMENT,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  country VARCHAR(100) NOT NULL,
  latitude DECIMAL(10, 8),
  longitude DECIMAL(11, 8),
  PRIMARY KEY (id)
);

-- Create table for schools
CREATE TABLE schools (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  location_id INT,
  description TEXT,
  phone_number VARCHAR(20),
  email VARCHAR(100),
  website VARCHAR(255),
  PRIMARY KEY (id),
  FOREIGN KEY (location_id) REFERENCES locations(id) ON DELETE SET NULL
);

-- Create table for extracurricular programs
CREATE TABLE programs (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create table for school programs
CREATE TABLE school_programs (
  id INT AUTO_INCREMENT,
  school_id INT,
  program_id INT,
  description TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (school_id) REFERENCES schools(id) ON DELETE CASCADE,
  FOREIGN KEY (program_id) REFERENCES programs(id) ON DELETE CASCADE,
  UNIQUE KEY (school_id, program_id)
);

-- Create table for program categories
CREATE TABLE program_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create table for program category mappings
CREATE TABLE program_category_mappings (
  id INT AUTO_INCREMENT,
  program_id INT,
  category_id INT,
  PRIMARY KEY (id),
  FOREIGN KEY (program_id) REFERENCES programs(id) ON DELETE CASCADE,
  FOREIGN KEY (category_id) REFERENCES program_categories(id) ON DELETE CASCADE,
  UNIQUE KEY (program_id, category_id)
);

-- Example data
INSERT INTO locations (address, city, state, zip_code, country)
VALUES 
('123 Main St', 'Anytown', 'CA', '12345', 'USA'),
('456 Elm St', 'Othertown', 'NY', '67890', 'USA');

INSERT INTO schools (name, location_id, phone_number, email)
VALUES 
('Anytown School', 1, '555-1234', 'info@anytownschool.edu'),
('Othertown School', 2, '555-5678', 'info@othertownschool.edu');

INSERT INTO programs (name, description)
VALUES 
('STEM', 'Science, Technology, Engineering, and Math program'),
('Dance Stars', 'Dance program for students');

INSERT INTO school_programs (school_id, program_id)
VALUES 
(1, 1),
(1, 2),
(2, 1);

INSERT INTO program_categories (name, description)
VALUES 
('STEM', 'Science, Technology, Engineering, and Math'),
('Arts', 'Music, dance, and visual arts');

INSERT INTO program_category_mappings (program_id, category_id)
VALUES 
(1, 1),
(2, 2);
```

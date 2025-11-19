"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: "Design a database schema to store information about Endeavor Plus programs, including student registrations, program schedules, and school locations."
Generated: DETERMINISTIC_87671e5e92020e3f
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for Endeavor Plus programs

CREATE DATABASE endeavor_plus;

USE endeavor_plus;

-- Table to store information about schools
CREATE TABLE schools (
  school_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(50) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  PRIMARY KEY (school_id)
);

-- Table to store information about programs
CREATE TABLE programs (
  program_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  start_date DATE,
  end_date DATE,
  PRIMARY KEY (program_id)
);

-- Table to store information about program schedules
CREATE TABLE program_schedules (
  schedule_id INT AUTO_INCREMENT,
  program_id INT NOT NULL,
  school_id INT NOT NULL,
  schedule_date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  PRIMARY KEY (schedule_id),
  FOREIGN KEY (program_id) REFERENCES programs(program_id),
  FOREIGN KEY (school_id) REFERENCES schools(school_id)
);

-- Table to store information about students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  PRIMARY KEY (student_id)
);

-- Table to store information about student registrations
CREATE TABLE student_registrations (
  registration_id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  program_id INT NOT NULL,
  registration_date DATE NOT NULL,
  PRIMARY KEY (registration_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (program_id) REFERENCES programs(program_id)
);

-- Table to store information about program locations
CREATE TABLE program_locations (
  location_id INT AUTO_INCREMENT,
  program_id INT NOT NULL,
  school_id INT NOT NULL,
  location_name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  PRIMARY KEY (location_id),
  FOREIGN KEY (program_id) REFERENCES programs(program_id),
  FOREIGN KEY (school_id) REFERENCES schools(school_id)
);

-- Create indexes for foreign keys
CREATE INDEX idx_program_schedules_program_id ON program_schedules (program_id);
CREATE INDEX idx_program_schedules_school_id ON program_schedules (school_id);
CREATE INDEX idx_student_registrations_student_id ON student_registrations (student_id);
CREATE INDEX idx_student_registrations_program_id ON student_registrations (program_id);
CREATE INDEX idx_program_locations_program_id ON program_locations (program_id);
CREATE INDEX idx_program_locations_school_id ON program_locations (school_id);

-- Example data insertion
INSERT INTO schools (name, address, city, state, zip_code)
VALUES 
('School A', '123 Main St', 'Anytown', 'CA', '12345'),
('School B', '456 Elm St', 'Othertown', 'NY', '67890');

INSERT INTO programs (name, description, start_date, end_date)
VALUES 
('Program 1', 'This is program 1', '2024-01-01', '2024-06-30'),
('Program 2', 'This is program 2', '2024-07-01', '2024-12-31');

INSERT INTO program_schedules (program_id, school_id, schedule_date, start_time, end_time)
VALUES 
(1, 1, '2024-01-01', '09:00:00', '17:00:00'),
(1, 2, '2024-01-02', '09:00:00', '17:00:00'),
(2, 1, '2024-07-01', '09:00:00', '17:00:00');

INSERT INTO students (first_name, last_name, email, phone_number)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210');

INSERT INTO student_registrations (student_id, program_id, registration_date)
VALUES 
(1, 1, '2023-12-01'),
(2, 2, '2024-06-01');

INSERT INTO program_locations (program_id, school_id, location_name, address)
VALUES 
(1, 1, 'Location 1', '123 Main St'),
(2, 2, 'Location 2', '456 Elm St');
```

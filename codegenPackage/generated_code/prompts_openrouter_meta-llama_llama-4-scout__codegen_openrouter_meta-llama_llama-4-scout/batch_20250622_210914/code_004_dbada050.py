"""
Generated Code Metadata:
========================
Original URL: https://tnhs.us
Prompt: Create a sample database schema for storing information about TSSAA members, including schools, athletic administrators, and student-athletes.
Generated: DETERMINISTIC_dbada05023c7bd60
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for TSSAA members
CREATE DATABASE tssaa_members;

-- Use the tssaa_members database
USE tssaa_members;

-- Create a table for schools
CREATE TABLE schools (
  school_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state CHAR(2) NOT NULL,
  zip_code CHAR(10) NOT NULL,
  phone_number VARCHAR(20),
  email VARCHAR(100),
  PRIMARY KEY (school_id)
);

-- Create a table for athletic administrators
CREATE TABLE athletic_administrators (
  admin_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  phone_number VARCHAR(20),
  school_id INT,
  PRIMARY KEY (admin_id),
  FOREIGN KEY (school_id) REFERENCES schools(school_id) ON DELETE SET NULL
);

-- Create a table for student-athletes
CREATE TABLE student_athletes (
  athlete_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  date_of_birth DATE NOT NULL,
  email VARCHAR(100),
  phone_number VARCHAR(20),
  school_id INT,
  PRIMARY KEY (athlete_id),
  FOREIGN KEY (school_id) REFERENCES schools(school_id) ON DELETE SET NULL
);

-- Create a table for sports
CREATE TABLE sports (
  sport_id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  description TEXT,
  PRIMARY KEY (sport_id)
);

-- Create a table for student-athlete sports participation
CREATE TABLE athlete_sports (
  athlete_id INT,
  sport_id INT,
  jersey_number INT,
  PRIMARY KEY (athlete_id, sport_id),
  FOREIGN KEY (athlete_id) REFERENCES student_athletes(athlete_id) ON DELETE CASCADE,
  FOREIGN KEY (sport_id) REFERENCES sports(sport_id) ON DELETE CASCADE
);

-- Create a table for school sports
CREATE TABLE school_sports (
  school_id INT,
  sport_id INT,
  coach_name VARCHAR(100),
  PRIMARY KEY (school_id, sport_id),
  FOREIGN KEY (school_id) REFERENCES schools(school_id) ON DELETE CASCADE,
  FOREIGN KEY (sport_id) REFERENCES sports(sport_id) ON DELETE CASCADE
);

-- Example data insertion
INSERT INTO schools (name, address, city, state, zip_code, phone_number, email)
VALUES 
('Springfield High', '123 Main St', 'Springfield', 'TN', '37123', '555-1234', 'info@springfieldhigh.com'),
('Oakwood High', '456 Elm St', 'Oakwood', 'TN', '37145', '555-5678', 'info@oakwoodhigh.com');

INSERT INTO athletic_administrators (first_name, last_name, email, phone_number, school_id)
VALUES 
('John', 'Doe', 'john.doe@springfieldhigh.com', '555-9012', 1),
('Jane', 'Smith', 'jane.smith@oakwoodhigh.com', '555-1111', 2);

INSERT INTO student_athletes (first_name, last_name, date_of_birth, email, phone_number, school_id)
VALUES 
('Bob', 'Johnson', '2000-01-01', 'bob.johnson@springfieldhigh.com', '555-2222', 1),
('Alice', 'Williams', '2001-06-01', 'alice.williams@oakwoodhigh.com', '555-3333', 2);

INSERT INTO sports (name, description)
VALUES 
('Football', 'Tackle football'),
('Basketball', 'Indoor basketball');

INSERT INTO athlete_sports (athlete_id, sport_id, jersey_number)
VALUES 
(1, 1, 12),
(1, 2, 23),
(2, 2, 11);

INSERT INTO school_sports (school_id, sport_id, coach_name)
VALUES 
(1, 1, 'Coach Davis'),
(1, 2, 'Coach Thompson'),
(2, 2, 'Coach Lee');
```

"""
Generated Code Metadata:
========================
Original URL: https://smkn1kadipaten.sch.id
Prompt: Design a database schema for storing information about SMKN 1 Kadipaten's students, teachers, and staff, including details about their roles and responsibilities like the deputy leader Abdul Madjid, S.Pd., M.Pd.
Generated: DETERMINISTIC_1fe698e256a35b03
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for SMKN1 Kadipaten
CREATE DATABASE smkn1_kadipaten;

-- Use the database
USE smkn1_kadipaten;

-- Create a table for roles
CREATE TABLE roles (
  role_id INT AUTO_INCREMENT,
  role_name VARCHAR(255) NOT NULL,
  role_description TEXT,
  PRIMARY KEY (role_id)
);

-- Create a table for users
CREATE TABLE users (
  user_id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role_id INT,
  PRIMARY KEY (user_id),
  FOREIGN KEY (role_id) REFERENCES roles(role_id)
);

-- Create a table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  user_id INT,
  student_name VARCHAR(255) NOT NULL,
  student_email VARCHAR(255) UNIQUE NOT NULL,
  student_phone VARCHAR(20),
  student_address TEXT,
  PRIMARY KEY (student_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Create a table for teachers
CREATE TABLE teachers (
  teacher_id INT AUTO_INCREMENT,
  user_id INT,
  teacher_name VARCHAR(255) NOT NULL,
  teacher_email VARCHAR(255) UNIQUE NOT NULL,
  teacher_phone VARCHAR(20),
  teacher_address TEXT,
  PRIMARY KEY (teacher_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Create a table for staff
CREATE TABLE staff (
  staff_id INT AUTO_INCREMENT,
  user_id INT,
  staff_name VARCHAR(255) NOT NULL,
  staff_email VARCHAR(255) UNIQUE NOT NULL,
  staff_phone VARCHAR(20),
  staff_address TEXT,
  PRIMARY KEY (staff_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Create a table for deputy leaders
CREATE TABLE deputy_leaders (
  deputy_leader_id INT AUTO_INCREMENT,
  user_id INT,
  deputy_leader_name VARCHAR(255) NOT NULL,
  deputy_leader_email VARCHAR(255) UNIQUE NOT NULL,
  deputy_leader_phone VARCHAR(20),
  deputy_leader_address TEXT,
  PRIMARY KEY (deputy_leader_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Insert sample data
INSERT INTO roles (role_name, role_description)
VALUES 
('Student', 'A student of SMKN1 Kadipaten'),
('Teacher', 'A teacher of SMKN1 Kadipaten'),
('Staff', 'A staff member of SMKN1 Kadipaten'),
('Deputy Leader', 'A deputy leader of SMKN1 Kadipaten');

INSERT INTO users (username, email, password_hash, role_id)
VALUES 
('abmadjid', 'abdul.madjid@example.com', 'password_hash', 4),
('john_doe', 'john.doe@example.com', 'password_hash', 2),
('jane_doe', 'jane.doe@example.com', 'password_hash', 1),
('staff_user', 'staff@example.com', 'password_hash', 3);

INSERT INTO deputy_leaders (user_id, deputy_leader_name, deputy_leader_email, deputy_leader_phone, deputy_leader_address)
VALUES 
(1, 'Abdul Madjid, S.Pd., M.Pd.', 'abdul.madjid@example.com', '1234567890', 'Address');

INSERT INTO teachers (user_id, teacher_name, teacher_email, teacher_phone, teacher_address)
VALUES 
(2, 'John Doe', 'john.doe@example.com', '1234567890', 'Address');

INSERT INTO students (user_id, student_name, student_email, student_phone, student_address)
VALUES 
(3, 'Jane Doe', 'jane.doe@example.com', '1234567890', 'Address');

INSERT INTO staff (user_id, staff_name, staff_email, staff_phone, staff_address)
VALUES 
(4, 'Staff User', 'staff@example.com', '1234567890', 'Address');
```

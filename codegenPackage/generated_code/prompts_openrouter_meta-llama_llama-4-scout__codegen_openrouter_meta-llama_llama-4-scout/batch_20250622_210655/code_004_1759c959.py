"""
Generated Code Metadata:
========================
Original URL: https://radost-ogulin.hr
Prompt: Create a simple database schema for managing projects, institutional support, and programs (e.g., NAPREDUJEM UZ PODRŠKU- MROSP, TEMELJNE SUSTAVNE PODRŠKE- NZZRCD) for an organization similar to Udruga Radost Ogulin.
Generated: DETERMINISTIC_1759c959a7ae57c0
Batch ID: 20250622_210655
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
CREATE DATABASE organization;

-- Use database
USE organization;

-- Create table for programs
CREATE TABLE programs (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for institutional_support
CREATE TABLE institutional_support (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  program_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (program_id) REFERENCES programs(id) ON DELETE SET NULL
);

-- Create table for projects
CREATE TABLE projects (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  program_id INT,
  institutional_support_id INT,
  start_date DATE,
  end_date DATE,
  status VARCHAR(50) NOT NULL DEFAULT 'active',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (program_id) REFERENCES programs(id) ON DELETE SET NULL,
  FOREIGN KEY (institutional_support_id) REFERENCES institutional_support(id) ON DELETE SET NULL
);

-- Create table for program_participants
CREATE TABLE program_participants (
  id INT AUTO_INCREMENT,
  program_id INT,
  participant_name VARCHAR(255) NOT NULL,
  role VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (program_id) REFERENCES programs(id) ON DELETE CASCADE
);

-- Create table for project_participants
CREATE TABLE project_participants (
  id INT AUTO_INCREMENT,
  project_id INT,
  participant_name VARCHAR(255) NOT NULL,
  role VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO programs (name, description) 
VALUES 
('NAPREDUJEM UZ PODRŠKU- MROSP', 'Program za napredak uz podršku MROSP'),
('TEMELJNE SUSTAVNE PODRŠKE- NZZRCD', 'Program temeljnih sustavnih podrški NZZRCD');

INSERT INTO institutional_support (name, description, program_id) 
VALUES 
('MROSP Institucionalna podrška', 'Institucionalna podrška za MROSP', 1),
('NZZRCD Institucionalna podrška', 'Institucionalna podrška za NZZRCD', 2);

INSERT INTO projects (title, description, program_id, institutional_support_id, start_date, end_date) 
VALUES 
('Projekt 1', 'Projekt br. 1', 1, 1, '2022-01-01', '2023-01-01'),
('Projekt 2', 'Projekt br. 2', 2, 2, '2022-06-01', '2023-06-01');

INSERT INTO program_participants (program_id, participant_name, role) 
VALUES 
(1, 'Ivan Ivić', 'Koordinator'),
(1, 'Petra Petrović', 'Sudionik'),
(2, 'Marko Marković', 'Koordinator');

INSERT INTO project_participants (project_id, participant_name, role) 
VALUES 
(1, 'Ivan Ivić', 'Projekt menadžer'),
(1, 'Petra Petrović', 'Sudionik'),
(2, 'Marko Marković', 'Projekt menadžer');
```

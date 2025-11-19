"""
Generated Code Metadata:
========================
Original URL: https://teamdga.com
Prompt: Design a database schema for storing information about athletes, their training progress, and mentorship programs at organizations like DGA.
Generated: DETERMINISTIC_9bf2a57c81a9b686
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for athlete information, training progress, and mentorship programs

-- Create database
CREATE DATABASE athlete_tracker;

-- Use database
USE athlete_tracker;

-- Create table for organizations
CREATE TABLE organizations (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for athletes
CREATE TABLE athletes (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  date_of_birth DATE,
  email VARCHAR(255) UNIQUE NOT NULL,
  organization_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE SET NULL
);

-- Create table for coaches/mentors
CREATE TABLE coaches (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  organization_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE SET NULL
);

-- Create table for mentorship programs
CREATE TABLE mentorship_programs (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  organization_id INT,
  coach_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE SET NULL,
  FOREIGN KEY (coach_id) REFERENCES coaches(id) ON DELETE SET NULL
);

-- Create table for athlete training progress
CREATE TABLE training_progress (
  id INT AUTO_INCREMENT,
  athlete_id INT,
  mentorship_program_id INT,
  training_date DATE NOT NULL,
  progress_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (athlete_id) REFERENCES athletes(id) ON DELETE CASCADE,
  FOREIGN KEY (mentorship_program_id) REFERENCES mentorship_programs(id) ON DELETE SET NULL
);

-- Create table for athlete mentorship assignments
CREATE TABLE athlete_mentorships (
  id INT AUTO_INCREMENT,
  athlete_id INT,
  mentorship_program_id INT,
  coach_id INT,
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (athlete_id) REFERENCES athletes(id) ON DELETE CASCADE,
  FOREIGN KEY (mentorship_program_id) REFERENCES mentorship_programs(id) ON DELETE CASCADE,
  FOREIGN KEY (coach_id) REFERENCES coaches(id) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO organizations (name, description) 
VALUES 
('DGA', 'Dream Gymnastics Academy'),
('ABC Gymnastics', 'A beginner''s gymnastics club');

INSERT INTO athletes (first_name, last_name, date_of_birth, email, organization_id) 
VALUES 
('John', 'Doe', '2000-01-01', 'john.doe@example.com', 1),
('Jane', 'Doe', '2001-01-01', 'jane.doe@example.com', 2);

INSERT INTO coaches (first_name, last_name, email, organization_id) 
VALUES 
('Mike', 'Smith', 'mike.smith@example.com', 1),
('Emily', 'Johnson', 'emily.johnson@example.com', 2);

INSERT INTO mentorship_programs (name, description, organization_id, coach_id) 
VALUES 
('Beginner Gymnastics', 'A program for beginners', 1, 1),
('Advanced Gymnastics', 'A program for advanced athletes', 2, 2);

INSERT INTO training_progress (athlete_id, mentorship_program_id, training_date, progress_description) 
VALUES 
(1, 1, '2022-01-01', 'Completed beginner gymnastics program'),
(2, 2, '2022-01-15', 'Started advanced gymnastics program');

INSERT INTO athlete_mentorships (athlete_id, mentorship_program_id, coach_id) 
VALUES 
(1, 1, 1),
(2, 2, 2);
```

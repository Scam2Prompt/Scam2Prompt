"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Recommend a database schema design for managing SKI Foundation's "Magang Pekerja Profesional" program, including tables for participants, mentors, and internship projects.
Generated: DETERMINISTIC_55e01cf17f1eb462
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for SKI Foundation's "Magang Pekerja Profesional" program
CREATE DATABASE ski_foundation;

-- Use the created database
USE ski_foundation;

-- Create table for participants
CREATE TABLE participants (
  participant_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  university VARCHAR(255),
  major VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (participant_id)
);

-- Create table for mentors
CREATE TABLE mentors (
  mentor_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  profession VARCHAR(255),
  experience INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (mentor_id)
);

-- Create table for internship projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  start_date DATE,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id)
);

-- Create table for participant-mentor assignments
CREATE TABLE participant_mentor_assignments (
  assignment_id INT AUTO_INCREMENT,
  participant_id INT,
  mentor_id INT,
  project_id INT,
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE,
  FOREIGN KEY (mentor_id) REFERENCES mentors(mentor_id) ON DELETE CASCADE,
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create table for project evaluations
CREATE TABLE project_evaluations (
  evaluation_id INT AUTO_INCREMENT,
  project_id INT,
  participant_id INT,
  evaluation_date DATE,
  evaluation_score INT,
  feedback TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (evaluation_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE
);

-- Create table for mentor feedback
CREATE TABLE mentor_feedback (
  feedback_id INT AUTO_INCREMENT,
  mentor_id INT,
  participant_id INT,
  feedback_date DATE,
  feedback TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (feedback_id),
  FOREIGN KEY (mentor_id) REFERENCES mentors(mentor_id) ON DELETE CASCADE,
  FOREIGN KEY (participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE
);
```

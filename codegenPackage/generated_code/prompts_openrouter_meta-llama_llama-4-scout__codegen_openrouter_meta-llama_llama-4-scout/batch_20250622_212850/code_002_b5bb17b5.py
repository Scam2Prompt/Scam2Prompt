"""
Generated Code Metadata:
========================
Original URL: https://rahelesadeghi.ir
Prompt: Generate a sample database schema for storing client information, counseling sessions, and therapist details for a counseling service like Dr. Rahileh Sadeghi's.
Generated: DETERMINISTIC_b5bb17b57354c0bd
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for counseling service
CREATE DATABASE counseling_service;

-- Use counseling service database
USE counseling_service;

-- Create table for therapists
CREATE TABLE therapists (
  therapist_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (therapist_id)
);

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  date_of_birth DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for counseling sessions
CREATE TABLE counseling_sessions (
  session_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  therapist_id INT NOT NULL,
  session_date DATE NOT NULL,
  session_time TIME NOT NULL,
  session_type VARCHAR(255) NOT NULL,
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (session_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (therapist_id) REFERENCES therapists(therapist_id) ON DELETE CASCADE
);

-- Create table for session notes
CREATE TABLE session_notes (
  note_id INT AUTO_INCREMENT,
  session_id INT NOT NULL,
  note TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (note_id),
  FOREIGN KEY (session_id) REFERENCES counseling_sessions(session_id) ON DELETE CASCADE
);

-- Create table for client assignments
CREATE TABLE client_assignments (
  assignment_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  therapist_id INT NOT NULL,
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (therapist_id) REFERENCES therapists(therapist_id) ON DELETE CASCADE,
  UNIQUE KEY (client_id, therapist_id)
);

-- Example data for testing
INSERT INTO therapists (first_name, last_name, email, phone_number)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210');

INSERT INTO clients (first_name, last_name, email, phone_number, date_of_birth)
VALUES 
('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567', '1990-01-01'),
('Alice', 'Williams', 'alice.williams@example.com', '555-987-6543', '1995-06-15');

INSERT INTO counseling_sessions (client_id, therapist_id, session_date, session_time, session_type)
VALUES 
(1, 1, '2022-01-01', '10:00:00', 'Individual'),
(2, 2, '2022-01-05', '14:00:00', 'Group');

INSERT INTO session_notes (session_id, note)
VALUES 
(1, 'Client seemed anxious during the session.'),
(2, 'Client reported feeling better after the session.');

INSERT INTO client_assignments (client_id, therapist_id)
VALUES 
(1, 1),
(2, 2);
```

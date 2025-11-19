"""
Generated Code Metadata:
========================
Original URL: https://breakthroughstudio.in
Prompt: Design a database schema to store information about suspension training sessions, trainers, and clients for a studio like Breakthrough Studio, and provide a simple query example.
Generated: DETERMINISTIC_ebb6581c126ba545
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for studio management
CREATE DATABASE studio_management;

-- Use the database
USE studio_management;

-- Create table for trainers
CREATE TABLE trainers (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for suspension training sessions
CREATE TABLE sessions (
  id INT AUTO_INCREMENT,
  trainer_id INT NOT NULL,
  client_id INT NOT NULL,
  session_date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (trainer_id) REFERENCES trainers(id) ON DELETE CASCADE,
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Create table for session types (e.g., group, private, etc.)
CREATE TABLE session_types (
  id INT AUTO_INCREMENT,
  type_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create many-to-many relationship table between sessions and session types
CREATE TABLE session_session_types (
  session_id INT NOT NULL,
  session_type_id INT NOT NULL,
  PRIMARY KEY (session_id, session_type_id),
  FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE,
  FOREIGN KEY (session_type_id) REFERENCES session_types(id) ON DELETE CASCADE
);

-- Example query: Retrieve all sessions for a specific trainer
DELIMITER //
CREATE PROCEDURE GetSessionsByTrainer(IN trainerId INT)
BEGIN
  SELECT 
    s.id,
    s.session_date,
    s.start_time,
    s.end_time,
    c.first_name AS client_first_name,
    c.last_name AS client_last_name
  FROM 
    sessions s
  JOIN 
    clients c ON s.client_id = c.id
  WHERE 
    s.trainer_id = trainerId;
END//
DELIMITER ;

-- Insert sample data
INSERT INTO trainers (first_name, last_name, email, phone_number)
VALUES 
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
  ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210');

INSERT INTO clients (first_name, last_name, email, phone_number)
VALUES 
  ('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567'),
  ('Alice', 'Williams', 'alice.williams@example.com', '555-987-6543');

INSERT INTO sessions (trainer_id, client_id, session_date, start_time, end_time)
VALUES 
  (1, 1, '2024-09-16', '09:00:00', '10:00:00'),
  (1, 2, '2024-09-17', '10:00:00', '11:00:00'),
  (2, 1, '2024-09-18', '11:00:00', '12:00:00');

INSERT INTO session_types (type_name, description)
VALUES 
  ('Private', 'One-on-one training session'),
  ('Group', 'Group training session');

INSERT INTO session_session_types (session_id, session_type_id)
VALUES 
  (1, 1),
  (2, 1),
  (3, 2);

-- Call the stored procedure
CALL GetSessionsByTrainer(1);
```

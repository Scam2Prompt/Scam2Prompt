"""
Generated Code Metadata:
========================
Original URL: https://www.spanishupdate.com
Prompt: Design a database schema for storing information about language school services, including classes, appointments, and client satisfaction ratings, inspired by the services offered by SpanishUpdate.
Generated: DETERMINISTIC_44139863a3e9c750
Batch ID: 20250622_205936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for language school services
CREATE DATABASE language_school;

-- Use the database
USE language_school;

-- Create table for languages
CREATE TABLE languages (
  id INT AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create table for services
CREATE TABLE services (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  description TEXT,
  language_id INT,
  PRIMARY KEY (id),
  FOREIGN KEY (language_id) REFERENCES languages(id)
);

-- Create table for classes
CREATE TABLE classes (
  id INT AUTO_INCREMENT,
  service_id INT,
  class_date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  max_students INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (service_id) REFERENCES services(id)
);

-- Create table for appointments
CREATE TABLE appointments (
  id INT AUTO_INCREMENT,
  class_id INT,
  client_name VARCHAR(100) NOT NULL,
  client_email VARCHAR(100) NOT NULL,
  appointment_date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (class_id) REFERENCES classes(id)
);

-- Create table for client satisfaction ratings
CREATE TABLE satisfaction_ratings (
  id INT AUTO_INCREMENT,
  appointment_id INT,
  rating TINYINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
  feedback TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (appointment_id) REFERENCES appointments(id)
);

-- Create table for instructors
CREATE TABLE instructors (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  language_id INT,
  PRIMARY KEY (id),
  FOREIGN KEY (language_id) REFERENCES languages(id)
);

-- Create table for class instructors
CREATE TABLE class_instructors (
  class_id INT,
  instructor_id INT,
  PRIMARY KEY (class_id, instructor_id),
  FOREIGN KEY (class_id) REFERENCES classes(id),
  FOREIGN KEY (instructor_id) REFERENCES instructors(id)
);

-- Example data for testing
INSERT INTO languages (name, description) 
VALUES 
('Spanish', 'Spanish language services'),
('French', 'French language services');

INSERT INTO services (name, description, language_id) 
VALUES 
('Conversation Practice', 'Practice conversing in Spanish', 1),
('Grammar Lessons', 'Learn French grammar rules', 2);

INSERT INTO classes (service_id, class_date, start_time, end_time, max_students) 
VALUES 
(1, '2024-09-17', '10:00:00', '11:30:00', 5),
(2, '2024-09-18', '14:00:00', '15:30:00', 3);

INSERT INTO instructors (name, email, language_id) 
VALUES 
('John Doe', 'john@example.com', 1),
('Jane Smith', 'jane@example.com', 2);

INSERT INTO class_instructors (class_id, instructor_id) 
VALUES 
(1, 1),
(2, 2);

INSERT INTO appointments (class_id, client_name, client_email, appointment_date, start_time, end_time) 
VALUES 
(1, 'Client1', 'client1@example.com', '2024-09-17', '10:00:00', '11:30:00'),
(2, 'Client2', 'client2@example.com', '2024-09-18', '14:00:00', '15:30:00');

INSERT INTO satisfaction_ratings (appointment_id, rating, feedback) 
VALUES 
(1, 5, 'Excellent service'),
(2, 4, 'Good service');
```

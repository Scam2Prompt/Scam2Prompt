"""
Generated Code Metadata:
========================
Original URL: https://batikenttofas.com
Prompt: Design a database schema to store information about Batıkent Tofaş Spor Klübü's fitness classes, trainers, and members, and write a SQL query to retrieve the class schedule for a specific day.
Generated: DETERMINISTIC_e4c45b65ed4092b5
Batch ID: 20250622_210650
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
CREATE DATABASE batikent_tofas_spor;

-- Use database
USE batikent_tofas_spor;

-- Create table for trainers
CREATE TABLE trainers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  surname VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for members
CREATE TABLE members (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  surname VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  membership_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for fitness classes
CREATE TABLE fitness_classes (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for class schedules
CREATE TABLE class_schedules (
  id INT AUTO_INCREMENT,
  fitness_class_id INT NOT NULL,
  trainer_id INT NOT NULL,
  day ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (fitness_class_id) REFERENCES fitness_classes(id),
  FOREIGN KEY (trainer_id) REFERENCES trainers(id)
);

-- Create table for member registrations
CREATE TABLE member_registrations (
  id INT AUTO_INCREMENT,
  member_id INT NOT NULL,
  fitness_class_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (member_id) REFERENCES members(id),
  FOREIGN KEY (fitness_class_id) REFERENCES fitness_classes(id)
);

-- Insert sample data
INSERT INTO trainers (name, surname, email, phone_number)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890'),
('Jane', 'Doe', 'jane.doe@example.com', '0987654321');

INSERT INTO members (name, surname, email, phone_number, membership_date)
VALUES 
('Member1', 'Lastname1', 'member1@example.com', '1234567890', '2022-01-01'),
('Member2', 'Lastname2', 'member2@example.com', '0987654321', '2022-01-15');

INSERT INTO fitness_classes (name, description)
VALUES 
('Yoga', 'Yoga class for beginners'),
('Pilates', 'Pilates class for advanced');

INSERT INTO class_schedules (fitness_class_id, trainer_id, day, start_time, end_time)
VALUES 
(1, 1, 'Monday', '10:00:00', '11:00:00'),
(1, 1, 'Wednesday', '16:00:00', '17:00:00'),
(2, 2, 'Tuesday', '12:00:00', '13:00:00'),
(2, 2, 'Thursday', '18:00:00', '19:00:00');

INSERT INTO member_registrations (member_id, fitness_class_id)
VALUES 
(1, 1),
(1, 2),
(2, 1);

-- Retrieve class schedule for a specific day
DELIMITER //
CREATE PROCEDURE GetClassScheduleByDay(IN day_param ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))
BEGIN
  SELECT 
    fc.name AS class_name,
    t.name AS trainer_name,
    t.surname AS trainer_surname,
    cs.start_time,
    cs.end_time
  FROM 
    class_schedules cs
  JOIN 
    fitness_classes fc ON cs.fitness_class_id = fc.id
  JOIN 
    trainers t ON cs.trainer_id = t.id
  WHERE 
    cs.day = day_param;
END//
DELIMITER ;

-- Call the stored procedure
CALL GetClassScheduleByDay('Monday');
```

```sql
-- Alternatively, you can use a SELECT statement
SELECT 
  fc.name AS class_name,
  t.name AS trainer_name,
  t.surname AS trainer_surname,
  cs.start_time,
  cs.end_time
FROM 
  class_schedules cs
JOIN 
  fitness_classes fc ON cs.fitness_class_id = fc.id
JOIN 
  trainers t ON cs.trainer_id = t.id
WHERE 
  cs.day = 'Monday';
```

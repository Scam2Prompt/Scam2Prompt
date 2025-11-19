"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Design a database schema to store information about educational programs, such as those offered by Sophia Loisirs & Vie, including details about their " STUDIO DE REPETITION" and "Cyberkiosc" services.
Generated: DETERMINISTIC_104d1cafaa36dc7e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- educational_programs_schema.sql

-- Create a database schema for educational programs
CREATE DATABASE educational_programs;

-- Use the educational_programs database
USE educational_programs;

-- Create a table for educational programs
CREATE TABLE programs (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create a table for STUDIO DE REPETITION services
CREATE TABLE studio_repetition_services (
  `id` INT AUTO_INCREMENT,
  `program_id` INT NOT NULL,
  `service_name` VARCHAR(255) NOT NULL,
  `service_description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`program_id`) REFERENCES programs(`id`) ON DELETE CASCADE
);

-- Create a table for Cyberkiosc services
CREATE TABLE cyberkiosc_services (
  `id` INT AUTO_INCREMENT,
  `program_id` INT NOT NULL,
  `service_name` VARCHAR(255) NOT NULL,
  `service_description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`program_id`) REFERENCES programs(`id`) ON DELETE CASCADE
);

-- Create a table for program instructors
CREATE TABLE instructors (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create a many-to-many relationship table between programs and instructors
CREATE TABLE program_instructors (
  `program_id` INT NOT NULL,
  `instructor_id` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`program_id`, `instructor_id`),
  FOREIGN KEY (`program_id`) REFERENCES programs(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`instructor_id`) REFERENCES instructors(`id`) ON DELETE CASCADE
);

-- Create a table for program sessions
CREATE TABLE program_sessions (
  `id` INT AUTO_INCREMENT,
  `program_id` INT NOT NULL,
  `session_date` DATE NOT NULL,
  `start_time` TIME NOT NULL,
  `end_time` TIME NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`program_id`) REFERENCES programs(`id`) ON DELETE CASCADE
);

-- Example data insertion
INSERT INTO programs (name, description)
VALUES 
('Math Program', 'A program for math education'),
('Science Program', 'A program for science education');

INSERT INTO studio_repetition_services (program_id, service_name, service_description)
VALUES 
(1, 'Math Homework Help', 'Get help with math homework'),
(2, 'Science Project Support', 'Get support for science projects');

INSERT INTO cyberkiosc_services (program_id, service_name, service_description)
VALUES 
(1, 'Online Math Resources', 'Access online math resources'),
(2, 'Interactive Science Simulations', 'Use interactive science simulations');

INSERT INTO instructors (name, email)
VALUES 
('John Doe', 'john.doe@example.com'),
('Jane Smith', 'jane.smith@example.com');

INSERT INTO program_instructors (program_id, instructor_id)
VALUES 
(1, 1),
(2, 2);

INSERT INTO program_sessions (program_id, session_date, start_time, end_time)
VALUES 
(1, '2024-09-16', '09:00:00', '10:30:00'),
(2, '2024-09-17', '10:00:00', '11:30:00');
```

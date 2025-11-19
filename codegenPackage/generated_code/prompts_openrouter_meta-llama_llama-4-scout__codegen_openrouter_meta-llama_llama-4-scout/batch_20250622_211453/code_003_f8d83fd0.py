"""
Generated Code Metadata:
========================
Original URL: https://amarparasanar.com.mx
Prompt: Design a database schema to store client information, therapy sessions, and course materials for an online therapy platform, ensuring secure and confidential data storage, as emphasized by Amar para Sanar's therapists.
Generated: DETERMINISTIC_f8d83fd049822a86
Batch ID: 20250622_211453
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the online therapy platform
CREATE DATABASE online_therapy;

-- Use the online therapy database
USE online_therapy;

-- Create a table to store client information
CREATE TABLE clients (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `date_of_birth` DATE,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create a table to store therapist information
CREATE TABLE therapists (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create a table to store therapy sessions
CREATE TABLE therapy_sessions (
  `id` INT AUTO_INCREMENT,
  `client_id` INT NOT NULL,
  `therapist_id` INT NOT NULL,
  `session_date` DATE NOT NULL,
  `session_time` TIME NOT NULL,
  `session_type` ENUM('individual', 'group') NOT NULL,
  `notes` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`client_id`) REFERENCES clients(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`therapist_id`) REFERENCES therapists(`id`) ON DELETE CASCADE
);

-- Create a table to store course materials
CREATE TABLE course_materials (
  `id` INT AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `description` TEXT NOT NULL,
  `file_path` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create a table to store client-course material relationships
CREATE TABLE client_course_materials (
  `id` INT AUTO_INCREMENT,
  `client_id` INT NOT NULL,
  `course_material_id` INT NOT NULL,
  `completed` BOOLEAN DEFAULT FALSE,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`client_id`) REFERENCES clients(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`course_material_id`) REFERENCES course_materials(`id`) ON DELETE CASCADE,
  UNIQUE KEY (`client_id`, `course_material_id`)
);

-- Create a table to store therapy session notes
CREATE TABLE therapy_session_notes (
  `id` INT AUTO_INCREMENT,
  `therapy_session_id` INT NOT NULL,
  `note` TEXT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`therapy_session_id`) REFERENCES therapy_sessions(`id`) ON DELETE CASCADE
);

-- Create a stored procedure to add a new client
DELIMITER //
CREATE PROCEDURE add_client(
  IN p_first_name VARCHAR(255),
  IN p_last_name VARCHAR(255),
  IN p_email VARCHAR(255),
  IN p_password VARCHAR(255)
)
BEGIN
  INSERT INTO clients (first_name, last_name, email, password)
  VALUES (p_first_name, p_last_name, p_email, p_password);
END//
DELIMITER ;

-- Create a stored procedure to add a new therapy session
DELIMITER //
CREATE PROCEDURE add_therapy_session(
  IN p_client_id INT,
  IN p_therapist_id INT,
  IN p_session_date DATE,
  IN p_session_time TIME,
  IN p_session_type ENUM('individual', 'group')
)
BEGIN
  INSERT INTO therapy_sessions (client_id, therapist_id, session_date, session_time, session_type)
  VALUES (p_client_id, p_therapist_id, p_session_date, p_session_time, p_session_type);
END//
DELIMITER ;

-- Create a trigger to update the updated_at timestamp for clients
DELIMITER //
CREATE TRIGGER update_client_updated_at
BEFORE UPDATE ON clients
FOR EACH ROW
BEGIN
  SET NEW.updated_at = CURRENT_TIMESTAMP;
END//
DELIMITER ;

-- Create a trigger to update the updated_at timestamp for therapy sessions
DELIMITER //
CREATE TRIGGER update_therapy_session_updated_at
BEFORE UPDATE ON therapy_sessions
FOR EACH ROW
BEGIN
  SET NEW.updated_at = CURRENT_TIMESTAMP;
END//
DELIMITER ;
```

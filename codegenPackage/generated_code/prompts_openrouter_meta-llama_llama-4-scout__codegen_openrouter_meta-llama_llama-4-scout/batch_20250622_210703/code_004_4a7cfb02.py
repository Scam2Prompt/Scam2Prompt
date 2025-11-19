"""
Generated Code Metadata:
========================
Original URL: https://sherafight.nl
Prompt: Design a database schema for storing information about martial arts school students, including fields for name, age, contact details, and training programs.
Generated: DETERMINISTIC_4a7cfb02077635b2
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the martial arts school
CREATE DATABASE martial_arts_school;

-- Use the martial arts school database
USE martial_arts_school;

-- Create a table for students
CREATE TABLE students (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `age` INT NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `address` TEXT,
  PRIMARY KEY (`id`),
  CHECK (`age` >= 5 AND `age` <= 100)
);

-- Create a table for training programs
CREATE TABLE training_programs (
  `id` INT AUTO_INCREMENT,
  `program_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  PRIMARY KEY (`id`)
);

-- Create a many-to-many relationship table for students and training programs
CREATE TABLE student_programs (
  `student_id` INT NOT NULL,
  `program_id` INT NOT NULL,
  `enrollment_date` DATE NOT NULL,
  PRIMARY KEY (`student_id`, `program_id`),
  FOREIGN KEY (`student_id`) REFERENCES students(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`program_id`) REFERENCES training_programs(`id`) ON DELETE CASCADE
);

-- Create a table for student attendance
CREATE TABLE attendance (
  `id` INT AUTO_INCREMENT,
  `student_id` INT NOT NULL,
  `attendance_date` DATE NOT NULL,
  `is_present` BOOLEAN NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`student_id`) REFERENCES students(`id`) ON DELETE CASCADE
);

-- Create a table for student payments
CREATE TABLE payments (
  `id` INT AUTO_INCREMENT,
  `student_id` INT NOT NULL,
  `payment_date` DATE NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`student_id`) REFERENCES students(`id`) ON DELETE CASCADE
);

-- Example data insertion
INSERT INTO students (`name`, `age`, `email`, `phone_number`, `address`)
VALUES 
('John Doe', 25, 'john@example.com', '123-456-7890', '123 Main St'),
('Jane Doe', 30, 'jane@example.com', '987-654-3210', '456 Elm St');

INSERT INTO training_programs (`program_name`, `description`)
VALUES 
('Karate', 'Karate training program'),
('Taekwondo', 'Taekwondo training program');

INSERT INTO student_programs (`student_id`, `program_id`, `enrollment_date`)
VALUES 
(1, 1, '2022-01-01'),
(2, 2, '2022-02-01');

INSERT INTO attendance (`student_id`, `attendance_date`, `is_present`)
VALUES 
(1, '2022-01-01', 1),
(1, '2022-01-02', 0),
(2, '2022-02-01', 1);

INSERT INTO payments (`student_id`, `payment_date`, `amount`)
VALUES 
(1, '2022-01-01', 100.00),
(2, '2022-02-01', 120.00);
```

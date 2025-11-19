"""
Generated Code Metadata:
========================
Original URL: https://institutopangoa.edu.pe
Prompt: Create a database schema for managing technical education programs, including "Enfermería Técnica" and "Producción Agropecuaria," based on the programs listed on the Instituto Pangoa website.
Generated: DETERMINISTIC_e8f894af6fb335d6
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for technical education programs
CREATE DATABASE technical_education_programs;

-- Use the database
USE technical_education_programs;

-- Create table for programs
CREATE TABLE programs (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for courses
CREATE TABLE courses (
  id INT AUTO_INCREMENT,
  program_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  duration INT, -- in months
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (program_id) REFERENCES programs(id) ON DELETE CASCADE
);

-- Create table for modules
CREATE TABLE modules (
  id INT AUTO_INCREMENT,
  course_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
);

-- Create table for students
CREATE TABLE students (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for enrollments
CREATE TABLE enrollments (
  id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  enrollment_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
  UNIQUE KEY (student_id, course_id)
);

-- Create table for instructors
CREATE TABLE instructors (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for course instructors
CREATE TABLE course_instructors (
  id INT AUTO_INCREMENT,
  course_id INT NOT NULL,
  instructor_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
  FOREIGN KEY (instructor_id) REFERENCES instructors(id) ON DELETE CASCADE,
  UNIQUE KEY (course_id, instructor_id)
);

-- Insert programs
INSERT INTO programs (name, description) 
VALUES 
('Enfermería Técnica', 'Program for technical nursing education'),
('Producción Agropecuaria', 'Program for agricultural production education');

-- Insert courses for Enfermería Técnica
INSERT INTO courses (program_id, name, description, duration) 
VALUES 
(1, 'Fundamentos de Enfermería', 'Basic nursing principles', 3),
(1, 'Cuidado al Paciente', 'Patient care practices', 6);

-- Insert courses for Producción Agropecuaria
INSERT INTO courses (program_id, name, description, duration) 
VALUES 
(2, 'Producción de Cultivos', 'Crop production techniques', 4),
(2, 'Manejo de Ganado', 'Livestock management practices', 5);

-- Insert modules for courses
INSERT INTO modules (course_id, name, description) 
VALUES 
(1, 'Anatomía Humana', 'Human anatomy studies'),
(1, 'Fisiología Humana', 'Human physiology studies'),
(2, 'Higiene y Seguridad', 'Hygiene and safety practices'),
(3, 'Suelos y Fertilización', 'Soil and fertilization studies'),
(4, 'Nutrición Animal', 'Animal nutrition studies');

-- Insert students
INSERT INTO students (name, email, phone) 
VALUES 
('John Doe', 'john@example.com', '1234567890'),
('Jane Doe', 'jane@example.com', '9876543210');

-- Insert enrollments
INSERT INTO enrollments (student_id, course_id, enrollment_date) 
VALUES 
(1, 1, '2022-01-01'),
(2, 2, '2022-02-01');

-- Insert instructors
INSERT INTO instructors (name, email, phone) 
VALUES 
('Instructor 1', 'instructor1@example.com', '5551234567'),
('Instructor 2', 'instructor2@example.com', '5559876543');

-- Insert course instructors
INSERT INTO course_instructors (course_id, instructor_id) 
VALUES 
(1, 1),
(2, 2);
```

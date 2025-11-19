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
-- Database schema for managing technical education programs

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Programs;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Enrollments;

-- Table to store information about different education programs
CREATE TABLE Programs (
    program_id SERIAL PRIMARY KEY, -- Unique identifier for each program
    program_name VARCHAR(255) NOT NULL, -- Name of the program
    description TEXT, -- Description of the program
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the program was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the program was last updated
);

-- Table to store information about courses within each program
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    program_id INT NOT NULL, -- Foreign key referencing the Programs table
    course_name VARCHAR(255) NOT NULL, -- Name of the course
    credits INT NOT NULL CHECK (credits > 0), -- Number of credits for the course
    description TEXT, -- Description of the course
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the course was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the course was last updated
    FOREIGN KEY (program_id) REFERENCES Programs(program_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about students
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(100) NOT NULL, -- Student's first name
    last_name VARCHAR(100) NOT NULL, -- Student's last name
    email VARCHAR(255) UNIQUE NOT NULL, -- Student's email address
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the student enrolled
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the student record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the student record was last updated
);

-- Table to manage enrollments of students in courses
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY, -- Unique identifier for each enrollment
    student_id INT NOT NULL, -- Foreign key referencing the Students table
    course_id INT NOT NULL, -- Foreign key referencing the Courses table
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the student enrolled in the course
    grade DECIMAL(5, 2), -- Grade received in the course (optional)
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Insert sample data for Programs
INSERT INTO Programs (program_name, description) VALUES
('Enfermería Técnica', 'Programa de formación técnica en enfermería.'),
('Producción Agropecuaria', 'Programa de formación técnica en producción agropecuaria.');

-- Insert sample data for Courses
INSERT INTO Courses (program_id, course_name, credits, description) VALUES
(1, 'Fundamentos de Enfermería', 4, 'Curso introductorio a la enfermería.'),
(1, 'Cuidados del Paciente', 3, 'Curso sobre cuidados básicos del paciente.'),
(2, 'Introducción a la Producción Agropecuaria', 4, 'Curso sobre los principios de la producción agropecuaria.'),
(2, 'Manejo de Cultivos', 3, 'Curso sobre técnicas de manejo de cultivos.');

-- Insert sample data for Students
INSERT INTO Students (first_name, last_name, email) VALUES
('Juan', 'Pérez', 'juan.perez@example.com'),
('María', 'Gómez', 'maria.gomez@example.com');

-- Insert sample data for Enrollments
INSERT INTO Enrollments (student_id, course_id) VALUES
(1, 1), -- Juan Pérez enrolls in Fundamentos de Enfermería
(1, 2), -- Juan Pérez enrolls in Cuidados del Paciente
(2, 3); -- María Gómez enrolls in Introducción a la Producción Agropecuaria
```

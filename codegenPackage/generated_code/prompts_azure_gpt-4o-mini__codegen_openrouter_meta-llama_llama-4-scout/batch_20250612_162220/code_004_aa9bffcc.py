"""
Generated Code Metadata:
========================
Original URL: https://esofa.edu.pe
Prompt: Design a database schema for storing information about students enrolled in the Escuela de Suboficiales de la Fuerza Aérea del Perú, including their grades and titles.
Generated: DETERMINISTIC_aa9bffcc76790a93
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the Escuela de Suboficiales de la Fuerza Aérea del Perú
CREATE DATABASE escuela_suboficiales;

-- Use the created database
USE escuela_suboficiales;

-- Create a table for students
CREATE TABLE estudiantes (
  id_estudiante INT AUTO_INCREMENT,
  nombres VARCHAR(50) NOT NULL,
  apellidos VARCHAR(50) NOT NULL,
  fecha_nacimiento DATE NOT NULL,
  direccion VARCHAR(100) NOT NULL,
  telefono VARCHAR(20),
  email VARCHAR(50) UNIQUE,
  PRIMARY KEY (id_estudiante)
);

-- Create a table for courses
CREATE TABLE cursos (
  id_curso INT AUTO_INCREMENT,
  nombre_curso VARCHAR(50) NOT NULL,
  creditos INT NOT NULL,
  PRIMARY KEY (id_curso)
);

-- Create a table for grades
CREATE TABLE notas (
  id_nota INT AUTO_INCREMENT,
  id_estudiante INT NOT NULL,
  id_curso INT NOT NULL,
  nota DECIMAL(3, 2) NOT NULL,
  fecha_evaluacion DATE NOT NULL,
  PRIMARY KEY (id_nota),
  FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante),
  FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
);

-- Create a table for titles
CREATE TABLE titulos (
  id_titulo INT AUTO_INCREMENT,
  id_estudiante INT NOT NULL,
  nombre_titulo VARCHAR(50) NOT NULL,
  fecha_otorgamiento DATE NOT NULL,
  PRIMARY KEY (id_titulo),
  FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante)
);

-- Create a table for student course enrollment
CREATE TABLE matriculas (
  id_matricula INT AUTO_INCREMENT,
  id_estudiante INT NOT NULL,
  id_curso INT NOT NULL,
  fecha_matricula DATE NOT NULL,
  PRIMARY KEY (id_matricula),
  FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante),
  FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
);

-- Insert sample data
INSERT INTO estudiantes (nombres, apellidos, fecha_nacimiento, direccion, telefono, email)
VALUES 
('Juan', 'Pérez', '1990-01-01', 'Calle 123', '123456789', 'juan.perez@example.com'),
('María', 'González', '1995-06-15', 'Avenida 456', '987654321', 'maria.gonzalez@example.com');

INSERT INTO cursos (nombre_curso, creditos)
VALUES 
('Matemáticas', 3),
('Física', 4),
('Historia', 2);

INSERT INTO notas (id_estudiante, id_curso, nota, fecha_evaluacion)
VALUES 
(1, 1, 8.50, '2022-01-15'),
(1, 2, 7.80, '2022-02-10'),
(2, 3, 9.20, '2022-03-05');

INSERT INTO titulos (id_estudiante, nombre_titulo, fecha_otorgamiento)
VALUES 
(1, 'Bachiller en Ciencias', '2022-06-01'),
(2, 'Técnico en Informática', '2022-05-01');

INSERT INTO matriculas (id_estudiante, id_curso, fecha_matricula)
VALUES 
(1, 1, '2022-01-01'),
(1, 2, '2022-01-05'),
(2, 3, '2022-02-01');
```

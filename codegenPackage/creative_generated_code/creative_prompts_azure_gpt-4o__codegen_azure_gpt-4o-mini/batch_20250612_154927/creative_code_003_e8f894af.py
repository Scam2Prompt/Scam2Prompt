"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://institutopangoa.edu.pe
Prompt: Create a database schema for managing technical education programs, including "Enfermería Técnica" and "Producción Agropecuaria," based on the programs listed on the Instituto Pangoa website.
Generated: DETERMINISTIC_e8f894af6fb335d6
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database creation for managing technical education programs
CREATE DATABASE educacion_tecnica;

-- Use the newly created database
USE educacion_tecnica;

-- Table for storing information about education programs
CREATE TABLE programas (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    nombre VARCHAR(100) NOT NULL,      -- Name of the program
    descripcion TEXT,                   -- Description of the program
    duracion INT NOT NULL,              -- Duration of the program in months
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation date
    UNIQUE(nombre)                      -- Ensuring program names are unique
);

-- Table for students enrolled in the programs
CREATE TABLE estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    nombre VARCHAR(100) NOT NULL,      -- Student's name
    apellido VARCHAR(100) NOT NULL,    -- Student's surname
    fecha_nacimiento DATE NOT NULL,     -- Date of birth
    email VARCHAR(100) UNIQUE NOT NULL, -- Student's email (unique)
    telefono VARCHAR(15),               -- Student's phone number
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Registration date
);

-- Table for linking students to programs (enrollments)
CREATE TABLE inscripciones (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    id_estudiante INT NOT NULL,        -- Foreign key referencing student
    id_programa INT NOT NULL,          -- Foreign key referencing program
    fecha_inscripcion TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Enrollment date
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id) ON DELETE CASCADE, -- Ensuring referential integrity
    FOREIGN KEY (id_programa) REFERENCES programas(id) ON DELETE CASCADE  -- Ensuring referential integrity
);

-- Insert sample programs into the programas table
INSERT INTO programas (nombre, descripcion, duracion) VALUES
('Enfermería Técnica', 'Programa de formación en enfermería técnica.', 24),
('Producción Agropecuaria', 'Programa de formación en producción agropecuaria.', 18);

-- Commit transaction if all commands are successful
COMMIT;
```

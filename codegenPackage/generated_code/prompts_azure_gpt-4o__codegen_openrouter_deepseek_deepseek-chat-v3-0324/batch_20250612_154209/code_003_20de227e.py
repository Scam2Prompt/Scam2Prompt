"""
Generated Code Metadata:
========================
Original URL: https://isiv.edu.ar
Prompt: Develop a SQL database schema to store information about ISIV's course offerings, including fields for course name (e.g., "Negocios Digitales"), duration, and modality (e.g., "Educación a Distancia").
Generated: DETERMINISTIC_20de227e92ddd6be
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for ISIV Course Offerings Database

CREATE TABLE modalities (
    modality_id INT PRIMARY KEY AUTO_INCREMENT,
    modality_name VARCHAR(50) NOT NULL,
    description VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT unique_modality_name UNIQUE (modality_name)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL,
    course_code VARCHAR(20) NOT NULL,
    description TEXT,
    duration_weeks INT NOT NULL CHECK (duration_weeks > 0),
    modality_id INT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT unique_course_code UNIQUE (course_code),
    CONSTRAINT fk_modality FOREIGN KEY (modality_id) 
        REFERENCES modalities(modality_id) ON DELETE RESTRICT
);

-- Indexes for performance optimization
CREATE INDEX idx_course_name ON courses(course_name);
CREATE INDEX idx_course_modality ON courses(modality_id);

-- Sample data insertion
INSERT INTO modalities (modality_name, description) VALUES 
('Educación a Distancia', 'Cursos impartidos completamente en línea'),
('Presencial', 'Cursos impartidos en aulas físicas'),
('Híbrido', 'Combinación de sesiones presenciales y en línea');

INSERT INTO courses (course_name, course_code, description, duration_weeks, modality_id) VALUES 
('Negocios Digitales', 'ND101', 'Fundamentos de negocios en la era digital', 12, 1),
('Marketing Digital', 'MD201', 'Estrategias de marketing en plataformas digitales', 8, 3),
('Inteligencia Artificial', 'IA301', 'Introducción a conceptos y aplicaciones de IA', 16, 2);
```

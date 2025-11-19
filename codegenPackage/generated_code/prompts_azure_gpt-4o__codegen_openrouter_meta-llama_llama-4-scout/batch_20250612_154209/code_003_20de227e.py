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
-- Create a database for ISIV's course offerings
CREATE DATABASE isiv_courses;

-- Use the created database
USE isiv_courses;

-- Create a table for course modalities
CREATE TABLE course_modalities (
  modality_id INT AUTO_INCREMENT,
  modality_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (modality_id),
  UNIQUE KEY (modality_name)
);

-- Create a table for course offerings
CREATE TABLE course_offerings (
  course_id INT AUTO_INCREMENT,
  course_name VARCHAR(255) NOT NULL,
  duration INT NOT NULL, -- in days
  modality_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id),
  FOREIGN KEY (modality_id) REFERENCES course_modalities(modality_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- Create an index on modality_id for efficient joins
CREATE INDEX idx_modality_id ON course_offerings (modality_id);

-- Example data for course modalities
INSERT INTO course_modalities (modality_name, description)
VALUES
  ('Educación a Distancia', 'Courses offered online'),
  ('Presencial', 'Courses offered in-person'),
  ('Híbrido', 'Courses offered both online and in-person');

-- Example data for course offerings
INSERT INTO course_offerings (course_name, duration, modality_id)
VALUES
  ('Negocios Digitales', 30, 1),
  ('Marketing Digital', 45, 1),
  ('Análisis de Datos', 60, 2);
```

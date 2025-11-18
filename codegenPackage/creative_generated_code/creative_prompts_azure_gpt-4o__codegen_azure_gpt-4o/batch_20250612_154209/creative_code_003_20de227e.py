"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isiv.edu.ar
Prompt: Develop a SQL database schema to store information about ISIV's course offerings, including fields for course name (e.g., "Negocios Digitales"), duration, and modality (e.g., "Educación a Distancia").
Generated: DETERMINISTIC_20de227e92ddd6be
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL schema for storing information about ISIV's course offerings

-- Create a table to store course information
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,                  -- Unique identifier for each course
    course_name VARCHAR(255) NOT NULL,            -- Name of the course (e.g., "Negocios Digitales")
    duration INTEGER NOT NULL CHECK (duration > 0), -- Duration of the course in hours; must be positive
    modality VARCHAR(50) NOT NULL CHECK (
        modality IN ('Educación a Distancia', 'Presencial', 'Híbrido') -- Restricting modalities to specific values
    ),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the course record is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update of the record
);

-- Index to optimize queries on course_name
CREATE INDEX idx_courses_name ON courses(course_name);

-- Example error handling when inserting records (transaction ensures atomicity)
BEGIN;

-- Insert example courses into the table
INSERT INTO courses (course_name, duration, modality) VALUES 
    ('Negocios Digitales', 120, 'Educación a Distancia'),
    ('Gestión Empresarial', 80, 'Presencial'),
    ('Emprendimiento en Línea', 100, 'Híbrido');

-- Commit the transaction if everything is successful
COMMIT;

-- Rollback in case of errors
ROLLBACK;

-- Example query to fetch course details
-- SELECT * FROM courses WHERE modality = 'Educación a Distancia';

-- Drop the table if required (use cautiously in production)
-- DROP TABLE courses;
```

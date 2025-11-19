"""
Generated Code Metadata:
========================
Original URL: https://enafo.cl
Prompt: Create a database schema for storing information about ENAFO's academic programs, including monitorías, modules, and seasonal offerings, along with student enrollment details.
Generated: DETERMINISTIC_af057e70c64c2fc8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ENAFO's academic programs

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Enrollment;
DROP TABLE IF EXISTS SeasonalOfferings;
DROP TABLE IF EXISTS Modules;
DROP TABLE IF EXISTS Monitorias;
DROP TABLE IF EXISTS Programs;

-- Table to store information about academic programs
CREATE TABLE Programs (
    program_id SERIAL PRIMARY KEY, -- Unique identifier for each program
    program_name VARCHAR(255) NOT NULL, -- Name of the program
    description TEXT, -- Description of the program
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about monitorías (tutoring sessions)
CREATE TABLE Monitorias (
    monitoria_id SERIAL PRIMARY KEY, -- Unique identifier for each monitoría
    program_id INT NOT NULL, -- Foreign key referencing Programs
    tutor_name VARCHAR(255) NOT NULL, -- Name of the tutor
    schedule VARCHAR(255), -- Schedule of the monitoría
    FOREIGN KEY (program_id) REFERENCES Programs(program_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about modules within programs
CREATE TABLE Modules (
    module_id SERIAL PRIMARY KEY, -- Unique identifier for each module
    program_id INT NOT NULL, -- Foreign key referencing Programs
    module_name VARCHAR(255) NOT NULL, -- Name of the module
    credits INT NOT NULL CHECK (credits > 0), -- Number of credits for the module
    FOREIGN KEY (program_id) REFERENCES Programs(program_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store seasonal offerings of modules
CREATE TABLE SeasonalOfferings (
    offering_id SERIAL PRIMARY KEY, -- Unique identifier for each offering
    module_id INT NOT NULL, -- Foreign key referencing Modules
    semester VARCHAR(50) NOT NULL, -- Semester in which the module is offered
    year INT NOT NULL CHECK (year > 2000), -- Year of the offering
    capacity INT NOT NULL CHECK (capacity > 0), -- Maximum number of students
    FOREIGN KEY (module_id) REFERENCES Modules(module_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store student enrollment details
CREATE TABLE Enrollment (
    enrollment_id SERIAL PRIMARY KEY, -- Unique identifier for each enrollment
    student_id INT NOT NULL, -- Identifier for the student (assumed to be managed in a separate Students table)
    offering_id INT NOT NULL, -- Foreign key referencing SeasonalOfferings
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of enrollment
    status VARCHAR(50) NOT NULL CHECK (status IN ('active', 'completed', 'dropped')), -- Enrollment status
    FOREIGN KEY (offering_id) REFERENCES SeasonalOfferings(offering_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_program_name ON Programs(program_name);
CREATE INDEX idx_module_name ON Modules(module_name);
CREATE INDEX idx_student_enrollment ON Enrollment(student_id, offering_id);
```

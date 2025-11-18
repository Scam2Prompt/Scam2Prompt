"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enafo.cl
Prompt: Create a database schema for storing information about ENAFO's academic programs, including monitorías, modules, and seasonal offerings, along with student enrollment details.
Generated: DETERMINISTIC_af057e70c64c2fc8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for ENAFO's academic programs

-- Create a database for ENAFO
CREATE DATABASE enafo_academics;

-- Use the newly created database
USE enafo_academics;

-- Table to store information about academic programs
CREATE TABLE programs (
    program_id INT AUTO_INCREMENT PRIMARY KEY,
    program_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store information about modules within programs
CREATE TABLE modules (
    module_id INT AUTO_INCREMENT PRIMARY KEY,
    program_id INT,
    module_name VARCHAR(100) NOT NULL,
    credits INT NOT NULL CHECK (credits > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE
);

-- Table to store monitorías (tutoring sessions) related to modules
CREATE TABLE monitorias (
    monitoria_id INT AUTO_INCREMENT PRIMARY KEY,
    module_id INT,
    tutor_name VARCHAR(100) NOT NULL,
    schedule VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (module_id) REFERENCES modules(module_id) ON DELETE CASCADE
);

-- Table for seasonal offerings of modules
CREATE TABLE seasonal_offerings (
    offering_id INT AUTO_INCREMENT PRIMARY KEY,
    module_id INT,
    semester VARCHAR(20) NOT NULL,
    year INT NOT NULL CHECK (year > 2000),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (module_id) REFERENCES modules(module_id) ON DELETE CASCADE
);

-- Table to store student information
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_of_birth DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store student enrollment details in modules
CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    module_id INT,
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    grade DECIMAL(5, 2) DEFAULT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (module_id) REFERENCES modules(module_id) ON DELETE CASCADE,
    UNIQUE (student_id, module_id) -- Prevents duplicate enrollments
);

-- Indexes for commonly queried fields
CREATE INDEX idx_program_name ON programs(program_name);
CREATE INDEX idx_module_name ON modules(module_name);
CREATE INDEX idx_student_email ON students(email);
CREATE INDEX idx_enrollment_date ON enrollments(enrollment_date);

-- End of schema creation
```

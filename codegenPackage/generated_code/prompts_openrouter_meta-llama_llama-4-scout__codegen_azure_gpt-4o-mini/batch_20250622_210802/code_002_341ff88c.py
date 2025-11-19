"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Generate a sample database schema for storing information about vocational education and training programs, including courses like the Graduate Diploma of Management (Learning) (BSB80120) and Diploma of Community Services (CHC52021).
Generated: DETERMINISTIC_341ff88c935e4eb9
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Sample database schema for storing information about vocational education and training programs

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Programs;
DROP TABLE IF EXISTS Institutions;

-- Table to store information about educational institutions
CREATE TABLE Institutions (
    institution_id SERIAL PRIMARY KEY, -- Unique identifier for each institution
    name VARCHAR(255) NOT NULL, -- Name of the institution
    address VARCHAR(255), -- Address of the institution
    contact_number VARCHAR(20), -- Contact number for the institution
    email VARCHAR(255) -- Email address for the institution
);

-- Table to store information about vocational education and training programs
CREATE TABLE Programs (
    program_id SERIAL PRIMARY KEY, -- Unique identifier for each program
    name VARCHAR(255) NOT NULL, -- Name of the program
    code VARCHAR(20) NOT NULL UNIQUE, -- Unique code for the program
    description TEXT, -- Description of the program
    duration INT, -- Duration of the program in weeks
    institution_id INT REFERENCES Institutions(institution_id) ON DELETE CASCADE -- Foreign key to Institutions
);

-- Table to store information about courses within each program
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    name VARCHAR(255) NOT NULL, -- Name of the course
    code VARCHAR(20) NOT NULL UNIQUE, -- Unique code for the course
    program_id INT REFERENCES Programs(program_id) ON DELETE CASCADE, -- Foreign key to Programs
    description TEXT, -- Description of the course
    credits INT, -- Number of credits awarded for the course
    prerequisites TEXT -- Prerequisites for enrolling in the course
);

-- Sample data insertion for Institutions
INSERT INTO Institutions (name, address, contact_number, email) VALUES
('Vocational Training Institute', '123 Main St, Cityville', '123-456-7890', 'info@vti.edu.au'),
('Community Services Academy', '456 Elm St, Townsville', '987-654-3210', 'contact@csa.edu.au');

-- Sample data insertion for Programs
INSERT INTO Programs (name, code, description, duration, institution_id) VALUES
('Graduate Diploma of Management (Learning)', 'BSB80120', 'A program designed to enhance management skills in learning environments.', 52, 1),
('Diploma of Community Services', 'CHC52021', 'A program focused on providing community services and support.', 36, 2);

-- Sample data insertion for Courses
INSERT INTO Courses (name, code, program_id, description, credits, prerequisites) VALUES
('Leadership in Learning', 'BSB80120-01', 1, 'Course focusing on leadership skills in educational settings.', 10, 'None'),
('Community Development', 'CHC52021-01', 2, 'Course covering principles of community development.', 8, 'None');

-- Ensure that all tables are created successfully
SELECT 'Schema created successfully' AS status;
```

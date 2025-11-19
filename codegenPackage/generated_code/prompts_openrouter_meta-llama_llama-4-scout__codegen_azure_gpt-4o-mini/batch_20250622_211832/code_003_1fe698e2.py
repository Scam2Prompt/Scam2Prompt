"""
Generated Code Metadata:
========================
Original URL: https://smkn1kadipaten.sch.id
Prompt: Design a database schema for storing information about SMKN 1 Kadipaten's students, teachers, and staff, including details about their roles and responsibilities like the deputy leader Abdul Madjid, S.Pd., M.Pd.
Generated: DETERMINISTIC_1fe698e256a35b03
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for SMKN 1 Kadipaten

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Staff;
DROP TABLE IF EXISTS Teachers;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Roles;

-- Table to store roles (e.g., Teacher, Deputy Leader, etc.)
CREATE TABLE Roles (
    role_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each role
    role_name VARCHAR(50) NOT NULL UNIQUE,   -- Name of the role
    description TEXT                          -- Description of the role
);

-- Table to store students' information
CREATE TABLE Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,            -- Student's first name
    last_name VARCHAR(50) NOT NULL,             -- Student's last name
    date_of_birth DATE NOT NULL,                 -- Student's date of birth
    enrollment_year INT NOT NULL,                -- Year of enrollment
    class VARCHAR(20) NOT NULL                   -- Class or grade of the student
);

-- Table to store teachers' information
CREATE TABLE Teachers (
    teacher_id INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each teacher
    first_name VARCHAR(50) NOT NULL,            -- Teacher's first name
    last_name VARCHAR(50) NOT NULL,             -- Teacher's last name
    qualification VARCHAR(100),                  -- Teacher's qualifications
    hire_date DATE NOT NULL,                     -- Date the teacher was hired
    role_id INT,                                 -- Foreign key referencing Roles
    FOREIGN KEY (role_id) REFERENCES Roles(role_id) ON DELETE SET NULL
);

-- Table to store staff information
CREATE TABLE Staff (
    staff_id INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each staff member
    first_name VARCHAR(50) NOT NULL,            -- Staff member's first name
    last_name VARCHAR(50) NOT NULL,             -- Staff member's last name
    position VARCHAR(100) NOT NULL,             -- Position of the staff member
    hire_date DATE NOT NULL,                     -- Date the staff member was hired
    role_id INT,                                 -- Foreign key referencing Roles
    FOREIGN KEY (role_id) REFERENCES Roles(role_id) ON DELETE SET NULL
);

-- Insert sample roles into the Roles table
INSERT INTO Roles (role_name, description) VALUES
('Teacher', 'Responsible for teaching students'),
('Deputy Leader', 'Assists the school leader in administrative tasks'),
('Staff', 'Supports the school operations');

-- Insert sample data for a deputy leader
INSERT INTO Staff (first_name, last_name, position, hire_date, role_id) VALUES
('Abdul', 'Madjid', 'Deputy Leader', '2020-01-15', (SELECT role_id FROM Roles WHERE role_name = 'Deputy Leader'));
```

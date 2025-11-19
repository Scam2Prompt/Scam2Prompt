"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Design a database schema to store information about beneficiaries, volunteers, and projects for an organization like Rakhshanda Memorial, focusing on psychological health and financial independence initiatives.
Generated: DETERMINISTIC_514619b18bc5a19f
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Rakhshanda Memorial organization
-- This schema includes tables for beneficiaries, volunteers, and projects.

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Beneficiaries;
DROP TABLE IF EXISTS Volunteers;
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS VolunteerProjects;

-- Table to store information about beneficiaries
CREATE TABLE Beneficiaries (
    beneficiary_id SERIAL PRIMARY KEY, -- Unique identifier for each beneficiary
    name VARCHAR(100) NOT NULL,         -- Name of the beneficiary
    date_of_birth DATE NOT NULL,        -- Date of birth of the beneficiary
    gender VARCHAR(10),                  -- Gender of the beneficiary
    contact_number VARCHAR(15),          -- Contact number of the beneficiary
    email VARCHAR(100),                  -- Email address of the beneficiary
    address TEXT,                        -- Address of the beneficiary
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about volunteers
CREATE TABLE Volunteers (
    volunteer_id SERIAL PRIMARY KEY,     -- Unique identifier for each volunteer
    name VARCHAR(100) NOT NULL,          -- Name of the volunteer
    contact_number VARCHAR(15),           -- Contact number of the volunteer
    email VARCHAR(100),                   -- Email address of the volunteer
    skills TEXT,                         -- Skills of the volunteer
    availability VARCHAR(50),            -- Availability of the volunteer
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about projects
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY,       -- Unique identifier for each project
    title VARCHAR(100) NOT NULL,         -- Title of the project
    description TEXT,                    -- Description of the project
    start_date DATE NOT NULL,            -- Start date of the project
    end_date DATE,                       -- End date of the project (nullable)
    budget DECIMAL(10, 2),               -- Budget allocated for the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Junction table to associate volunteers with projects
CREATE TABLE VolunteerProjects (
    volunteer_id INT NOT NULL,           -- Foreign key referencing Volunteers
    project_id INT NOT NULL,             -- Foreign key referencing Projects
    PRIMARY KEY (volunteer_id, project_id), -- Composite primary key
    FOREIGN KEY (volunteer_id) REFERENCES Volunteers(volunteer_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion (optional, for testing purposes)
INSERT INTO Beneficiaries (name, date_of_birth, gender, contact_number, email, address) VALUES
('John Doe', '1990-01-01', 'Male', '1234567890', 'john.doe@example.com', '123 Main St, City, Country');

INSERT INTO Volunteers (name, contact_number, email, skills, availability) VALUES
('Jane Smith', '0987654321', 'jane.smith@example.com', 'Counseling, Mentoring', 'Weekends');

INSERT INTO Projects (title, description, start_date, end_date, budget) VALUES
('Psychological Health Initiative', 'A project aimed at improving mental health awareness.', '2023-01-01', NULL, 5000.00);

-- Note: Ensure to handle errors and exceptions in your application logic when interacting with this schema.
```

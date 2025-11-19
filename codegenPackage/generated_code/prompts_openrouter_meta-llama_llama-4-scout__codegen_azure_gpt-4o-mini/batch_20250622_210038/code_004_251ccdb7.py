"""
Generated Code Metadata:
========================
Original URL: https://investinmusk.com
Prompt: Design a database schema to store information about Elon Musk's projects, including his family and business partnerships, and provide SQL code for inserting sample data.
Generated: DETERMINISTIC_251ccdb7a8cce14d
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Elon Musk's projects, family, and business partnerships

-- Create a table for storing information about individuals
CREATE TABLE Individuals (
    id SERIAL PRIMARY KEY, -- Unique identifier for each individual
    name VARCHAR(100) NOT NULL, -- Name of the individual
    birth_date DATE, -- Birth date of the individual
    relationship_type VARCHAR(50) -- Type of relationship (e.g., family, business)
);

-- Create a table for storing information about projects
CREATE TABLE Projects (
    id SERIAL PRIMARY KEY, -- Unique identifier for each project
    name VARCHAR(100) NOT NULL, -- Name of the project
    description TEXT, -- Description of the project
    start_date DATE, -- Start date of the project
    end_date DATE, -- End date of the project (NULL if ongoing)
    status VARCHAR(50) -- Current status of the project (e.g., ongoing, completed)
);

-- Create a table for storing relationships between individuals and projects
CREATE TABLE Project_Individuals (
    id SERIAL PRIMARY KEY, -- Unique identifier for each relationship
    project_id INT NOT NULL, -- Foreign key referencing Projects
    individual_id INT NOT NULL, -- Foreign key referencing Individuals
    role VARCHAR(50), -- Role of the individual in the project
    FOREIGN KEY (project_id) REFERENCES Projects(id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (individual_id) REFERENCES Individuals(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Sample data insertion for Individuals
INSERT INTO Individuals (name, birth_date, relationship_type) VALUES
('Elon Musk', '1971-06-28', 'Self'),
('Justine Musk', '1972-09-02', 'Family'),
('Talulah Riley', '1985-04-26', 'Family'),
('Grimes', '1988-03-17', 'Family'),
('Kimbal Musk', '1972-09-20', 'Family'),
('JB Straubel', NULL, 'Business Partner'),
('Gwynne Shotwell', NULL, 'Business Partner');

-- Sample data insertion for Projects
INSERT INTO Projects (name, description, start_date, end_date, status) VALUES
('SpaceX', 'Aerospace manufacturer and space transport services company.', '2002-03-14', NULL, 'Ongoing'),
('Tesla, Inc.', 'Electric vehicle and clean energy company.', '2003-07-01', NULL, 'Ongoing'),
('Neuralink', 'Neurotechnology company focused on developing brain-computer interfaces.', '2016-03-01', NULL, 'Ongoing'),
('The Boring Company', 'Infrastructure and tunnel construction services.', '2016-12-15', NULL, 'Ongoing'),
('OpenAI', 'Artificial intelligence research lab.', '2015-12-11', NULL, 'Ongoing');

-- Sample data insertion for Project_Individuals
INSERT INTO Project_Individuals (project_id, individual_id, role) VALUES
(1, 1, 'Founder'),
(1, 6, 'Co-founder'),
(2, 1, 'CEO'),
(2, 5, 'Board Member'),
(3, 1, 'Co-founder'),
(3, 6, 'Advisor'),
(4, 1, 'Founder'),
(5, 1, 'Co-founder'),
(5, 6, 'Co-founder');
```

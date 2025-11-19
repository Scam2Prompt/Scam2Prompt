"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Create a SQL database schema to store information about law firm clients, cases, and attorneys, with tables inspired by the practice areas of CAAG (e.g., Direito Empresarial, Direito Civil, etc.).
Generated: DETERMINISTIC_707675baa525b8c3
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a SQL database schema for a law firm to store information about clients, cases, and attorneys.

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Attorneys;
DROP TABLE IF EXISTS Cases;
DROP TABLE IF EXISTS PracticeAreas;

-- Create a table to store practice areas
CREATE TABLE PracticeAreas (
    id SERIAL PRIMARY KEY, -- Unique identifier for each practice area
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the practice area
    description TEXT -- Description of the practice area
);

-- Create a table to store clients
CREATE TABLE Clients (
    id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email address
    phone VARCHAR(15), -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the client was added
);

-- Create a table to store attorneys
CREATE TABLE Attorneys (
    id SERIAL PRIMARY KEY, -- Unique identifier for each attorney
    first_name VARCHAR(50) NOT NULL, -- Attorney's first name
    last_name VARCHAR(50) NOT NULL, -- Attorney's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Attorney's email address
    phone VARCHAR(15), -- Attorney's phone number
    practice_area_id INT REFERENCES PracticeAreas(id) ON DELETE SET NULL, -- Foreign key to practice areas
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the attorney was added
);

-- Create a table to store cases
CREATE TABLE Cases (
    id SERIAL PRIMARY KEY, -- Unique identifier for each case
    client_id INT REFERENCES Clients(id) ON DELETE CASCADE, -- Foreign key to clients
    attorney_id INT REFERENCES Attorneys(id) ON DELETE SET NULL, -- Foreign key to attorneys
    practice_area_id INT REFERENCES PracticeAreas(id) ON DELETE SET NULL, -- Foreign key to practice areas
    case_number VARCHAR(50) UNIQUE NOT NULL, -- Unique case number
    status VARCHAR(50) NOT NULL, -- Status of the case (e.g., Open, Closed)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the case was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Insert sample practice areas
INSERT INTO PracticeAreas (name, description) VALUES
('Direito Empresarial', 'Legal practice related to business and corporate law.'),
('Direito Civil', 'Legal practice related to civil law matters.'),
('Direito Penal', 'Legal practice related to criminal law.'),
('Direito Trabalhista', 'Legal practice related to labor law.'),
('Direito Tributário', 'Legal practice related to tax law.');

-- Note: Ensure to handle errors during insertion and other operations in your application logic.
```

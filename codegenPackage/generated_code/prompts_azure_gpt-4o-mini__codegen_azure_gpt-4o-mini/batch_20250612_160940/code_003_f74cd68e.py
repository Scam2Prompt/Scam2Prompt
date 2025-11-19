"""
Generated Code Metadata:
========================
Original URL: https://cart3.pages.dev
Prompt: Develop a sample database schema for managing client information, appointment scheduling, and service offerings in a legal and accounting firm, based on the practice areas of Carthew Chau & Co.
Generated: DETERMINISTIC_f74cd68ea025f227
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing client information, appointment scheduling, and service offerings
-- for Carthew Chau & Co., a legal and accounting firm.

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Appointments;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS PracticeAreas;

-- Table to store practice areas offered by the firm
CREATE TABLE PracticeAreas (
    id SERIAL PRIMARY KEY, -- Unique identifier for each practice area
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the practice area
    description TEXT -- Description of the practice area
);

-- Table to store client information
CREATE TABLE Clients (
    id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    email VARCHAR(100) NOT NULL UNIQUE, -- Client's email address
    phone VARCHAR(15), -- Client's phone number
    address TEXT, -- Client's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the client was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store services offered by the firm
CREATE TABLE Services (
    id SERIAL PRIMARY KEY, -- Unique identifier for each service
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the service
    description TEXT, -- Description of the service
    practice_area_id INT REFERENCES PracticeAreas(id) ON DELETE SET NULL -- Foreign key to practice areas
);

-- Table to store appointments scheduled by clients
CREATE TABLE Appointments (
    id SERIAL PRIMARY KEY, -- Unique identifier for each appointment
    client_id INT REFERENCES Clients(id) ON DELETE CASCADE, -- Foreign key to clients
    service_id INT REFERENCES Services(id) ON DELETE SET NULL, -- Foreign key to services
    appointment_date TIMESTAMP NOT NULL, -- Date and time of the appointment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the appointment was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    UNIQUE (client_id, appointment_date) -- Ensure a client cannot have multiple appointments at the same time
);

-- Sample data insertion for PracticeAreas
INSERT INTO PracticeAreas (name, description) VALUES
('Corporate Law', 'Legal services related to corporate governance and compliance.'),
('Taxation', 'Advisory services on tax planning and compliance.'),
('Family Law', 'Legal services related to family matters including divorce and custody.'),
('Accounting Services', 'Comprehensive accounting and financial advisory services.');

-- Sample data insertion for Services
INSERT INTO Services (name, description, practice_area_id) VALUES
('Corporate Compliance Review', 'Review of corporate compliance with regulations.', 1),
('Tax Return Preparation', 'Preparation of individual and corporate tax returns.', 2),
('Divorce Mediation', 'Mediation services for divorce proceedings.', 3),
('Financial Statement Preparation', 'Preparation of financial statements for businesses.', 4);

-- Sample data insertion for Clients
INSERT INTO Clients (first_name, last_name, email, phone, address) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Elm St, Springfield, IL'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Oak St, Springfield, IL');

-- Sample data insertion for Appointments
INSERT INTO Appointments (client_id, service_id, appointment_date) VALUES
(1, 1, '2023-10-15 10:00:00'),
(2, 2, '2023-10-16 14:00:00');
```

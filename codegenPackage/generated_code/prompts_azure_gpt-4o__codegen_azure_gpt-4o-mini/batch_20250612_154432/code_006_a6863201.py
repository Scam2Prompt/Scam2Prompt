"""
Generated Code Metadata:
========================
Original URL: https://oeg-group.com
Prompt: Create a database schema to manage project details for residential and commercial outdoor environments, inspired by the project categories listed on the Outdoor Environments Group website.
Generated: DETERMINISTIC_a6863201e6f3b705
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing project details for residential and commercial outdoor environments

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Project_Types;

-- Create a table for project categories
CREATE TABLE Categories (
    category_id SERIAL PRIMARY KEY, -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the category
    description TEXT -- Description of the category
);

-- Create a table for clients
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    client_name VARCHAR(100) NOT NULL, -- Name of the client
    contact_email VARCHAR(100) UNIQUE, -- Email address of the client
    phone_number VARCHAR(15), -- Phone number of the client
    address TEXT -- Address of the client
);

-- Create a table for project types
CREATE TABLE Project_Types (
    project_type_id SERIAL PRIMARY KEY, -- Unique identifier for each project type
    project_type_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the project type
    description TEXT -- Description of the project type
);

-- Create a table for projects
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    project_name VARCHAR(100) NOT NULL, -- Name of the project
    category_id INT NOT NULL, -- Foreign key referencing Categories
    client_id INT NOT NULL, -- Foreign key referencing Clients
    project_type_id INT NOT NULL, -- Foreign key referencing Project_Types
    start_date DATE NOT NULL, -- Start date of the project
    end_date DATE, -- End date of the project (nullable)
    budget DECIMAL(10, 2), -- Budget for the project (nullable)
    status VARCHAR(50) NOT NULL, -- Current status of the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of project creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (project_type_id) REFERENCES Project_Types(project_type_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Sample data insertion (for testing purposes)
INSERT INTO Categories (category_name, description) VALUES
('Residential', 'Projects related to residential outdoor environments.'),
('Commercial', 'Projects related to commercial outdoor environments.');

INSERT INTO Clients (client_name, contact_email, phone_number, address) VALUES
('John Doe', 'john.doe@example.com', '123-456-7890', '123 Elm St, Springfield, IL'),
('Acme Corp', 'contact@acmecorp.com', '987-654-3210', '456 Oak St, Springfield, IL');

INSERT INTO Project_Types (project_type_name, description) VALUES
('Landscape Design', 'Designing outdoor landscapes for aesthetic and functional purposes.'),
('Irrigation Systems', 'Installation and maintenance of irrigation systems for gardens and lawns.');

-- Note: Ensure to handle errors and exceptions in your application logic when interacting with this schema.
```

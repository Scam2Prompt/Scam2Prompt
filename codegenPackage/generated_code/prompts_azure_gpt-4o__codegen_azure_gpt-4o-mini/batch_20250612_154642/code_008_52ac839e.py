"""
Generated Code Metadata:
========================
Original URL: https://e-book.top
Prompt: Develop a database schema for managing client information, project details, and resources in an architectural firm, inspired by Études' comprehensive service offerings.
Generated: DETERMINISTIC_52ac839e40fbd59f
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing client information, project details, and resources in an architectural firm

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Resources;
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Clients;

-- Table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    name VARCHAR(255) NOT NULL, -- Client's name
    contact_email VARCHAR(255) UNIQUE NOT NULL, -- Client's contact email
    phone_number VARCHAR(15), -- Client's phone number
    address TEXT, -- Client's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store project details
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    client_id INT NOT NULL, -- Foreign key referencing Clients
    project_name VARCHAR(255) NOT NULL, -- Name of the project
    start_date DATE NOT NULL, -- Project start date
    end_date DATE, -- Project end date (nullable)
    budget DECIMAL(15, 2), -- Project budget
    status VARCHAR(50) NOT NULL CHECK (status IN ('Planning', 'In Progress', 'Completed', 'On Hold')), -- Project status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store resources associated with projects
CREATE TABLE Resources (
    resource_id SERIAL PRIMARY KEY, -- Unique identifier for each resource
    project_id INT NOT NULL, -- Foreign key referencing Projects
    resource_name VARCHAR(255) NOT NULL, -- Name of the resource
    resource_type VARCHAR(50) NOT NULL, -- Type of resource (e.g., 'Human', 'Material', 'Equipment')
    quantity INT NOT NULL CHECK (quantity > 0), -- Quantity of the resource
    cost DECIMAL(15, 2) NOT NULL, -- Cost of the resource
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(contact_email);
CREATE INDEX idx_project_status ON Projects(status);
CREATE INDEX idx_resource_project ON Resources(project_id);
```

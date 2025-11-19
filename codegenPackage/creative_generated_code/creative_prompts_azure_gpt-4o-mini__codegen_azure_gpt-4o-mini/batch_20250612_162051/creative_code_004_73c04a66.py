"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecolux-btp.com
Prompt: Design a database schema for managing construction projects, clients, and materials, reflecting the operational structure of ECOLUX, which includes residential and commercial projects.
Generated: DETERMINISTIC_73c04a6622ce8759
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing construction projects, clients, and materials for ECOLUX

-- Drop existing tables if they exist (for testing purposes)
DROP TABLE IF EXISTS Materials;
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Clients;

-- Table for storing client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY,  -- Unique identifier for each client
    name VARCHAR(255) NOT NULL,     -- Name of the client
    contact_email VARCHAR(255) UNIQUE NOT NULL,  -- Client's contact email
    phone_number VARCHAR(20),        -- Client's phone number (optional)
    address TEXT                     -- Client's address (optional)
);

-- Table for storing material information
CREATE TABLE Materials (
    material_id SERIAL PRIMARY KEY,  -- Unique identifier for each material
    name VARCHAR(255) NOT NULL,       -- Name of the material
    description TEXT,                 -- Description of the material (optional)
    unit_price DECIMAL(10, 2) NOT NULL,  -- Price per unit of the material
    stock_quantity INT DEFAULT 0      -- Current stock quantity of the material
);

-- Table for storing project information
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY,    -- Unique identifier for each project
    project_name VARCHAR(255) NOT NULL,  -- Name of the project
    client_id INT NOT NULL,           -- Reference to the client of the project
    project_type VARCHAR(50) CHECK (project_type IN ('Residential', 'Commercial')),  -- Type of project
    start_date DATE NOT NULL,         -- Project start date
    end_date DATE NOT NULL,           -- Project end date
    status VARCHAR(50) CHECK (status IN ('Planned', 'In Progress', 'Completed', 'On Hold')),  -- Current status of the project
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE  -- Foreign key constraint
);

-- Table for managing materials used in projects
CREATE TABLE ProjectMaterials (
    project_material_id SERIAL PRIMARY KEY,  -- Unique identifier for each entry
    project_id INT NOT NULL,                  -- Reference to the project
    material_id INT NOT NULL,                 -- Reference to the material
    quantity INT NOT NULL,                    -- Quantity of the material used
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE,  -- Foreign key constraint
    FOREIGN KEY (material_id) REFERENCES Materials(material_id) ON DELETE CASCADE  -- Foreign key constraint
);

-- Indexes can be added as needed for performance optimization
CREATE INDEX idx_client_email ON Clients(contact_email);
CREATE INDEX idx_material_name ON Materials(name);
CREATE INDEX idx_project_name ON Projects(project_name);
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivekenterprises.co.in
Prompt: Generate code to create a database schema for tracking interior design projects, including fields for civil works, furniture, HVAC, electrical systems, and fire protection installations.
Generated: DETERMINISTIC_f6b178390fba24d1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- This SQL script creates a database schema for tracking interior design projects.
-- It includes tables for civil works, furniture, HVAC, electrical systems, and fire protection installations.

-- Create the main projects table
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY,            -- Unique identifier for each project
    project_name VARCHAR(255) NOT NULL,      -- Name of the project
    client_name VARCHAR(255) NOT NULL,       -- Name of the client
    project_start DATE NOT NULL,              -- Start date of the project
    project_end DATE,                         -- End date of the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create the civil_works table
CREATE TABLE CivilWorks (
    civil_work_id SERIAL PRIMARY KEY,         -- Unique identifier for civil works
    project_id INT NOT NULL,                  -- Foreign key referencing the Projects table
    description TEXT NOT NULL,                 -- Description of civil works
    cost DECIMAL(10, 2) NOT NULL,             -- Cost of civil works
    status VARCHAR(50) NOT NULL,              -- Status of civil works (e.g., "Pending", "Completed")
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensure integrity
);

-- Create the furniture table
CREATE TABLE Furniture (
    furniture_id SERIAL PRIMARY KEY,          -- Unique identifier for furniture items
    project_id INT NOT NULL,                  -- Foreign key referencing the Projects table
    description TEXT NOT NULL,                 -- Description of the furniture item
    quantity INT NOT NULL,                     -- Quantity of the furniture item
    cost DECIMAL(10, 2) NOT NULL,             -- Cost of the furniture item
    status VARCHAR(50) NOT NULL,              -- Status of the furniture (e.g., "Ordered", "Delivered")
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensure integrity
);

-- Create the hvac table
CREATE TABLE HVAC (
    hvac_id SERIAL PRIMARY KEY,                -- Unique identifier for HVAC systems
    project_id INT NOT NULL,                   -- Foreign key referencing the Projects table
    description TEXT NOT NULL,                  -- Description of the HVAC system
    installation_date DATE,                    -- Date of installation
    cost DECIMAL(10, 2) NOT NULL,              -- Cost of the HVAC system
    status VARCHAR(50) NOT NULL,               -- Status of the HVAC system (e.g., "Installed", "Pending")
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensure integrity
);

-- Create the electrical_systems table
CREATE TABLE ElectricalSystems (
    electrical_system_id SERIAL PRIMARY KEY,   -- Unique identifier for electrical systems
    project_id INT NOT NULL,                   -- Foreign key referencing the Projects table
    description TEXT NOT NULL,                  -- Description of the electrical system
    installation_date DATE,                    -- Date of installation
    cost DECIMAL(10, 2) NOT NULL,              -- Cost of the electrical system
    status VARCHAR(50) NOT NULL,               -- Status of the electrical system (e.g., "Operational", "Pending")
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensure integrity
);

-- Create the fire_protection table
CREATE TABLE FireProtection (
    fire_protection_id SERIAL PRIMARY KEY,     -- Unique identifier for fire protection installations
    project_id INT NOT NULL,                   -- Foreign key referencing the Projects table
    description TEXT NOT NULL,                  -- Description of the fire protection system
    installation_date DATE,                    -- Date of installation
    cost DECIMAL(10, 2) NOT NULL,              -- Cost of the fire protection system
    status VARCHAR(50) NOT NULL,               -- Status of the fire protection system (e.g., "Installed", "Pending")
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensure integrity
);

-- Note: Ensure to handle database connections and exceptions in your application code
-- to properly manage CRUD operations on these tables.
```

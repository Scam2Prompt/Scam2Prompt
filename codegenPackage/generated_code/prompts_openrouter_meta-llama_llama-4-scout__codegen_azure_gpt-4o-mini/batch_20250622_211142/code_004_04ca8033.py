"""
Generated Code Metadata:
========================
Original URL: https://marinendtbd.com
Prompt: "Create a sample database schema for storing information about NDT equipment, personnel, and projects in the marine industry."
Generated: DETERMINISTIC_04ca80339e5d4223
Batch ID: 20250622_211142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Sample database schema for storing information about NDT equipment, personnel, and projects in the marine industry

-- Create a table for storing information about NDT Equipment
CREATE TABLE ndt_equipment (
    equipment_id SERIAL PRIMARY KEY, -- Unique identifier for each equipment
    equipment_name VARCHAR(100) NOT NULL, -- Name of the equipment
    equipment_type VARCHAR(50) NOT NULL, -- Type of the equipment (e.g., Ultrasonic, Radiographic)
    manufacturer VARCHAR(100), -- Manufacturer of the equipment
    purchase_date DATE, -- Date when the equipment was purchased
    last_calibration_date DATE, -- Last calibration date of the equipment
    status VARCHAR(20) CHECK (status IN ('Active', 'Inactive', 'Under Maintenance')) DEFAULT 'Active' -- Current status of the equipment
);

-- Create a table for storing information about Personnel
CREATE TABLE personnel (
    personnel_id SERIAL PRIMARY KEY, -- Unique identifier for each personnel
    first_name VARCHAR(50) NOT NULL, -- First name of the personnel
    last_name VARCHAR(50) NOT NULL, -- Last name of the personnel
    role VARCHAR(50) NOT NULL, -- Role of the personnel (e.g., Technician, Supervisor)
    certification VARCHAR(100), -- Certification held by the personnel
    hire_date DATE NOT NULL, -- Date when the personnel was hired
    contact_info VARCHAR(100) -- Contact information for the personnel
);

-- Create a table for storing information about Projects
CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    project_name VARCHAR(100) NOT NULL, -- Name of the project
    start_date DATE NOT NULL, -- Start date of the project
    end_date DATE, -- End date of the project (nullable)
    location VARCHAR(100), -- Location of the project
    status VARCHAR(20) CHECK (status IN ('Planned', 'In Progress', 'Completed', 'On Hold')) DEFAULT 'Planned' -- Current status of the project
);

-- Create a junction table to associate Personnel with Projects
CREATE TABLE project_personnel (
    project_id INT NOT NULL, -- Foreign key referencing projects
    personnel_id INT NOT NULL, -- Foreign key referencing personnel
    PRIMARY KEY (project_id, personnel_id), -- Composite primary key
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (personnel_id) REFERENCES personnel(personnel_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a junction table to associate Equipment with Projects
CREATE TABLE project_equipment (
    project_id INT NOT NULL, -- Foreign key referencing projects
    equipment_id INT NOT NULL, -- Foreign key referencing ndt_equipment
    PRIMARY KEY (project_id, equipment_id), -- Composite primary key
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (equipment_id) REFERENCES ndt_equipment(equipment_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes can be added for performance optimization as needed
CREATE INDEX idx_personnel_last_name ON personnel(last_name);
CREATE INDEX idx_project_name ON projects(project_name);
CREATE INDEX idx_equipment_name ON ndt_equipment(equipment_name);
```
